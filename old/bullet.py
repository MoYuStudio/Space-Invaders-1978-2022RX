
import random
import pygame

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

class Bullet:
    def __init__(self):

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
        self.bullet_list_list = [self.bullet1_list,self.bullet2_list,self.bullet3_list,self.bullet4_list,self.bullet5_list,self.bulletA1_list]
        self.bullet1_moving_speed = 6
        self.bullet1_width = 8
        self.bullet1_timer = 0
        self.bullet1_color = (50,250,50)
        self.bullet2_moving_speed = 2
        self.bullet2_width = 8
        self.bullet2_timer = 0
        self.bullet2_color = (150,50,250)
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

    def blit(self):
        for bullet in self.bullet1_list:
            pygame.draw.rect(self.window, self.bullet1_color, bullet)
            bullet.rect.y -= self.bullet1_moving_speed
            if bullet.rect.bottom < 0:
                self.bullet1_list.remove(bullet)
        for bullet in self.bullet2_list:
            pygame.draw.rect(self.window, self.bullet2_color, bullet)
            bullet.rect.y -= self.bullet2_moving_speed
            if bullet.rect.bottom < 0:
                self.bullet2_list.remove(bullet)
        for bullet in self.bullet3_list:
            pygame.draw.rect(self.window, self.bullet3_color, bullet)
            bullet.rect.y -= self.bullet3_moving_speed
            if bullet.rect.bottom < 0:
                self.bullet3_list.remove(bullet)
        for bullet in self.bullet4_list:
            pygame.draw.rect(self.window, self.bullet4_color, bullet)
            bullet.rect.y -= self.bullet4_moving_speed
            if bullet.rect.bottom < 0:
                self.bullet4_list.remove(bullet)
        for bullet in self.bullet5_list:
            pygame.draw.rect(self.window, self.bullet5_color, bullet)
            bullet.rect.y -= self.bullet5_moving_speed
            if bullet.rect.bottom < 0:
                self.bullet5_list.remove(bullet)

    def run(self):

        for buff_number in range(len(self.buff_list_list)):
            for buff in self.buff_list_list[buff_number]:
                buff.rect.y += self.buff_moving_speed_list[buff_number]
                if buff.rect.bottom >= self.window_rect.bottom:
                    self.buff_list_list[buff_number].remove(buff)

        if pygame.sprite.spritecollide(self.ship_sprite, self.buff1_list, True):
            self.buff1_timer += 240
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff2_list, True):
            self.buff2_timer += 240
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff3_list, True):
            self.buff3_timer += 1
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff4_list, True):
            self.buff4_timer += 1
        if pygame.sprite.spritecollide(self.ship_sprite, self.buff5_list, True):
            self.buff5_timer += 360
            
        # buff1
        if self.buff1_timer > 0:
            self.bullet_type = '3'
            self.buff1_timer -= 1
        if self.buff1_timer <= 0:
            self.bullet_type = '1'
            self.buff1_timer = 0
        # buff2
        if self.buff2_timer > 0:
            self.bullet_type = '2'
            self.buff2_effect = False
            self.buff2_timer -= 1
        if self.buff2_timer <= 0:
            self.bullet_type = '1'
            self.buff2_effect = True
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

    def spawn(self):
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