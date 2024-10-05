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

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SCREEN_SURFACE = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_SURFACE.fill(WHITE)
pygame.display.set_caption("HUBERT Game")

# Initialising fonts for text.

font = pygame.font.SysFont("8514oem", 20)
font_large = pygame.font.SysFont("8514oem", 50)



# Initialise other variables.

    #Setting up a clock (FPS) 
clock = pygame.time.Clock()     # The funtion to use our variable to set FPS.

FPS = 60        # The FPS we want the game to run.

collisions = 0
score = 0
player_speed = 5
enemy_speed = 5
etc,
etc,
etc,



# Define classes:

class Background():
      def __init__(self):
            self.background_image = pygame.image.load('IMAGE')
            self.background_rect = self.background_rect.get_rect()
        """ 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5"""
         
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
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("IMAGE")
        self.surf = pygame.Surface((SIZE))
        self.rect = self.surf.get_rect(center = (CENTRE,COORDINATES))
        
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

# Initialise class objects.

player1: Player = Player()

background: Background = Background()



# Create groups for enemy(ies), player(s) etc.
""" 
(EXAMPLES)
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
missiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
"""
all_sprites = pygame.sprite.Group()


# Define user events.
enemy_speed_increase = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_speed_increase, 1000)

""" 
(examples)
# Create custom events for adding a new enemy and cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
"""


# Set up music.
"""
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

# Create the game loop(s).
running = True

while running:
       
    # Check all events.
    for event in pygame.event.get():
        # First define an exit strategy for the loop.
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if KEYDOWN[K_SPACE]:
                running = False
        
        # Add user defined events here.
        elif event.type ===========???????: 
        
    # Update and render background.
    back_ground.update()
    back_ground.render()
    
    # Add a Scorecard/healthbar/etc here (example)
    """
    #SCREEN_SURFACE.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    SCREEN_SURFACE.blit(scores, (10,10))
    """

    # Move and Draw all Sprites
    for entity in all_sprites:
        SCREEN_SURFACE.blit(entity.image, entity.rect)
        entity.move()
    
    # Player killed and end game screen (example)
    """
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
        """
    
    pygame.display.update()
    clock.tick(FPS)

# End game call here.
pygame.quit()
sys.exit()