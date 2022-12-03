import unittest
from src.terminal_interactor import TerminalInteractor

from src.ttt_board import TTTBoard
from src.terminal_io import TerminalIO
from src.phrases import Phrases

class MockTerminalIO(TerminalIO):
  def __init__(self, bool):
    self.counter = 0
    self.printed = ""
    if bool: self.inputs = ["a", "blah", "-1", "y"]
    if not bool: self.inputs = ["a", "blah", "-1", "n"]

  def get(self, prompt):
    current_input = self.inputs[self.counter]
    self.counter = self.counter + 1
    return current_input

  def print(self, message):
    self.printed = message

class TestTerminalInteractor(unittest.TestCase):
  def test_board_gets_displayed_properly(self):
    board = TTTBoard(9)
    io = TerminalInteractor(None, None)
    expected = "-------\n|0|1|2|\n-------\n|3|4|5|\n-------\n|6|7|8|\n-------\n"
    self.assertEqual(expected, io._board_to_str(board))

    board.fill_space(0, 'X')
    board.fill_space(7, 'O')
    expected = "-------\n|X|1|2|\n-------\n|3|4|5|\n-------\n|6|O|8|\n-------\n"
    self.assertEqual(expected, io._board_to_str(board))

  def test_when_human_wants_to_go_first(self):
    test_terminal = MockTerminalIO(True)
    io = TerminalInteractor(test_terminal, Phrases())
    self.assertEqual(True, io.human_first())

  def test_when_human_wants_to_go_second(self):
    test_terminal = MockTerminalIO(False)
    io = TerminalInteractor(test_terminal, Phrases())
    self.assertEqual(False, io.human_first())

  def test_say_winner_when_there_is_one(self):
    test_terminal = MockTerminalIO(None)
    phrases = Phrases()
    io = TerminalInteractor(test_terminal, phrases)
    winner = "whatever"

    io.say_goodbye(winner)

    self.assertEqual(phrases.goodbye(winner), test_terminal.printed)

  def test_say_tie_when_there_is_no_winner(self):
    test_terminal = MockTerminalIO(None)
    phrases = Phrases()
    io = TerminalInteractor(test_terminal, phrases)

    io.say_goodbye(None)

    self.assertEqual(phrases.goodbye_tie_game(), test_terminal.printed)
