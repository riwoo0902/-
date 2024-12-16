import pygame
import random
class Mole():
    
    def __init__(self,screen,img):
        self.screen = screen
        self.img = img
        self.x = random.randint(0,1100)
        self.y = random.randint(0,800)
        self.rec = self.img.get_rect()
        self.rec.centerx = self.x
        self.rec.centery = self.y
        self.mysummontime = pygame.time.get_ticks()
       
    def moledel(self):
        if pygame.time.get_ticks() - self.mysummontime > 2500:
            return  True
        return False
    def draw(self):
        self.screen.blit(self.img,(self.x,self.y))
        self.moledel()


