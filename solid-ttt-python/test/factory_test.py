import unittest
from src.factory import Factory

class TestFactory(unittest.TestCase):
  def test_correct_ordering(self):
    expectedTrue = [1, 2]
    expectedFalse = [2, 1]
    self.assertEqual(expectedTrue, Factory.correctly_ordered_players(True, 1, 2))
    self.assertEqual(expectedFalse, Factory.correctly_ordered_players(False, 1, 2))
