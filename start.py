import pygame
from background import *
from hammer import *
from ending import *
class Start():
    isActive = True
    screen = (1200,900)
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Limriwoo Calculator")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen)
        self.background = Background(self.screen)
        self.hammer = Hammer(self.screen,self.background.moles)
        self.ending = Ending(self.screen)
        self.Font = pygame.font.SysFont('malgungothic', 50)
    def eventProcess(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.isActive = False
            
    def end(self):
        if pygame.time.get_ticks() >= 30000:
            self.isActive = False
        self.screen.blit(self.Font.render(f'time:{30000-pygame.time.get_ticks()}',True,(255,255,255)),(950,0)) 
    
    def run(self):
        while self.isActive:
            self.screen.fill((0, 255, 255))
            self.eventProcess()
            self.background.run()
            self.hammer.draw()
            self.end() 
            pygame.display.update()
            self.clock.tick(100)
        self.ending.draw(self.hammer.score)
        
        
if __name__ == '__main__':
    game = Start()
    game.run()