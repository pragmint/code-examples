import unittest
from src.rules_engine import RulesEngine

from src.board import Board
from collections import defaultdict

class TestBoard(Board):
  valid_teams_list = ['X', 'O']
  def set_board(self, board_data):
    self._board = defaultdict(str, board_data)

class TestRulesEngine(unittest.TestCase):
  def setUp(self):
    self.rules = RulesEngine()
    self.board = TestBoard(9)
    self.X = self.board.valid_teams_list[0]
    self.O = self.board.valid_teams_list[1]

  def test_game_ends_if_the_board_is_full(self):
    self.assertEqual(True, self.rules.is_game_active(self.board))
    self.board.set_board({0: self.X, 1: self.O, 2: self.X, 3: self.O, 4: self.X, 5: self.O, 6: self.X, 7: self.O, 8: self.X})
    self.assertEqual(False, self.rules.is_game_active(self.board))

  def test_game_ends_if_a_team_controls_a_win_set(self):
    self.assertEqual(True, self.rules.is_game_active(self.board))
    self.board.set_board({0: self.X, 1: self.X, 2: self.X})
    self.assertEqual(False, self.rules.is_game_active(self.board))
    self.board.set_board({2: self.O, 4: self.O, 6: self.O})
    self.assertEqual(False, self.rules.is_game_active(self.board))

  def test_player_0_gets_the_first_turn(self):
    self.assertEqual(0, self.rules.current_player_number(self.board))

  def test_player_0_and_player_1_alternate_turns(self):
    self.board.set_board({1: self.X})
    self.assertEqual(1, self.rules.current_player_number(self.board))
    self.board.set_board({1: self.X, 5: self.O})
    self.assertEqual(0, self.rules.current_player_number(self.board))

  def test_player_0_is_X(self):
    self.assertEqual(self.X, self.rules.current_player_mark(self.board))

  def test_either_one_team_wins_or_no_teams_win(self):
    self.assertEqual(None, self.rules.get_winner(self.board))
    self.board.set_board({0: self.X, 1: self.X, 2: self.X})
    self.assertEqual(self.X, self.rules.get_winner(self.board))
    self.board.set_board({2: self.O, 4: self.O, 6: self.O})
    self.assertEqual(self.O, self.rules.get_winner(self.board))
