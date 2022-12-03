from collections import defaultdict

class Board():
  num_spaces = 0
  valid_teams_list = []
  EMPTY_SPACE = ''

  def __init__(self, num_spaces):
    self._board = defaultdict(str)
    self.num_spaces = num_spaces

  def fill_space(self, location, team):
    self._board[location] = team

  def erase_space(self, location):
    if location in self._board: self._board.pop(location)

  def space_contents(self, location):
    if location in self._board: return self._board[location]
    return self.EMPTY_SPACE

  def num_full_spaces(self):
    return len(self._board)

  def empty_spaces(self):
    empty_spaces = []
    for space in list(range(0,self.num_spaces)):
      if self.space_contents(space) == self.EMPTY_SPACE: empty_spaces.append(space)
    return empty_spaces

  def to_dict(self):
    return self._board.copy()
