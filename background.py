import pygame
from mole import *

class Background():
    
    
    
    def __init__(self,screen):
        self.screen = screen
        self.img = pygame.image.load('./image/mole.png')
        self.img = pygame.transform.scale(self.img,(100,100))
        self.bgimg = pygame.image.load('./image/glass.jpg')
        self.bgimg = pygame.transform.scale(self.bgimg,(1200,900))
        self.molesummontime = 0
        self.moles = []
        
    def molesummon(self):
        if pygame.time.get_ticks() - self.molesummontime > 500:
            self.molesummontime = pygame.time.get_ticks()
            self.moles.append(Mole(self.screen,self.img))
            
    def moledraw(self):
        for i in range(len(self.moles)):
            self.moles[i].draw()
        if len(self.moles) != 0:
            if self.moles[0].moledel():
                del self.moles[0]
        

    def run(self):
        self.screen.blit(self.bgimg,(0,0))
        self.molesummon()
        self.moledraw()
        
        