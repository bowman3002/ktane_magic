from puzzle import _PUZZLE_CLASS_DICT
from bomb_info import BombInfo

#Games
import wires

class Driver:
    def __init__(self):
        global _PUZZLE_CLASS_DICT
        self.puzzle_dict = {}
        for key in _PUZZLE_CLASS_DICT:
            self.puzzle_dict[key] = _PUZZLE_CLASS_DICT[key]()

    def run(self):
        self.bomb_info = BombInfo()
        self.bomb_info.read_data()

        while True:
            self.puzzle_dict["Wires"].run(self.bomb_info)

def main():
    driver = Driver()
    driver.run()

if __name__ == "__main__":
    main()
