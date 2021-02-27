import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #Class to manage the ship in AlienInvasion
    def __init__(self, ai_game):
        #Initialize the ship and set its starting position in the game
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image from file folder Images
        self.image = pygame.image.load("Images\ship.bmp")
        self.rect = self.image.get_rect()

        #start each ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #Movement Flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        #update the ship's position based on the movement flag in initial definiton
        #update the ship's s value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect value
        self.rect.x = self.x

    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)