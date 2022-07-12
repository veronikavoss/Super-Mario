from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,small,super,pos,type,game_status):
        pygame.sprite.Sprite.__init__(self)
        # self.type='small_mario'
        self.type=type
        self.game_status=game_status
        self.status='idle'
        self.frame=0
        self.set_images(small,super)
        self.original_image=self.mario_image[self.type][self.status]
        self.flip=True
        self.image=pygame.transform.flip(self.original_image,self.flip,False)
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=self.dx,self.dy=pygame.Vector2(0,0)
        self.move_speed=4
        self.scroll_x_speed=0
        self.scroll_y_speed=0
        self.gravity=0.8
        self.on_ground=True
        self.down=False
        self.collide_tile=False
        self.jumpkey_pressed=False
    
    def set_images(self,small,super):
        self.mario_image={
            'small_mario':{
                'idle':small['small_mario'][0],
                'move':small['small_mario'][-17:-19:-1],
                'down':small['small_mario'][0],
                'jump':small['small_mario'][2],
                'falling':small['small_mario'][2]
                },
            'super_mario':{
                'idle':super['super_mario'][0],
                'move':super['super_mario'][1:3],
                'down':super['super_mario'][3],
                'jump':super['super_mario'][4],
                'falling':super['super_mario'][4]
                }
            }
        for i in range(1,-1,-1):
            self.mario_image['super_mario']['move'].append(super['super_mario'][i])
    
    def set_gravity(self):
        self.dy+=self.gravity
        self.rect.y+=self.dy
    
    def set_key_input(self):
        key_input=pygame.key.get_pressed()
        # print(self.game_status)
        # if key_input[pygame.K_e] and not self.game_status=='edit':
        #     self.game_status='edit'
        #     pygame.time.delay(100)
        # elif key_input[pygame.K_e] and self.game_status=='edit':
        #     self.game_status='playing'
        #     pygame.time.delay(100)
        if key_input[pygame.K_RIGHT] and not key_input[pygame.K_DOWN]:
            self.flip=True
            self.dx=1
        elif self.rect.left>0 and key_input[pygame.K_LEFT] and not key_input[pygame.K_DOWN]:
            self.flip=False
            self.dx=-1
        else:
            self.dx=0
            self.scroll_x_speed=0
        
        if key_input[pygame.K_DOWN]:
            self.down=True
        elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
            self.down=True
        elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
            self.down=True
        else:
            self.down=False
        
        if not self.jumpkey_pressed and self.status=='idle':
            if key_input[pygame.K_UP]:
                self.jumpkey_pressed=True
                self.dy=-20
    
    def set_status(self):
        if self.dy<0:
            self.status='jump'
            self.on_ground=False
        elif self.dy>1:
            self.status='falling'
            self.on_ground=False
        elif self.down:
            self.status='down'
            self.on_ground=True
        else:
            if self.on_ground:
                if self.dx!=0:
                    self.status='move'
                    self.on_ground=True
                else:
                        self.status='idle'
                        self.jumpkey_pressed=False
                        self.down=False
                        self.frame=0
    
    def animated(self):
        animation=self.mario_image[self.type][self.status]
        
        if self.status=='move':
            self.frame+=0.1
            if self.frame>=len(animation):
                self.frame=0
        
        if type(animation)!=list:
            self.image=animation
            self.image=pygame.transform.flip(self.image,self.flip,False)
        else:
            self.image=animation[int(self.frame)]
            self.image=pygame.transform.flip(self.image,self.flip,False)
    
    def update(self):
        self.set_key_input()
        if self.game_status=='playing':
            self.set_status()
            self.animated()