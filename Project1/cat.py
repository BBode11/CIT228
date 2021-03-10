import pygame
from pygame.sprite import Sprite

class Cat(Sprite):
    #A class to manage the cat
    def __init__(self, cm_game):
        #initialize the cat and set its starting position
        super().__init__()
        self.screen = cm_game.screen
        self.settings = cm_game.settings
        self.screen_rect = cm_game.screen.get_rect()

        #load the cat image and get its rect
        self.image = pygame.image.load("data/cat.png")
        self.rect = self.image.get_rect()

        #start each new cat at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

         #store a decimal value for cats horizontal position
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        #draw the cat
        self.screen.blit(self.image, self.rect)

    def update(self):
        #update cat position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.cat_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.cat_speed

        #update rect
        self.rect.x = self.x

    def center_cat(self):
        #center the cat on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)