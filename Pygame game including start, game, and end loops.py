import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()       # This initialises all the imported pygame modules.

# To ensure we can replay the game, we insert everything into a function.
#       When RESTART is clicked, we just call the function.

def play():
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
    screen_width = 1000
    screen_height = 600
    window = pygame.display.set_mode((screen_width, screen_height))

    # Setting a caption name.
    pygame.display.set_caption("The Adventures of Hubert")

    # Initialising fonts for text.
    font = pygame.font.SysFont("8514oem", 20)
    font_large = pygame.font.SysFont("8514oem", 50)

        # Initialise other variables.
    # Setting up a clock (FPS) 
    clock = pygame.time.Clock()     # The funtion to use our variable to set FPS.
    frames_per_sec = 60        # The FPS we want the game to run at.

    moving_speed = 0        # Background Scroll speed variable
    collisions = 0          # To keep score of killed enemies

    # Initialising Images
        # Button images
    start_button = pygame.image.load("START.png").convert_alpha()
    exit_button = pygame.image.load("EXIT.png").convert_alpha()
    restart_button = pygame.image.load("RESTART.png").convert_alpha()
        # Enemy images
    ant_image = pygame.image.load("Ant.png").convert_alpha()
        # Backgrounds
    # Start Background
    start_background_image = pygame.image.load("cave.jpg").convert_alpha()
    start_rect = start_background_image.get_rect()
    # Game Background
    background_image = pygame.image.load("golden_cave_background.png").convert_alpha()
    background_width = background_image.get_width()
    background_height = background_image.get_height()
    tiles = 3       # How many game background images for smooth screen movement.
    # Game-Over Background
    end_background_image = pygame.image.load("spiders.jpg").convert_alpha()
    end_rect = end_background_image.get_rect()
    # Text Images
    bye_img = font_large.render("Goodbye", True, PURPLE)
    game_over_image = font_large.render("...GAME OVER...", True, BLUE)
    game_start_image = font_large.render("The Adventures of Hubert the game", True, BLUE)

    # Drawing a grid on window for later.
    grid_size = 50     # Tile size for 'square' grid overlay.
    def grid():
        for line in range(0, 20):
            pygame.draw.line(window, BLACK, (0, line*grid_size),(screen_width, line*grid_size), 2)
            pygame.draw.line(window, BLACK, (line*grid_size, 0),(line*grid_size, screen_width), 2)

    # For later to add features to screen.
    background_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

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
            window.blit(self.image, (self.rect.x, self.rect.y))

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
        def __init__(self, health, scale):
            super(Player, self).__init__()
            self.surf = pygame.image.load("hubert.png").convert_alpha()
            self.surf.set_colorkey(WHITE)
            width = self.surf.get_width()
            height = self.surf.get_height()
            self.surf = pygame.transform.scale(self.surf, ((int(width * scale)), (int(height * scale))))
            self.rect = self.surf.get_rect()
            self.missiles = []
            self.health = health

        def move(self):
            pressed_keys = pygame.key.get_pressed()
            # Move the sprite based on keyboard input.
            if pressed_keys[K_UP]:      # If K_UP is in 'list' of pressed_keys.
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
            elif self.rect.right > screen_width:
                self.rect.right = screen_width
            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= 420:
                self.rect.bottom = 420

        # HealthBar
        def health_bar(self, surface, position, size, border_colour, background_colour, health_colour, remaining_health):
            pygame.draw.rect(surface, background_colour, (*position, *size))
            pygame.draw.rect(surface, border_colour, (*position, *size), 1)
            inner_position  = (position[0]+1, position[1]+1)
            inner_rect = ((size[0]-2) * remaining_health, size[1]-2)
            rect = (round(inner_position[0]), round(inner_position[1]), round(inner_rect[0]), round(inner_rect[1]))
            pygame.draw.rect(surface, health_colour, rect)

        def draw_health(self, surf):
            health_rect = pygame.Rect(0, 0, 100, 7)
            health_rect.midbottom = self.rect.centerx, self.rect.top
            max_health = 100
            self.health_bar(surf, health_rect.topleft, health_rect.size, BLACK, RED, GREEN, self.health/max_health)
        
        def shoot(self):
            missile = Weapon(self.rect.centerx, self.rect.bottom)
            self.missiles.append(missile)
            all_sprites.add(missile)

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, image, scale, speed, x, y):
            super(Enemy, self).__init__() 
            width = image.get_width()
            height = image.get_height()
            self.surf = pygame.transform.scale(image, ((int(width * scale)), (int(height * scale))))
            self.surf.set_colorkey(WHITE)
            self.rect = self.surf.get_rect()
            self.rect.center = (x, y)       # For now, the ant is generated, and then it generates closer and closer to the LHS.
            self.speed = speed

        def update(self):       
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()

    class Weapon(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Weapon, self).__init__()
            missile_img = pygame.image.load('missile.png').convert_alpha()
            missile_img_copy = missile_img.copy()
            # pygame.transform.flip() will flip the image 
            missile_img_with_flip = pygame.transform.flip(missile_img_copy, True, False)
            self.surf = missile_img_with_flip.convert_alpha()
            self.surf.set_colorkey(WHITE)
            self.rect = self.surf.get_rect(center = (x, y))

        def update(self):
            self.rect.move_ip(5, 0)
            if self.rect.right > screen_width:
                self.kill()
    
    """
    class Collectible:
        ""Collectibles are given values here.""
        def __init__(self, label: str, add_points: int, add_health: int, add_lives: int,) -> None:
            self.label = label
            self.add_points = add_points
            self.add_health = add_health
            self.add_lives = add_lives
    """
    # Initialise instances of class objects.

    player1: Player = Player(health = 100, scale = .2)
    ant_enemy: Enemy = Enemy(ant_image, .1, 5, 990, 420)

    #boss_enemy: Enemy = Enemy()

    start_button: Buttons = Buttons(130, 435, start_button, scale = 0.5)
    exit_button: Buttons = Buttons(510,435, exit_button, scale = 0.5)
    restart_button: Buttons = Buttons(130, 435, restart_button, scale = 0.5)

    # coin: Collectible = Collectible("Coin", add_points = 10, add_health = 0, add_lives = 0)
    # fruit: Collectible = Collectible("Fruit", add_points = 0, add_health = 20, add_lives = 0)
    # heart: Collectible = Collectible("Heart", add_points = 0, add_health = 0, add_lives = 1)

    # Create groups for enemy(ies), player(s) etc.

    enemies = pygame.sprite.Group()
    missiles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)

    """
    # Define user events. (EXAMPLES)
    enemy_speed_increase = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_speed_increase, 1000)
    """

    add_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(add_enemy, 500)


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

        # Start the Loops
    # Create the start page loop.
    start_loop = True
    while start_loop:
        window.fill(WHITE)

        # Draw the background image to the screen.
        window.blit(start_background_image, (260, 100))

        window.blit(game_start_image, (175,30))

        # Check for close or escape event.
        for event in pygame.event.get():
            # First define an exit strategy for the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # End the first loop, The Start Page, and move on to next loop.
        if start_button.draw():
            start_loop = False

            # Quit the application.
        if exit_button.draw():
            time.sleep(.5)
            window.fill(BLACK)
            window.blit(bye_img, (400,250))
            pygame.display.update()
            time.sleep(1.5)
            pygame.quit()
            sys.exit()

        # Update the display for each loop.
        pygame.display.update()

                                        # Create the main game loop (level1).
    running = True
    while running:

        # Set a frame rate for the game.
        clock.tick(frames_per_sec)
        window.fill(BLACK)

        # Update and render background.
        for i in range(0, tiles):
            window.blit(background_image, (i * background_width + moving_speed, 30))

        moving_speed -= .5

        if abs(moving_speed) > background_width:
            moving_speed = 0

        # Draw the grid over the screen.
        grid()

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

            # Is the time right for a new enemy.
            elif event.type == add_enemy:
                # Create the new enemy every 500Milisecs, and add it to our sprite groups.
                ant_enemy = Enemy(ant_image, .1, 5, 990, 420)
                enemies.add(ant_enemy)
                all_sprites.add(ant_enemy)

        # Player "update()" call.
        player1.move()

        # Update the position of our enemies.
        enemies.update()

        # Add a Scorecard/healthbar/etc here (example)
        player1.draw_health(window)

        scores = font.render(f"SCORE: {collisions}", True, WHITE)
        window.blit(scores, (10,10))

        # Draw all our sprites
        for entity in all_sprites:
            window.blit(entity.surf, entity.rect)

        for missile in player1.missiles:
                missile.update()
                missiles.add(missile)
                if pygame.sprite.spritecollide(missile, enemies, True):
                    missile.kill()
                    missiles.remove(missile)
                    player1.missiles.remove(missile)
                    collisions += 1

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollide(player1, enemies, dokill = True):
            # If so, kill missile and subtract health.
            player1.health -= 10

        if player1.health <= 0:         
            for entity in all_sprites:
                entity.kill()
            player1.health = 100
            time.sleep(0.5)               
            window.fill(RED)
            window.blit(game_over_image, (375,250)) 
            pygame.display.update()
            time.sleep(1)
            running = False
        
        # Update the display for each loop.
        pygame.display.update()

                                    # Create the final game-over page loop.
    game_over_screen = True

    while game_over_screen:
        
        window.fill(RED)
        window.blit(game_over_image, (375,150))
        # Player killed and end game screen (example)

        # Check all events.
        for event in pygame.event.get():
            # First define an exit strategy for the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_over_screen = False

        if restart_button.draw():
            play()

        if exit_button.draw():
            time.sleep(.5)
            window.fill(BLACK)
            window.blit(bye_img, (400,250))
            pygame.display.update()
            time.sleep(1)
            game_over_screen = False
        
        pygame.display.update()

play()

# End game call here.
pygame.quit()
sys.exit()