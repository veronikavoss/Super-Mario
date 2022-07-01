from setting import *

class Asset:
    def __init__(self):
        self.tile_sheet=pygame.image.load(os.path.join(IMAGE_PATH,'Stage Tiles.png')).convert_alpha()
        self.mario_sheet=pygame.image.load(os.path.join(IMAGE_PATH,'Mario & Luigi.png')).convert_alpha()
        self.ui_sheet=pygame.image.load(os.path.join(IMAGE_PATH,'HUD & Font.png')).convert_alpha()
        self.get_tile_images()
        self.get_mario_images()
        self.get_ui_images()
    
    def get_tile_images(self):
        self.stage_tile={'1':{'ground':[]}}
        tile_size=16,16
        for y in range(2):
            for x in range(3):
                surface=pygame.Surface(tile_size)
                surface.blit(self.tile_sheet,(0,0),(x*17+443,y*17+154,16,16))
                surface.set_colorkey((127,255,142))
                surface=pygame.transform.scale(surface,(tile_size[0]*SCALE,tile_size[1]*SCALE))
                self.stage_tile['1']['ground'].append(surface)
    
    def get_mario_images(self):
        self.small_mario_images={'small_mario':[],'small_luigi':[]}
        self.super_mario_images={'super_mario':[],'super_luigi':[]}
        
        small_mario=small_mario_width,small_mario_height=16,16
        super_mario1=super_mario1_width,super_mario1_height=16,32
        super_mario2=super_mario2_width,super_mario2_height=24,32
        
        # small mario
        for y,key in enumerate(self.small_mario_images.keys()):
            for x in range(18):
                surface=pygame.Surface(small_mario)
                surface.blit(self.mario_sheet,(0,0),(x*18+1,y*36+16,small_mario_width,small_mario_height))
                surface.set_colorkey((68,145,190))
                surface=pygame.transform.scale(surface,(small_mario_width*SCALE,small_mario_height*SCALE))
                self.small_mario_images[key].append(surface)
        
        # super mario
        for x in range(5):
            surface=pygame.Surface(super_mario1)
            surface.blit(self.mario_sheet,(0,0),(x*18+1,88,super_mario1_width,super_mario1_height))
            surface.set_colorkey((68,145,190))
            surface=pygame.transform.scale(surface,(super_mario1_width*SCALE,super_mario1_height*SCALE))
            self.super_mario_images['super_mario'].append(surface)
    
    def get_ui_images(self):
        temp=[]
        for y in range(3):
            for x in range(12):
                surface=pygame.Surface((8,8))
                surface.blit(self.ui_sheet,(0,0),(x*10+77,y*10+31,8,8))
                surface.set_colorkey('#00e08e')
                surface=pygame.transform.scale(surface,(8*SCALE,8*SCALE))
                temp.append(surface)
        
        self.font_images={'number':[temp[0:11]],'alphabet':[temp[10:]]}
        
        self.ui_images={
            'hud':None
        }
        hud=pygame.Surface((154,30))
        hud.blit(self.ui_sheet,(0,0),(11,127,154,30))
        hud.set_colorkey('#00e08e')
        hud=pygame.transform.scale(hud,(154*SCALE,30*SCALE))
        self.ui_images['hud']=hud