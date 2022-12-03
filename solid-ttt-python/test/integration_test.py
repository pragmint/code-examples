import unittest
from src.game_loop import GameLoop

from src.computer_player import ComputerPlayer
from src.human_player import HumanPlayer
from src.phrases import Phrases
from src.rules_engine import RulesEngine
from src.terminal_interactor import TerminalInteractor
from src.terminal_io import TerminalIO

class MockTerminalIO(TerminalIO):
  def __init__(self):
    self.input_calls = 0
    self.inputs = ["0", "8", "d", "7", "-1", "5"]
    self.prints = []

  def get(self, message):
    self.prints.append(message)
    return_val = self.inputs[self.input_calls]
    self.input_calls = self.input_calls + 1
    return return_val

  def print(self, message):
    self.prints.append(message)

  def print_with_clear(self, message):
    self.print(message)

class TestIntegration(unittest.TestCase):
  def setUp(self):
    self.rules_engine = RulesEngine()
    self.mock_terminal = MockTerminalIO()
    self.terminal_interactor = TerminalInteractor(self.mock_terminal, Phrases())

  def test_game_runs_until_it_is_over(self):
    GameLoop().run(self.terminal_interactor, [HumanPlayer(self.terminal_interactor), ComputerPlayer(self.rules_engine)], self.rules_engine)

    empty_board = "-------\n|0|1|2|\n-------\n|3|4|5|\n-------\n|6|7|8|\n-------\n"
    board_after_first_move = "-------\n|X|1|2|\n-------\n|3|4|5|\n-------\n|6|7|8|\n-------\n"
    game_over_message = "Congratulations O! You won!"

    self.assertEqual(empty_board, self.mock_terminal.prints[0])
    self.assertEqual(board_after_first_move, self.mock_terminal.prints[2])
    self.assertEqual(game_over_message, self.mock_terminal.prints[len(self.mock_terminal.prints)-1])
