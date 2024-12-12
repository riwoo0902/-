import pygame

class Hammer():
    
    def __init__(self,screen):
        self.screen = screen
        
        self.img1 = pygame.image.load('./image/hammer1.png')
        self.img2 = pygame.image.load('./image/hammer2.png')
        self.img = pygame.transform.scale(self.img1,(100,100))
        self.lock = 0
        self.hammertime = 0
        self.hammertime2 = 0
          
    def click(self):
        self.hammertime2 = pygame.time.get_ticks()
        if pygame.mouse.get_pressed()[0]:
            if self.lock == 0:
                self.lock = 1
                self.hammertime = pygame.time.get_ticks()
        if pygame.mouse.get_pressed()[0] == False:
            self.lock = 0
            
        if self.hammertime2 - self.hammertime < 250:
            self.img = pygame.transform.scale(self.img2,(100,100))
        else:
            self.img = pygame.transform.scale(self.img1,(100,100))
            
            
    def draw(self):
        self.click()
        pos = pygame.mouse.get_pos()
        self.screen.blit(self.img,(pos[0]-50,pos[1]-50))
    
    