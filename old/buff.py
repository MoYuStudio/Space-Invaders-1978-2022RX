
import pygame

class Buff:
    def __init__(self):
        # Buff =
        # 1范围Buff 2穿透Buff 3清屏Buff 4医疗Buff 5无敌Buff 6极速Buff
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
        self.buff1_timer_add = 240
        self.buff2_timer_add = 240
        self.buff3_timer_add = 1
        self.buff4_timer_add = 1
        self.buff5_timer_add = 360
        self.buff_timer_add_list = [self.buff1_timer_add,self.buff2_timer_add,self.buff3_timer_add,self.buff4_timer_add,self.buff5_timer_add]
        self.buff2_effect = True
        self.buff5_effect = True

    def blit(self):
        for buff_list in self.buff_list_list:
            try:
                buff_list.draw(self.window)
            except:
                pass