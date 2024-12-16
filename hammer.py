import pygame
from mole import *
class Hammer():
    
    def __init__(self,screen,moles):
        self.screen = screen
        self.moles = moles
        self.img1 = pygame.image.load('./image/hammer1.png')
        self.img2 = pygame.image.load('./image/hammer2.png')
        self.img = pygame.transform.scale(self.img1,(100,100))
        self.rec = self.img.get_rect()
        
        self.lock = 0
        self.hammertime = 0
        self.hammertime2 = 0
        self.Font = pygame.font.SysFont('malgungothic', 50)
        self.score = 0
    def click(self):
        self.hammertime2 = pygame.time.get_ticks()
        if pygame.mouse.get_pressed()[0]:
            if self.lock == 0:
                self.lock = 1
                self.hammertime = pygame.time.get_ticks()
                for i in range(len(self.moles)):
                    if self.moles[i].rec.colliderect(self.rec):
                        del self.moles[i]
                        self.score += 1
                        break
                
        if pygame.mouse.get_pressed()[0] == False:
            self.lock = 0
        if self.hammertime2 - self.hammertime < 250:
            self.img = pygame.transform.scale(self.img2,(100,100))
        else:
            self.img = pygame.transform.scale(self.img1,(100,100))
    

    def draw(self):
        self.click()
        pos = pygame.mouse.get_pos()
        self.rec.centerx = pos[0]-50
        self.rec.centery = pos[1]-50
        self.screen.blit(self.img,(pos[0]-50,pos[1]-50))
        self.screen.blit(self.Font.render(f'score:{self.score}',True,(255,255,255)),(0,0))
 
    
    