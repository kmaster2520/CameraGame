import pygame

from constants import WHITE, WIDTH, HEIGHT
from states.gamestate import Scene, GameState
from util import draw_text


class MenuScene(Scene):

    def __init__(self):
        super(MenuScene, self).__init__(GameState.MENU)
        self.rect_start_game = pygame.Rect(75, 4 * HEIGHT / 6, WIDTH / 3, 100)
        self.rect_credits = pygame.Rect(-1, -1, 200, 30)
        self.rect_credits.bottomright = (WIDTH, HEIGHT)

        self.screen_name = 'main'

        self.show_credits = False

    def tick(self, screen, game_stack):
        if self.screen_name == 'main':
            self.render_main_menu(screen)

    def render_main_menu(self, screen):
        draw_text(screen, "Press SPACE to START", self.rect_start_game, color=WHITE, ft_size=48)
        #
        draw_text(screen, "Press 'C' to show credits", self.rect_credits, color=WHITE, ft_size=24)




