from src.scenes import SceneBase
from src.utils import load_image
import pygame
from pygame.locals import *
from tresenraya.objects import Game, Player, Agent


class GameScene(SceneBase):
    def __init__(self, agente="./tresenraya/assets/agente.pickle"):
        SceneBase.__init__(self)
        self._game_over = False

        # background
        screen = pygame.display.get_surface()
        size = screen.get_size()
        background = pygame.Surface(size)
        background = background.convert()
        background.fill((0, 0, 0))

        # cuadrícula
        rect_width, rect_height = 5, 5
        for i in range(2):
            rect = pygame.Rect(
                (i+1)*(size[0] / 3) - 0.5*rect_width, 0, rect_width, size[1])
            pygame.draw.rect(background, (255, 255, 255), rect)
            rect = pygame.Rect(
                0, (i+1)*(size[1] / 3) - 0.5*rect_height, size[0], rect_height)
            pygame.draw.rect(background, (255, 255, 255), rect)
        self.initial_background = background
        self.background = self.initial_background.copy()
        self.size = size

        # objects
        self.player = Player()
        self.agent = Agent(agente)
        self.game = Game(self.player, self.agent)

    def start(self):
        self._game_over = False
        self.game.reset()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True, None
            # cambiar escena
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.game.reset()
                self.background = self.initial_background.copy()
                return False, self.next
            # click en la cuadrícula
            elif event.type == pygame.MOUSEBUTTONDOWN and not self._game_over:
                # coordenadas del click
                x = int(event.pos[0] // (self.size[0] / 3))
                y = int(event.pos[1] // (self.size[1] / 3))
                self.game.update(self.player.symbol, y, x)
                
                # pintar markers
                x = (x*2 + 1)*(self.size[0]/6)
                y = (y*2 + 1)*(self.size[1]/6)
                
                # player 1
                width, height = 50, 50
                rect = pygame.Rect(
                    x - width / 2, y - height / 2, width, height)
                pygame.draw.rect(
                    self.background, (255, 255, 255), rect)

                if self.game.is_game_over() == self.player.symbol:
                    self.game_over("You Win !")
                    break

                if self.game.is_game_over() == 0:
                    self.game_over("It's a draw")
                    break

                # player 2
                y, x = self.game.agent_move()
                self.game.update(self.agent.symbol, y, x)

                x = (x*2 + 1)*(self.size[0]/6)
                y = (y*2 + 1)*(self.size[1]/6)

                pygame.draw.circle(
                    self.background, (255, 255, 255), (x, y), 30)
                
                if self.game.is_game_over() == self.agent.symbol:
                    self.game_over("Game Over :(")
                    break
                    
        return False, self

    def game_over(self, msg):
        self._game_over = True
        # fondo transparente
        s = pygame.Surface(self.size)
        s.set_alpha(200)
        s.fill((0, 0, 0))
        self.background.blit(s, (0, 0))
        # texto
        font = pygame.font.Font(None, 56)
        text = font.render(msg, 1, (255, 0, 255))
        textpos = text.get_rect(
            centerx=self.background.get_width()/2,
            centery=self.background.get_height()/2)
        self.background.blit(text, textpos)

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()


