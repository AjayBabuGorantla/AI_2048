from copy import deepcopy

directions = (UP_DIR, DOWN_DIR, LEFT_DIR, RIGHT_DIR) = ((-1, 0), (1, 0), (0, -1), (0, 1))
direction_index = [UP, DOWN, LEFT, RIGHT] = range(4)

class Grid:
    def __init__(self, size = 4):
        self.size = size
        self.map = [[0] * self.size for i in range(self.size)]
    
    def change_cell_value(self, pos, value):
        self.map[pos[0]][pos[1]] = value
    
    def change_cell_value(self, pos, value):
        self.map[pos[0]][pos[1]] = value

    def return_empty_cells(self):
        cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] == 0:
                    cells.append((i,j))
        return cells

    def copying(self):
        temp = Grid()
        temp.map = deepcopy(self.map)
        temp.size = self.size
        return temp

    def get_largest_tile(self):
        highestValueCell = 0
        for i in range(self.size):
            for j in range(self.size):
                highestValueCell = max(highestValueCell, self.map[i][j])
        return highestValueCell

    def insertion_possibility_status(self, pos):
        return self.return_cell_value(pos) == 0

    def move(self, dir):
        dir = int(dir)
        if dir == UP:
            return self.slide_up_or_down(False)
        if dir == DOWN:
            return self.slide_up_or_down(True)
        if dir == LEFT:
            return self.slide_left_or_right(False)
        if dir == RIGHT:
            return self.slide_left_or_right(True)

    def slide_up_or_down(self, down):
        r = range(self.size -1, -1, -1) if down else range(self.size)
        moved_flag = False
        for j in range(self.size):
            cells = []
            for i in r:
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.combine(cells)
            for i in r:
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved_flag = True
                self.map[i][j] = value
        return moved_flag

    def slide_left_or_right(self, right):
        r = range(self.size - 1, -1, -1) if right else range(self.size)
        moved_flag = False
        for i in range(self.size):
            cells = []
            for j in r:
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.combine(cells)
            for j in r:
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved_flag = True
                self.map[i][j] = value
        return moved_flag

    def combine(self, cells):
        if len(cells) <= 1:
            return cells
        count = 0
        while count < len(cells) - 1:
            if cells[count] == cells[count+1]:
                cells[count] *= 2
                del cells[count+1]
            count += 1

    def move_made_status(self, dirs = direction_index):
        possible_moves = set(dirs)

        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y]:
                    for i in possible_moves:
                        possible_move = directions[i]
                        adjValue = self.return_cell_value((x + possible_move[0], y + possible_move[1]))
                        if adjValue == self.map[x][y] or adjValue == 0:
                            return True
                elif self.map[x][y] == 0:
                    return True
        return False

    def return_possible_moves(self, dirs = direction_index):
        possible_moves = list()
        for x in dirs:
            temp = self.copying()
            if temp.move(x):
                possible_moves.append(x)
        return possible_moves

    def cross_bound(self, pos):
        return pos[0] < 0 or pos[0] >= self.size or pos[1] < 0 or pos[1] >= self.size

    def return_cell_value(self, pos):
        if not self.cross_bound(pos):
            return self.map[pos[0]][pos[1]]
        else:
            return None

if __name__ == '__main__':

    main_grid = Grid()
    main_grid.map[0][0] = 2
    main_grid.map[2][0] = 4
    while True:
        for i in main_grid.map:
            print(i)
        print (main_grid.return_possible_moves())
        input_value = raw_input()
        main_grid.move(input_value)
