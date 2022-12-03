import imp
import unittest

from test.ttt_board_test import TestTTTBoard
from test.computer_player_test import TestComputerPlayer
from test.factory_test import TestFactory
from test.terminal_interactor_test import TestTerminalInteractor
from test.rules_engine_test import TestRulesEngine
from test.human_player_test import TestHumanPlayer
from test.integration_test import TestIntegration

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTTTBoard))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestComputerPlayer))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFactory))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTerminalInteractor))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRulesEngine))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHumanPlayer))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestIntegration))

    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
