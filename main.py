import pygame
import sys
from Player import Player

pygame.init()

window = pygame.display.set_mode((500, 480))


pygame.display.set_caption("Doodle Clone")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)


def redraw_window():
    window.fill(BLACK)
    player.draw(window)
    pygame.display.update()

player = Player(200, 400, 30, 30, RED)

run = True

while run:
    clock.tick(27)
    
    # player.y -= player.velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player.x > player.velocity:
        player.x -= player.velocity
    
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.velocity:
        player.x += player.velocity

    redraw_window()
