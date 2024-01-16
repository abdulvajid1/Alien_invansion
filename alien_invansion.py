import sys
import pygame

from settings import Settings

def run_game():
    # Initialize the game and create a screen object.
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))
    pygame.display.set_caption('Alien Invansion')

    # Start the main loop for the game
    while True:

        # Watch for the user inputs ( keyboard and mouse event ).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
                
        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()