from src.terminal_io import TerminalIO
from src.terminal_interactor import TerminalInteractor
from src.phrases import Phrases
from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer
from src.rules_engine import RulesEngine

class Factory():
  @staticmethod
  def stateless_objects():
    rules_engine = RulesEngine()
    terminal_interactor = TerminalInteractor(TerminalIO(), Phrases())
    human_first = terminal_interactor.human_first()
    human_player = HumanPlayer(terminal_interactor)
    computer_player = ComputerPlayer(rules_engine)

    return [terminal_interactor,
            Factory.correctly_ordered_players(human_first, human_player, computer_player),
            rules_engine]

  @staticmethod
  def correctly_ordered_players(human_first, human_player, computer_player):
    if human_first:
      return [human_player, computer_player]
    else:
      return [computer_player, human_player]
