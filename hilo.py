import random

class  Card:
  """a class declaration with the name Card that will be on the object to be called """
  def __init__(self):
    """this is a constructor method that will initialise the starting points to 300 and the current card to any given integer and 
    card_select to a random range of 1 to 13"""
    self.current_card = random.randrange(1, 13)
    self.points = 300
    self.next_card = random.randint(1, 13)
    self.guess = input('')
    
    def card_predict(self):
      answer = int(input(""))
      """this is a method that tells whats happens on the next predicted card be it lower or higher"""
      
      while self.guess != self.next_card:
        if self.guess <  self.next_card:
          print (f"Next card was", {self.next_card})
          self.points -= 75
          
        elif self.guess > self.next_card:
          print (f"Next card was", {self.next_card}) 
          self.points -= 75
          
      else:
          self.points += 100
          