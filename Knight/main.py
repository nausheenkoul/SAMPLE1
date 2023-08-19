def is_valid_move(board, x, y, N):
    if x >= 0 and y >= 0 and x < N and y < N and board[x][y] == -1:
        return True
    return False


def solve_knights_tour(board, N, x, y, move_count):
    if move_count == N * N:
        return True

    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(8):
        next_x = x + x_moves[i]
        next_y = y + y_moves[i]

        if is_valid_move(board, next_x, next_y, N):
            board[next_x][next_y] = move_count
            if solve_knights_tour(board, N, next_x, next_y, move_count + 1):
                return True
            board[next_x][next_y] = -1

    return False


def print_board(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end="\t")
        print()


N = int(input("Enter the board size (NxN): "))
start_x, start_y = map(int, input("Enter the starting position (row column): ").split())

board = [[-1 for _ in range(N)] for _ in range(N)]
board[start_x][start_y] = 0

if solve_knights_tour(board, N, start_x, start_y, 1):
    print("Solution exists:")
    print_board(board, N)
else:
    print("No solution exists.")
