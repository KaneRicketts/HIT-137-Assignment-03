To create a clickable button in Pygame, you can use the following steps:

Create a surface for the button. The surface should be the size and shape of the button.
Either:
Create a rectangle from pygame.image.get() ...

Or:
Create a font object
font = pygame.font.Font(None, 24)
Then create a surface for the button
button_surface = pygame.Surface((150, 50))

Draw the button’s text and border on the surface.
text = font.render("Click Me", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, 
                                  button_surface.get_height()/2))
Show the button text
button_surface.blit(text, text_rect)

Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect(125, 125, 150, 50)  # Adjust the position as needed

Draw the button on the screen
screen.blit(button_surface, (button_rect.x, button_rect.y))

Create a pygame.event.MOUSEBUTTONDOWN event handler that checks if the mouse is clicked inside the button’s boundaries.

Check for the mouse button down event
if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

if button_rect.collidepoint(event.pos):
    print("Button clicked!")

Call the pygame.display.update() function to display the button on the screen.
