from tresenraya.scenes import StartMenu, GameScene, Credits


def setup_scenes():

    start_menu = StartMenu()
    game = GameScene()
    credits = Credits()

    start_menu.next = game
    start_menu.credits = credits

    credits.next = start_menu

    game.next = start_menu

    return start_menu
