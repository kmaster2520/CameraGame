import pygame
from constants import WIDTH, HEIGHT, FPS, BLACK
from states import MenuScene

print()


pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

game_stack = [MenuScene()]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_stack[-1].mousedown_event(event, pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            game_stack[-1].mouseup_event(event, pygame.mouse.get_pos())

    screen.fill(BLACK)

    game_stack[-1].tick(screen, game_stack)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



