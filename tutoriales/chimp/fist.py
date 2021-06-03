import pygame
from utils import load_image


class Fist(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self, fullname):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image(fullname, None, -1)
        self.punching = 0

    def update(self):
        """move the fist based on the mouse position"""
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        """returns true if the fist collides with the target"""
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """called to pull the fist back"""
        self.punching = 0
