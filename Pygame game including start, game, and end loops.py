import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()       # This initializes all the imported pygame modules.

# To ensure we can replay the game, we insert everything into a function.
# When RESTART is clicked, we just call the function.

def play():
    # Initializing color variables for common colors.

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

    # Initializing fonts for text.
    font = pygame.font.SysFont("8514oem", 20)
    font_large = pygame.font.SysFont("8514oem", 50)

    # Initialize other variables.
    # Setting up a clock (FPS)
    clock = pygame.time.Clock()     # The function to use our variable to set FPS.
    frames_per_sec = 60        # The FPS we want the game to run at.

    moving_speed = 0        # Background Scroll speed variable
    collisions = 0          # To keep score of killed enemies
    coin_score = 0          # To keep score of collected coins
    current_level = 1       # To keep track of the current level
    boss_defeated = False   # Flag to indicate if boss is defeated

    # Initializing Images
    # Button images
    start_button_img = pygame.image.load("START.png").convert_alpha()
    exit_button_img = pygame.image.load("EXIT.png").convert_alpha()
    restart_button_img = pygame.image.load("RESTART.png").convert_alpha()
    # Enemy images
    ant_image = pygame.image.load("Ant.png").convert_alpha()
    # Backgrounds
    # Start Background
    start_background_image = pygame.image.load("cave.jpg").convert_alpha()
    start_rect = start_background_image.get_rect()

    # Game Background - Example only.
    background_image = pygame.image.load("golden_cave_background.png").convert_alpha()
    background_width = background_image.get_width()
    background_height = background_image.get_height()
    tiles = 3       # How many game background images for smooth screen movement.
 
     # Level 2 Background
    level2_background_image = pygame.image.load("large-deserted-cave-with-carved-entrance_1311536-6268.jpg").convert_alpha()
    level2_background_image = pygame.transform.scale(level2_background_image, (screen_width, screen_height))

# Level 3 Background
    level3_background_image = pygame.image.load("SpiderWebBackground.jpg").convert_alpha()
    level3_background_image = pygame.transform.scale(level3_background_image, (screen_width, screen_height))

    # Game-Over Background
    end_background_image = pygame.image.load("spiders.jpg").convert_alpha()
    end_rect = end_background_image.get_rect()
    # Text Images
    bye_img = font_large.render("See you next time", True, PURPLE)
    game_over_image = font_large.render("...GAME OVER...", True, BLUE)
    game_start_image = font_large.render("ADVENTURES OF HUBERT THE GAME", True, BLUE)

    # Load coin animation 
    coin_scale = 0.4  # make the coin smaller or larger
    walkCoin = [
        pygame.transform.scale(pygame.image.load("Coin1.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Coin2.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Coin3.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Coin4.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Coin5.png"), (int(100*coin_scale), int(100*coin_scale))),
        pygame.transform.scale(pygame.image.load("Coin6.png"), (int(100*coin_scale), int(100*coin_scale)))
    ]

    # Load bat animation 
    bat_scale = 0.6  # make the bat smaller or larger
    bat_images = [
        pygame.transform.scale(pygame.image.load("bat_1.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("bat_2.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("bat_3.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("bat_4.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("bat_5.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("bat_6.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("bat_7.png"), (int(100*bat_scale), int(50*bat_scale))),
        pygame.transform.scale(pygame.image.load("bat_8.png"), (int(100*bat_scale), int(50*bat_scale)))
    ]

    # Boss Spider Images

    # Spider Down images
    spider_down_images = [
        pygame.image.load("Spider_Down_1.png").convert_alpha(),
        pygame.image.load("Spider_Down_2.png").convert_alpha(),
        pygame.image.load("Spider_Down_3.png").convert_alpha(),
        pygame.image.load("Spider_Down_4.png").convert_alpha(),
        pygame.image.load("Spider_Down_5.png").convert_alpha(),
        pygame.image.load("Spider_Down_6.png").convert_alpha(),
    ]

    # Spider Left images
    spider_left_images = [
        pygame.image.load("Spider_Left_1.png").convert_alpha(),
        pygame.image.load("Spider_Left_2.png").convert_alpha(),
        pygame.image.load("Spider_Left_3.png").convert_alpha(),
        pygame.image.load("Spider_Left_4.png").convert_alpha(),
        pygame.image.load("Spider_Left_5.png").convert_alpha(),
        pygame.image.load("Spider_Left_6.png").convert_alpha(),
    ]

    # Spider Up images
    spider_up_images = [
        pygame.image.load("Spider_Up_1.png").convert_alpha(),
        pygame.image.load("Spider_Up_2.png").convert_alpha(),
        pygame.image.load("Spider_Up_3.png").convert_alpha(),
        pygame.image.load("Spider_Up_4.png").convert_alpha(),
        pygame.image.load("Spider_Up_5.png").convert_alpha(),
        pygame.image.load("Spider_Up_6.png").convert_alpha(),
    ]

    # Spider Right images
    spider_right_images = [
        pygame.image.load("Spider_Right_1.png").convert_alpha(),
        pygame.image.load("Spider_Right_2.png").convert_alpha(),
        pygame.image.load("Spider_Right_3.png").convert_alpha(),
        pygame.image.load("Spider_Right_4.png").convert_alpha(),
        pygame.image.load("Spider_Right_5.png").convert_alpha(),
        pygame.image.load("Spider_Right_6.png").convert_alpha(),
    ]

    # Boss shooting images
    boss_shoot_images = [
        pygame.image.load("Bossshoot1.png").convert_alpha(),
        pygame.image.load("Bossshoot2.png").convert_alpha(),
        pygame.image.load("Bossshoot3.png").convert_alpha(),
        pygame.image.load("Bossshoot4.png").convert_alpha(),
    ]

    # Drawing a grid on window for later.
    grid_size = 50     # Tile size for 'square' grid overlay.
    def grid():
        for line in range(0, 20):
            pygame.draw.line(window, BLACK, (0, line*grid_size),(screen_width, line*grid_size), 2)
            pygame.draw.line(window, BLACK, (line*grid_size, 0),(line*grid_size, screen_width), 2)

    # For later to add features to screen.
    background_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12 rows of 20 columns
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # All zeros for now
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Can be used for tile mapping
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # in the future
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
            """Draw onto surface with (x,y) coordinates. Determine if mouse click is on drawn button."""
            # Draw the image onto the screen at position rect.x and rect.y
            window.blit(self.image, (self.rect.x, self.rect.y))

            # Check for collision and click from mouse.
            clicked = False
            pos_mouse = pygame.mouse.get_pos()

            # Check if the mouse is over the button rect.
            if self.rect.collidepoint(pos_mouse):

                # Because the one click might return multiple "strikes",
                # we only want the first click to count.
                # We can set a flag for the first click, and ensure the if statement
                # is only true for that "un-raised flag" status

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
            self.image = pygame.image.load("hubert.png").convert_alpha()
            self.image.set_colorkey(WHITE)
            width = self.image.get_width()
            height = self.image.get_height()
            self.image = pygame.transform.scale(self.image, ((int(width * scale)), (int(height * scale))))
            self.rect = self.image.get_rect()
            self.missiles = []
            self.health = health
            self.jumping = False
            self.velocity = [0, 0]

        def move(self):
            pressed_keys = pygame.key.get_pressed()
            upwards_movement = 0
            # Move the sprite based on keyboard input.
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
            self.image = pygame.transform.scale(image, ((int(width * scale)), (int(height * scale))))
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
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
            self.image = missile_img_with_flip.convert_alpha()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect(center = (x, y))

        def update(self):
            self.rect.move_ip(5, 0)
            if self.rect.right > screen_width:
                self.kill()

    class Coin(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Coin, self).__init__()
            self.images = walkCoin
            self.index = 0
            self.animation_speed = 0.2
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

    class Bat(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Bat, self).__init__()
            self.images = bat_images
            self.index = 0
            self.animation_speed = 0.2
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
                self.kill()

    # Boss Spider class
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
            self.animation_speed = 0.3
            self.image = self.images[int(self.index)]
            self.rect = self.image.get_rect()
            self.rect.center = (screen_width - 100, screen_height // 2)  # Start at right side of screen
            self.speed = speed  # Adjust the speed of the boss spider here
            self.health = health  # Adjust the health of the boss spider here
            self.direction = random.choice(['up', 'down', 'left', 'right'])
            self.last_shot = pygame.time.get_ticks()
            self.shoot_cooldown = 3000  # Boss shoots every 5 seconds
            self.move_timer = pygame.time.get_ticks()
            self.move_delay = 1000  # Change direction every 1 second

        def update(self):

            self.index += self.animation_speed
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[int(self.index)]

            # Random movement 
            current_time = pygame.time.get_ticks()
            if current_time - self.move_timer > self.move_delay:
                self.direction = random.choice(['up', 'down', 'left', 'right'])
                self.move_timer = current_time

            if self.direction == 'up':
                self.rect.y -= self.speed
                self.images = self.images_up
            elif self.direction == 'down':
                self.rect.y += self.speed
                self.images = self.images_down
            elif self.direction == 'left':
                self.rect.x -= self.speed
                self.images = self.images_left
            elif self.direction == 'right':
                self.rect.x += self.speed
                self.images = self.images_right

            # Ensure the boss stays within the right-hand side of the screen
            if self.rect.left < screen_width // 2:
                self.rect.left = screen_width // 2
            if self.rect.right > screen_width:
                self.rect.right = screen_width
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height

            # Shooting
            if current_time - self.last_shot > self.shoot_cooldown:
                self.shoot()
                self.last_shot = current_time

        def shoot(self):
            boss_bullet = BossBullet(self.rect.centerx, self.rect.centery)
            all_sprites.add(boss_bullet)
            boss_bullets.add(boss_bullet)

        def draw_health(self, surf):
            # health bar above the boss
            health_rect = pygame.Rect(0, 0, 150, 10)  # Adjust the size of the health bar here
            health_rect.midbottom = self.rect.centerx, self.rect.top - 5
            max_health = 100  # Note: Adjust the max health of the boss spider here
            self.health_bar(surf, health_rect.topleft, health_rect.size, BLACK, RED, GREEN, self.health / max_health)

        def health_bar(self, surface, position, size, border_colour, background_colour, health_colour, remaining_health):
            pygame.draw.rect(surface, background_colour, (*position, *size))
            pygame.draw.rect(surface, border_colour, (*position, *size), 1)
            inner_position = (position[0] + 1, position[1] + 1)
            inner_rect = ((size[0] - 2) * remaining_health, size[1] - 2)
            rect = (round(inner_position[0]), round(inner_position[1]), round(inner_rect[0]), round(inner_rect[1]))
            pygame.draw.rect(surface, health_colour, rect)

    # Boss bullet 
    class BossBullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(BossBullet, self).__init__()
            # Load bullet images and animate them
            # Adjust bullet size here
            self.images = [pygame.transform.scale(img, (30, 30)) for img in boss_shoot_images]
            self.index = 0
            self.animation_speed = 0.1
            self.image = self.images[int(self.index)]
            self.rect = self.image.get_rect(center=(x, y))
            self.speed = 8  # Adjust bullet speed here

        def update(self):
            self.index += self.animation_speed
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[int(self.index)]
            # Move towards the player
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.kill()

    player = Player(health = 100, scale = .2)
    ant_enemy = Enemy(ant_image, .1, 4, 990, 420)

    start_button = Buttons(130, 435, start_button_img, scale = 0.5)
    exit_button = Buttons(510,435, exit_button_img, scale = 0.5)
    restart_button = Buttons(130, 435, restart_button_img, scale = 0.5)

    # Create groups for enemy(ies)

    enemies = pygame.sprite.Group()
    missiles = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    bats = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    boss_bullets = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()

    # Define user events.

    add_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(add_enemy, 500)

    add_coin = pygame.USEREVENT + 2
    pygame.time.set_timer(add_coin, 3000)

    add_bat = pygame.USEREVENT + 3
    pygame.time.set_timer(add_bat, 5000)

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
            window.blit(bye_img, (350,250))
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

        # Update background based on level.
        if current_level == 1:
            for i in range(0, tiles):
                window.blit(background_image, (i * background_width + moving_speed, 30))
            moving_speed -= .5
            if abs(moving_speed) > background_width:
                moving_speed = 0

        elif current_level == 2:
            window.blit(level2_background_image, (0, 0))  # No need for tiling if the image fits the screen

        elif current_level == 3:
            window.blit(level3_background_image, (0, 0))  # Level 3 background 

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
                    player.shoot()

            # Is the time right for a new enemy.
            elif event.type == add_enemy and current_level < 3:
                # Create the new enemy every 500 milliseconds, and add it to our sprite groups.
                ant_enemy = Enemy(ant_image, .1, 5, 990, 420)
                enemies.add(ant_enemy)
                all_sprites.add(ant_enemy)

            # Is the time right for a new coin.
            elif event.type == add_coin and current_level < 3:
                # Create a new coin every 3000 milliseconds.
                x = random.randint(screen_width + 50, screen_width + 100)
                y = random.randint(50, 350)
                coin = Coin(x, y)
                coins.add(coin)
                all_sprites.add(coin)

            # Is the time right for a new bat.
            elif event.type == add_bat and current_level < 3:
                # Only spawn a bat if there isn't one already
                if len(bats) == 0:
                    x = screen_width + 50
                    y = random.randint(0, 250)  # Above missile shooting height (adjust as needed)
                    bat = Bat(x, y)
                    bats.add(bat)
                    all_sprites.add(bat)

        # Player "update()" call.
        player.move()

        # Update the position of our enemies, coins, and bats.
        enemies.update()
        coins.update()
        bats.update()
        boss_bullets.update()

        # Add a Scorecard/healthbar/etc here
        player.draw_health(window)

        scores = font.render(f"SCORE: {collisions}", True, WHITE)
        coin_display = font.render(f"COINS: {coin_score}", True, WHITE)
        window.blit(scores, (10,10))
        window.blit(coin_display, (10,40))

        level_display = font.render(f"LEVEL: {current_level}", True, WHITE)
        window.blit(level_display, (10,70))

        # Level progression condition
        if collisions >= 10 and current_level == 1:
            current_level = 2

        elif collisions >= 20 and current_level == 2:
            current_level = 3
            # Initialize the boss spider
            boss_spider = BossSpider(health=100, speed=3, scale=0.5)  # Adjust speed and scale here
            all_sprites.add(boss_spider)
            boss_group.add(boss_spider)

        # Draw all our sprites
        for entity in all_sprites:
            window.blit(entity.image, entity.rect)

        if current_level == 3:
            boss_group.update()
            boss_spider.draw_health(window)
            boss_bullets.draw(window)

        for missile in player.missiles:
            missile.update()
            missiles.add(missile)
            if pygame.sprite.spritecollide(missile, enemies, True):
                missile.kill()
                missiles.remove(missile)
                player.missiles.remove(missile)
                collisions += 1

            # Check for collision with bats
            if pygame.sprite.spritecollide(missile, bats, True):
                missile.kill()
                missiles.remove(missile)
                player.missiles.remove(missile)
                collisions += 1

            # Check for collision with boss spider
            if current_level == 3 and pygame.sprite.spritecollide(missile, boss_group, False):
                missile.kill()
                missiles.remove(missile)
                player.missiles.remove(missile)
                # Reduce boss spider's health
                boss_spider.health -= 10  # Adjust damage value as needed

                
                if boss_spider.health <= 0:  # Check if boss spider is dead
                    boss_spider.kill()
                    boss_defeated = True
                    running = False  # Exit the game loop to show victory screen

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollide(player, enemies, dokill = True):
            # If so, subtract health.
            player.health -= 10

        # Check if any bats have collided with the player
        if pygame.sprite.spritecollide(player, bats, dokill = True):
            player.health -= 1  # Bat causes 1 damage

        # Check if any boss bullets have collided with the player
        if pygame.sprite.spritecollide(player, boss_bullets, dokill=True):
            # If so, subtract health.
            player.health -= 30  # Adjust damage from boss bullet here

        # Check if any coins have been collected by the player
        coins_collected = pygame.sprite.spritecollide(player, coins, dokill = True)
        if coins_collected:
            coin_score += len(coins_collected)

        if player.health <= 0:
            for entity in all_sprites:
                entity.kill()
            player.health = 100
            time.sleep(0.5)
            window.fill(RED)
            window.blit(game_over_image, (375,250))
            pygame.display.update()
            time.sleep(1)
            running = False

        # Update the display for each loop.
        pygame.display.update()

    # victory screen
    if boss_defeated:
        victory_screen = True
        while victory_screen:
            window.fill(GREEN)
            # message on the screen 
            congrats_text = font.render('Congratulations! You have survived the adventures of Hubert the game.', True, BLACK)
            congrats_rect = congrats_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
            window.blit(congrats_text, congrats_rect)

            
            button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2, 100, 50)
            pygame.draw.rect(window, BLACK, button_rect)
            finish_text = font.render('Finish', True, WHITE)
            finish_rect = finish_text.get_rect(center=button_rect.center)
            window.blit(finish_text, finish_rect)

            
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
        
        game_over_screen = True

        while game_over_screen:

            window.fill(RED)
            window.blit(game_over_image, (375,150))
            # Player killed and end game screen

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
