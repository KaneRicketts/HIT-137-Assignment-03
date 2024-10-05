import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()       # This initialises all the imported pygame modules.

# Initialising colour variables for common colours.

RED   = (255, 0, 0)
PINK = (255,20,147)
GREEN = (0, 255, 0)
DARKGREEN = (0,100,0)
BLUE  = (0, 0, 255)
SKYBLUE = (0,191,255)
CYAN = (0,255,255)
BLACK = (0, 0, 0)
GRAY = (128,128,128)
LIGHTGRAY = (211,211,211)
WHITE = (255, 255, 255)
MAGENTA = (255,0,255)
PURPLE = (128,0,128)
GOLD = (255,215,0)
ORANGE = (255,165,0)
BROWN = (139,69,19)

# Setting up the display.
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

SCREEN_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setting a caption name.
pygame.display.set_caption("HUBERT Game")

# Initialising fonts for text.
font = pygame.font.SysFont("8514oem", 20)
font_large = pygame.font.SysFont("8514oem", 50)

# Initialising button images
start_button = pygame.image.load("START.png").convert_alpha()
exit_button = pygame.image.load("EXIT.png").convert_alpha()
restart_button = pygame.image.load("RESTART.png").convert_alpha()

# Initialise other variables.
  #Setting up a clock (FPS) 
clock = pygame.time.Clock()     # The funtion to use our variable to set FPS.
FPS = 60        # The FPS we want the game to run.

collisions = 0
score = 0
player_speed = 5
enemy_speed = 5
# etc,
# etc,
# etc,

button_width = 760      # Approx
button_height = 260     # Approx
centre_of_screen = ((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# Define all the classes:
class Buttons():
    """Define the button class, including the function to detect mouse-over and click on buttons."""
    def __init__(self, x, y, image, scale) -> None:
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((int(width * scale)), (int(height * scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mouse_click = False

    def draw(self):
        """Draw onto surface with (x,y) coordinates."""
        SCREEN_SURFACE.blit(self.image, (self.rect.x, self.rect.y))
        
        # Check for collision and click from mouse.
        clicked = False
        pos_mouse = pygame.mouse.get_pos()

            # Cheeck if the mouse is over the button rect.
        if self.rect.collidepoint(pos_mouse):

            # Becasue the one click might return multiple "strikes", (governed by FPS??)
            #  we only want the first click to count. 
            # We can set a flag for the first click, and ensure the if statement
            #  is only true for that "un-raised flag" status

                # Check if the mouse is also clicked.
            if pygame.mouse.get_pressed()[0] == 1 and self.mouse_click == False:
                self.mouse_click = True         # Flag is set.
                clicked = True

            if pygame.mouse.get_pressed()[0] == 0:      # Once mouse click is lifted.
                self.mouse_click = False        # Flag is reset.
        return clicked

""" 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5
"""

class Backgrounds():
    def __init__(self):
        self.start_background_image = pygame.image.load("cave.jpg").convert_alpha()
        self.rect = self.start_background_image.get_rect()

        self.background_image = pygame.image.load("golden_cave_background.png").convert_alpha()
        self.rect = self.background_image.get_rect()

        self.stop_background_image = pygame.image.load("spiders.jpg").convert_alpha()
        self.rect = self.stop_background_image.get_rect()
    """
    def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.background_rect.height:
            self.bgY1 = self.background_rect.height
        if self.bgY2 <= -self.background_rect.height:
            self.bgY2 = self.background_rect.height
             

    def render(self):
        SCREEN_SURFACE.blit(self.background_image, (self.bgX1, self.bgY1))
        SCREEN_SURFACE.blit(self.background_image, (self.bgX2, self.bgY2))
    """

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("hubert.png")
        width = self.image.get_width()
        height = self.image.get_height()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(center = (int(width/2),int(height/2)))

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)      
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def shoot():
        pass

class weapon():
    pass
class enemies():
    pass  
class healthBar():
    pass

# Initialise instances of class objects.

player1: Player = Player()

start_background_image: Backgrounds = Backgrounds()
background_image: Backgrounds = Backgrounds()
exit_background_image: Backgrounds = Backgrounds()

start_button: Buttons = Buttons(130, 235, start_button, scale = 0.5)
exit_button: Buttons = Buttons(510,235, exit_button, scale = 0.5)
restart_button: Buttons = Buttons(130, 235, restart_button, scale = 0.5)

# Create groups for enemy(ies), player(s) etc.
""" 
(EXAMPLES)
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
missiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# all_sprites = pygame.sprite.Group()


# Define user events.
enemy_speed_increase = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_speed_increase, 1000)


(examples)
# Create custom events for adding a new enemy and cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)


# Set up music.

(EXAMPLES)
# Load and play our background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Load all our sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

# Set the base volume for all sounds
move_up_sound.set_volume(0.5)
move_down_sound.set_volume(0.5)
collision_sound.set_volume(0.5)
"""

# Create the start page loop.
start_loop = True
bye_img = font_large.render("GOODBYE", True, PURPLE)

while start_loop:
    SCREEN_SURFACE.fill(GOLD)
    # Check for close or escape event.
    for event in pygame.event.get():
        # First define an exit strategy for the loop.
        if event.type == QUIT:
            start_loop = False

        elif event.type == KEYDOWN:
            if KEYDOWN[K_ESCAPE]:
                start_loop = False

        # End the first loop, The Start Page, and move on to next loop.
    if start_button.draw():
        start_loop = False

        # Quit the application.
    if exit_button.draw():
        time.sleep(.5)
        SCREEN_SURFACE.fill(BLACK)
        SCREEN_SURFACE.blit(bye_img, (400,250))
        pygame.display.update()
        time.sleep(1.5)
        pygame.quit()
        sys.exit()
    pygame.display.update()

"""
# Create the game loop.
running = True

while running:

    # Check all events.
    for event in pygame.event.get():
        # First define an exit strategy for the loop.
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if KEYDOWN[K_ESCAPE]:
                running = False
        
        # Add user defined events here.
        #elif event.type ===========???????: 
        
    # Update and render background.
    #background.update()
    #background.render()

    # Add a Scorecard/healthbar/etc here (example)
    
    #SCREEN_SURFACE.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    SCREEN_SURFACE.blit(scores, (10,10))
    

    # Move and Draw all Sprites
    for entity in all_sprites:
        SCREEN_SURFACE.blit(entity.image, entity.rect)
        entity.move()
    
    # Player killed and end game screen (example)
    
    if pygame.sprite.spritecollideany(player1, enemies):
    
        pygame.mixer.Sound(SOUNDS).play()

        time.sleep(0.8)       # Delay until next
                    
        SCREEN_SURFACE.fill(RED)
        SCREEN_SURFACE.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(1.5)
        pygame.quit()
        sys.exit()        
        
    
    clock.tick(FPS)
    pygame.display.update()

"""

# Create the final game-over page loop.
game_over_screen = True
game_over_image = font_large.render("...GAME OVER...", True, BLUE)

while game_over_screen:
    
    SCREEN_SURFACE.fill(RED)
    SCREEN_SURFACE.blit(game_over_image, (375,150))
    # Player killed and end game screen (example)

    # Check all events.
    for event in pygame.event.get():
        # First define an exit strategy for the loop.
        if event.type == QUIT:
            game_over_screen = False

        elif event.type == KEYDOWN:
            if KEYDOWN[K_ESCAPE]:
                game_over_screen = False

    if restart_button.draw():
        print("Re-start")
        # reset??? continue game loop...

    if exit_button.draw():
        time.sleep(.5)
        SCREEN_SURFACE.fill(BLACK)
        SCREEN_SURFACE.blit(bye_img, (400,250))
        pygame.display.update()
        time.sleep(1.5)
        game_over_screen = False
    
    pygame.display.update()

# End game call here.
pygame.quit()
sys.exit()