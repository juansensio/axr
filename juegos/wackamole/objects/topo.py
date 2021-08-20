from src.utils import load_image, load_sound
import pygame
from .puntos import Puntos


class Topo():
    def __init__(self, pos, sound, reward):
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
        self.reward = reward

    def start(self):
        self.sprite = self.sprite1
        self.start_ticks = pygame.time.get_ticks()
        self.clicked = False
        self.puntos = []

    def click(self):
        self.start_ticks = pygame.time.get_ticks()
        self.sprite = self.sprite2
        self.clicked = True
        if self.sound:
            self.sound.play()
        self.puntos.append(Puntos(self.reward, self.rect.midtop))
        return self.reward

    def update(self):
        self.puntos = [puntos for puntos in self.puntos if not puntos.remove()]
        for puntos in self.puntos:
            puntos.update()
        if self.clicked:
            ms = pygame.time.get_ticks() - self.start_ticks
            if ms > 300:
                self.sprite = self.sprite1
                self.clicked = False

    def render(self, screen):
        for puntos in self.puntos:
            puntos.render(screen)
        screen.blit(self.sprite, self.rect)
