import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    # A class to manage the lasers fired from the cat
    
    def __init__(self, cm_game):
        #Create a laser object at the cats current position
        super().__init__()
        self.screen = cm_game.screen
        self.settings = cm_game.settings
        self.color = self.settings.laser_color

        #Create a bullet rect at (0,0) and then set correct laser position
        self.rect = pygame.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        self.rect.midtop = cm_game.cat.rect.midtop

        #store the lasers position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
            #update the laser up the screen towards aliens
            self.y -= self.settings.laser_speed
            #update the rect position
            self.rect.y = self.y

    def draw_laser(self):
            #Draw the laser onto screen
            pygame.draw.rect(self.screen, self.color, self.rect)