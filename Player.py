import pygame


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = 5
        self.left = False
        self.right = False

    def draw(self, window):
        
        pygame.draw.rect(window, self.color, pygame.Rect(
            self.x, self.y, self.width, self.height))
