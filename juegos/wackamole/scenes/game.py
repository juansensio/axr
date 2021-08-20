from .scenes import Scenes
from src.scenes import SceneBase
import pygame
from pygame.locals import *
import numpy as np
from ..objects import Topo
from ..objects.players import Players
from ..objects.agents import AgentEGreedy, AgentGradientAscent, AgentUCB
from ..objects.score import Score
from ..objects.timer import Timer


class GameScene(SceneBase):
    def __init__(self,
                 player=Players.HUMAN,
                 bg_img='./wackamole/assets/bgs/bg.png',
                 seed=42,
                 t_game=10,
                 epsilon=0.1,
                 alpha=0.5,
                 c=0.5,
                 ms_per_click=200,
                 verbose=True,
                 q0=0,
                 sound=True,
                 ):
        super().__init__(bg_img)

        # topos
        positions = [
            (150, 150),
            (250, 265),
            (390, 80),
            (490, 190),
            (670, 140),
        ]
        # inicializar puntos
        np.random.seed(seed)
        mu, sigma = 0, 1
        q = np.random.normal(mu, sigma, 5)
        # topos
        self.topos = [Topo(p, sound, reward)
                      for p, reward in zip(positions, q)]
        self.t_game = t_game
        self.player = player
        self.agent = None
        self.verbose = verbose
        # instanciar agente axr
        if self.player == Players.AGENT_E_GREEDY:
            self.agent = AgentEGreedy(
                ms_per_click, epsilon, alpha, q0, verbose)
        elif self.player == Players.AGENT_UCB:
            self.agent = AgentUCB(ms_per_click, alpha, c, q0, verbose)
        elif self.player == Players.AGENT_GRADIENT_ASCENT:
            self.agent = AgentGradientAscent(ms_per_click, alpha, verbose)

    def start(self):
        self.game_over = False
        self.score = Score()
        self.timer = Timer(self.t_game)
        for topo in self.topos:
            topo.start()
        if self.agent:
            self.agent.start()
        self.t = 1

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
            # cambiar escena
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                scene_manager.update(Scenes.MENU)
                return False
            # clicks
            elif event.type == MOUSEBUTTONDOWN and not self.game_over and self.player == Players.HUMAN:
                mouse_pos = event.pos
                for ix, topo in enumerate(self.topos):
                    if topo.rect.collidepoint(mouse_pos):
                        reward = topo.click()
                        self.score.update(reward)
                        return False
        return False

    def update(self):
        if not self.game_over:
            self.game_over = self.timer.update()
            if self.agent:
                a = self.agent.click(self.t)
                if a is not None:
                    self.t += 1
                    reward = self.topos[a].click()
                    if self.verbose:
                        print("turno", self.t)
                        print("q", [topo.reward for topo in self.topos])
                    self.agent.update(a, reward)
                    self.score.update(reward)
        for topo in self.topos:
            topo.update()

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        self.score.render(screen)
        self.timer.render(screen)
        for topo in self.topos:
            topo.render(screen)
        pygame.display.flip()
