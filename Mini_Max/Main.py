import numpy
from random import randint
import matplotlib.pyplot as plt
import time
from Grid import Grid
from Opponent import Opp
from Player import Player

class Game2048:
	def __init__(self, size = 4):
		self.grid = Grid(size)
		self.tile_values = [2, 4]
		self.probability = probability
		self.number_of_initial_tiles = number_of_initial_tiles
		self.opponent = None
		self.agent = None
		self.game_completed_flag = False

	def show_grid(self, grid):
		for i in range(grid.size):
			for j in range(grid.size):
				print("%6d  " % grid.map[i][j], end="")
			print ("")
		print ("")
		print ("")

	def check_if_game_is_finished(self):
		return not self.grid.move_made_status()

	def assign_agent(self, agent):
		self.agent = agent

	def assign_opponent(self, opponent):
		self.opponent = opponent

	def time(self, time):
		if time - self.previous_time > time_limit + 0.1:
			self.game_completed_flag = True
		else:
			self.previous_time = time

	def fill_random_tile(self):
		tile = self.return_next_tile()
		cells = self.grid.return_empty_cells()
		cell = cells[randint(0, len(cells) - 1)]
		self.grid.change_cell_value(cell, tile)

	def return_next_tile(self):
		if randint(0,99) < 100 * self.probability:
			return self.tile_values[0]
		else:
			return self.tile_values[1]

	def begin(self):
		for i in range(self.number_of_initial_tiles):
			self.fill_random_tile()

		self.show_grid(self.grid)

		player_turn = Agent
		largest_tile = 0

		self.previous_time = time.perf_counter()

		while not self.check_if_game_is_finished() and not self.game_completed_flag:
			grid_temp = self.grid.copying()
			next_move = None

			if player_turn == Agent:
				print("This is Agent's turn")
				next_move = self.agent.return_move(grid_temp)

				if next_move != None and next_move >= 0 and next_move < 4:
					if self.grid.move_made_status([next_move]):
						self.grid.move(next_move)
						largest_tile = self.grid.get_largest_tile()
					else:
						print("Illegal Move made! not accepted")
						self.game_completed_flag = True
				else:
					print("Illegal move made")
					self.game_completed_flag = True
			else:
				print("It is opponent's turn")
				next_move = self.opponent.return_move(grid_temp)
				if next_move and self.grid.insertion_possibility_status(next_move):
					self.grid.change_cell_value(next_move, self.return_next_tile())
				else:
					print("Illegal move made")
					self.game_completed_flag = True

			if not self.game_completed_flag:
				self.show_grid(self.grid)
			self.time(time.perf_counter())
			player_turn = 1 - player_turn
		list_max_tiles.append(largest_tile)
		print("Highest Score for this game:",largest_tile)


def main():
	game_instance = Game2048()
	agent = Player()
	opponent = Opp()
	game_instance.assign_agent(agent)
	game_instance.assign_opponent(opponent)
	game_instance.begin()


if __name__ == '__main__':

	number_of_initial_tiles = 2
	(Agent, Opponent) = (0, 1)
	time_limit = 1
	probability = 0.9
	list_max_tiles = list()
	number_of_iterations = 50

	for each_iteration in range(number_of_iterations):
		print("-----------------------------Iteration Number:", each_iteration + 1, "--------------------------------------")
		main()

	desired_values = [32, 64, 128, 256, 512, 1024, 2048]
	count_list = list()
	labels_list = list()
	
	print("Max tiles list : ", list_max_tiles)

	for i in range(len(desired_values)):
		if (list_max_tiles.count(desired_values[i]) != 0):
			count_list.append(list_max_tiles.count(desired_values[i]))
			labels_list.append(str(desired_values[i]) +'\n' + str((list_max_tiles.count(desired_values[i]) / number_of_iterations) * 100)+"%")

	result = numpy.array(count_list)

	print('Result :', result)
	print('Labels :', labels_list)
	print("Percentage of 32's :", (list_max_tiles.count(32) / number_of_iterations) * 100)
	print("Percentage of 64's :", (list_max_tiles.count(64) / number_of_iterations) * 100)
	print("Percentage of 128's :", (list_max_tiles.count(128) / number_of_iterations) * 100)
	print("Percentage of 256's :", (list_max_tiles.count(256) / number_of_iterations) * 100)
	print("Percentage of 512's :", (list_max_tiles.count(512) / number_of_iterations) * 100)
	print("Percentage of 1024's :", (list_max_tiles.count(1024) / number_of_iterations) * 100)
	print("Percentage of 2048's :", (list_max_tiles.count(2048) / number_of_iterations) * 100)

	plt.pie(result, labels=labels_list)
	plt.title("Percentage of Occurances :")
	plt.show()

