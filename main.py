from pygame import *
from random import randint
from time import time as timer
font.init()
window = display.set_mode((700,500))
display.set_caption("ЧТО ТО")
background = transform.scale(image.load('fon.png'),(700,500))
num_fire = 0
gaf = False
font.init
font = font.Font(None,70)

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


class Player2(GameSprite):
    
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
    
class Player(GameSprite):
    
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed    
        
       
            
    
        

lost = 0
jopa = 0




class Enemy(GameSprite):
    speed_x = 5
    speed_y = 5
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if sprite.collide_rect(hero, self) or sprite.collide_rect(hero2, self):
            self.speed_x *=-1
        if self.rect.y <0 or  self.rect.y >440:
            self.speed_y *=-1
        


            
            
            










hero = Player("brevno.png", 0, 0, 7, 80,120)

hero2 = Player2("brevno.png", 630, 0, 7, 80,120)

myachik = Enemy('myachik_erere.png', 200, 200, 7, 65, 65)




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
        myachik.update()
        myachik.reset()
        hero2.update()
        


        hero2.reset()
        hero.reset()
        if myachik.rect.x < -60:
            finish = True
            faf = font.render("Player 2 win!!!",True,(255,215,0))
            window.blit(faf, (200, 200))
    
        if myachik.rect.x > 680:
            finish = True
            rar = font.render("Player 1 win!!!",True,(255,215,0))
            window.blit(rar, (200, 200))
        


    for e in event.get():
        if e.type == QUIT:
            game = False


    clock. tick(FPS) 
    display.update()



