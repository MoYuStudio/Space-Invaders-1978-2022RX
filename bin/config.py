
import pygame

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

# Config =========================================================================================================

RUN = True

mark = 0

# Window =
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_rect = window.get_rect()
window_width, window_height = window_rect.size
window_title = pygame.display.set_caption("SPACE INVADERS 1978 2022RX")
window_icon = pygame.display.set_icon(pygame.image.load("assets/graphics/image/alien1.png"))
window_clock = pygame.time.Clock()

# Event =
event_pos = (0, 0)

# Page =    
page = 'MenuMain'

# Font =
font16 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 16)
font32 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 32)
font32_bold = pygame.font.Font("assets/graphics/font/LockClock.ttf", 32)
font32_bold.set_bold(True)
font64 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 64)
font64_bold = pygame.font.Font("assets/graphics/font/LockClock.ttf", 64)
font64_bold.set_bold(True)
font128 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 128)


