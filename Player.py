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
        self.is_jumping = False
        self.jump_count = 10
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.bottom_edge = (self.x, self.y + self.height,
                            self.x + width, self.y)
        self.on_platform = False
        self.is_falling = False

    def draw(self, window):

        pygame.draw.rect(window, self.color, pygame.Rect(
            self.x, self.y, self.width, self.height))

        pygame.draw.rect(window, (0, 255, 0), self.hitbox, 2)
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.bottom_edge = (self.x, self.y + self.height,
                            self.x + self.width, self.y)

    def move(self):
        if self.left:
            self.x -= self.velocity
            self.left = False
        elif self.right:
            self.x += self.velocity
            self.right = False

    def stop(self, x, y):
        self.on_platform = True
        self.is_falling = False
        self.is_jumping = False
        self.x = x
        self.y = y - self.height
        self.jump_count = 10
