import pygame
from Spritesheet import SpriteSheet
import Constants
import random 
#Player Colors

class Snake_limits(pygame.sprite.Sprite):
    limit_move = 0 
    snake_limit_list = []
    def __init__(self,x,y,speed,platform):
        super().__init__()
        
        self.x = x
        self.y = y
        self.platform = platform
        self.speed = speed
        
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(589, 70, 2, 12)
        self.snake_limit_list.append(image)
          
        self.image = self.snake_limit_list[0]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x = self.x - self.limit_move
        self.rect.y = self.y
                
    
class Snake(pygame.sprite.Sprite):
    snake_right = []
    snake_left = []
    change_x = 4
    change_y = 0
    direction = "R"
    snake_move_x = 2
    snake_screen_adjust = 0
      
    def __init__(self,x,y,limit, limit1, limit2):
        self.x = x
        self.limit2 = limit2
        self.y = y
        self.limit = limit
        self.limit1 = limit1
        super().__init__()
        sprite_sheet = SpriteSheet("Snakes.png")
        image = sprite_sheet.get_image(4, 1, 115, 82)
        self.snake_right.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(124, 2,87, 89)
        self.snake_right.append(image)
        image.set_colorkey(Constants.WHITE)
        
        image = sprite_sheet.get_image(4, 1, 115, 82)
        image = pygame.transform.flip(image, True, False)
        self.snake_left.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(124, 2,87, 89)
        image = pygame.transform.flip(image, True, False)
        self.snake_left.append(image)
        image.set_colorkey(Constants.WHITE)
        
        self.image = self.snake_right[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self): 
        self.rect.x += self.change_x 
        self.limit1
        self.limit2
        print(self.limit1)
        pos = self.rect.x 
        
        if self.direction == "R":
            frame = (pos // 20) % len(self.snake_right)
            self.image = self.snake_right[frame]
        elif self.direction == "L":
            frame = (pos // 20) % len(self.snake_left)
            self.image = self.snake_left[frame]
            
        if self.rect.x > self.limit1: 
            self.change_x = self.change_x * -1
            self.direction = "L"
        if self.rect.x < self.limit1: 
            self.change_x = self.change_x * -1
            self.direction = "R"
        
    
class Caged_Bunny(pygame.sprite.Sprite):
    caged_bunny_list = []
    Cage_move_x = 0 
    image_num = 0
    def __init__(self,x,y,platform):
        self.x = x
        self.y = y
        self.platform = platform
        image_num = 0
        super().__init__()
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(359, 311, 171, 149)
        self.caged_bunny_list.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(531, 395, 220, 343)
        self.caged_bunny_list.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(759, 89, 215, 641)
        self.caged_bunny_list.append(image)
        image.set_colorkey(Constants.WHITE)
        
        
        self.image = self.caged_bunny_list[self.image_num]
        self.rect = self.image.get_rect()
       
    def update(self):
        self.image = self.caged_bunny_list[self.image_num]
        if self.image_num == 0:
            self.rect.y = self.y
        elif self.image_num == 1:
            self.rect.y = self.y - 190
        elif self.image_num == 2: 
            self.rect.y = self.y - 494
        self.rect.x = self.x - self.Cage_move_x
    def free(self):
        self.image_num = 2
    def get_the_key(self):
        self.image_num = 1
class Key(pygame.sprite.Sprite):
    key_list = []
    key_move_x = 0 
    move = False
    def __init__(self, x,y,change):
        self.x = x
        self.change = change
        self.player = list
        self.y = y
        super().__init__()
        sprite_sheet = SpriteSheet("Sprites.png")
        image = sprite_sheet.get_image(544,4,82,86)
        self.key_list.append(image)
        image.set_colorkey(Constants.WHITE)
        
        self.image = self.key_list[0]
        self.rect = self.image.get_rect()        
        self.rect.x =self.x
        self.rect.y =self.y 
    def update(self):
        if self.move == False:
            self.rect.x = self.x - self.key_move_x
        elif self.move == True:
            self.rect.x = 10
        
    def move_key(self):
        self.rect.x = 10
        self.rect.y = 20
        self.move = True
    
    
        
class Player(pygame.sprite.Sprite):
 
    change_x = 0
    change_y = 0

    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    brown_bunny = ([35,2,95,88],[20,101,110,122],[5,226,137,116])
    black_bunny = ([179,0,102,88],[178,88,116,106],[175,198,137,131])
    green_bunny = ([389,14,99,88],[389,114,115,123],[367,232,139,127])
    blue_bunny = ([595,0,93,88],[612,92,115,123],[535,214,141,122])
    direction = "R"

    
    level = None

    
    def __init__(self,x,y,list_platform,grav,bunny_color,hight): 
        self.height = hight
        self.grav = grav
        self.x = x
        self.y = y
        self.list = list_platform

        super().__init__()
        sprite_sheet = SpriteSheet("Rabbit_Sprite.png")
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        image = sprite_sheet.get_image(99, 57, 56, 79)
        self.walking_frames_u.append(image)
        
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()        
        image.set_colorkey(Constants.YELLOW)
        self.rect.y = self.y
        self.rect.x = self.x

    def update(self):
        
        
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        pos = self.rect.x 
         
        if self.direction == "R" and self.change_y != 1:
            frame = (pos // 20) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "U":
            frame = self.walking_frames_u[0]

        elif self.direction == "L" and self.change_y != 1:
            frame = (pos // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        if self.grav == True:
            self.calc_grav()
        
        if self.rect.y == 0:
            self.rect.y = 0
            self.change_y = 1
               
        block_hit_list = pygame.sprite.spritecollide(self, self.list, False)
        for block in block_hit_list:
            
            if self.change_y >= 1:
                self.rect.bottom = block.rect.top
            elif self.change_y < 1:
                self.rect.top = block.rect.bottom
            
 
            # Stop our vertical movement
            self.change_y = 0

            
            
        
        
              
    def calc_grav(self):    
        
        if self.change_y == 0:
            self.change_y += 1
        else:
            self.change_y += .45
            
        if self.rect.y <= self.height - 96 and self.change_y == 0:
            self.rect.y = self.height - 95   

    def go_right(self):
        self.change_x = 3
        self.direction = "R"
    def stop(self):
        self.change_x = 0
        if self.direction == "R":
            self.image = self.walking_frames_r[0]
        elif self.direction == "L":
            self.image = self.walking_frames_l[0]
 
     
    def go_left(self):
        self.change_x -= 3
        self.direction = "L"
    def jump(self):
        if self.change_y <= 0:
            if self.rect.y >= 70:
                self.change_y = -13
            else:
                self.change_y = 1
        else:
            None
        
class Animated_Player(pygame.sprite.Sprite):
    
    
    change_x = 0
    change_y = 0
    
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    brown_bunny = ([35,2,95,88],[20,101,110,122],[5,226,137,116])
    black_bunny = ([179,0,102,88],[183,89,111,115],[175,198,137,131])
    green_bunny = ([389,14,99,88],[389,114,115,123],[367,232,139,127])
    blue_bunny = ([595,0,93,88],[612,92,115,123],[535,214,141,122])
    bunny_list = (brown_bunny, black_bunny, green_bunny, blue_bunny)
    direction = "R"

    
    level = None

    
    def __init__(self,bunny_color,width): 
        self.x = random.randrange(-500, -50)
        self.y = random.randrange(100, 700)
        self.width = width 

        super().__init__()
        sprite_sheet = SpriteSheet("Rabbit_Sprite.png")
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        image = sprite_sheet.get_image(99, 57, 56, 79)
        self.walking_frames_u.append(image)
        
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()        
        image.set_colorkey(Constants.YELLOW)
        self.rect.y = self.y
        self.rect.x = self.x

    def update(self):
        
        
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        pos = self.rect.x 
        
        if self.direction == "R":
            frame = (pos // 20) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "U":
            frame = self.walking_frames_u[0]

        else:
            frame = (pos // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        if self.rect.x >= self.width:
            self.rect.x = random.randrange(-100,-50)
        
        self.change_x = 3
        self.direction = "R"
    
    
     
    def go_left(self):
        self.change_x -= 3
        self.direction = "L"
    
        
