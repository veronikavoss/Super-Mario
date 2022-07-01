from setting import *
from asset import *

class Tile(pygame.sprite.Sprite,Asset):
    def __init__(self,type,pos):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        self.image=self.stage_tile['1']['ground'][int(type)]
        self.rect=self.image.get_rect(topleft=pos)
    
    def update(self):
        self.rect.center=pygame.mouse.get_pos()