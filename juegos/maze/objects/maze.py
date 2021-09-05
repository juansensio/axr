from src.utils import load_image
import pandas as pd
import pygame
import numpy as np


class Maze:
    def __init__(self,
                 level='./maze/levels/level0.csv',
                 #  size=(20, 20),
                 step=(32, 32),
                 assets_path='./maze/assets/tiles',
                 symbol2sprite={
                     '#': 'tile_0014.png',
                     '0': 'tile_0000.png',
                     '2': 'tile_0048.png',
                 }):

        # parse file with level
        level = pd.read_csv(level, header=None)
        # assert level.shape == size, 'invalid level shape'
        size = level.shape

        # check everything is ok
        assert np.all(np.unique(level.values) == list(
            symbol2sprite.keys())), 'invalid symbol'
        # assert (level.values == '2').sum() == 1, 'solo 1 casa'

        # load sprites
        self.sprites = {
            symbol: load_image(f'{assets_path}/{sprite}',
                               {'scale': [(32, 32)]}, -1)
            for symbol, sprite in symbol2sprite.items()
        }

        # create background
        screen = pygame.display.get_surface()
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        self.blocks, self.block_states = [], []
        self.terminal_states = []
        for i in range(size[0]):
            for j in range(size[1]):
                ix = level.values[i][j]
                sprite, rect = self.sprites[ix]
                rect.topleft = (step[0]*j, step[1]*i)
                if ix in ['#']:
                    self.blocks.append(rect.copy())
                    self.block_states.append(i*size[1]+j)
                if ix in ['2']:
                    self.terminal_states.append((i*size[1]+j, rect.copy()))
                background.blit(sprite, rect)
                self.background = background
        self.size = size

    def block(self, pos):
        for block in self.blocks:
            if block.contains(pos):
                return True

    def update(self, player):
        for terminal_state in self.terminal_states:
            if terminal_state[1].contains(player.rect):
                return True

    def render(self, screen):
        screen.blit(self.background, (0, 0))
