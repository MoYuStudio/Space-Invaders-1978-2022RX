
import sys
import time
import pygame

import config as C

class Event:
    def __init__(self):
        self.RUN = C.RUN

        self.page = C.page

        self.event_pos = C.event_pos

    def menu_main_mousebuttondown(self):
        # start
        if pygame.Rect.collidepoint(self.MenuMain_text3_rect,self.event.pos):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/sound/effect/switch_001.ogg"))
            time.sleep(0.1)
            self.page = "GameMain"
            self.mark = 0
            
        if pygame.Rect.collidepoint(self.MenuMain_text5_rect,self.event.pos):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/sound/effect/switch_001.ogg"))
            time.sleep(0.1)
            self.RUN = False
            sys.exit()
