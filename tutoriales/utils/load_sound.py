import pygame

class NoneSound:
    def play(self): 
        pass
        
def load_sound(fullname):
    print(pygame.mixer.get_init())
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print("Cannot load sound: %s" % fullname)
        raise SystemExit(str(geterror()))
    return sound