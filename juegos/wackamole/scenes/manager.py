from .start import StartMenu
from .game import GameScene
from .credits import Credits
from .scenes import Scenes
from src.utils import load_sound
from ..objects.players import Players


class SceneManager():

    def __init__(self, args):

        # escenas
        scenes = {}
        scenes[Scenes.MENU] = StartMenu()
        scenes[Scenes.GAME] = GameScene(
            player=Players(args.a),
            epsilon=args.eps,
            alpha=args.alpha,
            seed=args.s,
            verbose=args.v,
            q0=args.q,
            c=args.c,
            ms_per_click=args.mspa,
            t_game=args.t,
            sound=args.m
        )
        scenes[Scenes.CREDITS] = Credits()
        self.scenes = scenes
        self.current_scene = scenes[Scenes(args.e)]
        self.current_scene.start()

        # music
        self.music = args.m
        if self.music:
            self.sound = load_sound('./wackamole/assets/sounds/music.wav')
            self.sound.play()

    def update(self, new_scene):
        if self.scenes[new_scene] is not self.current_scene:
            self.current_scene.stop()
            self.current_scene = self.scenes[new_scene]
            self.current_scene.start()

    def stop(self):
        if self.music:
            self.sound.stop()
