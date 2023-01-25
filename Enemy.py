import pygame


class Enemy:
    
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = 5
       
       
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.bottom_edge = (self.x, self.y + self.height,
                            self.x + width, self.y)
        
        
        
    def move_left(self):
        self.x -= self.velocity
        
       

    def draw(self, window):

        pygame.draw.rect(window, self.color, pygame.Rect(
            self.x, self.y, self.width, self.height))

        pygame.draw.rect(window, (0, 255, 0), self.hitbox, 2)
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.bottom_edge = (self.x, self.y + self.height,
                            self.x + self.width, self.y)
