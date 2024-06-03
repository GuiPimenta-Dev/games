from abc import ABC, abstractmethod
import pygame


class Figure(ABC):
    @abstractmethod
    def draw(self, row, col):
        pass


class Circle(Figure):
    def __init__(self, screen, square_size):
        self.screen = screen
        self.square_size = square_size
        self.color = (255, 0, 0)
        self.radius = square_size // 3
        self.width = 15

    def draw(self, row, col):
        x, y = int(col * self.square_size + self.square_size // 2), int(row * self.square_size + self.square_size // 2)
        pygame.draw.circle(self.screen, self.color, (x, y), self.radius, self.width)


class Cross(Figure):
    def __init__(self, screen, square_size):
        self.screen = screen
        self.square_size = square_size
        self.color = (0, 0, 255)
        self.width = 25
        self.space = self.square_size // 4

    def draw(self, row, col):
        pygame.draw.line(
            self.screen,
            self.color,
            (col * self.square_size + self.space, row * self.square_size + self.square_size - self.space),
            (col * self.square_size + self.square_size - self.space, row * self.square_size + self.space),
            self.width,
        )
        pygame.draw.line(
            self.screen,
            self.color,
            (col * self.square_size + self.space, row * self.square_size + self.space),
            (
                col * self.square_size + self.square_size - self.space,
                row * self.square_size + self.square_size - self.space,
            ),
            self.width,
        )
