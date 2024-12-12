import pygame
from mole import *

class Background():
    
    moles = []
    
    def __init__(self,screen):
        self.screen = screen
        self.img = pygame.image.load('./image/mole.png')
        self.img = pygame.transform.scale(self.img,(100,100))
        self.molesummontime = 0
        
    def molesummon(self):
        
        if pygame.time.get_ticks() - self.molesummontime > 500:
            self.molesummontime = pygame.time.get_ticks()
            self.moles.append(Mole(self.screen,self.img))
    def moledraw(self):
        for i in range(len(self.moles)):
            self.moles[i].draw()
            if pygame.time.get_ticks() - self.moles[i].mysummontime > 2500:
                del self.moles[i]
                break
                
    def run(self):
        self.molesummon()
        self.moledraw()
        
        