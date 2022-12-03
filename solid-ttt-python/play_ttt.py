from src.factory import Factory
from src.game_loop import GameLoop

[terminal_interactor, ordered_players, rules_engine] = Factory.stateless_objects()
GameLoop().run(terminal_interactor, ordered_players, rules_engine)
