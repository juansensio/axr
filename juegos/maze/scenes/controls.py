from enum import Enum
import pygame


class Controls(Enum):
    UP = pygame.K_w
    DOWN = pygame.K_s
    LEFT = pygame.K_a
    RIGHT = pygame.K_d
    ALL = [UP, DOWN, LEFT, RIGHT]
