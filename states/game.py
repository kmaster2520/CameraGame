import pygame

from constants import HEIGHT, WIDTH
from states.gamestate import Scene, GameState


class GameScene(Scene):

    def __init__(self):
        super(GameScene, self).__init__(GameState.MENU)
        self.rect_start_game = pygame.Rect(75, 4 * HEIGHT / 6, WIDTH / 3, 100)
        self.rect_credits = pygame.Rect(-1, -1, 200, 30)
        self.rect_credits.bottomright = (WIDTH, HEIGHT)

        self.screen_name = 'main'

        self.show_credits = False
