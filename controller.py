from setting import *
from asset import Asset
from map import Map
from tile import Tile
from player import Player
from luigi import Luigi

class Controller(Asset,Map):
    def __init__(self,screen):
        Asset.__init__(self)
        Map.__init__(self)
        self.screen=screen
        self.tiles=pygame.sprite.Group()
        self.player=pygame.sprite.GroupSingle()
        self.luigi=pygame.sprite.GroupSingle(Luigi())
        self.level=1
        self.map_create()
    
    def map_create(self):
        for row,column in enumerate(self.stage[str(self.level)]):
            for index,data in enumerate(column):
                x=index*(16*SCALE)
                y=row*(16*SCALE)
                if data!='_' and data!='p' and data!='h':
                    self.tiles.add(Tile(data,(x,y)))
                elif data=='p':
                    self.player.add(Player((x,y),'super_mario'))
    
    def get_map_position(self,anything):
        for row,column in enumerate(self.stage[str(self.level)]):
            for index,data in enumerate(column):
                x=index*(16*SCALE)
                y=row*(16*SCALE)
                if data==anything:
                    return x,y
    
    def collision(self):
        player=self.player.sprite
        player.set_gravity()
        for tile in self.tiles:
            if pygame.sprite.collide_mask(player,tile):
                if player.rect.bottom>=tile.rect.top:
                    player.dy=0
                    player.rect.bottom=tile.rect.top
                    self.player.collide_tile=True
    
    def run(self):
        # self.tiles.update()
        self.collision()
        self.screen.fill('#aff9f0')
        self.tiles.draw(self.screen)
        self.player.update()
        self.player.draw(self.screen)
        self.luigi.draw(self.screen)
        self.screen.blit(self.ui_images['hud'],self.get_map_position('h'))
        # for y in range(14):
        #     for x in range(16):
        #         pygame.draw.rect(self.screen,'blue',(x*(16*SCALE),y*(16*SCALE),16*SCALE,16*SCALE), width=1)