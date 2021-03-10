import pygame

class Settings:
    #class to store game settings
    def __init__(self):
        #initialize the game's settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_image = pygame.image.load("data/background.jpg")
        self.bg_color = (245, 241, 210)

        #cat settings
        self.cat_speed = 1.5
        self.cat_limit = 3

        #Laser settings
        self.laser_speed = 1.5
        self.laser_width = 3
        self.laser_height = 20
        self.laser_color = (255, 0, 0)
        self.lasers_allowed = 3


        #mouse settings
        self.mouse_speed = 1.0
        self.family_drop_speed = 10
        #fleet of directions of 1 represents right; -1 represents left
        self.family_direction = 1

        #how quickly the game speeds up
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #initialize settings that change within the game
        self.cat_speed = 1.5
        self.laser_speed = 3.0
        self.mouse_speed = 1.0

        #family direction
        self.family_direction = 1

        #scoring
        self.mouse_points = 50

    def increase_speed(self):
        #increase the speed settings within the game
        self.cat_speed *= self.speedup_scale
        self.laser_speed *= self.speedup_scale
        self.mouse_speed *= self.speedup_scale

        self.mouse_points = int(self.mouse_points * self.score_scale)