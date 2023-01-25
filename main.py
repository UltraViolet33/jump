import pygame
import sys
from Player import Player
import random

pygame.init()

window = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Doodle Clone")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)

def redraw_window():
    window.fill(BLACK)

    player.move()
    player.draw(window)
    
    pygame.display.update()


player = Player(200, 400, 30, 30, RED)
platforms = []



run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.velocity:
        player.right = False
        player.left = True

    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.velocity:
        player.x += player.velocity
        player.left = False
        player.right = True

    if not player.is_jumping:

        if keys[pygame.K_SPACE]:
          
            print(player.bottom_edge[1])
            player.is_jumping = True

    else:
        if player.jump_count >= -10:
            neg = 1
            if player.jump_count < 0:
                neg = -1
            player.y -= (player.jump_count ** 2) * 0.5 * neg
            player.jump_count -= 1
        else:
            player.is_jumping = False
            player.jump_count = 10

    redraw_window()
