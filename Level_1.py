import pygame 
import random 
import Player
from Player import Player
import Constants
from Platforms import Platform
from Spritesheet import SpriteSheet 
width = 1366
hight = 768
screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)

def level_one():
    pygame.init()
    mouse_x = 0 
    mouse_y = 0 
    floor_x = 0  
    platform_list = pygame.sprite.Group()
    platform_test = Platform(floor_x,674,0)
    platform1 = Platform(400,450,1)
    platform2 = Platform(1000,350,1)
    platform3 = Platform(1500,450,1)
    platform5 = Platform(2000,350,1)
    platform6 = Platform(2400,250,1)
    platform_list.add(platform_test, platform2, platform1,platform3,platform5,platform6) 
    player = Player(25,400,platform_list,True,Player.black_bunny, hight)
    
    
    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player,platform_test,platform2,platform1,platform3,platform5,platform6)
    background_x_change = 0 
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    
    clock = pygame.time.Clock()
    done = False
    
    background_image = pygame.image.load("field_background.png")
    background_x = 0
    
    while not done:
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    background_x_change += 2
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                    background_x_change -= 2 
                elif event.key == pygame.K_SPACE:
                    player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                    background_x_change = 0 
                elif event.key == pygame.K_RIGHT:
                    player.stop()
                    background_x_change = 0 
                elif event.type == pygame.QUIT:
                    done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                    done = True

            
                                    
            
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [background_x, 0])
        
        active_sprite_list.update()
        active_sprite_list.draw(screen)
        if player.rect.x <=0:
            player.rect.x = 0
        #quit
        screen.blit(text11, [1200,650])    
        pos = pygame.mouse.get_pos()
        if background_x > 0:
            background_x = -7
        if floor_x > 0:
            floor_x = -7
        mouse_x = pos[0]
        mouse_y = pos[1]
                
        Platform.platform_move_x += player.change_x 
        background_x += background_x_change
        platform_test.update()
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    level_one() 
