from random import randint

class Opp():
	def return_move(self, grid):
		cells = grid.return_empty_cells()
		if cells:
			return cells[randint(0, len(cells) - 1)]
		else:
			None
