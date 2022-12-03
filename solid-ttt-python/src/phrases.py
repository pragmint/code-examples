class Phrases():
  def go_first(self):
    return "Would you like to go first? [y/n] "

  def goodbye(self, winner):
    return "Congratulations {0}! You won!".format(winner)

  def next_move(self):
    return "Enter your next move: [0-8] "

  def goodbye_tie_game(self):
    return "Tie game!"
