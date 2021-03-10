class GameStats:
    #Track game stats for the Cat and Mouse Game
    def __init__(self, cm_game):
        #initialize game stats
        self.high_score = 0
        self.settings = cm_game.settings
        self.reset_stats()


        #start CM in an active state
        self.game_active = False

    def reset_stats(self):
        #initialize stats that can change during gameplay
        self.cats_left = self.settings.cat_limit
        self.score = 0
        self.level = 1