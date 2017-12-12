from game_input import game_input
from game_input import game_loop
from puzzle import puzzle

@puzzle("Memory")
class Memory:
    def __init__(self):
        self.name = "Memory"

    def run(self, bomb_info):
        