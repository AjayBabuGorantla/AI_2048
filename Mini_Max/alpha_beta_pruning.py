from helper_functions import *
import numpy as np

def calculate(grid, depth, alpha, beta, max_flag):
    if depth == 0:
        return heuristic(grid)
    if not valid_move_status(grid):
        return heuristic(grid)
    if max_flag:
        best_value = -np.inf
        [child,moving] = return_children(grid)
        for each_child in child:
            best_value = max(best_value,calculate(each_child,depth-1,alpha,beta,False))
            if best_value >= beta:
                return best_value
            alpha = max(alpha,best_value)
        return best_value
    else:
        cells = [i for i, x in enumerate(grid) if x == 0]
        child = list()
        for each_cell in cells:
            temp = list(grid)
            temp[each_cell]=2
            child.append(temp)
            temp = list(grid)
            temp[each_cell]=4
            child.append(temp)
        best_value = np.inf
        for each_child in child:
            best_value = min(best_value,calculate(each_child,depth-1,alpha,beta,True))
            if best_value <= alpha:
                return best_value
            beta = min(beta,best_value)
        return best_value
