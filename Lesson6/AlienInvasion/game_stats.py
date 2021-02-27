class GameStats:
    #Track game stats for Alien Invasion
    def __init__(self, ai_game):
        #initialize game stats
        self.high_score = 0
        self.settings = ai_game.settings
        self.reset_stats()


        #start Alien Invasion in an active state
        self.game_active = False

    def reset_stats(self):
        #initialize stats that can change during gameplay
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1