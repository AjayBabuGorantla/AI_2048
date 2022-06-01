import math

def heuristic(grid):
    number_of_empty_tiles = len([i for i, x in enumerate(grid) if x == 0])
    largest_tile = max(grid)
    order = 0
    weights_list = [65536,32768,16384,8192,512,1024,2048,4096,256,128,64,32,2,4,8,16]
    if largest_tile == grid[0]:
        order += (math.log(grid[0])/math.log(2))*weights_list[0]
    for i in range(16):
        if grid[i] >= 8:
            order += weights_list[i]*(math.log(grid[i])/math.log(2))
    return order/(16-number_of_empty_tiles)

def return_children(grid):
    possible_moves = [0,1,2,3]
    children = list()
    moving = list()
    for each_move in possible_moves:
        temp_grid = list(grid)
        moved = move(temp_grid, each_move)
        if moved == True:
            children.append(temp_grid)
            moving.append(each_move)
    return [children,moving]

def combine(cells):
    if len(cells) <= 1:
        return cells
    count = 0
    while count < len(cells)-1:
        if cells[count] == cells[count+1]:
            cells[count] *= 2
            del cells[count+1]
        count += 1

def move(grid, dir):
    moved_flag = False

    if dir == 0:
        for i in range(4):
            cells = list()
            for j in range(i,i+13,4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            combine(cells)
            for j in range(i,i+13,4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved_flag = True
                grid[j] = value
        return moved_flag

    elif dir == 1:
        for i in range(4):
            cells = list()
            for j in range(i+12,i-1,-4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            combine(cells)
            for j in range(i+12,i-1,-4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved_flag = True
                grid[j] = value
        return moved_flag

    elif dir == 2:
        for i in [0,4,8,12]:
            cells = list()
            for j in range(i,i+4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            combine(cells)
            for j in range(i,i+4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved_flag = True
                grid[j] = value
        return moved_flag

    elif dir == 3:
        for i in [3,7,11,15]:
            cells = list()
            for j in range(i,i-4,-1):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            combine(cells)
            for j in range(i,i-4,-1):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved_flag = True
                grid[j] = value
        return moved_flag

def valid_move_status(grid):
    if 0 in grid:
        return True
    for i in range(16):
        if (i+1)%4!=0:
            if grid[i]==grid[i+1]:
                return True
        if i<12:
            if grid[i]==grid[i+4]:
                return True
    return False


