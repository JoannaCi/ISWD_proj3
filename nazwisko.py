import numpy as np
from player import Player

class Nazwisko(Player):   
    ### player's random strategy
    def putCard(self, declared_card):
        ### check if must draw
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        if declared_card is None and len(self.cards) >= 1:
            return min(self.cards, key=lambda x: x[0]), min(self.cards, key=lambda x: x[0])
        if declared_card is not None and len(self.cards) >= 1 and any(card[0] >= declared_card[0] for card in self.cards):
            return min((card[0], card[1]) for card in self.cards if card[0] >= declared_card[0]), min((card[0], card[1]) for card in self.cards if card[0] >= declared_card[0])
        if declared_card is not None and len(self.cards) >= 1 and not any(card[0] >= declared_card[0] for card in self.cards):
            return 'draw'
    def checkCard(self, opponent_declaration):
        if opponent_declaration in self.cards:
            return True
        if len(self.cards)>=1 and len(self.cards)<=4 and any(card[0] < opponent_declaration[0] for card in self.cards):
            return True
        return False