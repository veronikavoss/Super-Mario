from setting import *
from asset import Asset
from map import Map
from tile import Tile
from player import Player
from enemy import Enemy

class Controller(Asset,Map):
    def __init__(self,screen):
        Asset.__init__(self)
        Map.__init__(self)
        self.screen=screen
        self.edit_mode='playing'
        self.mouse_status='idle'
        self.level=1
        self.stage_level=1
        
        self.map_type='tile'
        self.map_element='0'
        self.tiles=pygame.sprite.Group()
        self.enemies=pygame.sprite.Group()
        self.player=pygame.sprite.GroupSingle()
        self.map_tiles=pygame.sprite.GroupSingle(Tile(self.stage_tile,'ground',self.map_element,(0,0)))
        self.scroll_x=False
        self.scroll_x_speed_edit=0
        self.scroll_y_speed_edit=0
        self.minus_scroll_x=0
        self.minus_scroll_y=-15*(16*SCALE)
        self.background()
        self.map_load()
    
    def background(self):
        bg=pygame.image.load(os.path.join(IMAGE_PATH,'stage1-1.png'))
        bg.set_alpha(120)
        self.bg=pygame.transform.scale(bg,(bg.get_width()*SCALE,bg.get_height()*SCALE))
        self.bg_rect=self.bg.get_rect(y=-15*(16*SCALE))
    
    def map_load(self):
        
        i=0
        for row,column in enumerate(self.stage[str(self.level)][str(self.stage_level)]):
            for index,data in enumerate(column):
                x=index*(16*SCALE)+self.minus_scroll_x
                y=row*(16*SCALE)+self.minus_scroll_y
                # y=row*(16*SCALE)-(16*SCALE*15)
                if data=='p':
                    self.player.add(Player(self.small_mario_images,self.super_mario_images,(x,y),'super_mario',self.edit_mode))
                # elif data=='h':
                #     self.hud_rect=self.ui_images['hud'].get_rect(topleft=(x,y))
                elif data=='g':
                    self.enemies.add(Enemy(self.enemy_images,'goombas','goomba',(x,y)))
                else:
                    if data!='_':
                        i+=1
                        self.tiles.add(Tile(self.stage_tile,'ground',data,(x,y),i))
                    # else:
                    #     self.tiles.add(Tile(self.stage_tile,'background',0,(x,y)))
        with open(os.path.join(CURRENT_PATH,'map_data.txt'),'w') as w:
            for data in self.stage['1']['1']:
                w.writelines(data)
                w.write('\n')
    
    def set_mouse_status(self):
        mouse_input=pygame.mouse.get_pressed()
        if mouse_input[0]:
            self.mouse_status='down'
        elif self.mouse_status=='down' and mouse_input:
            self.mouse_status='up'
        else:
            self.mouse_status='idle'
    
    def map_edit(self):
        self.edit_mode=self.player.sprite.game_status
        self.bg_rect.x+=self.scroll_x_speed_edit
        self.bg_rect.y+=self.scroll_y_speed_edit
        self.minus_scroll_x+=self.scroll_x_speed_edit
        self.minus_scroll_y+=self.scroll_y_speed_edit
        mouse_pos=pygame.mouse.get_pos()
        key_input=pygame.key.get_pressed()
        # mouse_input=pygame.mouse.get_pressed()
        player_type='small_mario'
        
        column,row=(mouse_pos[0]+self.bg_rect.x*-1)//(16*SCALE),(mouse_pos[1]+self.bg_rect.y*-1)//(16*SCALE)
        x,y=((mouse_pos[0]+self.bg_rect.x*-1)//(16*SCALE))*(16*SCALE),((mouse_pos[1]+self.bg_rect.y*-1)//(16*SCALE))*(16*SCALE)
        print(x-self.minus_scroll_x,y,row,column,self.minus_scroll_y)
        self.map_tiles.sprite.rect.topleft=(x+self.minus_scroll_x,y+self.minus_scroll_y)
        
        if key_input[pygame.K_LEFT] and self.bg_rect.left<0:
            self.scroll_x_speed_edit=4
        elif key_input[pygame.K_RIGHT] and self.bg_rect.right>SCREEN_WIDTH:
            self.scroll_x_speed_edit=-4
        elif key_input[pygame.K_UP] and self.bg_rect.top<0:
            self.scroll_y_speed_edit=4
        elif key_input[pygame.K_DOWN] and self.bg_rect.bottom>SCREEN_HEIGHT:
            self.scroll_y_speed_edit=-4
        else:
            self.scroll_x_speed_edit=0
            self.scroll_y_speed_edit=0
        
        if key_input[pygame.K_0]:
            if self.map_type=='tile':
                self.map_element='0'
                self.map_tiles.add(Tile(self.stage_tile,'ground',self.map_element,(mouse_pos)))
        elif key_input[pygame.K_1]:
            if self.map_type=='tile':
                self.map_element='1'
                self.map_tiles.add(Tile(self.stage_tile,'ground',self.map_element,(mouse_pos)))
        elif key_input[pygame.K_2]:
            if self.map_type=='tile':
                self.map_element='2'
                self.map_tiles.add(Tile(self.stage_tile,'ground',self.map_element,(mouse_pos)))
        elif key_input[pygame.K_3]:
            if self.map_type=='tile':
                self.map_element='3'
                self.map_tiles.add(Tile(self.stage_tile,'ground',self.map_element,(mouse_pos)))
        elif key_input[pygame.K_4]:
            if self.map_type=='tile':
                self.map_element='4'
                self.map_tiles.add(Tile(self.stage_tile,'ground',self.map_element,(mouse_pos)))
        elif key_input[pygame.K_5]:
            if self.map_type=='tile':
                self.map_element='5'
                self.map_tiles.add(Tile(self.stage_tile,'ground',self.map_element,(mouse_pos)))
        elif key_input[pygame.K_p]:
            self.map_type='mario'
            if self.map_type=='mario':
                self.map_element='small_mario'
                self.map_tiles.add(Player(self.small_mario_images,self.super_mario_images,(mouse_pos),self.map_element,self.edit_mode))
        
        if self.mouse_status=='up':
            self.set_mouse_input(row,column)
    
    def set_mouse_input(self,row,column):
        if self.stage[str(self.level)][str(self.stage_level)][row][column]=='_':
            self.stage[str(self.level)][str(self.stage_level)][row][column]=self.map_element
        else:
            self.stage[str(self.level)][str(self.stage_level)][row][column]='_'
        self.tiles.empty()
        self.map_load()
    
    def set_scroll_x(self):
        player=self.player.sprite
        if player.rect.right>SCREEN_WIDTH/2+player.rect.w and player.dx>0:
            self.scroll_x=True
            player.move_speed=0
            player.scroll_x_speed=-4
        elif not self.scroll_x and player.rect.left<SCREEN_WIDTH/2-player.rect.w and player.dx<0:
            self.scroll_x=True
            player.move_speed=0
            player.scroll_x_speed=4
        else:
            player.move_speed=4
            player.scroll_x_speed=0
    
    def set_scroll_y(self):
        player=self.player.sprite
    
    def collide_horizon(self):
        player=self.player.sprite
        player.rect.x+=player.dx*player.move_speed
        
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.dx<0:
                    player.dx=0
                    player.rect.left=tile.rect.right
                elif player.dx>0:
                    player.dx=0
                    player.rect.right=tile.rect.left
    
    def collide_vertical(self):
        player=self.player.sprite
        player.set_gravity()
        
        for tile in self.tiles.sprites():
            if tile.rect.collidepoint(pygame.mouse.get_pos()):
                print(tile.index)
            # player
            if pygame.sprite.collide_rect(player,tile):
                if player.rect.bottom>=tile.rect.top:
                    player.dy=0
                    player.rect.bottom=tile.rect.top
                    player.on_ground=True
            if tile.index==1:
                if tile.rect.left>-5:
                    self.scroll_x=True
                else:
                    self.scroll_x=False
    
    def run(self):
        print(self.minus_scroll_x)
        if self.player.sprite.game_status=='playing':
            self.screen.fill('#aff9f0')
            self.set_scroll_x()
            self.set_scroll_y()
            self.collide_horizon()
            self.collide_vertical()
            self.tiles.update(self.player.sprite.scroll_x_speed,self.player.sprite.scroll_y_speed)
            self.tiles.draw(self.screen)
            self.enemies.update(self.player.sprite.scroll_x_speed,self.tiles,self.player.sprite)
            self.enemies.draw(self.screen)
            self.player.update()
            self.player.draw(self.screen)
            self.screen.blit(self.ui_images['hud'],self.hud_rect)
        elif self.player.sprite.game_status=='edit':
            self.screen.fill('black')
            self.screen.blit(self.bg,self.bg_rect)
            self.set_mouse_status()
            self.map_edit()
            self.tiles.update(self.scroll_x_speed_edit,self.scroll_y_speed_edit)
            self.tiles.draw(self.screen)
            self.player.update()
            self.player.draw(self.screen)
            self.map_tiles.draw(self.screen)
            self.screen.blit(self.ui_images['hud'],self.hud_rect)
            for y in range(27):
                for x in range(176):
                    pygame.draw.rect(self.screen,'blue',(self.bg_rect.x+(x*(16*SCALE)),self.bg_rect.y+(y*(16*SCALE)),16*SCALE,16*SCALE), width=1)