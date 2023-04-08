from enum import Enum


class GameState(Enum):
    MENU = 0
    GAME = 1


class Scene:
    def __init__(self, state: GameState):
        self.state = state

    def tick(self, screen, game_stack):
        pass

        

