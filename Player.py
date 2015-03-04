import pygame
from Spritesheet import SpriteSheet
import Constants
import random 
#Player Colors

class Key(pygame.sprite.Sprite):
    cage_list = []
    def __init__(self, x,y):
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(238,206,115,99)
        self.cage_list.append(image)
        image.set_colorkey(Constants.WHITE)
    
        
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

            
            print ("hit")
        
        
              
    def calc_grav(self):    
        
        if self.change_y == 0:
            self.change_y += 1
        else:
            self.change_y += .35
            
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
        if self.rect.y >= 50:
            self.change_y = -13
        else:
            self.change_y = 1
        
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
    
        
