


maze = [[1, 0, 0, 0],
         [1, 1, 0, 1],
         [0, 1, 0, 0],
         [1, 1, 1, 1]]

m = n = 4
bt = [[0 for i in range(n)] for j in range(m)]


def check_valid(maze, x, y, m, n):
    if x < m and y < n and maze[x][y] == 1:
        return True
    return False


def solve_maze(maze, m, n, bt, x=0, y=0):

    # this is the terminating condition
    if x == m-1 and y == n-1:
        bt[x][y] = 1
        return True

    if check_valid(maze, x, y, m, n):
        if solve_maze(maze, m ,n , bt, x+1, y):
            bt[x+1][y] = 1
            return True

        elif solve_maze(maze, m ,n , bt, x, y+1):
            bt[x][y+1] = 1
            return True

        else:
            bt[x][y] =0
            return False

