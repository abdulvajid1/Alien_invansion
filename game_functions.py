import sys

import pygame

def check_events():
    "Responds to keypresses and mouse events."
    if event.type == Pygame.QUIT:
        sys.exit()

def update_screen(ai_settings,screen,ship):
    """Update images on the screen and flip to new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()