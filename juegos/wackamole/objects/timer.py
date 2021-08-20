import pygame


class Timer():
    def __init__(self, t_game):
        self.time = t_game
        self.font = pygame.font.Font(None, 36)
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks)/1000
        if seconds > 1:
            self.time -= 1
            self.start_ticks = pygame.time.get_ticks()
            if self.time <= 0:
                return True
        return False

    def render(self, screen):
        text = self.font.render(
            f"Time: {self.time}", 1, (255, 255, 255))
        textpos = text.get_rect(
            centerx=60,
            centery=20
        )
        screen.blit(text, textpos)
