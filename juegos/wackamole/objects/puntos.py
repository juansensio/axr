import pygame


class Puntos():
    def __init__(self, value, pos, speed=0.005, lifetime=800):
        self.value = f"{'+' if value >= 0 else '-'} {abs(value):.3f}"
        self.start_ticks = pygame.time.get_ticks()
        self.pos = [pos[0], pos[1] - 10]
        self.speed = speed
        self.font = pygame.font.Font(None, 28)
        self.lifetime = lifetime

    def get_dt(self):
        return pygame.time.get_ticks() - self.start_ticks

    def remove(self):
        dt = self.get_dt()
        return dt >= self.lifetime

    def update(self):
        dt = self.get_dt()
        self.pos[1] = self.pos[1] - dt*self.speed
        self.alpha = 255 - dt*(255 / self.lifetime)

    def render(self, screen):
        if pygame.font:
            text = self.font.render(
                self.value,
                1,
                (255, 255, 255)  # change alpha with t
            )
            text.set_alpha(self.alpha)
            textpos = text.get_rect(
                centerx=self.pos[0],
                centery=self.pos[1]
            )
            screen.blit(text, textpos)
