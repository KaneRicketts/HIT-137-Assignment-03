import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()       # This initialises all the imported pygame modules.

# Initialising colour variables for common colours.

RED   = (255, 0, 0)
PINK = (255, 20, 147)
GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)
BLUE  = (0, 0, 255)
SKYBLUE = (0, 191, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHTGRAY = (211, 211, 211)
WHITE = (255, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE = (128, 0, 128)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)

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

# Setting up a clock (FPS) 
clock = pygame.time.Clock()     # The funtion to use our variable to set FPS.
FPS = 60        # The FPS we want the game to run at.

collisions = 0
score = 0
player_speed = 5
enemy_speed = 5
speed = 2

        # Bakgrounds

# Start Background
start_background_image = pygame.image.load("cave.jpg").convert_alpha()
start_rect = start_background_image.get_rect()

# Game Background
background_image = pygame.image.load("golden_cave_background.png").convert_alpha()
background_width = background_image.get_width()
background_height = background_image.get_height()
print(background_height)

tiles = 3

# Game-Over Background
end_background_image = pygame.image.load("spiders.jpg").convert_alpha()
end_rect = end_background_image.get_rect()

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
        """Draw onto surface with (x,y) coordinates. Determine if mousclick is on drawn button."""
        # Draw the image onto the screen at position rect.x and rect.y
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

class Player(pygame.sprite.Sprite):
    def __init__(self, health: int):
        super(Player, self).__init__() 
        self.image = pygame.image.load("hubert.png").convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(center = (int(width/2),int(height/2)))
        self.missiles = []
        self.health = health

    def move(self):
        # Move the sprite based on keyboard input.
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)      
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Ensure the player never leaves the screen.

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def shoot(self):
        missile = Weapon(self.rect.centerx, self.rect.bottom)
        self.missiles.append(missile)
        all_sprites.add(missile)
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, 100, 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 100
        draw_health_bar(surf, health_rect.topleft, health_rect.size, 
                (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health/max_health)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("spiders.jpg")
        width = self.image.get_width()
        height = self.image.get_height()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(center = (int(width/2),int(height/2)))

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)      
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        return score
    
    def shoot():
        pass

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Weapon, self).__init__()
        
        missile_img = pygame.image.load('missile.png').convert_alpha()
        missile_img_copy = missile_img.copy()

        # pygame.transform.flip() will flip the image 
        missile_img_with_flip = pygame.transform.flip(missile_img_copy, True, False)
        self.surf = missile_img_with_flip.convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(x, y)) 

    def update(self):
        self.rect.move_ip(5, 0)
        if self.rect.right > SCREEN_WIDTH:
            self.kill()

class Collectible:
    """Collectibles are given values here."""
    def __init__(self, label: str, add_points: int, add_health: int, add_lives: int,) -> None:
        self.label = label
        self.add_points = add_points
        self.add_health = add_health
        self.add_lives = add_lives
"""
class HealthBar:
    ""The size and view of the Health Bar is defined here.""

    def __init__(self, name: str, pos_x_y: tuple, size_x: int, size_y: int, colour_background: str, colour_remaining: str) -> None:
        self.name = name
        self.pos_x_y = pos_x_y
        self.size_x = size_x
        self.size_y = size_y
        self.colour_background = colour_background
        self.colour_remaining = colour_remaining

    def display():
        position
        height
        width of full health
        width of remaining health

    def current_health():
        # at start, current health = max health
        # once "something happens", then check current health
        
        current_health += -(damage) + add_health
        return current_health
"""
        # (EXAMPLE from jet game)
def draw_health_bar(surf, pos, size, borderC, backC, healthC, progress):
    pygame.draw.rect(surf, backC, (*pos, *size))
    pygame.draw.rect(surf, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+1, pos[1]+1)
    innerSize = ((size[0]-2) * progress, size[1]-2)
    rect = (round(innerPos[0]), round(innerPos[1]), round(innerSize[0]), round(innerSize[1]))
    pygame.draw.rect(surf, healthC, rect)

# Initialise instances of class objects.

player1: Player = Player(health = 100)

#bug_enemy: Enemy = Enemy(speed = 4, max_health = 10, lives = 1, jump = 0, fly = False)
#bat_enemy: Enemy = Enemy(speed = 4, max_health = 20, lives = 1, jump = 0, fly = True)
#boss_enemy: Enemy = Enemy(speed = 5, max_health = 50, lives = 2, jump = 10, fly = False)

start_button: Buttons = Buttons(130, 435, start_button, scale = 0.5)
exit_button: Buttons = Buttons(510,435, exit_button, scale = 0.5)
restart_button: Buttons = Buttons(130, 435, restart_button, scale = 0.5)

# coin: Collectible = Collectible(label = "Coin", add_points = 10, add_health = 0, add_lives = 0)
# fruit: Collectible = Collectible(label = "Coin", add_points = 0, add_health = 20, add_lives = 0)
# heart: Collectible = Collectible(label = "Coin", add_points = 0, add_health = 0, add_lives = 1)

# Create groups for enemy(ies), player(s) etc.

enemies = pygame.sprite.Group()
missiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)

# Define user events. (EXAMPLES)
enemy_speed_increase = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_speed_increase, 1000)

add_enemy = pygame.USEREVENT + 1
pygame.time.set_timer(add_enemy, 750)


# Set up music.

"""
(EXAMPLES from jet game)
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

    # To ensure we can replay the game, we insert all the while loops into a function.
    #       When RESTART is clicked, we just call the function.
def play():

    
    start_loop = True
    bye_img = font_large.render("GOODBYE", True, PURPLE)
    game_over_image = font_large.render("...GAME OVER...", True, BLUE)
    game_start_image = font_large.render("...WELCOME TO THE HUBERT GAME...", True, BLUE)
    moving_speed = player_speed

                                            # Create the start page loop.
    while start_loop:
        
        # Set a frame rate for the game.
        clock.tick(FPS)

        SCREEN_SURFACE.fill(WHITE)

        # Draw the background image to the screen.
        SCREEN_SURFACE.blit(start_background_image, (260, 100))

        SCREEN_SURFACE.blit(game_start_image, (175,30))

        # Check for close or escape event.
        for event in pygame.event.get():
            # First define an exit strategy for the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if KEYDOWN[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

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

        # Update the display for each loop.
        pygame.display.update()

                                        # Create the main game loop.
    running = True
    while running:

        # Set a frame rate for the game.
        clock.tick(FPS)
        SCREEN_SURFACE.fill(BLACK)

        # Update and render background.
        for i in range(0, tiles):
            SCREEN_SURFACE.blit(background_image, (i * background_width + moving_speed, 30))
        
        moving_speed -= 1

        if abs(moving_speed) > background_width:
            moving_speed = 0

        # Check all events.
        for event in pygame.event.get():
            # First define an exit strategy for the loop.

            # Did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Was a button pressed?
            elif event.type == KEYDOWN:

                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

                # Was it the Space key? If so, player shoots weapon.
                if event.key == K_SPACE:
                    player1.shoot()

        """            
        # Is the time right for a new enemy.
            elif event.type == add_enemy:

                # Create the new enemy, and add it to our sprite groups.
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Get the set of keys pressed and check for user input to player controls.
        pressed_keys = pygame.key.get_pressed()
        player1.update(pressed_keys)
        
        # Update the position of our enemies.
        enemies.update()

        # Add a Scorecard/healthbar/etc here (example)
        player1.draw_health(SCREEN_SURFACE)
            
        #SCREEN_SURFACE.blit(background, (0,0))
        scores = font.render("SCORE", True, BLACK)
        SCREEN_SURFACE.blit(scores, (10,10))
        
    # Draw all our sprites
        for entity in all_sprites:
            SCREEN_SURFACE.blit(entity.surf, entity.rect)
        
        for missile in player1.missiles:
                missile.update()
                if pygame.sprite.spritecollide(missile, enemies, True):
                    missile.kill()
                    collisions +=1
                    continue

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollide(player1, enemies, dokill = True):
            # If so, kill missile and subtract health.
            player1.health -= 10
            if player1.health <= 0:
                time.sleep(0.5)
                SCREEN_SURFACE.fill(RED)
                SCREEN_SURFACE.blit(game_over_image, (30,250))

                pygame.display.update()
                for entity in all_sprites:
                    entity.kill() 
                time.sleep(1.5)
                running = False
            """
        
        # Update the display for each loop.
        pygame.display.update()

                                    # Create the final game-over page loop.
    game_over_screen = True

    while game_over_screen:
        
        SCREEN_SURFACE.fill(RED)
        SCREEN_SURFACE.blit(game_over_image, (375,150))
        # Player killed and end game screen (example)

        # Check all events.
        for event in pygame.event.get():
            # First define an exit strategy for the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if KEYDOWN[K_ESCAPE]:
                    game_over_screen = False

        if restart_button.draw():
            play()

        if exit_button.draw():
            time.sleep(.5)
            SCREEN_SURFACE.fill(BLACK)
            SCREEN_SURFACE.blit(bye_img, (400,250))
            pygame.display.update()
            time.sleep(1.5)
            game_over_screen = False
        
        pygame.display.update()

play()

# End game call here.
pygame.quit()
sys.exit()