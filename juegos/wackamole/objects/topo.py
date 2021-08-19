from src.utils import load_image, load_sound
import pygame


class Topo():
    def __init__(self, pos, sound):
        self.sprite1, self.rect = load_image('./wackamole/assets/topo1.png', {
            'scale': [(100, 100)]
        }, -1)
        self.rect.center = pos
        self.sprite2, _ = load_image('./wackamole/assets/topo2.png', {
            'scale': [(100, 100)]
        }, -1)

        self.sound = sound
        if sound:
            self.sound = load_sound('./wackamole/assets/sounds/click.ogg')

    def start(self):
        self.sprite = self.sprite1
        self.start_ticks = pygame.time.get_ticks()
        self.clicked = False

    def click(self):
        self.start_ticks = pygame.time.get_ticks()
        self.sprite = self.sprite2
        self.clicked = True
        if self.sound:
            self.sound.play()

    def update(self):
        if self.clicked:
            ms = (pygame.time.get_ticks() - self.start_ticks)
            if ms > 300:
                self.sprite = self.sprite1
                self.clicked = False
