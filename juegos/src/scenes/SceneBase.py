class SceneBase:
    def __init__(self):
        self.next = self

    def process_input(self, events):
        print("uh-oh, you didn't override this in the child class")

    def update(self):
        print("uh-oh, you didn't override this in the child class")

    def render(self, screen):
        print("uh-oh, you didn't override this in the child class")
