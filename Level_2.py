import pygame 
import random 

from Player import Player
from Player import Key
from Player import Caged_Bunny
from Player import Snake
import Constants
from Platforms import Platform
from Spritesheet import SpriteSheet 
from os.path import sys
width = 1366
hight = 768


def level_two(color):
    pygame.init()
    screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)
    mouse_x = 0  
    key_collected = False
    mouse_y = 0 
    key_x = 1940
    key_y = 100
    floor_x = 0  
    caged_bunny_list = pygame.sprite.Group()
    platform_list = pygame.sprite.Group()
    active_sprite_list = pygame.sprite.Group()
    key_list = pygame.sprite.Group()
    
    if color == "Blue":
        player_color = Player.blue_bunny
    elif color == "Brown":
        player_color = Player.brown_bunny
    elif color == "Purple":
        player_color = Player.purple_bunny
    elif color == "Green":
        player_color = Player.green_bunny 
    elif color == "Yellow":
        player_color = Player.green_bunny   
    elif color == "White":
        player_color = Player.green_bunny
    elif color == "Pink":
        player_color = Player.green_bunny
    else:
        player_color = Player.black_bunny
        
        
    platform_test = Platform(floor_x,674,0)
    platform1 = Platform(400,450,1)
    platform2 = Platform(1200,450,1)
    platform3 = Platform(1800,230,1)
    platform6 = Platform(2400,400,1)
    
    player2 = Player(25,400,platform_list,True,player_color, hight)
    
    caged_bunny = Caged_Bunny(3050,525,platform_list) 
    key = Key(key_x,key_y,player2.change_x)
    
    key_list.add(key)
    caged_bunny_list.add(caged_bunny)
    platform_list.add(platform_test, platform2, platform1,platform3,platform6)
    active_sprite_list.add(caged_bunny,player2,platform_test,platform2,platform1,platform3,platform6,key)
    
    background_x_change = 0 
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    
    clock = pygame.time.Clock()
    done = False
    
    background_image = pygame.image.load("Forest Background2.png")
    background_x = -100
    
    while not done:
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player2.go_left()
                    background_x_change += 2
                elif event.key == pygame.K_RIGHT:
                    player2.go_right()
                    background_x_change -= 2 
                elif event.key == pygame.K_SPACE:
                    player2.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player2.change_x < 0:
                    player2.stop()
                    background_x_change = 0 
                elif event.key == pygame.K_RIGHT:
                    player2.stop()
                    background_x_change = 0 
                elif event.type == pygame.QUIT:
                    done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                    done = True
                    raise SystemExit

            
                                    
            
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [background_x, 0])
        
        
        if player2.rect.x <=0:
            player2.rect.x = 0
        #quit
        screen.blit(text11, [1200,650])    
        pos = pygame.mouse.get_pos()
        if background_x > 0:
            background_x = -7
        if floor_x > 0:
            floor_x = -7
        mouse_x = pos[0]
        mouse_y = pos[1]
        
        caged_bunny_list.draw(screen)
        block_hit_list = pygame.sprite.spritecollide(player2, key_list, False)
        for block in block_hit_list:
            key.move_key()
            key_collected = True
            
            
        block_hit_list = pygame.sprite.spritecollide(player2, caged_bunny_list, False)
        for block in block_hit_list:
            pass
            if key_collected == True:
                caged_bunny.free()
            if key_collected == False:
                caged_bunny.get_the_key()
            
           
        
        if key_collected == False and player2.change_x > 0:
            Key.key_move_x += player2.change_x + 2
        elif key_collected == False and player2.change_x < 0:
            Key.key_move_x += player2.change_x - 2    
            
        if player2.change_x > 0:
            Platform.platform_move_x += player2.change_x + 2
            Caged_Bunny.Cage_move_x += player2.change_x + 2
            
            
             
        elif player2.change_x < 0:
            Platform.platform_move_x += player2.change_x - 2
            Caged_Bunny.Cage_move_x += player2.change_x - 2
            
            
        Snake.snake_screen_adjust = player2.change_x 
        background_x += background_x_change 
        
        if player2.rect.x == width:
            Platform.platform_move_x += 3
        active_sprite_list.update()
        active_sprite_list.draw(screen)    
        if player2.rect.x >= 1300 and key_collected == True:
            Constants.level = 3 
            break   
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    level_two("Purple")
