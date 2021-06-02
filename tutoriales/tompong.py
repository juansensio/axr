try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
    from tompong import Ball, Bat
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption('TomPong')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    speed = 3
    rand = ((0.1 * (random.randint(5, 8))))
    ball = Ball('data/intro_ball.gif', (0.47, speed))
    ballsprite = pygame.sprite.RenderPlain(ball)

    player1 = Bat("left")
    player2 = Bat("right")
    playersprites = pygame.sprite.RenderPlain((player1, player2))

    clock = pygame.time.Clock()

    # Event loop
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    player1.moveup()
                if event.key == K_z:
                    player1.movedown()
                if event.key == K_UP:
                    player2.moveup()
                if event.key == K_DOWN:
                    player2.movedown()
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_z:
                    player1.movepos = [0, 0]
                    player1.state = "still"
                if event.key == K_UP or event.key == K_DOWN:
                    player2.movepos = [0, 0]
                    player2.state = "still"

        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, player1.rect, player1.rect)
        screen.blit(background, player2.rect, player2.rect)

        ballsprite.update(player1, player2)
        playersprites.update()

        ballsprite.draw(screen)
        playersprites.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
