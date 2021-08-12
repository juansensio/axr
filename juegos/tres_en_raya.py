try:
    import sys
    import pygame
    from pygame.locals import *
    from tresenraya.scenes import SceneManager
    import argparse
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


def main(args):
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Tres en Raya')
    clock = pygame.time.Clock()
    scene_manager = SceneManager(initial_scene=args.e, music=args.m)
    game_over = False
    while not game_over:
        clock.tick(60)
        game_over = scene_manager.current_scene.process_input(scene_manager)
        scene_manager.current_scene.render(screen)
    scene_manager.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tres en Raya opciones.')
    parser.add_argument('-e', metavar='e', type=int, default=1, choices=[1,2,3], help='escena inicial')
    parser.add_argument('-m', action='store_false', default=True, help='sin música')
    args = parser.parse_args()
    main(args)
