from enum import Enum

class GameState(Enum):
    MENU = 0
    GAME = 1


class Scene:
    def __init__(self, state: GameState):
        self.state = state

    def tick(self, screen, game_stack):
        pass

    def mousedown_event(self, event, mouse_pos):
        print(event)

    def mouseup_event(self, event, mouse_pos):
        print(event)

    def keydown_event(self, event):
        print(event)

    def keyup_event(self, event):
        print(event)



        

