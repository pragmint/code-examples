import unittest
from src.human_player import HumanPlayer

from src.terminal_interactor import TerminalInteractor
from src.board import Board

class MockTerminalInteractor(TerminalInteractor):
  def __init__(self):
    self.counter = 0
    self.moves = ["a", "blah", "-1", "4"]

  def get_move(self):
    current_move = self.moves[self.counter]
    self.counter = self.counter + 1
    return current_move

class TestHumanPlayer(unittest.TestCase):
  def test_does_not_stop_until_a_legal_move_has_been_selected(self):
    test_board = Board(9)
    test_terminal_interactor = MockTerminalInteractor()
    human_player = HumanPlayer(test_terminal_interactor)
    self.assertEqual(4, human_player.get_next_move(test_board))
