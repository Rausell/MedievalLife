"""
Below is our medieval life game simulation.
This simulation focuses on a farming simulation and city building simulation.
The goal in this program is to efficiently manage data in terms of inventory.
As well as incorporate a smooth user interaction to the game. 
More insight into the program, its structure, legality, and related content
located in the README.md file.

Initial development on 10/3/2024 3:19 pm By RausellStudios.
"""

#Initializing pygame related modules
import sys, pygame
pygame.init()

#Importing modules to run game program
from item import Item
from inventory import Inventory

#Setting screen size (currently on adjusted to MacBook Air 2020 version)
size = width, height = 900, 710
speed = [2, 2]

#Defining RGB values
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

#Creating graphical window
screen = pygame.display.set_mode(size)

#Creating font for text input into the graphical screen via pygame module
font = pygame.font.Font('freesansbold.ttf', 32)

#Adjustment: tts ==> text to screen var shows what will be displayed to screen
tts = "SomeTemporaryTextHere"
#Creating text surface object from which the text will be drawn
#First parameter is the text that will be displayed
#Second parameter is boolean factor to allow anti-aliasing
#Anti-aliasing - technique to make pictures look more realistic/less pixelated
#Third parameter contains RGB values for text color
#Fourth paramter contains RGB values for background color
img = font.render(tts, True, green, blue)

#Creating rectangular object for text surface object
textRect = img.get_rect()

#Setting rectangular object to position itself in the middle of display surface
textRect.center = (width // 2, height // 2)

#screen.blit(img, (20, 20)) TEMP DEL

#Creating initial items
#Can be made into a callable function
stick = Item("Stick", 2)
wheat = Item("Wheat", 1)

#Creating initial inventory with capacity of 10
player_inventory = Inventory(capacity = 10)

#Adding items to inventory
#Can be made into a callable function
player_inventory.add_item(stick)

#Displaying inventory
#Can be made into a callable function based on user given command
player_inventory.display_items()

#Removing an item
#Can be made into a callable action
player_inventory.remove_item("Stick")

#Showing the updated inventory
player_inventory.display_items()

#Shows the graphical display until user exits from page
while True:
    #Display surface is covered in white
    screen.fill(white)
    #Copy text surface obj to display surface obj at middle coordinates
    screen.blit(img, textRect)
    #Iterate over list of event objs returned by pygame.event.get() method
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        #Updating new changes
        pygame.display.update()
