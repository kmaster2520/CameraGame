from enum import Enum

class GameState(Enum):
    MENU = 0
    GAME = 1


class Scene:
    def __init__(self, state: GameState):
        self.state = state

    def tick(self, screen, game_stack):
        pass

    def mousedown_event(self, mouse_pos):
        print(mouse_pos)

    def mouseup_event(self, mouse_pos):
        print(mouse_pos)

    def keydown_event(self, key):
        print(key)

    def keyup_event(self, key):
        print(key)



        

