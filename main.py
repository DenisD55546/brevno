from pygame import *
from random import randint
from time import time as timer
font.init()
window = display.set_mode((700,500))
display.set_caption("программа")
background = transform.scale(image.load('fon.png'),(700,500))
num_fire = 0
gaf = False


class GameSprite(sprite.Sprite):
    def __init__(self, playar_image, player_x, player_y, player_speed, width, heght):
        super().__init__()
        self.image = transform.scale(image.load(playar_image),(width, heght))
        self.speed = player_speed
        self.rect =self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 610:
            self.rect.x += self.speed
    
    
        
        
            
    
        

lost = 0
jopa = 0
font1 = font.SysFont('Arial',36)



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50
            self.rect.x = randint(1,645)
            self.speed = randint(1,2)

            global lost
            lost = lost + 1

class Enem(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50
            self.rect.x = randint(1,645)
            self.speed = randint(1,3)

            
            
            
psina = sprite.Group()



class Bulet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
            







hero = Player("brevno.png", 200, 400, 7, 65,65)



font = font.SysFont('Arial', 50)


clock = time .Clock()
FPS = 60
#mixer.init()
#mixer.music.load("space.ogg")
#mixer.music.play()
finish = False
game = True
while game:

    
    if finish != True:
        window.blit(background, (0, 0))
        hero.update()
        


        hero.reset()

        
    


        


    for e in event.get():
        if e.type == QUIT:
            game = False


    clock. tick(FPS) 
    display.update()











