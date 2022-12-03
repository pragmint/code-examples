import os

class TerminalIO():
  def get(self, message):
    return input(message)

  def print(self, message):
    print(message)

  def print_with_clear(self, message):
    os.system('clear')
    print(message)
