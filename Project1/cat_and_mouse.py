import sys
from time import sleep

import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from cat import Cat
from laser import Laser
from mouse import Mouse


class CatAndMouse:
    #Overall class to manage game assets and behavior
    def __init__(self):
        #initialize game and create game resources
        pygame.init()
        self.settings = Settings()
  
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Cat and Mouse Game")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.cat = Cat(self)
        self.lasers = pygame.sprite.Group()
        self.mice = pygame.sprite.Group()

        self._create_family()

        #create button
        self.play_button = Button(self, "Play")


    def run_game(self):
        #start the main loop of the game
        while True:
        #Watch for keyboard and mouse events
           self._check_events()

           if self.stats.game_active:
                self.cat.update()
                self._update_lasers()
                self._update_mice()

           self._update_screen()

    def _check_events(self):
        #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    #movements of cat
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)   

    def _check_keydown_events(self, event):
        #Respond to keypresses
            if event.key == pygame.K_RIGHT:
                self.cat.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.cat.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_laser()

    def _check_keyup_events(self, event):
        #Respone to key releases
         if event.key == pygame.K_RIGHT:
               self.cat.moving_right = False
         elif event.key == pygame.K_LEFT:
               self.cat.moving_left = False



    def  _fire_laser(self):
        #create a new laser and add it to the laser group
        if len(self.lasers) < self.settings.lasers_allowed:
            new_laser = Laser(self)
            self.lasers.add(new_laser)

    def _update_lasers(self):
        #update laser position and get rid of old lasers
         self.lasers.update()

 #get rid of lasers that have disappeared.
         for laser in self.lasers.copy():
             if laser.rect.bottom <= 0:
                 self.lasers.remove(laser)

         self._check_laser_mouse_collisions()


    def _check_laser_mouse_collisions(self):
        collisions = pygame.sprite.groupcollide(self.lasers, self.mice, True, True)
        
        if collisions:
            for mice in collisions.values():
                self.stats.score += self.settings.mouse_points * len(mice)
                self.sb.prep_score()
                self.sb.check_high_score()

        if not self.mice:
            #destroy exisitng lasers and create a new family
            self.lasers.empty()
            self._create_family()
            self.settings.increase_speed()

        #increase levels
            self.stats.level += 1
            self.sb.prep_level()

    def _cat_hit(self):
        #response for cat being hit by mouse
        #remove a cat
        if self.stats.cats_left > 0:

            self.stats.cats_left -= 1
            self.sb.prep_cats()

            #get rid of any remaining mice or lasers
            self.mice.empty()
            self.lasers.empty()

            #create a new family and center the cat on the screen
            self._create_family()
            self.cat.center_cat()

            #add a pause 
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_family(self):
       #create a family of mice
        #create a mouse and find the number of mice in a row
        #spacing between each mouse is equal to one mouse width
        mouse = Mouse(self)
        mouse_width, mouse_height = mouse.rect.size
        available_space_x = self.settings.screen_width - (2 * mouse_width)
        number_mice_x = available_space_x // (2 * mouse_width)

        #determine the number of rows of mice that fit onto the game screen
        cat_height = self.cat.rect.height
        available_space_y = (self.settings.screen_height - (3 * mouse_height) - cat_height)
        number_rows = available_space_y // (2 * mouse_height)

        #Create the full family of mice
        for row_number in range(number_rows):
            for mouse_number in range (number_mice_x):
                self._create_mouse(mouse_number, row_number)

    def _create_mouse(self, mouse_number, row_number):
         mouse = Mouse(self)
         mouse_width, mouse_height = mouse.rect.size
         mouse.x = mouse_width + 2 * mouse_width * mouse_number
         mouse.rect.x = mouse.x
         mouse.rect.y = mouse.rect.height + 2 * mouse.rect.height * row_number
         self.mice.add(mouse)

    def _check_family_edges(self):
        #Response for when mice reach the edge of the screen
        for mouse in self.mice.sprites():
            if mouse.check_edges():
                self._change_family_direction()
                break

    def _check_mice_bottom(self):
        #Check if any mice hit the bottom of the screen
        screen_rect = self.screen.get_rect()
        for mouse in self.mice.sprites():
            if mouse.rect.bottom >= screen_rect.bottom:
                #cat was hit
                self._cat_hit()
                break

    def _change_family_direction(self):
        #Drop the entire family and change directions
        for mouse in self.mice.sprites():
            mouse.rect.y += self.settings.family_drop_speed
        self.settings.family_direction *= -1

    def _update_mice(self):
        #update the positon of ALL mice
        self._check_family_edges()
        self.mice.update()

        #look for collisions
        if pygame.sprite.spritecollideany(self.cat, self.mice):
            self._cat_hit()

        self._check_mice_bottom()

    
    def _update_screen(self):
        #update images on screen and flip to new screen
        self.screen.blit(self.settings.background_image, [0,0])
        self.cat.blitme()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        self.mice.draw(self.screen)

        #draw score info
        self.sb.show_score()

        #Draw play button
        if not self.stats.game_active:
            self.play_button.draw_button()

            #make the most recently drawn screen visible
        pygame.display.flip()

    def _check_play_button(self, mouse_pos):
        #start a new game when the player clicks the mouse
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #reset game
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_cats()

            #get rid of screen elements
            self.mice.empty()
            self.lasers.empty()

            #create a new family and center cat
            self._create_family()
            self.cat.center_cat()



if __name__ == '__main__':
    #make a game instance and run the game
    cm = CatAndMouse()
    cm.run_game()