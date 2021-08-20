import pygame


class Score():
    def __init__(self,):
        self.score = 0.
        self.font = pygame.font.Font(None, 36)

    def update(self, score):
        self.score += score

    def render(self, screen):
        text = self.font.render(
            f"Score: {self.score:.3f}", 1, (255, 255, 255))
        textpos = text.get_rect(
            centerx=700,
            centery=380
        )
        screen.blit(text, textpos)
