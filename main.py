import pygame
import sys
from Player import Player
from Enemy import Enemy

pygame.init()

window = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Jump !")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

score = 10
font = pygame.font.SysFont('comicsans', 30, True, True)


def redraw_window():
    window.fill(BLACK)
    text = font.render('Score : ' + str(score), 1, RED)
    window.blit(text, (350, 10))

    for enemy in enemies:
        enemy.move_left()
        enemy.draw(window)

    player.move()
    player.draw(window)
    pygame.display.update()


def game_over():
    window.fill(BLACK)
    text = font.render('Game over', 1, RED)
    window.blit(text, (350, 10))
    pygame.display.update()


player = Player(200, 400, 30, 30, GREEN)

enemies = []
enemies.append(Enemy(500, 400, 30, 30, RED))
enemies.append(Enemy(700, 400, 30, 30, RED))

run = True

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False
        pygame.quit()
        sys.exit()

    if keys[pygame.K_LEFT] and player.x > player.velocity:
        player.right = False
        player.left = True

    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.velocity:
        player.x += player.velocity
        player.left = False
        player.right = True

    if not player.is_jumping:

        if keys[pygame.K_SPACE]:
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

    for enemy in enemies:

        if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2] and not enemy.collision:
                print("hi")
                score -= 1
                enemy.collision = True

    if score <= 0:
        game_over()
    else:
        redraw_window()
