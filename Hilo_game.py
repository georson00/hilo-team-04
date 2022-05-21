import random
from select import select

class Hi_lo:
    """ Face cards create a game of guessing whether the next card will be higher or lower in value than the previously drawn card."""
    def __init__(self):
        self.cards_list = []
        
    def create_cards(self):
            for i in range(4):
                for i in range(1,14):
                    self.cards_list.append(i)

    def random_select(self):
        """To randomly select a card"""
        i = random.choice(self.cards_list) 
        self.cards_list.remove(i)
        return i