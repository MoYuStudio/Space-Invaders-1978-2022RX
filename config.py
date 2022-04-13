
import pygame

# Config =========================================================================================================

RUN = True

# Window =
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_rect = window.get_rect()
window_width, window_height = window_rect.size
window_title = pygame.display.set_caption("SPACE INVADERS 1978 2022RX")
window_icon = pygame.display.set_icon(pygame.image.load("assets/graphics/image/alien1.png"))
window_clock = pygame.time.Clock()

# Page =    
page = 'MenuMain'

