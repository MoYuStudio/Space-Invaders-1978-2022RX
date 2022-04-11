
################################################################
#                 MoYu Studio © 2021 - 2022                    #
################################################################
#                SPACE INVADERS 1978 2022RX                    #
#                    Dv20220411 a1 Bata                        #
################################################################

import sys
import time
import pygame

class Game:

    def __init__(self):

        pygame.init()
        pygame.display.init()
        pygame.mixer.init()

        # Config =========================================================================================================

        self.RUN = True

        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.window_title = pygame.display.set_caption("SPACE INVADERS 1978 2022RX")
        self.window_icon = pygame.display.set_icon(pygame.image.load("assets/graphics/image/alien1.png"))
        self.window_clock = pygame.time.Clock()
        self.window_rect = self.window.get_rect()

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

        self.bullet_list = pygame.sprite.Group()
        self.bullet_moving_speed = 6

        self.alien_list = pygame.sprite.Group()
        self.alien_moving_speed = 16
        self.alien_direction = 3

    def set(self):

        self.alien_spawn()

        self.font32 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 32)
        self.font64 = pygame.font.Font("assets/graphics/font/LockClock.ttf", 64)

        self.text1 = self.font32.render("SPACE INVADERS 1978 2022RX", True, (255,255,255))
        self.text1_rect = self.text1.get_rect()
        self.text1_rect.midtop = self.window_rect.midtop

        self.text2 = self.font32.render("Press SPACE to Fire", True, (255,255,255))
        self.text2_rect = self.text2.get_rect()
        self.text2_rect.midtop = self.text1_rect.midbottom

        self.text3 = self.font32.render("Press Esc Out", True, (255,255,255))
        self.text3_rect = self.text3.get_rect()
        self.text3_rect.midtop = self.text2_rect.midbottom

        pygame.display.flip()

    def run(self):

        self.set()

        # Mainloop =========================================================================================================

        while self.RUN:

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.RUN = False
                    sys.exit()
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        self.RUN = False
                        sys.exit()

                    if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
                        self.ship_moving_up = True
                    if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
                        self.ship_moving_down = True
                    if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
                        self.ship_moving_left = True
                    if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
                        self.ship_moving_right = True
                    if self.event.key == pygame.K_SPACE:
                        bullet_sprite = pygame.sprite.Sprite()
                        bullet_sprite.rect = pygame.Rect(0,0,8,16)
                        bullet_sprite.rect.midbottom = self.ship_sprite.rect.midtop
                        # bullet_sprite.rect.y += 64
                        self.bullet_list.add(bullet_sprite)
                    
                if self.event.type == pygame.KEYUP:
                    if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
                        self.ship_moving_up = False
                    if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
                        self.ship_moving_down = False
                    if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
                        self.ship_moving_left = False
                    if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
                        self.ship_moving_right = False

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
                pygame.draw.rect(self.window, (255,0,0), bullet)
                bullet.rect.y -= self.bullet_moving_speed
                if bullet.rect.bottom < 0:
                    self.bullet_list.remove(bullet)
            for alien in self.alien_list:
                alien.rect.x += 1*self.alien_direction
                if alien.rect.right >= self.window_rect.right or alien.rect.left <= 0:
                    self.alien_direction *= -1
                    for alien in self.alien_list:
                        alien.rect.y += self.alien_moving_speed

                if alien.rect.bottom >= self.window_rect.bottom:
                    self.game_over()

            self.window.blit(self.ship_sprite.image, self.ship_sprite.rect)
            self.alien_list.draw(self.window)
            self.window.blit(self.text1, self.text1_rect)
            self.window.blit(self.text2, self.text2_rect)
            self.window.blit(self.text3, self.text3_rect)

            self.text4 = self.font64.render("Ship Blood :"+str(self.ship_blood), True, (255,255,255))
            self.text4_rect = self.text4.get_rect()
            self.text4_rect.midtop = self.text3_rect.midbottom
            self.window.blit(self.text4, self.text4_rect)

            pygame.sprite.groupcollide(self.bullet_list, self.alien_list, True, True)

            if not self.alien_list:
                self.alien_spawn()

            if pygame.sprite.spritecollideany(self.ship_sprite, self.alien_list):
                self.game_over()

            pygame.display.update()
            self.window_clock.tick(60)

    # Components ===========================================================================================================

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
                alien_sprite.rect.y = alien_sprite.rect.height + alien_sprite.rect.height*2*y
                self.alien_list.add(alien_sprite)

    def game_over(self):
        self.alien_list.empty()
        self.bullet_list.empty()
        self.alien_spawn()
        self.ship_sprite.rect.midbottom = self.window_rect.midbottom
        time.sleep(0.5)
        self.ship_blood -= 1
        if self.ship_blood == 0:
            RUN = False
            sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()