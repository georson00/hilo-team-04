
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.cards = Card()
        self.card_current = 0
        self.second_card = 0
        self.point = 300
        self.ask_guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_current_card()
            self.get_second_card()
            self.guess_card()
            self.get_play_again()

        print("Thank you for playing.")
    def get_current_card(self):
        """Get use's current card

        Args:
            self (Director): An instance of Director.
        """
        self.cards.get_cards()
        self.card_current = self.cards.current_card
        print(f"The card is: {self.card_current}")

    def get_second_card(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.ask_guess = input("Higher or Lower? [h/l]")
        self.second_card = self.cards.card_to_guess
        print(f"The next card was: {self.second_card}")

    def guess_card(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        

    def play_again()
