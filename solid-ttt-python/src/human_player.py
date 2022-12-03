class HumanPlayer():
  def __init__(self, terminal_interactor):
    self.terminal_interactor = terminal_interactor

  def get_next_move(self, board):
    while True:
      try:
        move = int(self.terminal_interactor.get_move())
        for available_space in board.empty_spaces():
          if available_space == move: return move
      except ValueError as e:
        pass
