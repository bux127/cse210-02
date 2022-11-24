from game.hilo import Card 

class Play:
  """this is where the game get its controls and commands"""
  def __init__(self):
    """this constructs a play , creates a card object and creates attributes for the class, and also sets a boolean to check if the game is still running"""
    self.card = Card() 
    self.game_running = True
    self.score = self.points
    
  def draw(self):
    print(f"The card is:", {self.current_card} )
      
  def play_game(self):
    print("Higher or Lower? [h/l]")
    return self.card
    print("Play again? [y/n]")
    if answer == y:
      return self.card
    else:
      return self.score
      
  
          
