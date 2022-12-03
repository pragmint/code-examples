class ComputerPlayer():
  def __init__(self, rules_engine):
    self.rules = rules_engine

  def random_move(self, low, high, board):
    import random
    move = random.randint(low, high)
    return board.empty_spaces()[move]

  def get_next_move(self, board):
    max_depth = 7
    def _minimax(current_depth, minimax_vals_for_depth):
      if current_depth >= max_depth: return 0
      if not self.rules.is_game_active(board):
        if self.rules.get_winner(board) == None:
          return 0
        return -1

      for space in board.empty_spaces():
        board.fill_space(space, self.rules.current_player_mark(board))
        minimax_vals_for_depth[space] = -1 * _minimax(current_depth+1, {})
        board.erase_space(space)

      best_move = max(minimax_vals_for_depth, key=minimax_vals_for_depth.get)
      if current_depth == 0:
        return best_move
      return minimax_vals_for_depth[best_move]

    if board.num_full_spaces() == 0: return self.random_move(0, len(board.empty_spaces())-1, board)
    return _minimax(0, {})
