import pygame
from pygame.sprite import Group
import random
import os

pygame.init()

red = (255,0,0)
width=500
height=400
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#load picture
backimg = pygame.image.load(os.path.join("picture","413726.png")).convert()
backimg = pygame.transform.scale(backimg,(500,400))

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x=(width/2)-25
        self .rect.bottom = height-10
        #self.radius = 3
        #pygame.draw.circle(self.image,(0,0,0),self.rect.center,self.radius)
        self.speed = 5
        
    def update(self):
        key = pygame.key.get_pressed()

        if key [pygame.K_d] or key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.rect.x -=self.speed
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left<0:
            self.rect.left = 0
    
    def attack(self):
        b1=ball(self.rect.centerx,self.rect.top)
        all_sprites.add(b1)
        balls.add(b1)

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((0,0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0 , width - self.rect.width)
        self.rect.y = -10
        self.radius = 5
        pygame.draw.circle(self.image,(255,255,255),(self.rect.x,self.rect.y),self.radius)
        self.speed = random.randrange(2,10)
        self.speedx = random.randrange(-2,2)
        
    def update(self):
        self.rect.y +=self.speed
        self.rect.x += self.speedx
        
        if self.rect.top >height or self.rect.left >width or self.rect.right<0:
            self.rect.x = random.randrange(0 , width - self.rect.width)
            self.rect.y = -10
            self.speed = random.randrange(2,10)
            self.speedx = random.randrange(-2,2)
        
class ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -5
        
    def update(self):
        self.rect.y +=self.speed
        
        if self.rect.bottom <0 :
            self.kill()
        

#setup
all_sprites = pygame.sprite.Group()
enemys = pygame.sprite.Group()
balls = pygame.sprite.Group()
p1=player()
all_sprites.add(p1)
for i in range(4):
    rock = enemy()
    all_sprites.add(rock)
    enemys.add(rock)


#gameloop
game = True

while (game):
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.attack()
        


    #更新遊戲
    all_sprites.update()
    hits = pygame.sprite.groupcollide(enemys,balls,True,True)
    for hit in hits:
        en = enemy()
        all_sprites.add(en)
        enemys.add(en)
    
    dmages = pygame.sprite.spritecollide(p1,enemys,False)
    if dmages:
        for x in all_sprites:
            x.speed = 0
            x.speedx = 0



    #render
    screen.fill((255,255,255))
    screen.blit(backimg,(0,0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()