from .start import StartMenu
from .game import GameScene
from .credits import Credits
from .scenes import Scenes
from src.utils import load_sound


class SceneManager():

    def __init__(self, args):

        # escenas
        scenes = {}
        scenes[Scenes.MENU] = StartMenu()
        scenes[Scenes.GAME] = GameScene(
            args.a, args.its, args.l, args.v, args.p)
        scenes[Scenes.CREDITS] = Credits()
        self.scenes = scenes
        self.current_scene = scenes[Scenes(args.e)]
        self.current_scene.start()

        # music
        # self.music = args.m
        # if self.music:
        #     self.sound = load_sound('./wackamole/assets/sounds/music.wav')
        #     self.sound.play()

    def update(self, new_scene):
        if self.scenes[new_scene] is not self.current_scene:
            self.current_scene.stop()
            self.current_scene = self.scenes[new_scene]
            self.current_scene.start()

    def stop(self):
        pass
        # if self.music:
        #     self.sound.stop()
