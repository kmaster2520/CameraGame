import pygame

from constants import HEIGHT, WIDTH, BLACK
from states.gamestate import Scene, GameState


class GameScene(Scene):

    def __init__(self):
        super(GameScene, self).__init__(GameState.MENU)
        self.offset_x = 0
        self.offset_y = 0
        self.rect_desk = pygame.Rect(-1, -1, WIDTH, HEIGHT - 100)
        self.rect_desk.bottomleft = (0, HEIGHT)

        self.rect_left_door = pygame.Rect(-1, -1, WIDTH * 0.2, HEIGHT * 0.7)
        self.rect_left_door.bottomleft = (0, HEIGHT)

        self.rect_right_door = pygame.Rect(-1, -1, WIDTH * 0.2, HEIGHT * 0.7)
        self.rect_right_door.bottomright = (WIDTH, HEIGHT)

        self.screen_name = 'desk'

    def tick(self, screen, game_stack):
        screen.fill((90, 90, 90))
        if self.screen_name == 'desk':
            pygame.draw.rect(screen, color=BLACK, rect=self.rect_left_door)
            pygame.draw.rect(screen, color=BLACK, rect=self.rect_right_door)


