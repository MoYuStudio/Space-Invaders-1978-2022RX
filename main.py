
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

        # Need Save =
        

        # Window =
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.window_title = pygame.display.set_caption("SPACE INVADERS 1978 2022RX")
        self.window_icon = pygame.display.set_icon(pygame.image.load("assets/graphics/image/alien1.png"))
        self.window_clock = pygame.time.Clock()
        self.window_rect = self.window.get_rect()

        # Ship =
        self.ship_sprite = pygame.sprite.Sprite()
        self.ship_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/ship1.png"),(64,64))
        self.ship_sprite.rect = self.ship_sprite.image.get_rect()
        self.ship_sprite.rect.midbottom = self.window_rect.midbottom
        self.ship_moving_speed = 6
        self.ship_moving_up = False
        self.ship_moving_down = False
        self.ship_moving_right = False
        self.ship_moving_left = False
        self.ship_blood = 3

        # Bullet =
        self.bullet_list = pygame.sprite.Group()
        self.bullet_moving_speed = 6
        self.bullet_width = 8
        self.bullet_fire_switch = True
        self.bullet_timer = 0
        self.bullet_color = (50,250,50)

        # Alien =
        self.alien_list = pygame.sprite.Group()
        # self.alien_moving_speed = 16
        # self.alien_direction = 3
        self.alien_moving_speed = 12
        self.alien_direction = 1

        # Buff =
        self.buff1_list = pygame.sprite.Group()
        self.buff2_list = pygame.sprite.Group()
        self.buff3_list = pygame.sprite.Group()
        self.buff4_list = pygame.sprite.Group()
        self.buff5_list = pygame.sprite.Group()
        self.buff_moving_speed = 3
        self.buff1_timer = 0
        self.buff2_timer = 0
        self.buff3_timer = 0
        self.buff4_timer = 0
        self.buff5_timer = 0
        self.buff2_effect = True
        self.buff5_effect = True

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

        self.buff_spawn()

        if self.ship_moving_up and self.ship_sprite.rect.top > 0:
            self.ship_sprite.rect.y -= self.ship_moving_speed
        if self.ship_moving_down and self.ship_sprite.rect.bottom < self.window_rect.bottom:
            self.ship_sprite.rect.y += self.ship_moving_speed
        if self.ship_moving_right and self.ship_sprite.rect.right < self.window_rect.right:
            self.ship_sprite.rect.x += self.ship_moving_speed
        if self.ship_moving_left and self.ship_sprite.rect.left > 0:
            self.ship_sprite.rect.x -= self.ship_moving_speed

        self.window.fill((0, 0, 0))
        
        for bullet in self.bullet_list:
            pygame.draw.rect(self.window, self.bullet_color, bullet)
            bullet.rect.y -= self.bullet_moving_speed
            if bullet.rect.bottom < 0:
                self.bullet_list.remove(bullet)

        for alien in self.alien_list:
            alien.rect.x += 1*self.alien_direction
            if alien.rect.top <= self.window_rect.top:
                alien.rect.y += self.alien_moving_speed
            if alien.rect.right >= self.window_rect.right or alien.rect.left <= 0:
                self.alien_direction *= -1
                for alien in self.alien_list:
                    alien.rect.y += self.alien_moving_speed

            if alien.rect.bottom >= self.window_rect.bottom:
                self.game_over()

        for buff in self.buff1_list:
            buff.rect.y += self.buff_moving_speed
            if buff.rect.bottom >= self.window_rect.bottom:
                self.buff1_list.remove(buff)
        for buff in self.buff2_list:
            buff.rect.y += self.buff_moving_speed
            if buff.rect.bottom >= self.window_rect.bottom:
                self.buff2_list.remove(buff)
        for buff in self.buff3_list:
            buff.rect.y += self.buff_moving_speed
            if buff.rect.bottom >= self.window_rect.bottom:
                self.buff3_list.remove(buff)
        for buff in self.buff4_list:
            buff.rect.y += self.buff_moving_speed
            if buff.rect.bottom >= self.window_rect.bottom:
                self.buff4_list.remove(buff)
        for buff in self.buff5_list:
            buff.rect.y += self.buff_moving_speed
            if buff.rect.bottom >= self.window_rect.bottom:
                self.buff5_list.remove(buff)

        if pygame.sprite.spritecollide(self.ship_sprite, self.buff1_list, True):
            self.buff1_timer += 120
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff2_list, True):
            self.buff2_timer += 120
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff3_list, True):
            self.buff3_timer += 1
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff4_list, True):
            self.buff4_timer += 1
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff5_list, True):
            self.buff5_timer += 240
            
        # buff1
        if self.buff1_timer > 0:
            self.bullet_width = 300
            self.buff1_timer -= 1
        if self.buff1_timer <= 0:
            self.bullet_width = 8
            self.buff1_timer = 0
        # buff2
        if self.buff2_timer > 0:
            self.bullet_color = (150,50,250)
            self.buff2_effect = False
            self.buff2_timer -= 1
        if self.buff2_timer <= 0:
            self.bullet_color = (50,250,50)
            self.buff2_effect = True
            self.buff2_timer = 0
        # buff3
        if self.buff3_timer > 0:
            self.alien_list.empty()
            self.buff3_timer -= 1
        if self.buff3_timer <= 0:
            self.buff3_timer = 0
        # buff4
        if self.buff4_timer > 0:
            self.ship_blood += 1
            self.buff4_timer -= 1
        if self.buff4_timer <= 0:
            self.buff4_timer = 0
        # buff5
        if self.buff5_timer > 0:
            self.ship_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/ship1_buff5.png"),(64,64))
            self.buff5_effect = False
            self.buff5_timer -= 1
        if self.buff5_timer <= 0:
            self.ship_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/ship1.png"),(64,64))
            self.buff5_effect = True
            self.buff5_timer = 0


        self.window.blit(self.ship_sprite.image, self.ship_sprite.rect)
        self.alien_list.draw(self.window)

        try:
            self.buff1_list.draw(self.window)
        except:
            pass
        try:
            self.buff2_list.draw(self.window)
        except:
            pass
        try:
            self.buff3_list.draw(self.window)
        except:
            pass
        try:
            self.buff4_list.draw(self.window)
        except:
            pass
        try:
            self.buff5_list.draw(self.window)
        except:
            pass

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

        self.bullet_with_alien = pygame.sprite.groupcollide(self.bullet_list, self.alien_list, self.buff2_effect, True)
        
        if len(self.bullet_with_alien) != 0:
            self.mark += len(self.bullet_with_alien)
            random_hit_sound_effect = random.randint(1,4)
            hit_sound_effect = pygame.mixer.Sound("assets/sound/effect/toggle_00"+str(random_hit_sound_effect)+".ogg")
            hit_sound_effect.set_volume(0.1)
            pygame.mixer.Channel(1).play(hit_sound_effect)
        


        if self.bullet_fire_switch == True:
            if self.bullet_timer > 0:
                self.bullet_timer -= 1
            if self.bullet_timer <= 0:
                bullet_sprite = pygame.sprite.Sprite()
                bullet_sprite.rect = pygame.Rect(0,0,self.bullet_width,16)
                bullet_sprite.rect.midbottom = self.ship_sprite.rect.midtop
                self.bullet_list.add(bullet_sprite)
                self.bullet_timer = 15

        if not self.alien_list:
            self.alien_spawn()

        if self.buff5_effect == True:
            if pygame.sprite.spritecollideany(self.ship_sprite, self.alien_list):
                self.game_over()

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
                bullet_sprite.rect = pygame.Rect(0,0,self.bullet_width,16)
                bullet_sprite.rect.midbottom = self.ship_sprite.rect.midtop
                self.bullet_list.add(bullet_sprite)
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

    def alien_spawn(self):
        self.alien_space_sprite = pygame.sprite.Sprite()
        self.alien_space_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien1.png"),(64,64))
        self.alien_space_sprite.rect = self.alien_space_sprite.image.get_rect()
        self.window_width, self.window_height = self.window_rect.size
        self.ship_width, self.ship_height = self.ship_sprite.rect.size
        self.space_x = self.window_width - self.alien_space_sprite.rect.width*2
        self.space_y = self.window_height - self.ship_height - self.alien_space_sprite.rect.height*3
        self.number_x = self.space_x // (self.alien_space_sprite.rect.width*2)
        self.number_y = self.space_y // (self.alien_space_sprite.rect.height*2)
        for y in range(self.number_y):
            for x in range(self.number_x):
                alien_sprite = pygame.sprite.Sprite()
                alien_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien1.png"),(64,64))
                alien_sprite.rect = alien_sprite.image.get_rect()
                alien_sprite.rect.x = alien_sprite.rect.width + alien_sprite.rect.width*2*x
                alien_sprite.rect.y = alien_sprite.rect.height + alien_sprite.rect.height*2*y - self.space_y
                self.alien_list.add(alien_sprite)

    def buff_spawn(self):
        try_buff_spawn = random.randint(1,300)
        if try_buff_spawn == 1:
            buff_spawn_type = random.randint(1,100)
            if 1 <= buff_spawn_type <= 20:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff1.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff1_list.add(buff_sprite)
            if 21 <= buff_spawn_type <= 40:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff2.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff2_list.add(buff_sprite)
            if 41 <= buff_spawn_type <= 60:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff3.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff3_list.add(buff_sprite)
            if 61 <= buff_spawn_type <= 80:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff4.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff4_list.add(buff_sprite)
            if 81 <= buff_spawn_type <= 100:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff5.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff5_list.add(buff_sprite)

    def game_over(self):
        self.alien_list.empty()
        self.bullet_list.empty()
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


if __name__ == '__main__':
    game = Game()
    game.run()