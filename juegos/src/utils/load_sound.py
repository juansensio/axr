import pygame


class NoneSound:
    def play(self):
        pass


def load_sound(fullname):
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    try:
        sound = pygame.mixer.Sound(fullname)
        #sound = pygame.mixer.music.load(fullname)
    except pygame.error as err:
        print("Cannot load sound: %s" % fullname)
        raise SystemExit(str(err))
    return sound
