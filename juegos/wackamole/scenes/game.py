from pygame.display import update
from .scenes import Scenes
from src.scenes import SceneBase
import pygame
from pygame.locals import *
from ..objects import Topo
import numpy as np
from ..objects.players import Players
from ..objects.agents import AgentEGreedy, AgentGradientAscent, AgentUCB


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
        np.random.seed(seed)
        mu, sigma = 0, 1
        self.q = {k: v for k, v in enumerate(np.random.normal(mu, sigma, 5))}
        self.topos = [Topo(p, sound) for p in positions]
        self.t_game = t_game
        self.player = player
        self.agent = None
        self.verbose = verbose
        self.t = 1
        if self.player == Players.AGENT_E_GREEDY:
            self.agent = AgentEGreedy(
                ms_per_click, epsilon, alpha, q0, verbose)
        elif self.player == Players.AGENT_UCB:
            self.agent = AgentUCB(ms_per_click, alpha, c, q0, verbose)
        elif self.player == Players.AGENT_GRADIENT_ASCENT:
            self.agent = AgentGradientAscent(ms_per_click, alpha, verbose)

    def start(self):
        self.game_over = False
        self.score = 0
        self.time = self.t_game
        self.start_ticks = pygame.time.get_ticks()
        for topo in self.topos:
            topo.start()
        if self.agent:
            self.agent.start()
            self.agent_last_click = pygame.time.get_ticks()

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
                        topo.click()
                        self.update_score(self.q[ix])
                        return False
        return False

    def update(self):
        if not self.game_over:
            self.update_timer()
            if self.agent:
                ms = (pygame.time.get_ticks() - self.agent_last_click)
                if ms > self.agent.ms_per_click:
                    self.agent_last_click = pygame.time.get_ticks()
                    a = self.agent.get_action(self.t)
                    self.t += 1
                    self.topos[a].click()
                    reward = self.q[a]
                    if self.verbose:
                        print("turno", self.t)
                        print("q", self.q)
                    self.agent.update(a, reward)
                    self.update_score(reward)
        for topo in self.topos:
            topo.update()

    def update_score(self, score):
        self.score += score

    def update_timer(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks)/1000
        if seconds > 1:
            self.time -= 1
            self.start_ticks = pygame.time.get_ticks()
            if self.time <= 0:
                self.game_over = True

    def render(self, screen):
        # render bg
        screen.blit(self.background, (0, 0))
        # render topos
        for topo in self.topos:
            screen.blit(topo.sprite, topo.rect)
        # render score
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render(
                f"Score: {self.score:.3f}", 1, (255, 255, 255))
            textpos = text.get_rect(
                centerx=700,
                centery=380
            )
            screen.blit(text, textpos)
            # render timer
            font = pygame.font.Font(None, 36)
            text = font.render(
                f"Time: {self.time}", 1, (255, 255, 255))
            textpos = text.get_rect(
                centerx=60,
                centery=20
            )
            screen.blit(text, textpos)
        # render
        pygame.display.flip()
