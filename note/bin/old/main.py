
################################################################
#                 MoYu Studio © 2021 - 2022                    #
################################################################
#                SPACE INVADERS 1978 2022RX                    #
#                    Dv20220411 a1 Bata                        #
################################################################

import os
import sys
import time
import random
import pickle
import pygame

from bullet import Bullet

class Game:

    def __init__(self):

        pygame.init()
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init()
        
        # Config =========================================================================================================

        self.RUN = True

        self.mark = 0

        # Save =
        self.save_path = "data/"
        self.save_slot_name = 'save'
        self.save_write_data = {}
        self.save_read_data = {}

        # Window =
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.window_rect = self.window.get_rect()
        self.window_width, self.window_height = self.window_rect.size
        self.window_title = pygame.display.set_caption("SPACE INVADERS 1978 2022RX")
        self.window_icon = pygame.display.set_icon(pygame.image.load("assets/graphics/image/alien1.png"))
        self.window_clock = pygame.time.Clock()

        # Ship =
        self.ship_sprite = pygame.sprite.Sprite()
        self.ship_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/ship1.png"),(64,64))
        self.ship_sprite.rect = self.ship_sprite.image.get_rect()
        self.ship_width, self.ship_height = self.ship_sprite.rect.size
        self.ship_sprite.rect.midbottom = self.window_rect.midbottom
        self.ship_moving_speed = 7
        self.ship_moving_up = False
        self.ship_moving_down = False
        self.ship_moving_right = False
        self.ship_moving_left = False
        self.ship_blood = 3
        

        




        # Font =
        self.font16 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 16)
        self.font32 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 32)
        self.font32_bold = pygame.font.Font("assets/graphics/font/LockClock.ttf", 32)
        self.font32_bold.set_bold(True)
        self.font64 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 64)
        self.font64_bold = pygame.font.Font("assets/graphics/font/LockClock.ttf", 64)
        self.font64_bold.set_bold(True)
        self.font128 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 128)

        # Page =
        self.page = "MenuMain"

        pygame.mixer.set_num_channels(10)  # default is 8


    def set(self):

        self.alien_spawn()



        self.GameOver_text1 = self.font128.render("Game Over", True, (255,255,255))
        self.GameOver_text1_rect = self.GameOver_text1.get_rect()
        self.GameOver_text1_rect.center = self.window_rect.center

        bgm = pygame.mixer.Sound("assets/sound/song/魔王魂 旧ゲーム音楽 ラストボス02.mp3")
        bgm.set_volume(0.1)
        pygame.mixer.Channel(0).play(bgm,loops=0)
        

        pygame.display.flip()

    def run(self):

        self.set()

        # Mainloop =========================================================================================================

        while self.RUN:

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.RUN = False
                    sys.exit()

                if self.event.type == pygame.MOUSEMOTION:
                    if self.page == "MenuMain":
                        self.event_MenuMain_mousemotion()

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    if self.page == "MenuMain":
                        self.event_MenuMain_mousebuttondown()
                        
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        self.page = "MenuMain"

                    if self.page == "GameMain":
                        self.event_GameMain_keydown()
                    
                if self.event.type == pygame.KEYUP:

                    if self.page == "GameMain":
                        self.event_GameMain_keyup()
                    
            self.window.fill((255,55,55,0))
            if self.page == "MenuMain":
                self.page_MenuMain()
            if self.page == "GameMain":
                self.page_GameMain()
            if self.page == "GameOver":
                self.page_GameOver()

            pygame.display.update()
            self.window_clock.tick(60)

    # Page ============================================================================================================

    def page_MenuMain(self):

        self.load()

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

    def page_GameMain(self):

        if self.ship_moving_up and self.ship_sprite.rect.top > 0:
            self.ship_sprite.rect.y -= self.ship_moving_speed
        if self.ship_moving_down and self.ship_sprite.rect.bottom < self.window_rect.bottom:
            self.ship_sprite.rect.y += self.ship_moving_speed
        if self.ship_moving_right and self.ship_sprite.rect.right < self.window_rect.right:
            self.ship_sprite.rect.x += self.ship_moving_speed
        if self.ship_moving_left and self.ship_sprite.rect.left > 0:
            self.ship_sprite.rect.x -= self.ship_moving_speed

        self.window.fill((0, 0, 0))
        
        try:
            self.alien1_list.draw(self.window)
        except:
            pass
        try:
            self.alien2_list.draw(self.window)
        except:
            pass
        try:
            self.alien3_list.draw(self.window)
        except:
            pass
        try:
            self.alien4_list.draw(self.window)
        except:
            pass
        try:
            self.alien5_list.draw(self.window)
        except:
            pass
        try:
            self.alien_group1_list.draw(self.window)
        except:
            pass



        try_alien3_effect = random.randint(1,3)
        if try_alien3_effect == 1:
            self.alien3_effect = False
        else:
            self.alien3_effect = True
        

        self.buff_blit()


        self.window.blit(self.ship_sprite.image, self.ship_sprite.rect)






        self.GameMain_text2 = self.font32.render("Press SPACE or F to Fire", True, (255,255,255))
        self.GameMain_text2_rect = self.GameMain_text2.get_rect()
        self.GameMain_text2_rect.midtop = self.window_rect.midtop
        self.window.blit(self.GameMain_text2, self.GameMain_text2_rect)

        self.GameMain_text3 = self.font32.render("Press Esc Out", True, (255,255,255))
        self.GameMain_text3_rect = self.GameMain_text3.get_rect()
        self.GameMain_text3_rect.midtop = self.GameMain_text2_rect.midbottom
        self.window.blit(self.GameMain_text3, self.GameMain_text3_rect)

        self.GameMain_text4 = self.font64.render("Ship Blood :"+str(self.ship_blood), True, (255,255,255))
        self.GameMain_text4_rect = self.GameMain_text4.get_rect()
        self.GameMain_text4_rect.midtop = self.GameMain_text3_rect.midbottom
        self.window.blit(self.GameMain_text4, self.GameMain_text4_rect)

        self.GameMain_text5 = self.font64.render("Mark :"+str(self.mark), True, (255,255,255))
        self.GameMain_text5_rect = self.GameMain_text5.get_rect()
        self.GameMain_text5_rect.midtop = self.GameMain_text4_rect.midbottom
        self.window.blit(self.GameMain_text5, self.GameMain_text5_rect)
        
        for bullet_list in self.bullet_list_list:
            try:
                self.bullet_with_alien1 = pygame.sprite.groupcollide(bullet_list, self.alien1_list, self.buff2_effect, True)
                self.bullet_with_alien2 = pygame.sprite.groupcollide(bullet_list, self.alien2_list, self.buff2_effect, True)
                self.bullet_with_alien3 = pygame.sprite.groupcollide(bullet_list, self.alien3_list, self.buff2_effect, self.alien3_effect)
                self.bullet_with_alien4 = pygame.sprite.groupcollide(bullet_list, self.alien4_list, self.buff2_effect, True)
                self.bullet_with_alien5 = pygame.sprite.groupcollide(bullet_list, self.alien5_list, self.buff2_effect, True)
            except:
                pass

        self.bullet_with_alien_group1 = pygame.sprite.groupcollide(self.bullet1_list, self.alien_group1_list, self.buff2_effect, True)

        if len(self.bullet_with_alien1) != 0 or \
            len(self.bullet_with_alien2) != 0 or \
            len(self.bullet_with_alien3) != 0 or \
            len(self.bullet_with_alien4) != 0 or \
            len(self.bullet_with_alien5) != 0 or \
            len(self.bullet_with_alien_group1) != 0:

            self.mark += \
            len(self.bullet_with_alien1) + \
            len(self.bullet_with_alien2) + \
            len(self.bullet_with_alien3) + \
            len(self.bullet_with_alien4) + \
            len(self.bullet_with_alien5) + \
            len(self.bullet_with_alien_group1)
            random_hit_sound_effect = random.randint(1,4)
            hit_sound_effect = pygame.mixer.Sound("assets/sound/effect/toggle_00"+str(random_hit_sound_effect)+".ogg")
            hit_sound_effect.set_volume(0.1)
            pygame.mixer.Channel(1).play(hit_sound_effect)
        
        if self.bullet_fire_switch == True:
            if self.bullet_type == '1':
                if self.bullet1_timer > 0:
                    self.bullet1_timer -= 1
                if self.bullet1_timer <= 0:
                    bullet_sprite = pygame.sprite.Sprite()
                    bullet_sprite.rect = pygame.Rect(0,0,self.bullet1_width,16)
                    bullet_sprite.rect.midbottom = self.ship_sprite.rect.midtop
                    self.bullet1_list.add(bullet_sprite)
                    self.bullet1_timer = 15
            if self.bullet_type == '2':
                if self.bullet2_timer > 0:
                    self.bullet2_timer -= 1
                if self.bullet2_timer <= 0:
                    bullet_sprite = pygame.sprite.Sprite()
                    bullet_sprite.rect = pygame.Rect(0,0,self.bullet2_width,16)
                    bullet_sprite.rect.midbottom = self.ship_sprite.rect.midtop
                    self.bullet2_list.add(bullet_sprite)
                    self.bullet2_timer = 5
            if self.bullet_type == '3':
                if self.bullet3_timer > 0:
                    self.bullet3_timer -= 1
                if self.bullet3_timer <= 0:
                    bullet_sprite = pygame.sprite.Sprite()
                    bullet_sprite.rect = pygame.Rect(0,0,self.bullet3_width,16)
                    bullet_sprite.rect.midbottom = self.ship_sprite.rect.midtop
                    self.bullet3_list.add(bullet_sprite)
                    self.bullet3_timer = 15

        if self.buff5_effect == True:
            if pygame.sprite.spritecollideany(self.ship_sprite, self.alien1_list) or \
               pygame.sprite.spritecollideany(self.ship_sprite, self.alien2_list) or \
               pygame.sprite.spritecollideany(self.ship_sprite, self.alien3_list) or \
               pygame.sprite.spritecollideany(self.ship_sprite, self.alien4_list) or \
               pygame.sprite.spritecollideany(self.ship_sprite, self.alien5_list):
                self.game_over()
        
        self.spawn()
        self.save()

    def page_GameOver(self):

        self.window.fill((0, 0, 0))

        self.window.blit(self.GameOver_text1, self.GameOver_text1_rect)

        self.GameOver_text2 = self.font64.render("Your Mark is "+str(self.mark), True, (255,255,255))
        self.GameOver_text2_rect = self.GameOver_text2.get_rect()
        self.GameOver_text2_rect.midtop = self.GameOver_text1_rect.midbottom
        self.window.blit(self.GameOver_text2, self.GameOver_text2_rect)

    # Event ===========================================================================================================

    # GameMain =
    def event_GameMain_keydown(self):
        if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
            self.ship_moving_up = True
        if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
            self.ship_moving_down = True
        if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
            self.ship_moving_left = True
        if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
            self.ship_moving_right = True
        if self.event.key == pygame.K_f:
            if self.bullet_fire_switch == True:
                self.bullet_fire_switch = False
            elif self.bullet_fire_switch == False:
                self.bullet_fire_switch = True
        if self.event.key == pygame.K_SPACE:
            if self.bullet_fire_switch == False:
                bullet_sprite = pygame.sprite.Sprite()
                bullet_sprite.rect = pygame.Rect(0,0,self.bullet1_width,16)
                bullet_sprite.rect.midbottom = self.ship_sprite.rect.midtop
                self.bullet1_list.add(bullet_sprite)
    def event_GameMain_keyup(self):
        if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
            self.ship_moving_up = False
        if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
            self.ship_moving_down = False
        if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
            self.ship_moving_left = False
        if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
            self.ship_moving_right = False

    # MenuMain =
    def event_MenuMain_mousemotion(self):

        pass

    def event_MenuMain_mousebuttondown(self):
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

    # Function ===========================================================================================================

    def spawn(self):
        self.buff_spawn()
        if not self.alien1_list and not self.alien2_list and not self.alien3_list and not self.alien4_list and not self.alien5_list:
            for i in range((self.mark//1)+1):
                self.alien_spawn()
        if not self.alien_group1_list:
            if self.try_alien_group_spawn_timer > 0:
                self.try_alien_group_spawn_timer -= 1
            if self.try_alien_group_spawn_timer <= 0:
                self.alien_group_spawn()
                self.try_alien_group_spawn_timer = random.randint(100,200)


    def game_over(self):
        self.empty_all_alien()
        self.bullet1_list.empty()
        self.alien_spawn()
        self.ship_sprite.rect.midbottom = self.window_rect.midbottom
        time.sleep(0.5)
        self.ship_blood -= 1
        sound_effect = pygame.mixer.Sound("assets/sound/effect/question_002.ogg")
        sound_effect.set_volume(0.3)
        pygame.mixer.Channel(1).play(sound_effect)
        if self.ship_blood == 0:
            self.page = "GameOver"
            sound_effect = pygame.mixer.Sound("assets/sound/effect/question_001.ogg")
            sound_effect.set_volume(0.3)
            pygame.mixer.Channel(1).play(sound_effect)
            self.save()

    def save_write(self):
        f=open(self.save_path + self.save_slot_name,'wb')
        pickle.dump(self.save_write_data, f)
        f.close()
    def save_read(self):
        try:
            f=open(self.save_path + self.save_slot_name,'rb')
            self.save_read_data = pickle.load(f)
            f.close()
        except:
            pass
        return self.save_read_data
    
    def save(self):
        if self.mark >= self.top_mark:
                self.save_write_data = {"top_mark":self.mark}
                self.save_write()
    def load(self):
        self.save_read()
        if len(self.save_read_data) != 0:
            self.top_mark = self.save_read_data['top_mark']
        else:
            self.top_mark = 0

    def empty_all_alien(self):
        self.alien1_list.empty()
        self.alien2_list.empty()
        self.alien3_list.empty()
        self.alien4_list.empty()
        self.alien5_list.empty()
        self.alien_group1_list.empty()

if __name__ == '__main__':
    game = Game()
    game.run()