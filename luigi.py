from setting import *
from asset import *

class Luigi(pygame.sprite.Sprite,Asset):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        self.frame=0
        self.image=self.small_mario_images['small_luigi'][self.frame]
        self.rect=self.image.get_rect(right=SCREEN_WIDTH)