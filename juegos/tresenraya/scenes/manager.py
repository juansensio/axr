from .start import StartMenu
from .game import GameScene
from .credits import Credits
from .scenes import Scenes
from src.utils import load_sound

class SceneManager():

    def __init__(self, initial_scene = 1, music = False):

        # escenas
        scenes = {}
        scenes[Scenes.MENU] = StartMenu()
        scenes[Scenes.GAME] = GameScene()
        scenes[Scenes.CREDITS] = Credits()
        self.scenes = scenes
        self.current_scene = scenes[Scenes(initial_scene)]
        self.current_scene.start()

        # musica
        self.music = music
        if self.music:
            self.sound = load_sound('./tresenraya/assets/music/game.wav')
            self.sound.play()

    def update(self, new_scene):
        if self.scenes[new_scene] is not self.current_scene:
            self.current_scene.stop()
            self.current_scene = self.scenes[new_scene]
            self.current_scene.start()

    def stop(self):
        if self.music:
            self.sound.stop()
