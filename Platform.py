import pygame


class Platform:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = 1
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.top_edge = (self.x, self.y, self.x + width, self.y)

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(
            self.x, self.y, self.width, self.height))

        self.top_edge = (self.x, self.y, self.x + self.width, self.y)

    def move(self):
        self.y += self.velocity
