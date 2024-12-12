import pygame
import random
class Mole():
    
    def __init__(self,screen,img):
        self.screen = screen
        self.img = img
        self.xy = (random.randint(0,1200),random.randint(0,900))
        self.mysummontime = pygame.time.get_ticks()
        
    def draw(self):
        self.screen.blit(self.img,(self.xy))



