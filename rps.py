# file created by Joshua Cortezano

# import libraries
# sleep used to delay code as needed, slow down, provide effect, help troubleshoot
from time import sleep
# going to use randint to get a random reult in carrot gun bunny
from random import randint
# pretty elaborate, thorough game library for use with python
import pygame as pg
# manage files and folders in directories
import os
# special variable, this stores where we r currently working in the game folder
game_folder = os.path.dirname(__file__)
#game settings
WIDTH = 1280
HEIGHT = 720
FPS = 30

# define colors
# tuple not changeable
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
#initialize all of pygame
pg.init()
# use sounds
pg.mixer.init()
# window
screen = pg.display.set_mode((WIDTH, HEIGHT))
# caption for the display
pg.display.set_caption
# fps
clock = pg.time.Clock()
# get image
carrot_image = pg.image.load(os.path.join(game_folder, 'carrot.png')).convert()
# gets rectangle of the image, stores where the pixels are. how many there are, and allows us to change those things
carrot_image_rect = carrot_image.get_rect()

gun_image = pg.image.load(os.path.join(game_folder, 'gun.png')).convert()
gun_image_rect = gun_image.get_rect()

bunny_image = pg.image.load(os.path.join(game_folder, 'bunny.png')).convert()
bunny_image_rect = bunny_image.get_rect()

BCG_image = pg.image.load(os.path.join(game_folder, 'BCG.png')).convert()
BCG_image_rect = BCG_image.get_rect()

Bcgwon_image = pg.image.load(os.path.join(game_folder, 'Bcgwon.png')).convert()
Bcgwon_image_rect = Bcgwon_image.get_rect()

Bcgcat_image = pg.image.load(os.path.join(game_folder, 'Bcgcat.jpg')).convert()
Bcgcat_image_rect = Bcgcat_image.get_rect()

Bcglost_image = pg.image.load(os.path.join(game_folder, 'Bcglost.png')).convert()
Bcglost_image_rect = Bcglost_image.get_rect()

Bcgmin_image = pg.image.load(os.path.join(game_folder, 'Bcgmin.gif')).convert()
Bcgmin_image_rect = Bcgmin_image.get_rect()

Bcgpa_image = pg.image.load(os.path.join(game_folder, 'Bcgpa.png')).convert()
Bcgpa_image_rect = Bcgpa_image.get_rect()

choices1 = ["carrot" , "gun", "bunny"]

same = ["tie" , "draw", "cat's game"]

winlose = "winlose"

play = "playing"

# defining a funciton
def cpu_randchoice():
    # computer decides
    # print("computer randomly decides ...")
    # enables the variable to be used outside the function
    global cpu
    # gets a random choice for the cpu to play
    cpu = choices1[randint(0,2)]
    return cpu


def compare(): 
    # if elif statements are conditional statements. python will run the code if the if statement or elif statement is true, if not it will skip the code
    global winlose
    if user == cpu:
        print(same[randint(0,2)])
        winlose = "tie"
    elif user == "carrot" and cpu == choices1[1] or user == "gun" and cpu == choices1[2] or user == "bunny" and cpu == choices1[0]:
        winlose = "win"
        print("u won!")
        sleep(1)
        print(user, "beats", cpu + "!")
    elif user == "gun" and cpu == choices1[0] or user == "carrot" and cpu == choices1[2] or user == "bunny" and cpu == choices1[1]:
        winlose = "lose"
        print("u lost!")
        sleep(1)
        print(cpu, "beats", user + "!")
    else:
        print("an error has occured in this instance")
        print("let us no find out what will happen with the respect to the error that has occured in this instance which might affect how this program will run so we will find out pretty soon what will happen or maybe this is part of what is happening to me")
        print("e")


running = True
while running:
    #try make computer run at set fps
    clock.tick(FPS)
    # pygame get every event, for loop goes thru a list
    for event in pg.event.get():
        # listening for when quit
        ########   input ##########
        # keyboard, mouse, joystick, controller, vr headset,
        if event.type == pg.QUIT:
            # breaks the while loop
            running = False
            # listening for when left is clicked and released
        if event.type == pg.MOUSEBUTTONUP:
            # displays coordinates where u clicked
            # print(pg.mouse.get_pos()[0])
            # print(pg.mouse.get_pos()[1])
            # sets a variable equal to the x coordinate of the position clicked on by the mouse
            # sets a variable equal to the y coordinate of the position clicked on by the mouse
            global m_x
            global m_y
            m_x = pg.mouse.get_pos()[0]
            m_y = pg.mouse.get_pos()[1]
            # stores cords
            global m_cords
            m_cords = pg.mouse.get_pos()
            # print(xsubone, ysubone)
            # and ensures that both statements have to be true
            # if 0 <= m_x <= 200 and 0 <= m_y <= 188:
            # uses rectangle height and width instead of us having to look for the rect height and width
            # if m_x <= my_image_rect.width and m_y <= my_image_rect.height:
                # print("the carrot")
            # else:
                # print("not the carrot")
            # when mouse cords are in the rectangle of the image,
            #print(carrot_image_rect.collidepoint(m_cords))
            #print(gun_image_rect.collidepoint(m_cords))
            #print(bunny_image_rect.collidepoint(m_cords))
            # allows user to choose smthn
    # return use
# randomize, cpu_choose, computer_decides
            if carrot_image_rect.collidepoint(m_cords):
                user = "carrot"
                print("you clicked on" , user)
            elif gun_image_rect.collidepoint(m_cords):
                user = "gun"
                print("you clicked on" , user)
            elif bunny_image_rect.collidepoint(m_cords):
                user = "bunny"
                print("you clicked on" , str(user))
            else:
                print("u did not click on an image")
                user = "error" 
                ''' runnin the functions '''
            cpu_randchoice()
            sleep(0.5)
            print("the computer chose", str(cpu))
            sleep(1)
            compare()
            


            
            
            
            
                



    
    ######## update #########
    # sets the image rect y values to a position 
    carrot_image_rect.y = 400
    bunny_image_rect.y  = 200
    gun_image_rect.y  = 600
    BCG_image_rect.x = 200
    BCG_image_rect.y = 10
    # the img rect x value will add by 1 during loop
    carrot_image_rect.x += 1
    bunny_image_rect.x  += 1
    gun_image_rect.x  += 1
    
    

    ######### draw ##########
    # fills the screen with the color black
    ''' if and elif statements with the variable winlose that was globalized from the compare function
    winlose determines if user won or lost and the if elif statments here determine what image to put on the screen '''
    if winlose == "winlose":
        screen.fill(BLACK)
    # draw image
        screen.blit(BCG_image, BCG_image_rect)
        screen.blit(carrot_image, carrot_image_rect)
        screen.blit(gun_image, gun_image_rect)
        screen.blit(bunny_image, bunny_image_rect)
    elif winlose == "win":
        screen.blit(Bcgwon_image, Bcgwon_image_rect)
        screen.blit(Bcgmin_image, Bcgmin_image_rect)
        sleep(1)
        
    elif winlose == "lose":
        screen.blit(Bcglost_image, Bcglost_image_rect)
        sleep(1)
    elif winlose == "tie":
        screen.blit(Bcgcat_image, Bcgcat_image_rect)
        sleep(1)
    
    pg.display.flip()

    

# in conjunction with the for loop, breaks the while loop
# pg.quit()



# rgb, plural index, pixels, screen window