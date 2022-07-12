from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image,type,enemy,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.type=type
        self.enemy=enemy
        self.status='move'
        self.on_ground=False
        self.set_images(image)
        self.frame=0
        self.image=self.enemy_images[type][enemy][self.status][self.frame]
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=self.dx,self.dy=pygame.Vector2(0,0)
        self.move_speed=1
        self.gravity=0.8
    
    def set_images(self,image):
        self.enemy_images={
            'goombas':{
                'goomba':{
                    'move':image['goombas']['goomba'][0:2],
                    'jump':image['goombas']['goomba'][0:2],
                    'falling':image['goombas']['goomba'][0:2],
                    'die':image['goombas']['goomba'][2]
                    }}}
    
    def set_status(self):
        if self.dy<0:
            self.status='jump'
            self.on_ground=False
        elif self.dy>1:
            self.status='falling'
            self.on_ground=False
        else:
            if self.on_ground:
                if self.dx!=0:
                    self.status='move'
                    self.on_ground=True
    
    def set_move(self,scroll_speed):
        if self.status=='move':
            self.dx=-1
        elif self.status=='die':
            self.dx=0
        self.rect.x+=self.dx*self.move_speed+scroll_speed
        # print(self.status,self.dx*self.move_speed)
    
    def set_gravity(self):
        self.dy+=self.gravity
        self.rect.y+=self.dy
    
    def collision(self,tiles,mario):
        if pygame.sprite.collide_mask(self,mario):
            if mario.rect.bottom>=self.rect.top:
                self.status=='die'
        for tile in tiles:
            if pygame.sprite.collide_rect(self,tile):
                if self.dx*self.move_speed<0:
                    self.move_speed*=-1
                    self.rect.left=tile.rect.right
                elif self.dx*self.move_speed>0:
                    self.move_speed*=-1
                    self.rect.right=tile.rect.left
            # if tile.rect.collidepoint(self.rect.bottomright):
            #     # self.move_speed*=-1
            #     print('r')
            # if tile.rect.collidepoint(self.rect.bottomleft):
            #     # self.move_speed*=-1
            #     print('l')
        
        self.set_gravity()
        
        for tile in tiles:
            if pygame.sprite.collide_rect(self,tile):
                if self.dy>0:
                    self.dy=0
                    self.rect.bottom=tile.rect.top
                    self.on_ground=True
    
    def animated(self):
        animation=self.enemy_images[self.type][self.enemy][self.status]
        self.frame+=0.04
        if self.frame>=len(animation):
            self.frame=0
        self.image=animation[int(self.frame)]
    
    def update(self,scroll_speed,tiles,mario):
        self.set_status()
        self.set_move(scroll_speed)
        self.collision(tiles,mario)
        self.animated()