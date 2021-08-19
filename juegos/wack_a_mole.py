try:
    import sys
    import pygame
    from pygame.locals import *
    from wackamole.scenes import SceneManager
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
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Wack A Mole')
    clock = pygame.time.Clock()
    scene_manager = SceneManager(args)
    game_over = False
    while not game_over:
        clock.tick(60)
        game_over = scene_manager.current_scene.process_input(scene_manager)
        scene_manager.current_scene.update()
        scene_manager.current_scene.render(screen)
    scene_manager.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wack-A-Mole opciones.')
    parser.add_argument('-e', metavar='e', type=int, default=1,
                        choices=[1, 2, 3], help='escena inicial')
    parser.add_argument('-m', action='store_false',
                        default=True, help='sin música')
    parser.add_argument('-a', metavar='a', type=int, default=1,
                        choices=[1, 2, 3, 4], help='jugador')
    parser.add_argument('-eps', metavar='eps', type=float, default=0.1,
                        help='epsilon')
    parser.add_argument('-alpha', metavar='alpha', type=float, default=0.5,
                        help='alpha')
    parser.add_argument('-s', metavar='s', type=int, default=42,
                        help='seed')
    parser.add_argument('-v', action='store_true',
                        default=False, help='verbose')
    parser.add_argument('-q',  metavar='q', type=float, default=0,
                        help='initial q value for e-greedy agents')
    parser.add_argument('-c',  metavar='c', type=float, default=0.5,
                        help='UCB c param')
    parser.add_argument('-mspa',  metavar='mspa', type=int, default=200,
                        help='miliseconds per action')
    parser.add_argument('-t',  metavar='t', type=int, default=10,
                        help='game duration in seconds')
    args = parser.parse_args()
    main(args)
