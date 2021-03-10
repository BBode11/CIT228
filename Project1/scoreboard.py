import pygame.font
from pygame.sprite import Group

from cat import Cat

class Scoreboard:

    def __init__(self, cm_game):
        #initialize attributes
        self.cm_game = cm_game
        self.screen = cm_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = cm_game.settings
        self.stats = cm_game.stats

        #font settings for the scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the intial score to be an image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_cats()

    def prep_cats(self):
        #show how many cats are left
        self.cats = Group()
        for cat_number in range(self.stats.cats_left):
            cat = Cat(self.cm_game)
            cat.rect.x = 10 + cat_number * cat.rect.width
            cat.rect.y = 10
            self.cats.add(cat)

    def prep_level(self):
        #turn level into image
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        #turn high score into image
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #center the high score at the top of the screen 
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        #turn score into an image
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #display the score near the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #add score to screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.cats.draw(self.screen)

    def check_high_score(self):
        #check for a new high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()