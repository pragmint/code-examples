import unittest
from src.ttt_board import TTTBoard

class TestTTTBoard(unittest.TestCase):
  def setUp(self):
    self.board = TTTBoard(9)
    self.X = self.board.valid_teams_list[0]
    self.O = self.board.valid_teams_list[1]

  def test_a_ttt_board_can_only_have_9_spaces(self):
    try:
      self.board = TTTBoard(8)
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'A TTTBoard can only be initialized with 9 spaces')
    else:
      self.fail('BoardError not thrown when it should be')

  def test_a_ttt_board_is_square(self):
    self.assertNotEqual(None, self.board.num_rows)
    self.assertEqual(self.board.num_rows, self.board.num_cols)

  def test_an_empty_space_is_represented_by_an_empty_string(self):
    self.assertEqual('', self.board.EMPTY_SPACE)

  def test_by_default_there_are_only_two_teams_allowed_to_fill_spaces_on_this_board(self):
    self.assertTrue('X' in self.board.valid_teams_list)
    self.assertTrue('O' in self.board.valid_teams_list)

  def test_has_an_empty_board_by_default(self):
    self.assertEqual(0, len(self.board.to_dict()))

  def test_can_fill_spaces_on_the_board(self):
    self.board.fill_space(1, self.X)
    self.assertEqual({1: self.X}, self.board.to_dict())
    self.board.fill_space(0, self.O)
    self.assertEqual({1: self.X, 0: self.O}, self.board.to_dict())

  def test_knows_how_many_moves_have_been_made(self):
    self.assertEqual(0, self.board.num_full_spaces())
    self.board.fill_space(1, self.X)
    self.assertEqual(1, self.board.num_full_spaces())

  def test_can_erase_spaces_on_the_board(self):
    self.board.fill_space(1, self.X)
    self.board.erase_space(1)
    self.assertEqual(0, self.board.num_full_spaces())

  def test_can_only_fill_space_with_X_or_O(self):
    try:
      self.board.fill_space(1, 'invalid')
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Team')
    else:
      self.fail('BoardError not thrown when it should be')

  def test_can_only_fill_spaces_from_0_to_one_less_than_the_num_spaces_on_the_board(self):
    try:
      self.board.fill_space(-1, self.X)
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Move')
    else:
      self.fail('BoardError not thrown when it should be')

    try:
      self.board.fill_space(9, self.X)
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Move')
    else:
      self.fail('BoardError not thrown when it should be')

    try:
      self.board.fill_space('A', self.X)
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Move')
    else:
      self.fail('BoardError not thrown when it should be')

  def test_can_only_fill_an_empty_space(self):
    space = 1
    try:
      self.board.fill_space(space, self.X)
      self.board.fill_space(space, self.O)
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], "Space '{0}' is already full".format(space))
    else:
      self.fail('BoardError not thrown when it should be')

  def test_can_retrieve_space_contents(self):
    self.assertEqual('', self.board.space_contents(0), "We haven't set the space yet")
    self.board.fill_space(0, self.O)
    self.assertEqual(self.O, self.board.space_contents(0), "After we made a move")

  def test_doesnt_create_a_key_val_pair_on_inspection_of_a_missing_key_like_a_regular_default_dict_does(self):
    self.board.space_contents(0)
    self.assertEqual(0, self.board.num_full_spaces())

  def test_doesnt_throw_an_error_if_you_erase_a_non_existent_space(self):
    self.board.erase_space(0)
    self.assertEqual(0, self.board.num_full_spaces())

  def test_can_retrieve_the_board_in_dict_form(self):
    self.board.fill_space(4, self.X)
    self.board.fill_space(2, self.O)
    self.assertEqual({4: self.X, 2: self.O}, self.board.to_dict())
    self.board.fill_space(6, self.X)
    self.assertEqual({4: self.X, 2: self.O, 6: self.X}, self.board.to_dict())

  def test_returns_a_list_of_all_empty_spaces(self):
    self.board.fill_space(4, self.X)
    self.board.fill_space(2, self.O)
    self.assertEqual([0,1,3,5,6,7,8], self.board.empty_spaces())
