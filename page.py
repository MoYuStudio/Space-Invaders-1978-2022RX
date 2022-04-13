
import random
import pygame

import config

class Page:
    def __init__(self):
        self.window = config.window
        
    def menu_main(self):

        self.window.fill((0, 0, 0))

        self.MenuMain_text1 = self.font64.render("SPACE INVADERS 1978", True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.MenuMain_text1_rect = self.MenuMain_text1.get_rect()
        self.MenuMain_text1_rect.midtop = self.window_rect.midtop
        self.MenuMain_text1_rect.x = self.window_rect.width//36
        self.MenuMain_text1_rect.y += self.MenuMain_text1_rect.height//4
        self.window.blit(self.MenuMain_text1, self.MenuMain_text1_rect)

        self.MenuMain_text2 = self.font32.render("Power BY MoYuStudio", True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.MenuMain_text2_rect = self.MenuMain_text2.get_rect()
        self.MenuMain_text2_rect.midtop = self.MenuMain_text1_rect.midbottom
        self.MenuMain_text2_rect.x = self.window_rect.width//36
        self.MenuMain_text2_rect.y += self.MenuMain_text2_rect.height//4
        self.window.blit(self.MenuMain_text2, self.MenuMain_text2_rect)

        self.MenuMain_text3_mousemotion_color = (255,255,255)
        self.MenuMain_text3 = self.font64.render("Start", True, self.MenuMain_text3_mousemotion_color)
        self.MenuMain_text3_rect = self.MenuMain_text3.get_rect()
        self.MenuMain_text3_rect.midtop = self.MenuMain_text1_rect.midbottom
        self.MenuMain_text3_rect.x = self.window_rect.width//36
        self.MenuMain_text3_rect.y += self.MenuMain_text2_rect.height+self.MenuMain_text3_rect.height
        self.window.blit(self.MenuMain_text3, self.MenuMain_text3_rect)

        self.MenuMain_text4 = self.font64.render("Setting", True, (150,150,150))
        self.MenuMain_text4_rect = self.MenuMain_text4.get_rect()
        self.MenuMain_text4_rect.midtop = self.MenuMain_text3_rect.midbottom
        self.MenuMain_text4_rect.x = self.window_rect.width//36
        self.MenuMain_text4_rect.y += self.MenuMain_text4_rect.height//2
        self.window.blit(self.MenuMain_text4, self.MenuMain_text4_rect)

        self.MenuMain_text5 = self.font64.render("Quit", True, (255,255,255))
        self.MenuMain_text5_rect = self.MenuMain_text4.get_rect()
        self.MenuMain_text5_rect.midtop = self.MenuMain_text4_rect.midbottom
        self.MenuMain_text5_rect.x = self.window_rect.width//36
        self.MenuMain_text5_rect.y += self.MenuMain_text5_rect.height//2
        self.window.blit(self.MenuMain_text5, self.MenuMain_text5_rect)

        self.MenuMain_text6 = self.font32.render("Your Top Mark "+str(self.top_mark), True, (255,255,255))
        self.MenuMain_text6_rect = self.MenuMain_text6.get_rect()
        self.MenuMain_text6_rect.midtop = self.window_rect.midtop
        self.MenuMain_text6_rect.x = self.window_rect.width-self.MenuMain_text6_rect.width
        self.window.blit(self.MenuMain_text6, self.MenuMain_text6_rect)

    def game_main(self):
        pass
    def game_over(self):
        pass