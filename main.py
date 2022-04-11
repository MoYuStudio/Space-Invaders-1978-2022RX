
################################################################
#                 MoYu Studio © 2021 - 2022                    #
################################################################
#                SPACE INVADERS 1978 2022RX                    #
#                    Dv20220411 a1 Bata                        #
################################################################

import sys
import time
import pygame

pygame.init()

RUN = True

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_title = pygame.display.set_caption("SPACE INVADERS 1978 2022RX")
window_icon = pygame.display.set_icon(pygame.image.load("image/alien1.png"))
window_clock = pygame.time.Clock()
window_rect = window.get_rect()

ship_sprite = pygame.sprite.Sprite()
ship_sprite.image = pygame.transform.scale(pygame.image.load("image/ship1.png"),(64,64))
ship_sprite.rect = ship_sprite.image.get_rect()
ship_sprite.rect.midbottom = window_rect.midbottom
ship_moving_speed = 6
ship_moving_up = False
ship_moving_down = False
ship_moving_right = False
ship_moving_left = False
ship_blood = 3

bullet_list = pygame.sprite.Group()
bullet_moving_speed = 6

alien_list = pygame.sprite.Group()
alien_moving_speed = 16
alien_direction = 3

def alien_spawn():
    alien_space_sprite = pygame.sprite.Sprite()
    alien_space_sprite.image = pygame.transform.scale(pygame.image.load("image/alien1.png"),(64,64))
    alien_space_sprite.rect = alien_space_sprite.image.get_rect()
    window_width, window_height = window_rect.size
    ship_width, ship_height = ship_sprite.rect.size
    space_x = window_width - alien_space_sprite.rect.width*2
    space_y = window_height - ship_height - alien_space_sprite.rect.height*3
    number_x = space_x // (alien_space_sprite.rect.width*2)
    number_y = space_y // (alien_space_sprite.rect.height*2)
    for y in range(number_y):
        for x in range(number_x):
            alien_sprite = pygame.sprite.Sprite()
            alien_sprite.image = pygame.transform.scale(pygame.image.load("image/alien1.png"),(64,64))
            alien_sprite.rect = alien_sprite.image.get_rect()
            alien_sprite.rect.x = alien_sprite.rect.width + alien_sprite.rect.width*2*x
            alien_sprite.rect.y = alien_sprite.rect.height + alien_sprite.rect.height*2*y
            alien_list.add(alien_sprite)

alien_spawn()

font32 = pygame.font.Font("font/LockClock.ttf", 32)
font64 = pygame.font.Font("font/LockClock.ttf", 64)

text1 = font32.render("SPACE INVADERS 1978 2022RX", True, (255,255,255))
text1_rect = text1.get_rect()
text1_rect.midtop = window_rect.midtop

text2 = font32.render("Press SPACE to Fire", True, (255,255,255))
text2_rect = text2.get_rect()
text2_rect.midtop = text1_rect.midbottom

text3 = font32.render("Press Esc Out", True, (255,255,255))
text3_rect = text3.get_rect()
text3_rect.midtop = text2_rect.midbottom

pygame.display.flip()

while RUN:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUN = False
                sys.exit()

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                ship_moving_up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                ship_moving_down = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship_moving_left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship_moving_right = True
            if event.key == pygame.K_SPACE:
                bullet_sprite = pygame.sprite.Sprite()
                bullet_sprite.rect = pygame.Rect(0,0,8,16)
                bullet_sprite.rect.midbottom = ship_sprite.rect.midtop
                # bullet_sprite.rect.y += 64
                bullet_list.add(bullet_sprite)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                ship_moving_up = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                ship_moving_down = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship_moving_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship_moving_right = False

    if ship_moving_up and ship_sprite.rect.top > 0:
        ship_sprite.rect.y -= ship_moving_speed
    if ship_moving_down and ship_sprite.rect.bottom < window_rect.bottom:
        ship_sprite.rect.y += ship_moving_speed
    if ship_moving_right and ship_sprite.rect.right < window_rect.right:
        ship_sprite.rect.x += ship_moving_speed
    if ship_moving_left and ship_sprite.rect.left > 0:
        ship_sprite.rect.x -= ship_moving_speed

    window.fill((0, 0, 0))
    
    for bullet in bullet_list:
        pygame.draw.rect(window, (255,0,0), bullet)
        bullet.rect.y -= bullet_moving_speed
        if bullet.rect.bottom < 0:
            bullet_list.remove(bullet)
    for alien in alien_list:
        alien.rect.x += 1*alien_direction
        if alien.rect.right >= window_rect.right or alien.rect.left <= 0:
            alien_direction *= -1
            for alien in alien_list:
                alien.rect.y += alien_moving_speed

        if alien.rect.bottom >= window_rect.bottom:
            alien_list.empty()
            bullet_list.empty()
            alien_spawn()
            ship_sprite.rect.midbottom = window_rect.midbottom
            time.sleep(0.5)
            ship_blood -= 1
            if ship_blood == 0:
                RUN = False
                sys.exit()

    window.blit(ship_sprite.image, ship_sprite.rect)
    alien_list.draw(window)
    window.blit(text1, text1_rect)
    window.blit(text2, text2_rect)
    window.blit(text3, text3_rect)

    text4 = font64.render("Ship Blood :"+str(ship_blood), True, (255,255,255))
    text4_rect = text4.get_rect()
    text4_rect.midtop = text3_rect.midbottom
    window.blit(text4, text4_rect)

    pygame.sprite.groupcollide(bullet_list, alien_list, True, True)

    if not alien_list:
        alien_spawn()

    if pygame.sprite.spritecollideany(ship_sprite, alien_list):
        alien_list.empty()
        bullet_list.empty()
        alien_spawn()
        ship_sprite.rect.midbottom = window_rect.midbottom
        time.sleep(0.5)
        ship_blood -= 1
        if ship_blood == 0:
            RUN = False
            sys.exit()

    pygame.display.update()
    window_clock.tick(60)

    