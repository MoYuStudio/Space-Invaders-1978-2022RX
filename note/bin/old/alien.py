
import pygame

class Alien:
    def __init__(self):
                # Alien =
        # 1普通怪 2普通怪 3格挡怪 4攻击怪 5速度怪
        self.alien1_list = pygame.sprite.Group()
        self.alien2_list = pygame.sprite.Group()
        self.alien3_list = pygame.sprite.Group()
        self.alien4_list = pygame.sprite.Group()
        self.alien5_list = pygame.sprite.Group()
        self.alien_group1_list = pygame.sprite.Group()
        self.alien1_moving_speed = 1
        self.alien2_moving_speed = 1
        self.alien3_moving_speed = 1
        self.alien4_moving_speed = 1
        self.alien5_moving_speed = 3
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

    def blit(self):
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

    def run(self):
        for alien in self.alien1_list:
            alien.rect.y += self.alien1_moving_speed
            if alien.rect.bottom >= self.window_rect.bottom:
                self.game_over()
        for alien in self.alien2_list:
            alien.rect.y += self.alien2_moving_speed
            if alien.rect.bottom >= self.window_rect.bottom:
                self.game_over()
        for alien in self.alien3_list:
            alien.rect.y += self.alien3_moving_speed
            if alien.rect.bottom >= self.window_rect.bottom:
                self.game_over()
        for alien in self.alien4_list:
            alien.rect.y += self.alien4_moving_speed
            if alien.rect.bottom >= self.window_rect.bottom:
                self.game_over()
        for alien in self.alien5_list:
            alien.rect.y += self.alien5_moving_speed
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