from .scenes import Scenes
from src.scenes import SceneBase
import pygame
from pygame.locals import *


class Credits(SceneBase):
    def __init__(self):
        super().__init__()

        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render(
                "Maze \n by Janus Noise", 1, (255, 255, 255))
            textpos = text.get_rect(
                centerx=self.background.get_width()/2,
                centery=self.background.get_height()/2
            )
            self.background.blit(text, textpos)

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                scene_manager.update(Scenes.MENU)
                return False
        return False
