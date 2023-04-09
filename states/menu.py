import pygame
import numpy as np

from constants import WHITE, WIDTH, HEIGHT, BLACK
from states.game import GameScene
from states.gamestate import Scene, GameState
from util import draw_text


class MenuScene(Scene):

    def __init__(self):
        super(MenuScene, self).__init__(GameState.MENU)
        self.rect_start_game = pygame.Rect(75, 4 * HEIGHT / 6, WIDTH / 3, 100)
        self.rect_credits = pygame.Rect(-1, -1, 200, 30)
        self.rect_credits.bottomright = (WIDTH, HEIGHT)

        self.screen_name = 'main'

        self.do_show_credits = False
        self.do_start_game = False

    def mousedown_event(self, event, mouse_pos):
        if self.screen_name == 'main':
            if self.rect_start_game.collidepoint(mouse_pos):
                self.do_start_game = True

    def tick(self, screen, game_stack):
        if self.do_start_game:
            print('starting game')
            self.do_start_game = False
            game_stack.append(GameScene())

        if self.screen_name == 'main':
            self.render_main_menu(screen)

    def render_main_menu(self, screen):
        pygame.draw.rect(screen, color=WHITE, rect=self.rect_start_game)
        draw_text(screen, "START GAME", self.rect_start_game, color=BLACK, ft_size=48)
        #
        pygame.draw.rect(screen, color=WHITE, rect=self.rect_credits)
        draw_text(screen, "Credits", self.rect_credits, color=BLACK, ft_size=24)





