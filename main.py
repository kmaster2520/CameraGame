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
    current_scene = game_stack[-1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_scene.mousedown_event(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            current_scene.mouseup_event(pygame.mouse.get_pos())

        elif event.type == pygame.KEYDOWN:
            current_scene.keydown_event(event.key)
        elif event.type == pygame.KEYUP:
            current_scene.keyup_event(event.key)

    screen.fill(BLACK)

    current_scene.tick(screen, game_stack)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



