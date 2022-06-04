def draw_sudoku_puzzle(sudoku_puzzle):
    split_line = '\n---------------------------------------\n'
    split_line3 = '\n=======================================\n'
    map_sudoku_puzzle = split_line
    
    for i, cells in enumerate(sudoku_puzzle, 1):
        map_sudoku_puzzle += '| '
        
        for j, cell in enumerate(cells, 1):
            map_sudoku_puzzle += str(cell) if cell != -1 else ' '
            map_sudoku_puzzle += ' | ' if j % 3 != 0 or j == 9 else ' || '
        
        map_sudoku_puzzle += split_line if i % 3 != 0 or i == 9 else split_line3

    return map_sudoku_puzzle

def is_valid(sudoku_puzzle, n, i, j):
    for x in range(len(sudoku_puzzle[0])):
        if n in (sudoku_puzzle[x][j], sudoku_puzzle[i][x]):
            return False

    i_square = (i // 3) * 3
    j_square = (j // 3) * 3
    for i_s in range(i_square, i_square + 1):
        for j_s in range(j_square, j_square + 3):
            if n == sudoku_puzzle[i_s][j_s]:
                return False

    return True

def find_next_empty_cell(sudoku_puzzle):
    for i, cells in enumerate(sudoku_puzzle):
        for j, cell in enumerate(cells):
            if cell == -1:
                return i, j

def solve_sudoku_puzzle(sudoku_puzzle):
    empty_cell = find_next_empty_cell(sudoku_puzzle)
    
    if not empty_cell:
        return True, sudoku_puzzle
    
    i, j = empty_cell
    for x in range(1, len(sudoku_puzzle[0]) + 1):
        if is_valid(sudoku_puzzle, x, i, j):
            sudoku_puzzle[i][j] = x
            if solve_sudoku_puzzle(sudoku_puzzle)[0]:
                return True, sudoku_puzzle
            sudoku_puzzle[i][j] = -1
        
    return False, sudoku_puzzle


if __name__ == '__main__':
    from example_sudoku_puzzles import *
    for sudoku_puzzle, sudoku_puzzle_name in ((sudoku_puzzle_easy, 'sudoku puzzle easy'),
                            (sudoku_puzzle_medium, 'sudoku puzzle medium'),
                            (sudoku_puzzle_hard, 'sudoku puzzle hard'),
                            (sudoku_puzzle_expert, 'sudoku puzzle expert'),
                            (sudoku_puzzle_evil, 'sudoku puzzle evil')):

        status, solved_sudoku_puzzle = solve_sudoku_puzzle(sudoku_puzzle_easy)

        if not status:
            print("I Can't solve this sudoku puzzle")

        print(sudoku_puzzle_name, end='')
        print(draw_sudoku_puzzle(solved_sudoku_puzzle))