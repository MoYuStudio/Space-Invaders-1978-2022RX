
import os
import sys
import time
import random
import pickle
import pygame

import config as C
from page import Page

class Game:
    def __init__(self):

        pygame.init()
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init()

        self.RUN = C.RUN

        self.window = C.window
        self.window_clock = C.window_clock

        self.page = C.page

        self.Page = Page()

    def set(self):

        bgm = pygame.mixer.Sound("assets/sound/song/魔王魂 旧ゲーム音楽 ラストボス02.mp3")
        bgm.set_volume(0.1)
        pygame.mixer.Channel(0).play(bgm,loops=0)
        pygame.display.flip()

    def run(self):

        self.set()

        # Mainloop =========================================================================================================

        while self.RUN:

            self.window.fill((255,55,55,0))
            if self.page == "MenuMain":
                self.Page.menu_main()

            pygame.display.update()
            self.window_clock.tick(60)

    def blit(self):
        pass

    def event(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.RUN = False
                sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()