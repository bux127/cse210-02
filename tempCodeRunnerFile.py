ets a boolean to check if the game is still running""" 
    self.game_running = True
    self.score = self.points
    
  def draw(self):
    print(f"The card is:", {self.current_card} )
      
  def play_game(self):
    card = Card()
    while not Tr