import pygame

import pygame

from figures import Circle, Cross


pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)


class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(BG_COLOR)
        pygame.display.set_caption("Tic Tac Toe")
        self.board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turn = 1
        self.draw_lines()

    def draw_lines(self):
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def is_square_available(self, row, col):
        return self.board[row][col] == 0

    def mark_square(self, row, col):
        figure = Circle(self.screen, SQUARE_SIZE) if self.turn == 1 else Cross(self.screen, SQUARE_SIZE)
        self.board[row][col] = figure
        self.turn =  self.turn % 2 + 1
        self.draw_figures()

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(row, col)      

    def is_draw(self):
      for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
          if self.board[row][col] == 0:
            return False
      return True
    
    def is_winner(self):
      print(self.board)
      for col in range(BOARD_COLS):
        if type(self.board[0][col]) == type(self.board[1][col]) == type(self.board[2][col]) and self.board[0][col] != 0:
          self.draw_vertical_winning_line(col, self.board[0][col])
          return True
      
      for row in range(BOARD_ROWS):
        if type(self.board[row][0]) == type(self.board[row][1]) == type(self.board[row][2]) and self.board[row][0] != 0:
          self.draw_horizontal_winning_line(row, self.board[row][0])
          return True
      
      if type(self.board[2][0]) == type(self.board[1][1]) == type(self.board[0][2]) and self.board[2][0] != 0:
        self.draw_asc_diagonal(self.board[2][0])
        return True
      
      if type(self.board[0][0]) == type(self.board[1][1]) == type(self.board[2][2]) and self.board[0][0] != 0:
        self.draw_desc_diagonal(self.board[0][0])
        return True
    
    def draw_vertical_winning_line(self, col, figure):
      posX = col * SQUARE_SIZE + SQUARE_SIZE//2
      pygame.draw.line(self.screen, figure.color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

    def draw_horizontal_winning_line(self, row, figure):
        posY = row * SQUARE_SIZE + SQUARE_SIZE//2
        pygame.draw.line(self.screen, figure.color, (15, posY), (WIDTH - 15, posY), LINE_WIDTH)

    def draw_asc_diagonal(self, figure):
        pygame.draw.line(self.screen, figure.color, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)

    def draw_desc_diagonal(self, figure):
        pygame.draw.line(self.screen, figure.color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)
    
    def restart(self):
      self.screen.fill(BG_COLOR)
      self.draw_lines()
      self.turn = 1
      for row in range(BOARD_ROWS):
          for col in range(BOARD_COLS):
              self.board[row][col] = 0