"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
TEAL = (46,232,201)
YELLOW = (255,239,29)
# BACK_SCROLLER_COLOR = (190,158,255)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():

    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color
    
        
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height))
       
        """
        uses pygame and the global screen variable to draw the building on the screen
        """

    def move(self, speed):

        self.x_point += speed
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """



class Scroller():
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.buildings_list = []
        self.combined_width = 0
        self.create_buildings()


    def create_buildings(self):
        # width of scroller (self.width) == 
        # width of all buildings created(buildings_list)
        # until buildings fill width of scroller
        # combined_width = add all buildings in buildings_list
        while self.combined_width <= self.width: 
            self.create_building(self.combined_width)
            # self.combined_width += self.buildings_list[-1].width

        """
        Will call add_building until there the buildings fill up the width of the
        scroller.
        """

    def create_building(self, x_location):
        width = random.randint(70,100)
        self.combined_width += width 
        building1 = Building(x_location, 600, width, -random.randint(50,500), self.color)
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a building.
        Adds a building to list of buildings.
        """
       
        self.buildings_list.append(building1)

    def draw_buildings(self):
        for building in self.buildings_list:
            building.draw()
         
        """        This calls the draw method on each building.
        """

    def move_buildings(self):
        last_building = self.buildings_list[-1]
        first_building = self.buildings_list[0]
        for building in self.buildings_list:
            building.move(8)
        if last_building.x_point > SCREEN_WIDTH:
            self.buildings_list.remove(last_building)
        if first_building.x_point < SCREEN_WIDTH:
            width = random.randint(70,100)
            x_location = first_building.x_point - width
            building1 = Building(x_location, 600, width, -random.randint(50,500), self.color)
            self.buildings_list.insert(0,building1)
        
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """
class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.width = 30
        self.height = 60
        mouse_pos = 
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        center = self.mouse_pos

    # def jump()

sprite1 = Player(YELLOW)

FRONT_SCROLLER_COLOR =(255,0,83)

 # (231, 38,255)

MIDDLE_SCROLLER_COLOR =  (149,17,255)
BACK_SCROLLER_COLOR = (99,94,232)
# (36,255,163)
# (227,159,232)
# (97,171,232)
# (190,158,255)
BACKGROUND_COLOR = (107,205,255)
front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

buildings = Scroller(25,80,15, BLUE, 3)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    
    
  
    pygame.draw.circle(screen, YELLOW, (100,50),50,0 )
    # cloud 1
    pygame.draw.circle(screen, WHITE, (300,50), 32, 0 )
    pygame.draw.circle(screen, WHITE, (340,50), 32, 0 )
    pygame.draw.circle(screen, WHITE, (380,50), 32, 0 )
    # cloud 2
    pygame.draw.circle(screen, WHITE, (500,50), 32, 0 )
    pygame.draw.circle(screen, WHITE, (540,50), 32, 0 )
    pygame.draw.circle(screen, WHITE, (580,50), 32, 0 )
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    back_scroller.draw_buildings()
    back_scroller.move_buildings()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE

