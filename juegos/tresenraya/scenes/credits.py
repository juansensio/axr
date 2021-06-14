from src.scenes import SceneBase
from src.utils import load_image
import pygame
from pygame.locals import *


class Credits(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        screen = pygame.display.get_surface()
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))

        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render(
                "Tres en raya \n by Juan Sensio", 1, (255, 255, 255))
            textpos = text.get_rect(
                centerx=background.get_width()/2,
                centery=background.get_height()/2
            )
            background.blit(text, textpos)

        self.background = background

    def process_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True, None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return False, self.next
        return False, self

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()
