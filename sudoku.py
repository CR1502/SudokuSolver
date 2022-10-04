M = 9 

def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end = " ")
        print()

def solve(grid, row , col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
        
    for x in range(9):
        if grid[x][col] == num:
            return False
        
    StartRow = row - row % 3
    StartCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + StartRow][j + StartCol] == num:
                return False
    return True

def Suduko(grid, row, col):
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)

    for num in  range(1, M + 1, 1):

        if solve(grid, row, col, num):
            grid[row][col] = num

            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


grid = [[7, 9, 1, 3, 0, 5, 0, 0, 0],
        [0, 0, 5, 6, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 6, 0],
        [1, 0, 2, 5, 0, 4, 9, 0, 3],
        [0, 7, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 1, 8, 0, 0],
        [0, 0, 0, 2, 0, 6, 5, 1, 9]]

if(Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("No solution.")