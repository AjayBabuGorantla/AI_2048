import sys
from gui import *
import pandas as pd
import numpy as np
import random
from datetime import datetime
from win_percentage_plot import plot_win_percentage

def initialize(size):
	board = np.zeros((size*size))
	initial_twos = np.random.default_rng().choice(16, 2, replace=False)
	board[initial_twos] = 2
	board = board.reshape((size, size))

	return board

class Board:
	def __init__(self, size, gui_flag):
		random.seed(datetime.now())
		self.board = initialize(size)
		self.size = size
		self.TARGET = 2048
		self.TILE_VALUES = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
		self.DEPTH = 10
		self.SEARCHES = 50
		self.DIRECTIONS = ["DOWN", "UP", "LEFT", "RIGHT"]
		self.INVALID_MOVES = 10
		self.GUI_FLAG = gui_flag

	def update_board(self, array):
		self.board = array

	def is_won(self):
		win_status = False
		for row in range(self.size):
			for col in range(self.size):
				if self.board[row][col] == self.TARGET:
					win_status = True
		return win_status

	def is_loss(self):
		loss_status = True
		original_board = np.copy(self.board)
		for move in self.DIRECTIONS:
			if self.move(move):
				loss_status = False
				self.update_board(original_board)
				break
			else:
				self.update_board(original_board)
		return loss_status

	def slide_towards_right(self):
		board_after_slide = np.zeros((self.size, self.size))
		action_completed = False
		for i in range(4):
			count = self.size-1
			for j in range(self.size-1, -1, -1):
				if self.board[i][j] != 0:
					board_after_slide[i][count] = self.board[i][j]
					if j != count:
						action_completed = True
					count -= 1
		self.update_board(board_after_slide)
		return action_completed

	def merge_tiles(self):
		action_completed = False
		for i in range(4):
			for j in range(3, 0, -1):
				if self.board[i][j] == self.board[i][j-1] and self.board[i][j] != 0:
					self.board[i][j] *= 2
					self.board[i][j-1] = 0
					action_completed = True
		return action_completed

	def move(self, direction):
		if direction == "DOWN":
			self.board = np.rot90(self.board)
			slide_done = self.slide_towards_right()
			merge_done = self.merge_tiles()
			self.slide_towards_right()
			self.board = np.rot90(self.board, 3)
			change =  slide_done or merge_done

		elif direction == "UP":
			self.board = np.rot90(self.board, 3)
			slide_done = self.slide_towards_right()
			merge_done = self.merge_tiles()
			self.slide_towards_right()
			self.board = np.rot90(self.board)
			change =  slide_done or merge_done

		elif direction == "LEFT":
			self.board = np.rot90(self.board, 2)
			slide_done = self.slide_towards_right()
			merge_done = self.merge_tiles()
			self.slide_towards_right()
			self.board = np.rot90(self.board, 2)
			change =  slide_done or merge_done

		elif direction == "RIGHT":
			slide_done = self.slide_towards_right()
			merge_done = self.merge_tiles()
			self.slide_towards_right()
			change =  slide_done or merge_done
		else:
			pass

		if change:
			value_of_tile = self.TILE_VALUES[random.randint(0, len(self.TILE_VALUES)-1)]
			options_row, options_col = np.nonzero(np.logical_not(self.board))
			location = random.randint(0, len(options_row)-1)
			self.board[options_row[location], options_col[location]] = value_of_tile

		return change

	def evaluate_board(self):
		if self.is_won():
			return 2
		elif self.is_loss():
			return 0
		else:
			final_score = 0
			final_score += (16 - np.count_nonzero(self.board)) / 16
			if np.argmax(self.board) in [0, 3, 12, 15]:
				final_score *= 1.5

			return final_score

	def gui_flag_search(self):
		
		original_board = np.copy(self.board)
		results_after_move = np.zeros(4)
		# results_after_move = np.zeros(4)
		#game_gui = gg.Game_gui()

		for move in range(4):
			for _ in range(self.SEARCHES):
				move_made_status = self.move(self.DIRECTIONS[move])
				 
				if not move_made_status:
					break
				wrong_moves_made = 0
				depth_level = 0
				while depth_level < self.DEPTH:
					direction = self.DIRECTIONS[random.randint(0, 3)]
					move_made_status = self.move(direction)
					if move_made_status:
						depth_level += 1
					else: 
						wrong_moves_made += 1
					if wrong_moves_made == self.INVALID_MOVES:
						break
				board_evaluation = self.evaluate_board()
				results_after_move[move] += board_evaluation
				self.update_board(original_board)
			if self.GUI_FLAG :

				game_gui.update_GUI(self.board.astype(int),self.evaluate_board())

		maximum_value_move = results_after_move.argmax()
		# print(self.DIRECTIONS[move])

		return self.move(self.DIRECTIONS[maximum_value_move])

	def employ_ai(self):
		slides = 0

		while slides < 1100:
			slides += 1
			# print(self.board)
			# print(slides)
			not_stuck_status = self.gui_flag_search()

			if slides > 930:
				if self.is_won():
					print('Hurray! We have won. This gives me the confidence that I will be the next Alexander the great!')
					return "Win"
			if not not_stuck_status:
				print("Oops! Let's try again..definitely not the end of our conquest")
				print(self.board)
				return "Loss"
		return slides,
      

def main():

    evaluation_dataFrame = pd.DataFrame(columns=[128, 256, 512, 1024, 2048])

    output_file = open("results.txt", "w")
    for i in range(20):
        board = Board(4, gui_flag=sys.argv[0])
        if board.GUI_FLAG:
            global game_gui
            game_gui = Game_gui()

        result = board.employ_ai()
        print(i)
        if result == "Win":
            output_file.write("Win\n")
        elif result == "Loss":
            output_file.write("Loss\n")
        else: 
            output_file.write("Incomplete\n")
        board_flattened = list(board.board.astype(int).flatten())
        for col in evaluation_dataFrame.columns:
            if col in board_flattened:
                evaluation_dataFrame.loc()[len(evaluation_dataFrame),[col]] = 1

        if board.GUI_FLAG:
            game_gui.update_GUI(board.board.astype(int),result)
            game_gui.mainloop()

    output_file.close()


if __name__ == "__main__":
    main()

