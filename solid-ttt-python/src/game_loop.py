from src.ttt_board import TTTBoard

class GameLoop():
  def __init__(self):
    self.board = TTTBoard(9)

  def run(self, terminal_interactor, ordered_players, rules_engine):
    while rules_engine.is_game_active(self.board):
      terminal_interactor.display_board(self.board)
      move_location = ordered_players[rules_engine.current_player_number(self.board)].get_next_move(self.board)
      current_team = rules_engine.current_player_mark(self.board)
      try:
        self.board.fill_space(move_location, current_team)
      except TTTBoard.TTTBoardError as e:
        pass

    terminal_interactor.display_board(self.board)
    winner = rules_engine.get_winner(self.board)
    terminal_interactor.say_goodbye(winner)
