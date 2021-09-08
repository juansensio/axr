try:
    import sys
    import pygame
    from pygame.locals import *
    from maze.scenes import SceneManager
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
    # tiles de 16x16 (a x2, 32x32, 15x15 tiles)
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption('Maze')
    clock = pygame.time.Clock()
    scene_manager = SceneManager(args)
    game_over = False
    while not game_over:
        clock.tick(10)
        game_over = scene_manager.current_scene.process_input(scene_manager)
        scene_manager.current_scene.update(scene_manager)
        scene_manager.current_scene.render(screen)
    scene_manager.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wack-A-Mole opciones.')
    parser.add_argument('-e', metavar='e', type=int, default=1,
                        choices=[1, 2, 3], help='escena inicial')
    parser.add_argument('-m', action='store_false',
                        default=True, help='sin música')
    parser.add_argument('-a', action='store_true',
                        default=False, help='agente axr')
    parser.add_argument('-v', action='store_true',
                        default=False, help='verbose')
    parser.add_argument('-its', type=int, default=20, help="value iterations")
    parser.add_argument(
        '-l', type=str, default='level0.csv', help="level file")
    parser.add_argument(
        '-p', type=int, nargs='+', default=(7, 7), help="initial position")
    args = parser.parse_args()
    main(args)
