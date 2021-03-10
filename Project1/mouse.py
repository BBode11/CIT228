import pygame
from pygame.sprite import Sprite

class Mouse(Sprite):
    #Class to represent a single mouse in the family

    def __init__(self, cm_game):
        #initialize the mouse and set its position
        super().__init__()
        self.screen =cm_game.screen
        self.settings = cm_game.settings

        #load the mouse image and set its rect attribute
        self.image = pygame.image.load("data/mouse-icon.png")
        self.rect = self.image.get_rect()

        #start each new mouse near the top left part of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the mouse exact horizontal position on the screen
        self.x = float(self.rect.x)

    def update(self):
        #move the mouse to the right
        self.x += (self.settings.mouse_speed * self.settings.family_direction)
        self.rect.x = self.x

    def check_edges(self):
        #Checks to see if mouse are at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True