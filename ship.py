import pygame

class Ship():
    """this class manage all the configaration of User ship."""

    def __init__(self,screen) -> None:
        """initilize the ship and set its starting Postition."""
        self.screen = screen        

        # Load the ship images and get its react.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom centre of screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)