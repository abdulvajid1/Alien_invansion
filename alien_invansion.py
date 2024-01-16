import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize the game and create a screen object.
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))
    pygame.display.set_caption('Alien Invansion')

    ship = Ship(screen)

    # Start the main loop for the game
    while True:

        # Watch for the user inputs ( keyboard and mouse event ).
        gf.check_events()
        # Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship)    
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()