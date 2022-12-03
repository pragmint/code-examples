class TerminalInteractor():
  def __init__(self, terminal, phrases):
    self.terminal = terminal
    self.phrases = phrases

  def human_first(self):
    while True:
      go_first = self.terminal.get(self.phrases.go_first())
      if go_first == "y": return True
      if go_first == "n": return False

  def display_board(self, board):
    self.terminal.print_with_clear(self._board_to_str(board))

  def _board_to_str(self, board):
    def _space_to_str(space_number):
      space = board.space_contents(space_number)
      if space == board.EMPTY_SPACE: return '{0}'.format(space_number)
      return space

    output = "-------\n"
    for row in iter(range(0, board.num_rows)):
      output += "|"
      for col in iter(range(0, board.num_cols)):
        space_number = (3 * row) + col
        output += "{0}|".format(_space_to_str(space_number))
      output += "\n-------\n"

    return output

  def say_goodbye(self, winner):
    if winner == None:
      self.terminal.print(self.phrases.goodbye_tie_game())
    else:
      self.terminal.print(self.phrases.goodbye(winner))

  def get_move(self):
    return self.terminal.get(self.phrases.next_move())
