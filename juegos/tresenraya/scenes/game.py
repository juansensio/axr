from src.scenes import SceneBase
from src.utils import load_image
import pygame
from pygame.locals import *
from tresenraya.objects import Board, Player


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.game_over = False

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
        player1 = Player('X')
        player2 = Player('O')
        self.board = Board(player1, player2)

    def start(self):
        self.game_over = False
        self.board.start()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True, None
            # cambiar escena
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.board.reset()
                self.background = self.initial_background.copy()
                return False, self.next
            # click en la cuadrícula
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                # coordenadas del click
                x = int(event.pos[0] // (self.size[0] / 3))
                y = int(event.pos[1] // (self.size[1] / 3))
                # pintar markers
                if self.board.update(y, x):
                    x = (x*2 + 1)*(self.size[0]/6)
                    y = (y*2 + 1)*(self.size[1]/6)
                    if self.board.current_player.marker == 'O':
                        width, height = 50, 50
                        rect = pygame.Rect(
                            x - width / 2, y - height / 2, width, height)
                        pygame.draw.rect(
                            self.background, (255, 255, 255), rect)
                    else:
                        pygame.draw.circle(
                            self.background, (255, 255, 255), (x, y), 30)
                    # check game over
                    if self.board.is_game_over():
                        # fondo transparente
                        s = pygame.Surface(self.size)
                        s.set_alpha(200)
                        s.fill((0, 0, 0))
                        self.background.blit(s, (0, 0))
                        # texto
                        font = pygame.font.Font(None, 56)
                        if self.board.current_player.marker == 'O':
                            text = font.render("You Win !", 1, (255, 0, 255))
                        else:
                            text = font.render(
                                "Game Over :(", 1, (255, 0, 255))
                        textpos = text.get_rect(
                            centerx=self.background.get_width()/2,
                            centery=self.background.get_height()/2)
                        self.background.blit(text, textpos)
                        self.game_over = True
        return False, self

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()
