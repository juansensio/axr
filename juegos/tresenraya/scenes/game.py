from .scenes import Scenes
from src.scenes import SceneBase
import pygame
from pygame.locals import *
from tresenraya.objects import Player, Agent, Board


class GameScene(SceneBase):
    def __init__(self, agente="./tresenraya/assets/agente.pickle"):
        super().__init__()
        self._game_over = False

        # cuadrícula
        screen = pygame.display.get_surface()
        size = screen.get_size()
        rect_width, rect_height = 5, 5
        for i in range(2):
            rect = pygame.Rect(
                (i+1)*(size[0] / 3) - 0.5*rect_width, 0, rect_width, size[1])
            pygame.draw.rect(self.background, (255, 255, 255), rect)
            rect = pygame.Rect(
                0, (i+1)*(size[1] / 3) - 0.5*rect_height, size[0], rect_height)
            pygame.draw.rect(self.background, (255, 255, 255), rect)
        
        self.initial_background = self.background
        self.background = self.initial_background.copy()
        self.size = size

        # objects
        self.player = Player()
        self.agent = Agent(agente)
        self.board = Board()

    def start(self):
        self._game_over = False
        self.board.reset()
        self.background = self.initial_background.copy()

    def grid2pixels(self, x, y):
        x = (x*2 + 1)*(self.size[0]/6)
        y = (y*2 + 1)*(self.size[1]/6)
        return x, y

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
            # cambiar escena
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:                
                scene_manager.update(Scenes.MENU)
                return False
            # click en la cuadrícula
            elif event.type == pygame.MOUSEBUTTONDOWN and not self._game_over:
                # coordenadas del click
                x = int(event.pos[0] // (self.size[0] / 3))
                y = int(event.pos[1] // (self.size[1] / 3))
                # movimiento jugador
                if (y, x) in self.board.valid_moves():
                    self.board.update(self.player.symbol, y, x)
                    self.update_board(x, y)
                    # comprobar si jugador 1 ha ganado o hay empate
                    if self.board.is_game_over() == self.player.symbol:
                        self.game_over("You Win !")
                        break
                    if self.board.is_game_over() == 0:
                        self.game_over("It's a draw")
                        break
                    # mueve el agente
                    #time.sleep(random.random() + 1.)
                    y, x = self.agent.move(self.board)
                    self.board.update(self.agent.symbol, y, x)
                    self.update_board(x, y)
                    if self.board.is_game_over() == self.agent.symbol:
                        self.game_over("Game Over :(")
                return False
        return False

    def update_board(self, j, i):
        # pintar marcadores
        x, y = self.grid2pixels(j, i)
        state = self.board.state[i, j]
        if state == -1:
            width, height = 50, 50
            rect = pygame.Rect(
                x - width / 2, y - height / 2, width, height)
            pygame.draw.rect(
                self.background, (255, 255, 255), rect)
        elif state == 1:
            pygame.draw.circle(self.background, (255, 255, 255), (x, y), 30)

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

