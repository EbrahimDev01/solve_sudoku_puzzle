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