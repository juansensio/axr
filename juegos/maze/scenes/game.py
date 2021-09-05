from ..objects.maze import Maze
from ..objects.player import Player
from ..objects.agent import Agent
from .scenes import Scenes
from src.scenes import SceneBase
import pygame
from pygame.locals import *
import numpy as np
from .controls import Controls


class GameScene(SceneBase):
    def __init__(self, agent=False, its=0, level='level0.csv', verbose=False, pos=(3, 3)):
        super().__init__()
        self.maze = Maze(f'./maze/levels/{level}')
        self.agent = False
        if agent:
            self.agent = True
            self.player = Agent(self.maze, its, pos=pos, verbose=verbose)
        else:
            self.player = Player(pos=pos)

    def start(self):
        self.player.start()

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True

            if not self.agent:
                if event.type == pygame.KEYDOWN:
                    # cambio escena
                    if event.key == pygame.K_RETURN:
                        scene_manager.update(Scenes.MENU)
                    # movimiento jugador
                    elif event.key == Controls.UP.value:
                        self.player.move_up()
                    elif event.key == Controls.DOWN.value:
                        self.player.move_down()
                    elif event.key == Controls.LEFT.value:
                        self.player.move_left()
                    elif event.key == Controls.RIGHT.value:
                        self.player.move_right()
                    return False
                elif event.type == pygame.KEYUP:
                    if event.key in Controls.ALL.value:
                        self.player.stop()
                    return False
        return False

    def update(self, scene_manager):
        self.player.update(self.maze)
        if self.maze.update(self.player):
            scene_manager.update(Scenes.MENU)

    def render(self, screen):
        self.maze.render(screen)
        self.player.render(screen)
        pygame.display.flip()
