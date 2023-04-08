import pygame


def draw_text(screen, text, rect, *, color, ft_name=None, ft_size=48):
    font = pygame.font.SysFont(ft_name, ft_size)
    text_surface = font.render(text, True, color)

    text_width, text_height = text_surface.get_size()
    text_x = rect.centerx - (text_width / 2)
    text_y = rect.centery - (text_height / 2)

    screen.blit(text_surface, (text_x, text_y))
