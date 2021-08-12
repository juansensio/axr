import pygame
from pygame.locals import *

class SceneBase:
    def __init__(self):
        
        # fondo negro del mismo tamaño que la pantalla
        screen = pygame.display.get_surface()
        background = pygame.Surface(screen.get_size())
        background = background.convert()
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
        
    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()
