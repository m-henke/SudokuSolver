import pygame
import time
from SudokuClass import Sudoku

pygame.init()
WINDOW_SIZE = [306, 306]
WIDTH = HEIGHT = 28
MARGIN = 5
ROWS = COLS = 9
FPS = 60

FONT = pygame.font.Font('falling-sky-font/FallingSky-JKwK.otf', 32)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Sudoku')

GAME_BOARD = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def get_color(x, y, r, c):
    if r < x:
        return 'green'
    if r == x and c <= y:
        if r == x and x == y:
            return 'red'
        return 'green'
    return 'white'


def draw_board(win, grid, x, y, done):
    win.fill(BLACK)
    for row in range(9):
        for column in range(9):
            color = get_color(x, y, row, column)
            color = 'green' if done else color
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            # draw number
            num = str(grid[row][column])
            if num == '0':
                num = ''
            text = FONT.render(num, True, BLUE)
            win.blit(text, [((MARGIN + WIDTH) * column + MARGIN) + 6,
                            ((MARGIN + HEIGHT) * row + MARGIN) - 5,
                            WIDTH,
                            HEIGHT])


def visual_solve(board, game):
    game.increment_calls()
    if game.check_complete(board):
        return True
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for move in range(9):
                    board[x][y] = move + 1
                    game.increment_guesses()
                    if game.legal_move(board, x, y):
                        time.sleep(.004)
                        draw_board(screen, board, x, y, False)
                        pygame.display.update()
                        if visual_solve(board, game):
                            return True
                board[x][y] = 0
                return False


def main():
    run = True
    clock = pygame.time.Clock()
    solved = False
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = Sudoku()
                    solved = visual_solve(GAME_BOARD, game)
                    print(f'It took {game.num_calls} recursive calls,'
                          f' and {game.guesses} guesses to solve.')
                if event.key == pygame.K_ESCAPE:
                    run = False
        draw_board(screen, GAME_BOARD, -1, -1, solved)
        pygame.display.update()
    pygame.quit()


main()
