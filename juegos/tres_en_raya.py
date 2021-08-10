try:
    import sys
    import pygame
    from socket import *
    from pygame.locals import *
    from src.utils import load_sound
    from tresenraya.scenes import setup_scenes
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

SOUND = False

def main():
    # Init screen
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Tres en Raya')
    clock = pygame.time.Clock()
    # escenas
    scene = setup_scenes()
    # musica
    if SOUND:
        music = load_sound('./tresenraya/assets/music/game.wav')
        music.play()
    # Event loop
    game_over = False
    while not game_over:
        clock.tick(60)
        game_over, scene = scene.process_input()
        if not game_over:
            scene.update()
            scene.render(screen)
    if SOUND:
        music.stop()


if __name__ == '__main__':
    main()
