
################################################################
#                 MoYu Studio © 2021 - 2022                    #
################################################################
#                SPACE INVADERS 1978 2022RX                    #
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
        
        # Alien =
        # 1普通怪 2普通怪 3格挡怪 4攻击怪 5速度怪
        self.alien1_list = pygame.sprite.Group()
        self.alien2_list = pygame.sprite.Group()
        self.alien3_list = pygame.sprite.Group()
        self.alien4_list = pygame.sprite.Group()
        self.alien5_list = pygame.sprite.Group()
        self.alien_list_list = [self.alien1_list, self.alien2_list, self.alien3_list, self.alien4_list, self.alien5_list]
        self.alien_group1_list = pygame.sprite.Group()
        self.alien_group_list_list = [self.alien_group1_list]
        self.alien1_moving_speed = 1
        self.alien2_moving_speed = 1
        self.alien3_moving_speed = 1
        self.alien4_moving_speed = 1
        self.alien5_moving_speed = 3
        self.alien_moving_speed_list = [self.alien1_moving_speed, self.alien2_moving_speed, self.alien3_moving_speed, self.alien4_moving_speed, self.alien5_moving_speed]
        self.alien_group1_moving_speed = 12
        self.alien_group1_moving_direction_speed = 3
        self.alien3_effect = False

        self.alien_group1_line = 3
        self.alien_group1_line_timer = 0
        # self.alien_moving_speed = 16
        # self.alien_direction = 3
        self.try_alien_group_spawn_timer = 0
        #self.alien_moving_speed = 12
        self.alien_direction = 1

        # Bullet =
        # 1普通弹 2极速弹 3范围弹 4穿透弹   A1普通弹(怪物)
        self.bullet_fire_switch = True
        self.bullet_type = '1'
        self.bullet1_list = pygame.sprite.Group()
        self.bullet2_list = pygame.sprite.Group()
        self.bullet3_list = pygame.sprite.Group()
        self.bullet4_list = pygame.sprite.Group()
        self.bullet5_list = pygame.sprite.Group()
        self.bulletA1_list = pygame.sprite.Group()
        self.bullet_list_list = [self.bullet1_list,self.bullet2_list,self.bullet3_list,self.bullet4_list,self.bullet5_list]
        self.bulletA_list_list = [self.bulletA1_list]
        self.bullet1_moving_speed = 6
        self.bullet1_width = 12
        self.bullet1_timer = 0
        self.bullet1_color = (50,250,50)
        self.bullet2_moving_speed = 9
        self.bullet2_width = 6
        self.bullet2_timer = 0
        self.bullet2_color = (0,250,250)
        self.bullet3_moving_speed = 6
        self.bullet3_width = 300
        self.bullet3_timer = 0
        self.bullet3_color = (50,250,50)
        self.bullet4_moving_speed = 6
        self.bullet4_width = 8
        self.bullet4_timer = 0
        self.bullet4_color = (50,250,50)
        self.bullet5_moving_speed = 6
        self.bullet5_width = 8
        self.bullet5_timer = 0
        self.bullet5_color = (50,250,50)
        self.bulletA1_moving_speed = -3
        self.bulletA1_width = 8
        self.bulletA1_timer = 0
        self.bulletA1_color = (150,50,250)
        self.bullet_moving_speed_list = [self.bullet1_moving_speed,self.bullet2_moving_speed,self.bullet3_moving_speed,self.bullet4_moving_speed,self.bullet5_moving_speed]
        self.bullet_width_list = [self.bullet1_width,self.bullet2_width,self.bullet3_width,self.bullet4_width,self.bullet5_width]
        self.bullet_timer_list = [self.bullet1_timer,self.bullet2_timer,self.bullet3_timer,self.bullet4_timer,self.bullet5_timer]
        self.bullet_color_list = [self.bullet1_color,self.bullet2_color,self.bullet3_color,self.bullet4_color,self.bullet5_color]
        self.bulletA_moving_speed_list = [self.bulletA1_moving_speed]
        self.bulletA_width_list = [self.bulletA1_width]
        self.bulletA_timer_list = [self.bulletA1_timer]
        self.bulletA_color_list = [self.bulletA1_color]

        # Buff =
        # 1范围Buff 2极速Buff 3清屏Buff 4医疗Buff 5无敌Buff 6穿透Buff
        self.buff1_list = pygame.sprite.Group()
        self.buff2_list = pygame.sprite.Group()
        self.buff3_list = pygame.sprite.Group()
        self.buff4_list = pygame.sprite.Group()
        self.buff5_list = pygame.sprite.Group()
        self.buff_list_list = [self.buff1_list,self.buff2_list,self.buff3_list,self.buff4_list,self.buff5_list]
        self.buff1_moving_speed = 2
        self.buff2_moving_speed = 2
        self.buff3_moving_speed = 2
        self.buff4_moving_speed = 2
        self.buff5_moving_speed = 2
        self.buff_moving_speed_list = [self.buff1_moving_speed,self.buff2_moving_speed,self.buff3_moving_speed,self.buff4_moving_speed,self.buff5_moving_speed]
        self.buff1_timer = 0
        self.buff2_timer = 0
        self.buff3_timer = 0
        self.buff4_timer = 0
        self.buff5_timer = 0
        self.buff_timer_list = [self.buff1_timer,self.buff2_timer,self.buff3_timer,self.buff4_timer,self.buff5_timer]
        self.buff1_timer_add = 360
        self.buff2_timer_add = 360
        self.buff3_timer_add = 1
        self.buff4_timer_add = 1
        self.buff5_timer_add = 512
        self.buff_timer_add_list = [self.buff1_timer_add,self.buff2_timer_add,self.buff3_timer_add,self.buff4_timer_add,self.buff5_timer_add]
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

        def text_render():
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
        text_render()

    def page_GameMain(self):

        def ship_move():
            if self.ship_moving_up and self.ship_sprite.rect.top > 0:
                self.ship_sprite.rect.y -= self.ship_moving_speed
            if self.ship_moving_down and self.ship_sprite.rect.bottom < self.window_rect.bottom:
                self.ship_sprite.rect.y += self.ship_moving_speed
            if self.ship_moving_right and self.ship_sprite.rect.right < self.window_rect.right:
                self.ship_sprite.rect.x += self.ship_moving_speed
            if self.ship_moving_left and self.ship_sprite.rect.left > 0:
                self.ship_sprite.rect.x -= self.ship_moving_speed
        ship_move()

        self.window.fill((0, 0, 0))

        for bullet_list in range(len(self.bullet_list_list)):
            for bullet in self.bullet_list_list[bullet_list]:
                pygame.draw.rect(self.window, self.bullet_color_list[bullet_list], bullet)
                bullet.rect.y -= self.bullet_moving_speed_list[bullet_list]
                if bullet.rect.bottom < 0:
                    self.bullet_list_list[bullet_list].remove(bullet)
        for bulletA_list in range(len(self.bulletA_list_list)):
            for bulletA in self.bulletA_list_list[bulletA_list]:
                pygame.draw.rect(self.window, self.bulletA_color_list[bulletA_list], bulletA)
                bulletA.rect.y -= self.bulletA_moving_speed_list[bulletA_list]
                if bulletA.rect.bottom < 0:
                    self.bulletA_list_list[bulletA_list].remove(bulletA)
        
        try_draw_list = [self.alien_list_list,self.alien_group_list_list,self.buff_list_list]
        for draw_list in try_draw_list:
            for draw in draw_list:
                try:
                    draw.draw(self.window)
                except:
                    pass

        try_alien3_effect = random.randint(1,3)
        if try_alien3_effect == 1:
            self.alien3_effect = False
        else:
            self.alien3_effect = True
        

       # self.buff_blit()

        self.window.blit(self.ship_sprite.image, self.ship_sprite.rect)

        def text_rander():
            # self.GameMain_text2 = self.font32.render("Press SPACE or F to Fire", True, (255,255,255))
            # self.GameMain_text2_rect = self.GameMain_text2.get_rect()
            # self.GameMain_text2_rect.midtop = self.window_rect.midtop
            # self.window.blit(self.GameMain_text2, self.GameMain_text2_rect)

            # self.GameMain_text3 = self.font32.render("Press Esc Out", True, (255,255,255))
            # self.GameMain_text3_rect = self.GameMain_text3.get_rect()
            # self.GameMain_text3_rect.midtop = self.GameMain_text2_rect.midbottom
            # self.window.blit(self.GameMain_text3, self.GameMain_text3_rect)

            self.GameMain_text4 = self.font64.render("Ship Blood :"+str(self.ship_blood), True, (255,255,255))
            self.GameMain_text4_rect = self.GameMain_text4.get_rect()
            self.GameMain_text4_rect.x = self.window_rect.width//36
            self.GameMain_text4_rect.y = self.GameMain_text4_rect.height//8
            self.window.blit(self.GameMain_text4, self.GameMain_text4_rect)

            self.GameMain_text5 = self.font64.render("Mark :"+str(self.mark), True, (255,255,255))
            self.GameMain_text5_rect = self.GameMain_text5.get_rect()
            self.GameMain_text5_rect.midleft = self.GameMain_text4_rect.midright
            self.GameMain_text5_rect.x += self.window_rect.width//8
            self.window.blit(self.GameMain_text5, self.GameMain_text5_rect)
        text_rander()

        for alienlist_number in range(len(self.alien_list_list)):
            for alien in self.alien_list_list[alienlist_number]:
                alien.rect.y += self.alien_moving_speed_list[alienlist_number]
                if alien.rect.bottom >= self.window_rect.bottom:
                    self.game_over()
        
        for alien in self.alien_group1_list:
            alien.rect.x += 1*self.alien_group1_moving_direction_speed
            if alien.rect.top <= self.window_rect.top:
                alien.rect.y += self.alien_group1_moving_speed
            if alien.rect.right >= self.window_rect.right or alien.rect.left <= 0:
                self.alien_group1_moving_direction_speed *= -1
                for alien in self.alien_group1_list:
                    alien.rect.y += self.alien_group1_moving_speed
            if alien.rect.bottom >= self.window_rect.bottom:
                self.game_over()

        for buff_number in range(len(self.buff_list_list)):
            for buff in self.buff_list_list[buff_number]:
                buff.rect.y += self.buff_moving_speed_list[buff_number]
                if buff.rect.bottom >= self.window_rect.bottom:
                    self.buff_list_list[buff_number].remove(buff)

        # for buff_list in range(len(self.buff_list_list)):
        #     if pygame.sprite.spritecollide(self.ship_sprite, self.buff_list_list[buff_list], True):
        #         self.buff_timer_list[buff_list] = self.buff_timer_list[buff_list] + self.buff_timer_add_list[buff_list]

        if pygame.sprite.spritecollide(self.ship_sprite, self.buff1_list, True):
            self.buff1_timer += 360
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff2_list, True):
            self.buff2_timer += 360
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff3_list, True):
            self.buff3_timer += 1
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff4_list, True):
            self.buff4_timer += 1
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff5_list, True):
            self.buff5_timer += 512
        
        # buff1
        if self.buff1_timer > 0:
            self.bullet1_width = 300
            self.buff1_timer -= 1
        if self.buff1_timer <= 0:
            self.bullet1_width = 8
            self.buff1_timer = 0
        # buff2
        if self.buff2_timer > 0:
            self.bullet_type = '2'
            self.buff2_effect = False
            self.ship_moving_speed = 12
            self.buff2_timer -= 1
        if self.buff2_timer <= 0:
            self.bullet_type = '1'
            self.buff2_effect = True
            self.ship_moving_speed = 7
            self.buff2_timer = 0
        # buff3
        if self.buff3_timer > 0:
            self.empty_all_alien()
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
        
        self.bullet_with_alien1 = []
        for bullet_list in self.bullet_list_list:
            self.bullet_with_alien1.append(pygame.sprite.groupcollide(bullet_list, self.alien1_list, self.buff2_effect, True))
        self.bullet_with_alien2 = []
        for bullet_list in self.bullet_list_list:
            self.bullet_with_alien2.append(pygame.sprite.groupcollide(bullet_list, self.alien2_list, self.buff2_effect, True))
        self.bullet_with_alien3 = []
        for bullet_list in self.bullet_list_list:
            self.bullet_with_alien3.append(pygame.sprite.groupcollide(bullet_list, self.alien3_list, self.buff2_effect, self.alien3_effect))
        self.bullet_with_alien4 = []
        for bullet_list in self.bullet_list_list:
            self.bullet_with_alien4.append(pygame.sprite.groupcollide(bullet_list, self.alien4_list, self.buff2_effect, True))
        self.bullet_with_alien5 = []
        for bullet_list in self.bullet_list_list:
            self.bullet_with_alien5.append(pygame.sprite.groupcollide(bullet_list, self.alien5_list, self.buff2_effect, True))

        self.bullet_with_alien_group1 = []
        for bullet_list in self.bullet_list_list:
            self.bullet_with_alien_group1.append(pygame.sprite.groupcollide(bullet_list, self.alien_group1_list, self.buff2_effect, True))

        self.bullet_with_alien_list = [self.bullet_with_alien1, self.bullet_with_alien2, self.bullet_with_alien3, self.bullet_with_alien4, self.bullet_with_alien5, self.bullet_with_alien_group1]

        for bullet_with_alien in  self.bullet_with_alien_list:
            for hit in bullet_with_alien:
                if len(hit) != 0:
                    self.mark += len(hit)
                    random_hit_sound_effect = random.randint(1,4)
                    hit_sound_effect = pygame.mixer.Sound("assets/sound/effect/toggle_00"+str(random_hit_sound_effect)+".ogg")
                    hit_sound_effect.set_volume(0.1)
                    pygame.mixer.Channel(1).play(hit_sound_effect)

        bullet_with_bullet = pygame.sprite.groupcollide(self.bullet1_list, self.bulletA1_list, True, True)
        
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
            elif self.bullet_type == '2':
                if self.bullet2_timer > 0:
                    self.bullet2_timer -= 1
                if self.bullet2_timer <= 0:
                    bullet_sprite = pygame.sprite.Sprite()
                    bullet_sprite.rect = pygame.Rect(0,0,self.bullet2_width,16)
                    bullet_sprite.rect.midbottom = self.ship_sprite.rect.midtop
                    self.bullet2_list.add(bullet_sprite)
                    self.bullet2_timer = 5

        for alien4 in self.alien4_list:
            if self.bulletA1_timer > 0:
                self.bulletA1_timer -= 1
            if self.bulletA1_timer <= 0:
                bullet_sprite = pygame.sprite.Sprite()
                bullet_sprite.rect = pygame.Rect(0,0,self.bulletA1_width,16)
                bullet_sprite.rect.midtop = alien4.rect.midbottom
                self.bulletA1_list.add(bullet_sprite)
                self.bulletA1_timer = 30

        if self.buff5_effect == True:
            game_over_list_list = [self.alien_list_list,self.bulletA_list_list]
            for game_over_list in game_over_list_list:
                for item in game_over_list:
                    if pygame.sprite.spritecollideany(self.ship_sprite, item):
                        self.game_over()

        
        self.spawn()
        self.save()

    def page_GameOver(self):

        self.window.fill((0, 0, 0))

        self.GameOver_text1 = self.font128.render("Game Over", True, (255,255,255))
        self.GameOver_text1_rect = self.GameOver_text1.get_rect()
        self.GameOver_text1_rect.center = self.window_rect.center
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
            time.sleep(0.2)
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

    def alien_group_spawn(self):
        if self.try_alien_group_spawn_timer == 0:
            alien_space_sprite = pygame.sprite.Sprite()
            alien_space_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien1.png"),(64,64))
            alien_space_sprite.rect = alien_space_sprite.image.get_rect()
            
            space_x = self.window_width - alien_space_sprite.rect.width*2
            # space_y = self.window_height - self.ship_height - alien_space_sprite.rect.height*3
            number_x = space_x // (alien_space_sprite.rect.width*2)
            # number_y = space_y // (alien_space_sprite.rect.height*2)
            # for y in range(number_y):
            for x in range(number_x):
                alien_sprite = pygame.sprite.Sprite()
                alien_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien1.png"),(64,64))
                alien_sprite.rect = alien_sprite.image.get_rect()
                alien_sprite.rect.x = alien_sprite.rect.width + alien_sprite.rect.width*2*x
                alien_sprite.rect.y = - alien_sprite.rect.height*2
                self.alien_group1_list.add(alien_sprite)

    def alien_spawn(self):
        try_alien_spawn = random.randint(1,10)
        if try_alien_spawn == 1:
            alien_spawn_type = random.randint(1,100)
            if 1 <= alien_spawn_type <= 20:
                alien_sprite = pygame.sprite.Sprite()
                alien_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien1.png"),(64,64))
                alien_sprite.rect = alien_sprite.image.get_rect()
                alien_sprite.rect.x = random.randint(alien_sprite.rect.width,self.window_width-alien_sprite.rect.width*2)
                alien_sprite.rect.y = -alien_sprite.rect.height
                self.alien1_list.add(alien_sprite)
            if 21 <= alien_spawn_type <= 40:
                alien_sprite = pygame.sprite.Sprite()
                alien_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien2.png"),(64,64))
                alien_sprite.rect = alien_sprite.image.get_rect()
                alien_sprite.rect.x = random.randint(alien_sprite.rect.width,self.window_width-alien_sprite.rect.width*2)
                alien_sprite.rect.y = -alien_sprite.rect.height
                self.alien2_list.add(alien_sprite)
            if 41 <= alien_spawn_type <= 60:
                alien_sprite = pygame.sprite.Sprite()
                alien_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien3.png"),(64,64))
                alien_sprite.rect = alien_sprite.image.get_rect()
                alien_sprite.rect.x = random.randint(alien_sprite.rect.width,self.window_width-alien_sprite.rect.width*2)
                alien_sprite.rect.y = -alien_sprite.rect.height
                self.alien3_list.add(alien_sprite)
            if 61 <= alien_spawn_type <= 80:
                alien_sprite = pygame.sprite.Sprite()
                alien_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien4.png"),(64,64))
                alien_sprite.rect = alien_sprite.image.get_rect()
                alien_sprite.rect.x = random.randint(alien_sprite.rect.width,self.window_width-alien_sprite.rect.width*2)
                alien_sprite.rect.y = -alien_sprite.rect.height
                self.alien4_list.add(alien_sprite)
            if 81 <= alien_spawn_type <= 100:
                alien_sprite = pygame.sprite.Sprite()
                alien_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/alien5.png"),(64,64))
                alien_sprite.rect = alien_sprite.image.get_rect()
                alien_sprite.rect.x = random.randint(alien_sprite.rect.width,self.window_width-alien_sprite.rect.width*2)
                alien_sprite.rect.y = -alien_sprite.rect.height
                self.alien5_list.add(alien_sprite)
    
    def buff_spawn(self):
        try_buff_spawn = random.randint(1,500)
        if try_buff_spawn == 1:
            buff_spawn_type = random.randint(1,100)
            if 1 <= buff_spawn_type <= 30:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff1.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff1_list.add(buff_sprite)
            if 31 <= buff_spawn_type <= 70:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff2.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff2_list.add(buff_sprite)
            if 71 <= buff_spawn_type <= 80:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff3.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff3_list.add(buff_sprite)
            if 81 <= buff_spawn_type <= 90:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff4.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff4_list.add(buff_sprite)
            if 91 <= buff_spawn_type <= 100:
                buff_sprite = pygame.sprite.Sprite()
                buff_sprite.image = pygame.transform.scale(pygame.image.load("assets/graphics/image/buff5.png"),(32,32))
                buff_sprite.rect = buff_sprite.image.get_rect()
                buff_sprite.rect.x = random.randint(buff_sprite.rect.width,self.window_width-buff_sprite.rect.width*2)
                buff_sprite.rect.y = -buff_sprite.rect.height
                self.buff5_list.add(buff_sprite)

    def game_over(self):
        self.empty_all_alien()
        self.empty_all_bullet()
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
        all_alien_list = [self.alien1_list,self.alien2_list,self.alien3_list,self.alien4_list,self.alien5_list,self.alien_group1_list]
        for alien_list in all_alien_list:
            for alien_sprite in alien_list:
                alien_sprite.kill()
            # self.alien1_list.empty()
    def empty_all_bullet(self):
        all_bullet_list_list_list = [self.bullet_list_list,self.bulletA_list_list]
        for bullet_list_list in all_bullet_list_list_list:
            for bullet_list in bullet_list_list:
                for bullet_sprite in bullet_list:
                    bullet_sprite.kill()

if __name__ == '__main__':
    game = Game()
    game.run()