class Sudoku:
    def __init__(self):
        self.num_calls = 0
        self.guesses = 0
        self.solved = False

    def get_stats(self):
        return self.num_calls, self.guesses

    def print_board(self, board):
        for x in range(len(board)):
            print('')
            if x % 3 == 0 and x != 0:
                for y in range(11):
                    print('-', end=' ')
                print()
            for y in range(9):
                print(board[x][y], end=' ')
                if (y + 1) % 3 == 0 and (y + 1 != 9):
                    print('|', end=' ')

    def check_complete(self, board):
        for x in range(9):
            for y in range(9):
                if board[x][y] == 0:
                    return False
        self.solved = True
        return True

    def test(self, p1, p2, x, y, i, j, board, move):
        if board[i + p1][j + p2] == move:
            if x == i + p1 and y == j + p2:
                # found but on the guess
                return True
            else:
                # Found but not on the guess
                return False
        return True

    def legal_move(self, board, x, y):
        move = board[x][y]
        # check horizontal/vertical
        for c in range(9):
            if board[x][c] == move and c != y:
                return False
            if board[c][y] == move and c != x:
                return False
        if x < 3:
            if y < 3:
                for i in range(3):
                    for j in range(3):
                        if not self.test(0, 0, x, y, i, j, board, move):
                            return False
            elif 2 < y < 6:
                for i in range(3):
                    for j in range(3):
                        if not self.test(0, 3, x, y, i, j, board, move):
                            return False
            else:
                for i in range(3):
                    for j in range(3):
                        if not self.test(0, 6, x, y, i, j, board, move):
                            return False
        elif 2 < x < 6:
            if y < 3:
                for i in range(3):
                    for j in range(3):
                        if not self.test(3, 0, x, y, i, j, board, move):
                            return False
            elif 2 < y < 6:
                for i in range(3):
                    for j in range(3):
                        if not self.test(3, 3, x, y, i, j, board, move):
                            return False
            else:
                for i in range(3):
                    for j in range(3):
                        if not self.test(3, 6, x, y, i, j, board, move):
                            return False
        else:
            if y < 3:
                for i in range(3):
                    for j in range(3):
                        if not self.test(6, 0, x, y, i, j, board, move):
                            return False
            elif 2 < y < 6:
                for i in range(3):
                    for j in range(3):
                        if not self.test(6, 3, x, y, i, j, board, move):
                            return False
            else:
                for i in range(3):
                    for j in range(3):
                        if not self.test(6, 6, x, y, i, j, board, move):
                            return False
        return True

    def increment_calls(self):
        self.num_calls += 1

    def increment_guesses(self):
        self.guesses += 1

    def solve(self, board):
        self.increment_calls()
        if self.check_complete(board):
            self.print_board(board)
            return True
        for x in range(9):
            for y in range(9):
                if board[x][y] == 0:
                    for move in range(9):
                        board[x][y] = move + 1
                        self.increment_guesses()
                        if self.legal_move(board, x, y):
                            if self.solve(board):
                                return True
                    board[x][y] = 0
                    return False


game = Sudoku()
game.solve([[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]])
