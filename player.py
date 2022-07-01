from setting import *
from asset import *

class Player(pygame.sprite.Sprite,Asset):
    def __init__(self,pos,type):
        pygame.sprite.Sprite.__init__(self)
        Asset.__init__(self)
        # self.type='small_mario'
        self.type=type
        self.status='idle'
        self.frame=0
        self.set_images()
        self.original_image=self.mario_image[self.type][self.status]
        self.flip=True
        self.image=pygame.transform.flip(self.original_image,self.flip,False)
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=self.dx,self.dy=pygame.Vector2(0,0)
        self.gravity=0.8
        self.down=False
        self.collide_tile=False
    
    def set_images(self):
        self.mario_image={
            'small_mario':{
                'idle':self.small_mario_images['small_mario'][0],
                'move':self.small_mario_images['small_mario'][-17:-19:-1],
                'down':self.small_mario_images['small_mario'][0],
                'jump':self.small_mario_images['small_mario'][2],
                'falling':self.small_mario_images['small_mario'][2]
                },
            'super_mario':{
                'idle':self.super_mario_images['super_mario'][0],
                'move':self.super_mario_images['super_mario'][1:3],
                'down':self.super_mario_images['super_mario'][3],
                'jump':self.super_mario_images['super_mario'][4],
                'falling':self.super_mario_images['super_mario'][4]
                }
            }
        for i in range(1,-1,-1):
            self.mario_image['super_mario']['move'].append(self.super_mario_images['super_mario'][i])
    
    def set_gravity(self):
        self.dy+=self.gravity
        self.rect.y+=self.dy
    
    def set_key_input(self):
        self.dx=0
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_RIGHT] and not key_input[pygame.K_DOWN]:
            self.flip=True
            self.dx=4
        elif key_input[pygame.K_LEFT] and not key_input[pygame.K_DOWN]:
            self.flip=False
            self.dx=-4
        if key_input[pygame.K_DOWN]:
            self.down=True
        elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
            self.down=True
        elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
            self.down=True
        else:
            self.down=False
        if key_input[pygame.K_UP]:
            self.status='jump'
            self.dy=-20
        self.rect.x+=self.dx
    
    def set_status(self):
        if self.dy<0:
            self.status='jump'
        elif self.dy>3:
            self.status='falling'
        elif self.down:
            self.status='down'
        else:
            if self.dx!=0:
                self.status='move'
            else:
                self.status='idle'
                self.down=False
                self.frame=0
    
    def animated(self):
        animation=self.mario_image[self.type][self.status]
        
        if self.status=='move':
            self.frame+=0.1
            if self.frame>=len(animation):
                self.frame=0
        
        if type(animation)!=list:
        # if self.status=='idle' or self.status=='down' or self.status=='jump':
            self.image=animation
            self.image=pygame.transform.flip(self.image,self.flip,False)
        else:
            self.image=animation[int(self.frame)]
            self.image=pygame.transform.flip(self.image,self.flip,False)
        
        print(self.status,int(self.frame))
    
    def update(self):
        self.set_key_input()
        self.set_status()
        self.animated()