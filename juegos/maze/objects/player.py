from src.utils import load_image
import pygame


class Player:
    def __init__(self, pos=(0, 0), step=(32, 32), sprite="./maze/assets/sprites/character0.png"):
        self.step = step
        self.sprite, self.rect = load_image(sprite, {'scale': [(32, 32)]}, -1)
        self.init_pos = (pos[0]*step[0], pos[1]*step[1])
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.start_ticks = pygame.time.get_ticks()

    def start(self):
        self.rect.topleft = self.init_pos
        self._speed = (0, 0)

    def move_right(self):
        self._speed = (self.step[0], 0)

    def move_left(self):
        self._speed = (-self.step[0], 0)

    def move_up(self):
        self._speed = (0, -self.step[1])

    def move_down(self):
        self._speed = (0, self.step[1])

    def stop(self):
        self._speed = (0, 0)

    def update(self, maze):
        newpos = self.rect.move((self._speed[0], self._speed[1]))
        if not self.area.contains(newpos):
            self.stop()
        if maze.block(newpos):
            self.stop()
        else:
            self.rect = newpos

    def render(self, screen):
        screen.blit(self.sprite, self.rect)
