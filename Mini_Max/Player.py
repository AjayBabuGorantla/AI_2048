import Minimax
# import alpha_beta_pruning
from Grid import Grid
import numpy as np
from helper_functions import *

class Player():
        def return_move(self, grid):
                grid_temp = list()
                for i in range(4):
                        grid_temp.extend(grid.map[i])
                [child,moves] = return_children(grid_temp)
                max_possible_path = -np.inf
                direction = 0
                for i in range(len(child)):
                        grid = child[i]
                        number_of_moves = moves[i]
                        highest_value = -np.inf
                        max_depth = 4
                        # highest_value = alpha_beta_pruning.calculate(grid, max_depth, -np.inf, np.inf, False)
                        highest_value = Minimax.calculate(grid, max_depth, False)
                        if number_of_moves == 0 or number_of_moves == 2:
                            highest_value += 10000
                        if highest_value > max_possible_path:
                            direction = number_of_moves
                            max_possible_path = highest_value

                return direction

if __name__ == '__main__':
        agent = Player()
        main_grid=Grid()
        main_grid.map[0][0] = 2
        main_grid.map[2][0] = 4
        while True:
                value = agent.return_move(main_grid)
                main_grid.move(value)



