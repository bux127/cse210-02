from hilo import Card 


class Play:
  """this is where the game get its controls and commands"""
  def __init__(self):
    """this constructs a play , creates a card object and creates attributes for the class, and also sets a boolean to check if the game is still running 
    """
    self.card = 0
    self.game_running = ''
    self.points = 0
    self.next_card = 0
    self.guess = ""
    
  
    
      
  def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Play): an instance of Play.
        """
        self.points = 300
        self.game_running = True


        while self.game_running:
            display_card = Card()
            self.card = display_card.current_card()
            self.next_card = display_card.next_card()

            self.print_card()

            self.get_input()
            self.update_points()

            if self.game_running == False:
                break

            self.play_again()
            
          
  def update_points(self):
        """A method that determines the score for the game
        """
        print ("Higher or lower? [h/l]".lower())
        if self.points > 0:
            if (self.card < self.next_card and self.guess == 'l') or (self.card > self.next_card and self.guess == 'h'):
              
                self.points -= 75
            else:
                self.points += 100

        else:
            self.points < 0
            self.game_running = False
          
  def get_input(self):
        """Ask the user to guess if the next card is higher or lower, and confirm the input is entered correctly (either "h" or "l" only).
        After the input, call the function current_card(self) and display a new card.
        Args:
        """

        while not True:
            
            self.guess = input('Higher or Lower [h/l]: ').lower()
            while not True:
                    display_card = Card()
                    self.card = display_card.current_card()
                    next_cd = Card()
                    self.next_card = next_cd.next_card()
                    if (self.card < self.next_card and self.guess == 'l') or (self.card > self.next_card and self.guess == 'h'):
                        continue
                    else:
                      if self.points < 0:
                        break

        print(f'Next card was: ',{self.guess_card})

            
  def play_again(self):
        """Ask the user if he wants to play again.
        Args:
            self (Play): an instance of Play.
        """

        play = input('Play again [y/n]: ')

        if play == 'y':
            self.is_playing = True
        else:
            self.is_playing = False
            