class Roundcounter:


    def __init__(self, round, players, currentplayer):
        self.round = round
        self.players = players
        self.currentplayer = currentplayer

    def update_round(self):
        self.round += 1

    def update_current_player(self):
        if self.currentplayer + 1 > self.players:
            Roundcounter.update_round(self)
            self.currentplayer = 1
        else:
            self.currentplayer += 1

    def return_round(self):
        return self.round

    def return_currentplayer(self):
        return self.currentplayer

    def remove_player(self):
        self.players -=1

