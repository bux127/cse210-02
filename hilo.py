import random

class  Card:
  """a class declaration with the name Card that will be on the object to be called """
  def __init__(self):
    """this is a constructor method that will initialise the starting points to 300 and the current card to any given integer and 
    """
    self.current_card = 0
    self.next_card = 0 
  def current_card(self):
    """This function prints a random current card .
        """
    self.current_card = random.randint(1, 13)

    print(f"The card is:'", {self.current_card})

  def next_card(self):
    """This function prints a random current card .
        """
    self.next_card = random.randrange(1, 13)

    print(f"Next card was:'", {self.next_card})
    
    
