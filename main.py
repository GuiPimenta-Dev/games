import time
import pygame
import sys

from board import Board, SQUARE_SIZE

board = Board()
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board.is_square_available(clicked_row, clicked_col):
                board.mark_square(clicked_row, clicked_col)
                draw = board.is_draw()
                winner = board.is_winner()
                pygame.display.update()
                if draw or winner:
                  time.sleep(1)
                  board.restart()

    pygame.display.update()
