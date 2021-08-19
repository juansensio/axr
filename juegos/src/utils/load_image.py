import os
import pygame
from pygame.locals import RLEACCEL


def load_image(fullname, trans=None, colorkey=None):
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit(message)
    if trans is not None:
        for trans, params in trans.items():
            image = getattr(pygame.transform, trans)(image, *params)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
