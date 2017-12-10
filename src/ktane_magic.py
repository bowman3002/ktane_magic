from puzzle import _PUZZLE_CLASS_DICT
from bomb_info import BombInfo
from game_input import game_input
from game_input import game_loop

#Games
import wires
import button

class Driver:
    def __init__(self):
        global _PUZZLE_CLASS_DICT
        self.puzzle_dict = {}
        for key in _PUZZLE_CLASS_DICT:
            self.puzzle_dict[key] = _PUZZLE_CLASS_DICT[key]()

    def run(self):
        self.bomb_info = BombInfo()
        self.bomb_info.read_data()

        with game_loop("KEEP TALKING AND NOBODY EXPLODES") as loop:
            while True:
                command = game_input("Enter name of the puzzle, 'help' to list puzzles, or ~ to return: ")
                if command == "help":
                    self.print_puzzles()
                elif command in self.puzzle_dict:
                    self.puzzle_dict[command].run(self.bomb_info)
                else:
                    print("Unknown puzzle")
                    self.print_puzzles()

    def print_puzzles(self):
        print("Puzzle List:")
        for key in self.puzzle_dict:
            print("    {}".format(key))

def main():
    driver = Driver()
    driver.run()

if __name__ == "__main__":
    main()
