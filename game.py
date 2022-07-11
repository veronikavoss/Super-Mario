from setting import *
from controller import Controller
from map import Map

class SuperMario:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen=pygame.display.set_mode(SCREEN_SIZE)
        self.clock=pygame.time.Clock()
        self.running=True
        self.controller=Controller(self.screen)
        self.loop()
    
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            
            self.controller.run()
            
            self.clock.tick(FPS)
            pygame.display.update()

SuperMario()
pygame.quit()