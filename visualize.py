import pygame
import time
import math
from SudokuClass import Sudoku


pygame.init()
WINDOW_SIZE = [300, 300]
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

# GAME_BOARD = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#               [6, 0, 0, 1, 9, 5, 0, 0, 0],
#               [0, 9, 8, 0, 0, 0, 0, 6, 0],
#               [8, 0, 0, 0, 6, 0, 0, 0, 3],
#               [4, 0, 0, 8, 0, 3, 0, 0, 1],
#               [7, 0, 0, 0, 2, 0, 0, 0, 6],
#               [0, 6, 0, 0, 0, 0, 2, 8, 0],
#               [0, 0, 0, 4, 1, 9, 0, 0, 5],
#               [0, 0, 0, 0, 8, 0, 0, 7, 9]]
# GAME_BOARD = [[0, 0, 5, 3, 0, 0, 0, 0, 0],
#               [8, 0, 0, 0, 0, 0, 0, 2, 0],
#               [0, 7, 0, 0, 1, 0, 5, 0, 0],
#               [4, 0, 0, 0, 0, 5, 3, 0, 0],
#               [0, 1, 0, 0, 7, 0, 0, 0, 6],
#               [0, 0, 3, 2, 0, 0, 0, 8, 0],
#               [0, 6, 0, 5, 0, 0, 0, 0, 9],
#               [0, 0, 4, 0, 0, 0, 0, 3, 0],
#               [0, 0, 0, 0, 0, 9, 7, 0, 0]]
GAME_BOARD = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def draw_board(win, grid, x, y):
    win.fill(BLACK)
    for row in range(9):
        for column in range(9):
            color = WHITE
            if x != -1 and y != -1:
                if row == x and column == y:
                    color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
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
                        # time.sleep(.04)
                        draw_board(screen, board, x, y)
                        pygame.display.update()
                        if visual_solve(board, game):
                            return True
                board[x][y] = 0
                return False


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(math.floor((pos[0] - MARGIN) / WIDTH), end=', ')
                print(math.floor((pos[1] - MARGIN) / HEIGHT))
                y_pos = math.floor((pos[0] - MARGIN) / WIDTH)
                x_pos = math.floor((pos[1] - MARGIN) / HEIGHT)
                GAME_BOARD[x_pos][y_pos] = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = Sudoku()
                    visual_solve(GAME_BOARD, game)
                if event.key == pygame.K_ESCAPE:
                    run = False
        draw_board(screen, GAME_BOARD, -1, -1)
        pygame.display.update()
    pygame.quit()


main()
