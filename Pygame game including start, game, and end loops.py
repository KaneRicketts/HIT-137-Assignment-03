import os
import sys  
import random  
import time  
import pygame  
from pygame.locals import * 

pygame.init()  # Start pygame so we can use it

# To play the game again, we put everything in a function called play
def play():
    
    RED = (255, 0, 0)            
    PINK = (255, 20, 147)        
    GREEN = (0, 255, 0)          
    DARKGREEN = (0, 100, 0)      
    BLUE = (0, 0, 255)          
    SKYBLUE = (0, 191, 255)      
    CYAN = (0, 255, 255)         
    BLACK = (0, 0, 0)            
    GRAY = (128, 128, 128)       
    LIGHTGRAY = (211, 211, 211)  
    WHITE = (255, 255, 255)      
    MAGENTA = (255, 0, 255)      
    PURPLE = (128, 0, 128)       
    GOLD = (255, 215, 0)         
    BROWN = (139, 69, 19)        

    GRAVITY = 0.5        # How strong gravity is
    JUMP_VELOCITY = -10  # How high the player can jump

    # Set up the game window size
    screen_width = 1000
    screen_height = 600
    window = pygame.display.set_mode((screen_width, screen_height))  
    pygame.display.set_caption("The Adventures of Hubert")  # Set the title of the window

    # Choose fonts to write text on the screen
    font = pygame.font.SysFont("8514oem", 20)      # Small font
    font_large = pygame.font.SysFont("8514oem", 50) # Big font

    # More game stuff
    clock = pygame.time.Clock()     # Keep track of time
    frames_per_sec = 60             # How many times the screen updates each second

    moving_speed = 0        # How fast the background moves
    collisions = 0          # How many enemies we've hit
    coin_score = 0          # How many coins we've collected
    current_level = 1       # What level we're on
    boss_defeated = False   # Did we beat the boss?

    # Keep track of hearts in each level
    heart_spawned = {1: False, 2: False, 3: False}  # Hearts for levels 1, 2, and 3

    # Load pictures
    start_button_img = pygame.image.load("Resources/START.png").convert_alpha()    # Start button
    exit_button_img = pygame.image.load("Resources/EXIT.png").convert_alpha()      # Exit button
    restart_button_img = pygame.image.load("Resources/RESTART.png").convert_alpha()# Restart button

    # Load ant pictures to make them walk
    ant_walk_images = [
        pygame.image.load("Resources/Ant1.png").convert_alpha(),
        pygame.image.load("Resources/Ant2.png").convert_alpha(),
        pygame.image.load("Resources/Ant3.png").convert_alpha(),
        pygame.image.load("Resources/Ant4.png").convert_alpha(),
        pygame.image.load("Resources/Ant5.png").convert_alpha(),
        pygame.image.load("Resources/Ant6.png").convert_alpha(),
    ]
    
    # Load backgrounds for different screens
    start_background_image = pygame.image.load("Resources/You Found a Cave2.png").convert_alpha()  # Start screen background
    start_background_image = pygame.transform.scale(start_background_image, (screen_width, screen_height))  
    start_rect = start_background_image.get_rect()  #

    # Load game backgrounds for different levels
    background_image = pygame.image.load("Resources/golden_cave_background.png").convert_alpha()  # Level 1 background
    background_width = background_image.get_width()    
    background_height = background_image.get_height()  
    tiles = 3  # How many times the background repeats to make scrolling smooth

    # Load Level 2 background
    level2_background_image = pygame.image.load("Resources/Background 2.png").convert_alpha()
    level2_background_width = level2_background_image.get_width()
    level2_background_height = level2_background_image.get_height()

    # Load Level 3 (boss) background
    spider_boss_background_image = pygame.image.load("Resources/Spider boss background.png").convert_alpha()
    spider_boss_background_image = pygame.transform.scale(spider_boss_background_image, (screen_width, screen_height))  # Make it fit the screen

    # Load Game-Over background
    you_died_background_image = pygame.image.load("Resources/You died background.png").convert_alpha()
    you_died_background_image = pygame.transform.scale(you_died_background_image, (screen_width, screen_height))  # Make it fit the screen
    you_died_rect = you_died_background_image.get_rect()

    # Create text images
    bye_img = font_large.render("See you next time", True, PURPLE)            # Bye text
    game_over_image = font_large.render("...GAME OVER...", True, BLUE)         # Game over text
    game_start_image = font_large.render("ADVENTURES OF HUBERT THE GAME", True, BLUE)  # Game heading title text

    # Load images between levels
    all_levels_image = pygame.image.load("Resources/All levels.png").convert_alpha()
    level1_done_image = pygame.image.load("Resources/Level 1 done.png").convert_alpha()
    level2_done_image = pygame.image.load("Resources/Level 2 done.png").convert_alpha()
    level3_done_image = pygame.image.load("Resources/Level 3 done.png").convert_alpha()

    # Make images fit the screen
    all_levels_image = pygame.transform.scale(all_levels_image, (screen_width, screen_height))
    level1_done_image = pygame.transform.scale(level1_done_image, (screen_width, screen_height))
    level2_done_image = pygame.transform.scale(level2_done_image, (screen_width, screen_height))
    level3_done_image = pygame.transform.scale(level3_done_image, (screen_width, screen_height))

    # Load and scale coin images
    coin_scale = 0.4  # How big the coins are
    walkCoin = [
        pygame.transform.scale(pygame.image.load("Resources/Coin1.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Resources/Coin2.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Resources/Coin3.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Resources/Coin4.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Resources/Coin5.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Resources/Coin6.png"), (int(100*coin_scale), int(100*coin_scale)))
    ]

    # Load and scale bat images
    bat_scale = 0.75  # How big the bats are
    bat_images = [
        pygame.transform.scale(pygame.image.load("Resources/bat_1.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("Resources/bat_2.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("Resources/bat_3.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("Resources/bat_4.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("Resources/bat_5.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("Resources/bat_6.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("Resources/bat_7.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("Resources/bat_8.png"), (int(100*bat_scale), int(50*bat_scale)))
    ]
   
    # Load spider (boss) images 
    # Spider Down images
    spider_down_images = [
        pygame.image.load("Resources/Spider_Down_1.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Down_2.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Down_3.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Down_4.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Down_5.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Down_6.png").convert_alpha(),
    ]

    # Spider Left images
    spider_left_images = [
        pygame.image.load("Resources/Spider_Left_1.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Left_2.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Left_3.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Left_4.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Left_5.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Left_6.png").convert_alpha(),
    ]

    # Spider Up images
    spider_up_images = [
        pygame.image.load("Resources/Spider_Up_1.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Up_2.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Up_3.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Up_4.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Up_5.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Up_6.png").convert_alpha(),
    ]

    # Spider Right images
    spider_right_images = [
        pygame.image.load("Resources/Spider_Right_1.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Right_2.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Right_3.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Right_4.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Right_5.png").convert_alpha(),
        pygame.image.load("Resources/Spider_Right_6.png").convert_alpha(),
    ]

    # Load boss shooting images
    boss_shoot_images = [
        pygame.image.load("Resources/Bossshoot1.png").convert_alpha(),
        pygame.image.load("Resources/Bossshoot2.png").convert_alpha(),
        pygame.image.load("Resources/Bossshoot3.png").convert_alpha(),
        pygame.image.load("Resources/Bossshoot4.png").convert_alpha(),
    ]

    # Load and scale heart images
    heart_scale = 0.2  # How big the hearts are
    heart_images = [
        pygame.transform.scale(pygame.image.load("Resources/HP+1.1.png").convert_alpha(),
                              (int(pygame.image.load("Resources/HP+1.1.png").get_width() * heart_scale),
                               int(pygame.image.load("Resources/HP+1.1.png").get_height() * heart_scale))),
        pygame.transform.scale(pygame.image.load("Resources/HP+1.2.png").convert_alpha(),
                              (int(pygame.image.load("Resources/HP+1.2.png").get_width() * heart_scale),
                               int(pygame.image.load("Resources/HP+1.2.png").get_height() * heart_scale))),
        pygame.transform.scale(pygame.image.load("Resources/HP+1.3.png").convert_alpha(),
                              (int(pygame.image.load("Resources/HP+1.3.png").get_width() * heart_scale),
                               int(pygame.image.load("Resources/HP+1.3.png").get_height() * heart_scale)))
    ]
    
    # Load Hubert walking and missile images for instructions page
    hubert_walk_img = pygame.image.load("Resources/hubert1.png").convert_alpha()  # Hubert walking
    missile_img = pygame.image.load("Resources/Bossshoot1.png").convert_alpha()  # Shooting image

    # Scale Hubert walk and missile images
    hubert_action_scale = 0.5  # How big Hubert and missiles are
    hubert_walk_img = pygame.transform.scale(hubert_walk_img, (int(hubert_walk_img.get_width() * hubert_action_scale), int(hubert_walk_img.get_height() * hubert_action_scale)))
    missile_info_img = pygame.transform.scale(missile_img, (int(missile_img.get_width() * hubert_action_scale), int(missile_img.get_height() * hubert_action_scale)))

    # Load and scale the victory coin image on last page/screen
    victory_coin_image = pygame.image.load("Resources/Coin1.png").convert_alpha()  
    victory_coin_scale = 0.3  # How big the victory coin is
    victory_coin_image = pygame.transform.scale(victory_coin_image, (int(victory_coin_image.get_width() * victory_coin_scale), int(victory_coin_image.get_height() * victory_coin_scale)))

  
    # Function to show level screens
    def show_level_screen(image):
        window.blit(image, (0,0))    
        pygame.display.update()      
        time.sleep(2)                # Wait for 2 seconds

    # give health to the player
    class Heart(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Heart, self).__init__()
            self.images = heart_images  
            self.index = 0
            self.animation_speed = 0.1  # How fast the heart apperas
            self.image = self.images[int(self.index)]  
            self.rect = self.image.get_rect(center=(x, y))  
            self.speed = 2  # How fast the heart moves

        def update(self):
            self.index += self.animation_speed  # Change animation frame
            if self.index >= len(self.images):
                self.index = 0  
            self.image = self.images[int(self.index)]  
            self.rect.move_ip(-self.speed, 0)  
            if self.rect.right < 0:
                self.kill()  # Remove the heart if it goes off screen
   
    # ants that walk
    class AnimatedAnt(pygame.sprite.Sprite):
        def __init__(self, images, scale, speed, x, y):
            super(AnimatedAnt, self).__init__()
            # Make the ant images bigger
            self.images = [pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) for img in images]
            self.index = 0
            self.animation_speed = 0.1  # How fast the ant walks
            self.image = self.images[self.index]  
            self.rect = self.image.get_rect(center=(x, y))  
            self.speed = speed  # How fast the ant moves

        def update(self):
            self.index += self.animation_speed  
            if self.index >= len(self.images):
                self.index = 0  
            self.image = self.images[int(self.index)]  
            self.rect.move_ip(-self.speed, 0)  #
            if self.rect.right < 0:
                self.kill()  # Remove the ant if it goes off screen
   
    # Buttons Class - makes buttons you can click
    class Buttons():
        """Make buttons and check if you clicked them."""
        def __init__(self, x, y, image, scale) -> None:
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, ((int(width * scale)), (int(height * scale))))  
            self.rect = self.image.get_rect()  
            self.rect.topleft = (x, y)  
            self.mouse_click = False  

        def draw(self):
            """Draw the button and check if it was clicked."""
            window.blit(self.image, (self.rect.x, self.rect.y))  

            clicked = False  
            pos_mouse = pygame.mouse.get_pos()  

            if self.rect.collidepoint(pos_mouse):  

                if pygame.mouse.get_pressed()[0] == 1 and not self.mouse_click:  
                    self.mouse_click = True  #
                    clicked = True  # Button was clicked

                if pygame.mouse.get_pressed()[0] == 0:  # If mouse button is released
                    self.mouse_click = False  # Reset the click

            return clicked  # Tell if the button was clicked

    # Player Class - the main character
    class Player(pygame.sprite.Sprite):
        def __init__(self, health, scale):
            super(Player, self).__init__()
            
            # Load Hubert's walking images
            self.images = [
                pygame.image.load("Resources/hubert1.png").convert_alpha(),
                pygame.image.load("Resources/hubert2.png").convert_alpha(),
                pygame.image.load("Resources/hubert3.png").convert_alpha(),
                pygame.image.load("Resources/hubert4.png").convert_alpha(),
                pygame.image.load("Resources/hubert5.png").convert_alpha(),
                pygame.image.load("Resources/hubert6.png").convert_alpha()
            ]
            
            # Make Hubert's images bigger or smaller
            self.images = [
                pygame.transform.scale(img, (
                    int(img.get_width() * scale), 
                    int(img.get_height() * scale)
                )) for img in self.images
            ]
            self.index = 0  # Current image
            self.image = self.images[self.index]  # Show the current image
            self.rect = self.image.get_rect()
            self.rect.bottom = 420  # Start position on the ground
            
            self.animation_speed = 0.15  # How fast Hubert walks
            self.animation_timer = 0  
            self.is_moving = False  
            self.missiles = []  # List of missiles Hubert has shot
            self.health = health  # How much health Hubert has
            self.jumping = False
            self.velocity = [0, 0]
            
            # Jumping and Gravity
            self.vel_y = 0
            self.is_jumping = False

        def move(self, current_level):
            pressed_keys = pygame.key.get_pressed()  # Check which keys are pressed
            self.is_moving = False  # Reset moving flag each frame
            
            # Move based on arrow keys
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)  # Move up
                self.is_moving = True
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)   # Move down
                self.is_moving = True
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # Move left
                self.is_moving = True
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)   # Move right
                self.is_moving = True

            # Apply gravity
            self.vel_y += GRAVITY  
            self.rect.y += self.vel_y  
            
            # Keep Hubert on the ground for levels 1 and 2
            if current_level in [1, 2]:
                if self.rect.bottom >= 420:
                    self.rect.bottom = 420  # Stay on the ground
                    self.vel_y = 0
                    self.is_jumping = False
            elif current_level == 3:
                # Keep Hubert inside the screen for level 3
                if self.rect.bottom >= screen_height:
                    self.rect.bottom = screen_height
                    self.vel_y = 0
                    self.is_jumping = False
                if self.rect.top <= 0:
                    self.rect.top = 0
                    self.vel_y = 0

            # Don't let Hubert go off the sides of the screen
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > screen_width:
                self.rect.right = screen_width

            # Animate Hubert if moving
            if self.is_moving:
                self.animation_timer += self.animation_speed  
                if self.animation_timer >= len(self.images):
                    self.animation_timer = 0  
                self.index = int(self.animation_timer)  
                self.image = self.images[self.index]  
            else:
                # If not moving, show the first image
                self.index = 0
                self.image = self.images[self.index]

        # Make Hubert jump
        def jump(self):
            if not self.is_jumping:
                self.vel_y = JUMP_VELOCITY  
                self.is_jumping = True  

        # Draw the health bar on the screen
        def health_bar(self, surface, position, size, border_colour, background_colour, health_colour, remaining_health):
            pygame.draw.rect(surface, background_colour, (*position, *size))  
            pygame.draw.rect(surface, border_colour, (*position, *size), 1)  
            inner_position  = (position[0]+1, position[1]+1)  
            inner_rect = ((size[0]-2) * remaining_health, size[1]-2)  
            rect = (round(inner_position[0]), round(inner_position[1]), round(inner_rect[0]), round(inner_rect[1]))
            pygame.draw.rect(surface, health_colour, rect)  

        # Show the health bar
        def draw_health(self, surf):
            health_rect = pygame.Rect(0, 0, 100, 7)  # Size of health bar
            health_rect.midbottom = self.rect.centerx, self.rect.top 
            max_health = 100  # Maximum health
            self.health_bar(surf, health_rect.topleft, health_rect.size, BLACK, RED, GREEN, self.health/max_health) 

        # Make Hubert shoot missiles when pressing 'F'
        def shoot(self):
            missile_offset = 65  # Where the missile shoot from on the picture of hubert
            missile = Weapon(self.rect.centerx, self.rect.top + missile_offset)  
            self.missiles.append(missile) 
            all_sprites.add(missile)  

    # Enemy Class 
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, image, scale, speed, x, y):
            super(Enemy, self).__init__()
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, ((int(width * scale)), (int(height * scale))))  # Make enemy bigger
            self.image.set_colorkey(WHITE) 
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)  
            self.speed = speed  

        def update(self):
            self.rect.move_ip(-self.speed, 0) 
            if self.rect.right < 0:
                self.kill()  # Remove enemy if it goes off screen

    # Weapon Class 
    class Weapon(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Weapon, self).__init__()
            missile_img = pygame.image.load("Resources/missile.png").convert_alpha()  
            missile_img_copy = missile_img.copy()
            missile_img_with_flip = pygame.transform.flip(missile_img_copy, True, False)
            self.image = missile_img_with_flip.convert_alpha() 
            self.image.set_colorkey(WHITE)  
            self.rect = self.image.get_rect(center = (x, y))  

        def update(self):
            self.rect.move_ip(5, 0)  
            if self.rect.right > screen_width:
                self.kill()  

    # Coin Class - coins that Hubert can collect
    class Coin(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Coin, self).__init__()
            self.images = walkCoin  
            self.index = 0
            self.animation_speed = 0.2  # How fast the coin animates
            self.image = self.images[int(self.index)]  
            self.rect = self.image.get_rect(center=(x, y))  

        def update(self):
            self.index += self.animation_speed  
            if self.index >= len(self.images):
                self.index = 0  
            self.image = self.images[int(self.index)] 
            self.rect.move_ip(-2, 0)  
            if self.rect.right < 0:
                self.kill()  

    # Bat Class - bats that fly
    class Bat(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Bat, self).__init__()
            self.images = bat_images  
            self.index = 0
            self.animation_speed = 0.2  # How fast the bat animates
            self.image = self.images[int(self.index)]  
            self.rect = self.image.get_rect(center=(x, y))  
            self.speed = 5  

        def update(self):
            self.index += self.animation_speed  
            if self.index >= len(self.images):
                self.index = 0  
            self.image = self.images[int(self.index)]  
            self.rect.move_ip(-self.speed, 0)  
            if self.rect.right < 0:
                self.kill()  #

    # BossSpider Class - the big boss enemy
    class BossSpider(pygame.sprite.Sprite):
        def __init__(self, health, speed, scale):
            super(BossSpider, self).__init__()

            # Load images for different directions
            self.images_down = [pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) for img in spider_down_images]
            self.images_left = [pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) for img in spider_left_images]
            self.images_up = [pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) for img in spider_up_images]
            self.images_right = [pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) for img in spider_right_images]

            self.images = self.images_down  
            self.index = 0
            self.animation_speed = 0.3  # How fast the boss animates
            self.image = self.images[int(self.index)]  
            self.rect = self.image.get_rect()
            self.rect.center = (screen_width - 100, screen_height // 2)  
            self.speed = speed  
            self.health = health  
            self.direction = random.choice(["up", "down", "left", "right"])  
            self.last_shot = pygame.time.get_ticks()  
            self.shoot_cooldown = 3000  # How often the boss shoots (milliseconds)
            self.move_timer = pygame.time.get_ticks()  #
            self.move_delay = 1000  # How often the boss changes direction

        def update(self):
            self.index += self.animation_speed  
            if self.index >= len(self.images):
                self.index = 0  
            self.image = self.images[int(self.index)]  

            # Change direction every move_delay milliseconds
            current_time = pygame.time.get_ticks()
            if current_time - self.move_timer > self.move_delay:
                self.direction = random.choice(["up", "down", "left", "right"])  
                self.move_timer = current_time  

            # Move the boss based on direction
            if self.direction == "up":
                self.rect.y -= self.speed  
                self.images = self.images_up  
            elif self.direction == "down":
                self.rect.y += self.speed  
                self.images = self.images_down  
            elif self.direction == "left":
                self.rect.x -= self.speed  
                self.images = self.images_left  
            elif self.direction == "right":
                self.rect.x += self.speed  
                self.images = self.images_right  

            # Keep the boss on the right half of the screen so its easier to kill
            if self.rect.left < screen_width // 2:
                self.rect.left = screen_width // 2 
            if self.rect.right > screen_width:
                self.rect.right = screen_width  
            if self.rect.top < 0:
                self.rect.top = 0  
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height  

            
            if current_time - self.last_shot > self.shoot_cooldown:
                self.shoot()  
                self.last_shot = current_time  

        def shoot(self):
            boss_bullet = BossBullet(self.rect.centerx, self.rect.centery)  
            all_sprites.add(boss_bullet)  
            boss_bullets.add(boss_bullet)  

        # Draw the boss's health bar
        def draw_health(self, surf):
            # Health bar above the boss
            health_rect = pygame.Rect(0, 0, 150, 10)  # Size of the health bar
            health_rect.midbottom = self.rect.centerx, self.rect.top - 5  
            max_health = 100  # Maximum health
            self.health_bar(surf, health_rect.topleft, health_rect.size, BLACK, RED, GREEN, self.health / max_health)  

        # Draw the health bar
        def health_bar(self, surface, position, size, border_colour, background_colour, health_colour, remaining_health):
            pygame.draw.rect(surface, background_colour, (*position, *size))  
            pygame.draw.rect(surface, border_colour, (*position, *size), 1)  
            inner_position = (position[0] + 1, position[1] + 1)  #
            inner_rect = ((size[0] - 2) * remaining_health, size[1] - 2)  
            rect = (round(inner_position[0]), round(inner_position[1]), round(inner_rect[0]), round(inner_rect[1]))
            pygame.draw.rect(surface, health_colour, rect)  

    # BossBullet Class - bullets shot by the boss
    class BossBullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(BossBullet, self).__init__()
            # Load and scale bullet images
            self.images = [pygame.transform.scale(img, (30, 30)) for img in boss_shoot_images]
            self.index = 0
            self.animation_speed = 0.1  # How fast the bullet animates
            self.image = self.images[int(self.index)]  
            self.rect = self.image.get_rect(center=(x, y))  
            self.speed = 8  # How fast the bullet moves

        def update(self):
            self.index += self.animation_speed  
            if self.index >= len(self.images):
                self.index = 0  
            self.image = self.images[int(self.index)]  
            self.rect.x -= self.speed  
            if self.rect.right < 0:
                self.kill()  

    # Create the player
    player = Player(health=100, scale=0.5)  # Make the player health here

    # Create buttons for main screen
    start_button = Buttons(130, 435, start_button_img, scale=0.5)     
    exit_button = Buttons(510, 435, exit_button_img, scale=0.5)       
    restart_button = Buttons(130, 435, restart_button_img, scale=0.5) 

    # Create groups for different sprites
    enemies = pygame.sprite.Group()   # Group for enemies
    missiles = pygame.sprite.Group()  # Group for missiles
    coins = pygame.sprite.Group()     # Group for coins
    bats = pygame.sprite.Group()      # Group for bats
    all_sprites = pygame.sprite.Group()  # All sprites group
    all_sprites.add(player)  # Add the player to all sprites
    boss_bullets = pygame.sprite.Group()  # Group for boss bullets
    boss_group = pygame.sprite.Group()    # Group for the boss
    hearts = pygame.sprite.Group()  # Group for hearts

   #EVENTS ON THE SCREEN
    add_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(add_enemy, 1000)  # Add an enemy every 1 second
    
    add_coin = pygame.USEREVENT + 2
    pygame.time.set_timer(add_coin, 3000)    # Add a coin every 3 seconds

    add_bat = pygame.USEREVENT + 3
    pygame.time.set_timer(add_bat, 5000)     # Add a bat every 5 seconds

    add_heart = pygame.USEREVENT + 4
    pygame.time.set_timer(add_heart, 10000)  # Add a heart every 10 seconds

    
    start_loop = True
    while start_loop:
        window.fill(WHITE)  
        window.blit(start_background_image, (0, 0))  # Show the start background
        window.blit(game_start_image, (175, 30))      

       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        
        if start_button.draw():
            start_loop = False

        # If Exit button is clicked, quit the game
        if exit_button.draw():
            time.sleep(0.5)  # Wait half a second
            window.fill(BLACK)  
            window.blit(bye_img, (350, 250))  #
            pygame.display.update()  
            time.sleep(1.5)  
            pygame.quit()
            sys.exit()

        pygame.display.update()

    
    info_loop = True
    info_start_time = pygame.time.get_ticks()  

    standard_width = 100  # Width for info images
    standard_height = 100 # Height for info images

    # info screen
    ant_info_img = pygame.transform.scale(ant_walk_images[0], (standard_width, standard_height))  # Ant picture
    bat_info_img = pygame.transform.scale(bat_images[0], (standard_width, standard_height))        # Bat picture
    coin_info_img = pygame.transform.scale(walkCoin[0], (standard_width, standard_height))          # Coin picture
    heart_info_img = pygame.transform.scale(heart_images[0], (standard_width, standard_height))      # Heart picture

    # info screen
    hubert_walk_info_img = pygame.transform.scale(hubert_walk_img, (standard_width, standard_height))  # Hubert walking
    missile_info_scaled_img = pygame.transform.scale(missile_info_img, (standard_width, standard_height))  # Missile

    # info screen text
    info_text1 = font_large.render("Watch out for these cave creatures that live in the cave.", True, WHITE)  
    info_text2 = font.render("Be on the look out for the BOSS:", True, WHITE) 

    # Instruction Texts on 2nd page
    instruction_text1 = font.render("Space Bar to Jump", True, WHITE)         # Jump instruction
    instruction_text2 = font.render("'F' to Shoot", True, WHITE)            # Shoot instruction
    instruction_text3 = font.render("Use Arrow Keys to Walk", True, WHITE)  # Move instruction

    while info_loop:
        window.fill(BLACK)  # Make the screen black

       
        window.blit(info_text1, (50, 50))  
        window.blit(info_text2, (50, 500))  

        spacing = 50  # Space between images
        total_width = 4 * standard_width + 3 * spacing  
        start_x = (screen_width - total_width) // 2  
        y_position = 150  # Vertical position for the images

        window.blit(ant_info_img, (start_x, y_position))  # Ant image
        window.blit(bat_info_img, (start_x + standard_width + spacing, y_position))  # Bat image
        window.blit(coin_info_img, (start_x + 2 * (standard_width + spacing), y_position))  # Coin image
        window.blit(heart_info_img, (start_x + 3 * (standard_width + spacing), y_position))  # Heart image

        # Add labels below images
        ant_label = font.render("Ant Enemy", True, WHITE)  # Label for ant
        bat_label = font.render("Bat Enemy", True, WHITE)  # Label for bat
        coin_label = font.render("Coins", True, WHITE)     # Label for coins
        heart_label = font.render("Hearts (Health)", True, WHITE)  # Label for hearts

        window.blit(ant_label, (start_x + (standard_width - ant_label.get_width()) // 2, y_position + standard_height + 10))  # Ant label
        window.blit(bat_label, (start_x + standard_width + spacing + (standard_width - bat_label.get_width()) // 2, y_position + standard_height + 10))  # Bat label
        window.blit(coin_label, (start_x + 2 * (standard_width + spacing) + (standard_width - coin_label.get_width()) // 2, y_position + standard_height + 10))  # Coin label
        window.blit(heart_label, (start_x + 3 * (standard_width + spacing) + (standard_width - heart_label.get_width()) // 2, y_position + standard_height + 10))  # Heart label

        # Instructions for Player on the info screen
        instructions_start_x = (screen_width - (3 * standard_width + 2 * spacing)) // 2  
        instructions_y_position = 250  # Vertical position 
        instruction_spacing = spacing  # Space between instructions
        window.blit(hubert_walk_info_img, (instructions_start_x, instructions_y_position))  # Hubert walking image
        window.blit(missile_info_scaled_img, (instructions_start_x + standard_width + instruction_spacing, instructions_y_position))  # Missile image
        window.blit(hubert_walk_info_img, (instructions_start_x + 2 * (standard_width + instruction_spacing), instructions_y_position))  # Hubert walking image again

        # Show instruction texts below each image
        window.blit(instruction_text1, (instructions_start_x, instructions_y_position + standard_height + 10))  # Jump
        window.blit(instruction_text2, (instructions_start_x + standard_width + instruction_spacing, instructions_y_position + standard_height + 10))  # Shoot
        window.blit(instruction_text3, (instructions_start_x + 2 * (standard_width + instruction_spacing), instructions_y_position + standard_height + 10))  # Move

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # If 5 seconds have passed, go to the next screen
        current_time = pygame.time.get_ticks()
        if current_time - info_start_time > 5000:
            info_loop = False  

        pygame.display.update()
  
    show_level_screen(all_levels_image)  # Show all levels screen

    # Main Game Loop
    running = True
    while running:

        clock.tick(frames_per_sec)  
        window.fill(BLACK)  

        # Show background based on the current level
        if current_level == 1:
            for i in range(0, tiles):
                window.blit(background_image, (i * background_width + moving_speed, 30))  # Show Level 1 background
            moving_speed -= 0.5  # Move the background speed
            if abs(moving_speed) > background_width:
                moving_speed = 0  

        elif current_level == 2:
            for i in range(0, tiles):
                window.blit(level2_background_image, (i * level2_background_width + moving_speed, -75))  # Show Level 2 background
            moving_speed -= 0.5  # Move the background speed
            if abs(moving_speed) > level2_background_width:
                moving_speed = 0 

        elif current_level == 3:
            window.blit(spider_boss_background_image, (0, 0))  # Show Level 3 (boss) background

        
        # Check all events like key presses and spawning enemies
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False  # Stop the game loop

                if event.key == K_SPACE:
                    player.jump()  # Make Hubert jump

                if event.key == K_f:
                    player.shoot()  # Make Hubert shoot

            elif event.type == add_enemy and current_level < 3:
                
                ant_enemy = AnimatedAnt(ant_walk_images, scale=0.5, speed=5, x=990, y=420)  
                enemies.add(ant_enemy)  # Add to enemies group
                all_sprites.add(ant_enemy)  # Add to all sprites

            elif event.type == add_coin and current_level < 3:
                # Create a new coin at a random position
                x = random.randint(screen_width + 50, screen_width + 100)  # Start off the screen
                y = random.randint(50, 350)  
                coin = Coin(x, y)  
                coins.add(coin)  
                all_sprites.add(coin)  

            elif event.type == add_bat and current_level < 3:
            
                if len(bats) == 0:
                    x = screen_width + 50  
                    y = random.randint(0, 250)  
                    bat = Bat(x, y)  
                    bats.add(bat)  
                    all_sprites.add(bat)  

            elif event.type == add_heart and current_level <= 3 and not heart_spawned[current_level]:
                # Add a heart once per level
                heart = Heart(screen_width + 50, screen_height // 2)  
                hearts.add(heart)  
                all_sprites.add(heart)  
                heart_spawned[current_level] = True  

        player.move(current_level)  

       
        enemies.update()       
        coins.update()         
        bats.update()          
        boss_bullets.update()  
        hearts.update()        

        # If we're on Level 3, add the boss spider
        if current_level == 3 and not boss_group:
            boss_spider = BossSpider(health=120, speed=4, scale=1.0)  # Create the boss
            all_sprites.add(boss_spider)  # Add to all sprites
            boss_group.add(boss_spider)    # Add to boss group

        if current_level == 3:
            boss_group.update()              # Update the boss
            boss_spider.draw_health(window)  # Show boss health
            boss_bullets.draw(window)        # Show boss bullets

        # Show the player's health
        player.draw_health(window)

        # Show scores and level on the screen
        scores = font.render(f"SCORE: {collisions}", True, WHITE)       # Show score
        coin_display = font.render(f"COINS: {coin_score}", True, WHITE)  # Show coins
        window.blit(scores, (10,10))      # Put score on screen
        window.blit(coin_display, (10,40))  # Put coins on screen

        level_display = font.render(f"LEVEL: {current_level}", True, WHITE)  # Show level
        window.blit(level_display, (10,70))  # Put level on screen

        # Check if we've hit enough enemies to go to the next level
        if collisions >= 20 and current_level == 1:
            current_level = 2  # Go to level 2
            heart_spawned[current_level] = False  # Reset heart spawn
            show_level_screen(level1_done_image)  # Show Level 1 done screen

        elif collisions >= 40 and current_level == 2:
            current_level = 3  # Go to level 3
            heart_spawned[current_level] = False  # Reset heart spawn
            show_level_screen(level2_done_image)  # Show Level 2 done screen
            player.rect.bottom = screen_height  # Move player to the bottom of the screen

        # Draw all sprites on the screen
        for entity in all_sprites:
            window.blit(entity.image, entity.rect)

        hearts.draw(window)  # Draw hearts

        # Check if the player got a heart
        heart_collisions = pygame.sprite.spritecollide(player, hearts, dokill=True)
        if heart_collisions:
            player.health = 100  # Restore health to full

        # Check if missiles hit enemies
        for missile in player.missiles[:]:
            missile.update()  
            missiles.add(missile)  
            if pygame.sprite.spritecollide(missile, enemies, True):  
                missile.kill()  
                player.missiles.remove(missile)  
                collisions += 1  

            # Check if missiles hit bats
            if pygame.sprite.spritecollide(missile, bats, True):
                missile.kill()  
                player.missiles.remove(missile)  
                collisions += 1  

            # Check if missiles hit the boss
            if current_level == 3 and pygame.sprite.spritecollide(missile, boss_group, False):
                missile.kill()  
                player.missiles.remove(missile)  
                boss_spider.health -= 10  # Reduce boss health

                if boss_spider.health <= 0:  # If boss is dead
                    boss_spider.kill()  
                    boss_defeated = True  # 
                    running = False  # Stop the game loop
                    show_level_screen(level3_done_image)  # Show Level 3 done screen

        # Check if enemies hit the player
        if pygame.sprite.spritecollide(player, enemies, dokill=True):
            player.health -= 10  # Lose health

        # Check if bats hit the player
        if pygame.sprite.spritecollide(player, bats, dokill=True):
            player.health -= 5  # Lose a little health

        # Check if boss bullets hit the player
        if pygame.sprite.spritecollide(player, boss_bullets, dokill=True):
            player.health -= 35  # Lose a lot of health

        # Check if player collected any coins
        coins_collected = pygame.sprite.spritecollide(player, coins, dokill=True)
        if coins_collected:
            coin_score += len(coins_collected)  # Increase coin score

        # If the player's health is zero or less, the player dies
        if player.health <= 0:
            for entity in all_sprites:
                entity.kill() 
            player.health = 100  # Reset health
            time.sleep(0.5)  
            window.blit(you_died_background_image, (0,0))  # Show death background
            
            # Show "You Died!" text
            death_text = font_large.render("You Died!", True, RED)
            death_text_rect = death_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
            window.blit(death_text, death_text_rect)

            # Ask the player what to do next
            prompt_text = font.render("What would you like to do?", True, WHITE)
            prompt_text_rect = prompt_text.get_rect(center=(screen_width // 2, screen_height // 2))
            window.blit(prompt_text, prompt_text_rect)

            pygame.display.update()  
            time.sleep(1.5)  
            running = False  

        
        pygame.display.update()

    # After the game loop ends, check if the boss was defeated
    if boss_defeated:
        victory_screen = True
        while victory_screen:
        
            cave_exit_background = pygame.image.load("Rescources/Cave Exit.png").convert_alpha()  # Load victory background
            cave_exit_background = pygame.transform.scale(cave_exit_background, (screen_width, screen_height))  
            window.blit(cave_exit_background, (0,0))  
    
            # Show texts
            congrats_text1 = font_large.render("You have survived the cave", True, BLACK)
            congrats_text2 = font_large.render("Now enjoy that treasure.", True, BLACK)
            congrats_rect1 = congrats_text1.get_rect(center=(screen_width // 2, 250))  
            congrats_rect2 = congrats_text2.get_rect(center=(screen_width // 2, 300))  
            window.blit(congrats_text1, congrats_rect1)  
            window.blit(congrats_text2, congrats_rect2)  

            # Create the Finish button
            button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 50, 100, 50)  # Button size and position
            pygame.draw.rect(window, BLACK, button_rect)  
            finish_text = font.render("Finish", True, WHITE)  
            finish_rect = finish_text.get_rect(center=button_rect.center)  
            window.blit(finish_text, finish_rect)  #

            # Show the victory coin image
            coin_y_offset = 30  # Make the coin higher on the screen
            coin_x = screen_width // 2
            coin_y = screen_height // 2 + 50 + coin_y_offset  
            window.blit(victory_coin_image, (coin_x - victory_coin_image.get_width() // 2, coin_y))  

            # Show how many coins were collected
            coin_count_text = font.render(f"Coins Collected: {coin_score}", True, BLACK)  # Coin count
            coin_count_rect = coin_count_text.get_rect(center=(screen_width // 2, coin_y + victory_coin_image.get_height() // 2 + 20))  
            window.blit(coin_count_text, coin_count_rect)  # Show the coin count

            # Show a message below the coin
            tax_message = font.render("Don't forget to pay your taxes with these winnings.", True, BLACK)  
            tax_message_rect = tax_message.get_rect(center=(screen_width // 2, coin_count_rect.bottom + 30))  
            window.blit(tax_message, tax_message_rect)  

            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        victory_screen = False  
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        victory_screen = False  

            pygame.display.update()  

    else:
        # If the boss wasn't defeated, show the game over screen
        game_over_screen = True

        while game_over_screen:
            window.blit(you_died_background_image, (0,0))  # Show death background
    
            # Show "You Died!" text
            death_text = font_large.render("You Died!", True, RED)
            death_text_rect = death_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
            window.blit(death_text, death_text_rect)

            # Ask the player what to do next
            prompt_text = font.render("What would you like to do?", True, WHITE)
            prompt_text_rect = prompt_text.get_rect(center=(screen_width // 2, screen_height // 2))
            window.blit(prompt_text, prompt_text_rect)

            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_over_screen = False  # Exit the game over screen

            # Show Restart and Exit buttons
            if restart_button.draw():
                play()  

            if exit_button.draw():
                time.sleep(0.5)  
                window.fill(BLACK)  
                window.blit(bye_img, (400,250))  # Show bye text
                pygame.display.update()  # Update the screen
                time.sleep(1)  # Wait 1 second
                game_over_screen = False  # Exit the game over screen

            # Update the screen
            pygame.display.update()

play()  


pygame.quit()
sys.exit()
