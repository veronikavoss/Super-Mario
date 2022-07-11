from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,image,type,element,pos,index=0):
        pygame.sprite.Sprite.__init__(self)
        self.index=index
        self.image=image['1'][type][int(element)]
        self.rect=self.image.get_rect(topleft=pos)
        self.stop=False
    
    def update(self,speed_x,speed_y):
        self.rect.x+=speed_x
        self.rect.y+=speed_y