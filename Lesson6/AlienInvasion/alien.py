import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Class to represent a single alien in the fleet

    def __init__(self, ai_game):
        #initialize the alien and set its position
        super().__init__()
        self.screen =ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load("Images/alien.bmp")
        self.rect = self.image.get_rect()

        #start each new alien near the top left part of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position on the screen
        self.x = float(self.rect.x)

    def update(self):
        #move the alien to the right
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        #Checks to see if aliens are at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True