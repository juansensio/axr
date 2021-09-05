import pygame
from pygame.locals import *
from src.utils import load_image


class SceneBase:
    def __init__(self, bg_image=None):

        screen = pygame.display.get_surface()
        background = pygame.Surface(screen.get_size())
        background = background.convert()

        if bg_image:
            bg, rect = load_image(bg_image)
            background.blit(bg, rect)
        else:
            # fondo negro del mismo tamaño que la pantalla
            background.fill((0, 0, 0))

        self.background = background

    def start(self):
        pass

    def stop(self):
        pass

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
        return False

    def update(self, scene_manager):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()
