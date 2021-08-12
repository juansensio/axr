from .scenes import Scenes
from src.scenes import SceneBase
from src.utils import load_image
import pygame
from pygame.locals import *


class StartMenu(SceneBase):
    def __init__(self):
        super().__init__()

        btns_path = './tresenraya/assets/buttons/'
        start_btn, rect = load_image(f'{btns_path}/start.png')
        credits_btn, credits_rect = load_image(
            f'{btns_path}/credits.png')

        screen = pygame.display.get_surface()
        area = screen.get_rect()
        rect.center = area.center
        credits_rect.midbottom = area.midbottom
        self.background.blit(start_btn, rect)
        self.background.blit(credits_btn, credits_rect)

        self.game_rect = rect
        self.credits_rect = credits_rect

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                scene_manager.update(Scenes.GAME)
                return False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.game_rect.collidepoint(mouse_pos):
                    scene_manager.update(Scenes.GAME)
                    return False
                if self.credits_rect.collidepoint(mouse_pos):
                    scene_manager.update(Scenes.CREDITS)
                    return False
        return False

        