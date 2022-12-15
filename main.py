import pygame
import sys
from Player import Player
from Camera import *
from Platform import Platform
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
    for platform in platforms:
        # platform.move()
        platform.draw(window)
    pygame.display.update()


player = Player(200, 400, 30, 30, RED)
platforms = []

for i in range(4):
    x = random.randint(1, 400)
    y = random.randint(100, 500)
    platforms.append(Platform(x, y, 50, 5, (0, 255, 0)))

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    for platform in platforms:
        if player.hitbox[1] + player.hitbox[3] > platform.hitbox[1] and player.hitbox[1] < platform.hitbox[1]:
            if player.hitbox[0] > platform.hitbox[0] and player.hitbox[0] < platform.hitbox[0] + platform.hitbox[2]:
                print('hi')
                print(player.hitbox[0])
                print(platform.hitbox[0] + platform.hitbox[2])
                player.stop(platform.x, platform.y)

        if player.on_platform:
            if player.hitbox[0] > platform.hitbox[0] + platform.hitbox[2]:
                player.is_falling = True

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
            print(platforms[0].top_edge[1])
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
