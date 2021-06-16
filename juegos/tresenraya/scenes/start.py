from src.scenes import SceneBase
from src.utils import load_image
import pygame
from pygame.locals import *


class StartMenu(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        btns_path = './tresenraya/assets/buttons/'
        start_btn, rect = load_image(f'{btns_path}/start.png')
        credits_btn, credits_rect = load_image(
            f'{btns_path}/credits.png')

        screen = pygame.display.get_surface()
        area = screen.get_rect()
        rect.center = area.center
        credits_rect.midbottom = area.midbottom
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        background.blit(start_btn, rect)
        background.blit(credits_btn, credits_rect)

        self.background = background
        self.rect = rect
        self.credits_rect = credits_rect
        self.render(screen)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True, None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.next.start()
                return False, self.next
            elif event.type == MOUSEBUTTONDOWN:
                # Now it will have the coordinates of click point.
                mouse_pos = event.pos
                if self.rect.collidepoint(mouse_pos):
                    self.next.start()
                    return False, self.next
                if self.credits_rect.collidepoint(mouse_pos):
                    return False, self.credits
        return False, self

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()
