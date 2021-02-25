import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #set background color
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)
        #Initialize the ship

    def run_game(self):
        #Starts the main loop for game
        while True:
            self._check_events()
            self._update_screen()
            
            

    def _check_events(self):
        #watch for keyboard and mouse events
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
    
    def _update_screen(self):
        #redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and then run the game
    ai = AlienInvasion()
    ai.run_game()

