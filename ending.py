import pygame

class Ending():
    
    run = True
    
    def __init__(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.Font = pygame.font.SysFont('malgungothic', 250)
    def draw(self,score):
        self.score = score
        self.time = pygame.time.get_ticks()
        while self.run:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.Font.render(f'score:{self.score}',True,(255,255,255)),(175,200))
            if pygame.time.get_ticks() - self.time > 5000:
                self.run = False
            pygame.display.update()
            self.clock.tick(100)
