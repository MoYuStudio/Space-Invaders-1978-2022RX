
import sqlite3
import pygame

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()
 
data = sqlite3.connect('data.db')
c = data.cursor()

data_name = 'window_widen'

cursor = c.execute('select * from main where name = "{}"'.format(str(data_name)))

dataline = 1
data_out = cursor.fetchone()
print(data_out[dataline])
print(type(data_out[dataline]))

sound = pygame.mixer.Sound("assets/sound/song/魔王魂 旧ゲーム音楽 ラストボス02.mp3")

# set
# c.execute('insert into main values("window_widen", "1")')
# update
# c.execute('update main set info = "2" where name = "window_widen"')

sound_save = 'insert into main values("sound1", {})'.format(sound)
print(sound_save)
c.execute(sound_save)

data_load = {}
for row in c.execute('select * from main'):
    data_load[row[0]] = row[1]

print(data_load)

data.commit()
data.close()