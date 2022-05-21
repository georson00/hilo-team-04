"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""
from Hilo_game import Hi_lo

print()
print("Welcome to HiLo Games!!!")
print("Games by Team04")
print()

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
        self.hilo= Hi_lo() 
        self.card_list = self.hilo.create_cards()
        self.guess = ""
        self.previous_card =  self.hilo.random_select()
        self.is_playing = True
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.
        Args:
            self (Director): An instance of Director.
        """
        
        playing = input("Would you like to play?\n:Y/N\n:")
        if playing.lower() =="n":
            self.is_playing = False
            print("Thank you for playing.")

        elif playing.lower() =="y":
            print(f"The card is {self.previous_card}.")
            self.guess= input("What will be the next card, Is it higher or lower?\n:H/L \n:")

        else:
            print("Incorrect reponse selected. Please select a correct response: y or n") 
            self.is_playing = (playing == "y")   

    def do_updates(self):
        """Updates the player's score.
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        card = self.hilo.random_select()

        print(f"The previous card was {self.previous_card}.\nThe new card is {card}.")

        if card > self.previous_card:
            if self.guess.lower() in "h":
                print("You guessed it correctly and you earned 100 points!")
                self.total_score += 100
            else:
                print("Sorry you guessed it incorrectly and you lose 75 points.")
                self.total_score -= 75
        elif card < self.previous_card:
            if self.guess.lower() in "l":
                print("You guessed correct and earned 100 points!")
                self.total_score += 100
            else:
                print("Sorry you guessed incorrectly and lose 75 points.")
                self.total_score -= 75
        else:
            print("The cards were the same you lose 75 points.")
            self.total_score -= 75
        self.previous_card = card
        
       

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your total score is {self.total_score}.")
        self.is_playing == (self.total_score > 0)

        
