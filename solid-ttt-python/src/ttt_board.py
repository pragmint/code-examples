from src.board import Board

class TTTBoard(Board):
  valid_teams_list = ['X', 'O']

  class TTTBoardError(RuntimeError):
    pass

  def __init__(self, num_spaces):
    if num_spaces == 9:
      self.num_rows = 3
      self.num_cols = 3
      super().__init__(num_spaces)
    if num_spaces != 9: raise self.TTTBoardError("A TTTBoard can only be initialized with 9 spaces")

  def validate_move(fn):
    def func(*args):
      self, location, team = args
      self.validate_location(location)
      self.validate_team(team)
      self.validate_empty_space(location)
      return fn(*args)
    return func

  def validate_location(self, location):
    if not type(location) is int:
      raise self.TTTBoardError("Invalid Move")
    if location >= self.num_spaces or location < 0:
      raise self.TTTBoardError("Invalid Move")

  def validate_team(self, team):
    if team not in self.valid_teams_list:
      raise self.TTTBoardError("Invalid Team")

  def validate_empty_space(self, location):
    if self._board[location] != self.EMPTY_SPACE:
      raise self.TTTBoardError("Space '{0}' is already full".format(location))

  @validate_move
  def fill_space(self, location, team):
    super().fill_space(location, team)
