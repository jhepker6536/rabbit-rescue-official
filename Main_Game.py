import pygame 
import random 
from Player import Player, Caged_Bunny,Key, Not_Moving_Bunny
from Player import Animated_Player
from Platforms import Platform
from Level_1 import level_one
from Level_2 import level_two
import Constants
import Level_2
 

# Define some colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (16, 81, 148)
PURPLE = (163, 73, 164)
YELLOW = (255, 242, 0)
GREEN = (34, 177, 76)
# Screen Size and creation
width = 1366
hight = 768
screen = pygame.display.set_mode((width, hight), pygame.FULLSCREEN, 32)

# Button Rectangle class
 

def main():
    """ Main function for the game. """
    pygame.init()
    rabbit_color = None   
    # Random Variables
    
    
   
       
    # Ad sprites to list 
    empty_platform_list = []
    
    sitting_bunny_list = pygame.sprite.Group()
    Brown_Bunny = Not_Moving_Bunny(0,100,200)
    Black_Bunny = Not_Moving_Bunny(1,300,200)
    Green_Bunny = Not_Moving_Bunny(2,500,200)
    Blue_Bunny = Not_Moving_Bunny(3,100,400)
    Purple_Bunny = Not_Moving_Bunny(4,300,400)

    
    running_bunny = Animated_Player(Animated_Player.bunny_list[random.randrange(0, 4)], width,False)
    running_bunny2 = Animated_Player(Animated_Player.bunny_list[random.randrange(0, 4)], width,False)
    running_bunny3 = Animated_Player(Animated_Player.bunny_list[random.randrange(0, 4)], width,True)
    running_bunny4 = Animated_Player(Animated_Player.bunny_list[random.randrange(0, 4)], width,True)
    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(running_bunny,running_bunny2,running_bunny3,running_bunny4,Brown_Bunny,Black_Bunny,Blue_Bunny,Green_Bunny,Purple_Bunny) 
    
    # All blitted Text
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    font = pygame.font.SysFont('comicsansms', 90, True, False)
    text1 = pygame.image.load('PlayGameButton.png')
    text2 = pygame.image.load('Settingsbutton.png')
    text3 = pygame.image.load('Loadscreen.png')
    text1.set_colorkey(WHITE)
    text2.set_colorkey(WHITE)
    text3.set_colorkey(WHITE)
    
    text4 = font.render("INSERT GAME HERE", True, RED)
    text5 = font.render("LOAD SCREEN", True, RED)
    text6 = font.render("<-BACK", True, RED)
    text7 = font2.render("DIFFICULTY", True, RED)
    text11 = font2.render("Exit", True, RED)
        
   
    # cursor picture
    
    pygame.mouse.set_visible(True)
    
    # load logo screen
    logo = pygame.image.load('LOADER.png')
    title = pygame.image.load('title_logo.png')
    title.set_colorkey(WHITE)
    # Creat instance of button rectangles 
    
 
    # Loop until the user clicks the close button.
    done = False
    really_done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    Constants.level = 1
    # What screen we see and background
    background_image = pygame.image.load("Field.png")
    screen_view = 0 
    font = pygame.font.Font(None, 25)
    frame_count = 0
    frame_rate = 60
    start_time = 90 
    # Parent while loop
    while not really_done:
        
        print(Constants.level)
        # child loop containing loading screen!
        while screen_view == 0 and done == False:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True 
                    really_done = True  
                    
            # Background logo
            screen.fill(BLACK)
            screen.blit(logo, [0, 0])
            
            # count
            total_seconds = frame_count // frame_rate
            seconds = total_seconds % 60
            frame_count += 1 
            if seconds == 1:
                screen_view = 1
            # mouse
            
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            
            
            pygame.display.flip()
            # Limit to 60 frames per second
            clock.tick(frame_rate)            
            
        # child while loop, containing menu!
        while screen_view == 1 and done == False:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True 
                    really_done = True
                # Do they hit the bottons and change mouse anamation
                elif event.type == pygame.MOUSEBUTTONDOWN:                   
                    if mouse_x >= 399 and mouse_x <= 917 and mouse_y >= 325 and mouse_y <= 416:
                        print("game") 
                        while (Constants.level == 1):
                            level_one()
                        while (Constants.level == 2):
                            Platform.platform_move_x = 0 
                            Caged_Bunny.Cage_move_x = 0 
                            Key.key_move_x = 0 
                            level_two()  
                        while (Constants.level == 3):
                            pygame.quit()
                    elif mouse_x >= 398 and mouse_x <= 649 and mouse_y >= 574 and mouse_y <= 666:
                        print("got it load")
                        color2 = WHITE 
                        screen_view = 3
                        (399, 575, 250, 91)
                    elif mouse_x >= 398 and mouse_x <= 889 and mouse_y >= 450 and mouse_y <= 541:
                        print("and again setting")
                        color3 = GREEN
                        screen_view = 4
                    elif mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                        done = True
                        really_done = True                     
                # Do they let off the mouse button change mouse
                   
                    
            # Background
            screen.blit(background_image, [0, 0])
            
            
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            print(seconds)
            frame_count += 1
            # Creat Buttons
            screen.blit(title, [250, 100])            
            screen.blit(text1, [400, 300])
            screen.blit(text2, [400, 425])
            
            # quit
            screen.blit(text11, [1200, 650])
            
            
            # Creat Bunny
            active_sprite_list.draw(screen)
            active_sprite_list.update()
    
            # Chanage mouse pic
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            
            pygame.display.flip()
    
            # Limit to 20 frames per second
            clock.tick(frame_rate)

        # child while loop, containing load screen!
        while screen_view == 3 and done == False:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True 
                    really_done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x >= 99 and mouse_x <= 249 and mouse_y >= 349 and mouse_y <= 398:
                        screen_view = 1
                    elif mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                        done = True
                        really_done = True                 

                # Creat Background
                screen.fill(BLACK)
                total_seconds = frame_count // frame_rate
                minutes = total_seconds // 60
                seconds = total_seconds % 60
                print (seconds) 
                frame_count += 1
                # Creat Buttons
                screen.blit(text5, [200, 300])
                
                screen.blit(text6, [100, 350])    
                
                # quit
                screen.blit(text11, [1200, 650])
                 
                
                # Change Mouse
                
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1] 
                
                pygame.display.update()
                pygame.display.flip()
            
                # Limit to 20 frames per second
                clock.tick(frame_rate) 
                
                
        COLOR4 = RED
        COLOR5 = RED
        COLOR6 = RED                
        # child while loop, containing setttings screen!
        while screen_view == 4 and done == False:
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT:
                        done = True
                        really_done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                          
                        if mouse_x >= 99 and mouse_x <= 249 and mouse_y >= 349 and mouse_y <= 398:
                            screen_view = 1
                        elif mouse_x >= 199 and mouse_x <= 264 and mouse_y >= 159 and mouse_y <= 188:
                            COLOR4 = WHITE
                            COLOR5 = RED
                            COLOR6 = RED
                        elif mouse_x >= 274 and mouse_x <= 392 and mouse_y >= 159 and mouse_y <= 188:
                            COLOR5 = WHITE
                            COLOR4 = RED
                            COLOR6 = RED
                        elif mouse_x >= 399 and mouse_x <= 474 and mouse_y >= 159 and mouse_y <= 188:
                            COLOR6 = WHITE
                            COLOR4 = RED
                            COLOR5 = RED
                        elif mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                            done = True
                            really_done = True 
                            
                       
                                      
                    # Background
                    screen.fill(BLACK)
                    total_seconds = frame_count // frame_rate
                    minutes = total_seconds // 60
                    seconds = total_seconds % 60
                    
                    print (seconds)
                    frame_count += 1                   
                    # Creat Buttons
                    sitting_bunny_list.draw()
                    
                                        
                    text8 = font2.render("EASY", True, COLOR4)
                    text9 = font2.render("MEDIUM", True, COLOR5)
                    text10 = font2.render("HARD", True, COLOR6)                    
                    screen.blit(text6, [100, 350])
                    screen.blit(text7, [200, 100])
                    screen.blit(text8, [200, 160])
                    screen.blit(text9, [275, 160])
                    screen.blit(text10, [400, 160])
                    screen.blit(text11, [1200, 650])
                    
                    # Change mouse
                    
                    pos = pygame.mouse.get_pos()
                    mouse_x = pos[0]
                    mouse_y = pos[1] 
                    
                    pygame.display.update()
                    pygame.display.flip()
                
                    # Limit to 20 frames per second
                    clock.tick(frame_rate)  
    

    
    clock.tick(frame_rate)
    pygame.quit()    
            
                
if __name__ == "__main__":
    main()
