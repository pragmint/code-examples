class RulesEngine():
  def __init__(self):
    self.WIN_SETS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

  def _set_is_controlled_by(self, board, win_set):
    teams_in_set = []
    for space in win_set:
      team_in_space = board.space_contents(space)
      if team_in_space != '': teams_in_set.append(team_in_space)
    if len(set(teams_in_set)) == 1 and len(teams_in_set) == len(win_set): return teams_in_set[0]
    return None

  def is_game_active(self, board):
    if board.num_full_spaces() == board.num_spaces: return False
    for win_set in self.WIN_SETS:
      if self._set_is_controlled_by(board, win_set) != None: return False
    return True

  def current_player_number(self, board):
    num_moves = board.num_full_spaces()
    num_teams = len(board.valid_teams_list)
    return num_moves % num_teams

  def current_player_mark(self, board):
    return board.valid_teams_list[self.current_player_number(board)]

  def get_winner(self, board):
    for win_set in self.WIN_SETS:
      if self._set_is_controlled_by(board, win_set) != None: return self._set_is_controlled_by(board, win_set)
