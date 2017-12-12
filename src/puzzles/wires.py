from game_input import game_input
from game_input import game_loop
from format_error import FormatError
from puzzle import puzzle

_PRIVATE_DICT = {}

@puzzle("Wires")
class Wires:
    def __init__(self):
        self.name = "Wires"
        self.function_dict = _PRIVATE_DICT

    def run(self, bomb_info):
        """
        Runs the wires game with info from bomb_info
        """
        with game_loop(self.name) as loop:
            while True:
                wires = game_input("Please enter character for each wire color, top to bottom, no spaces: ").lower()
                try:
                    if not (set("bkrwy") >= set(wires)):
                        raise FormatError(wires)

                    self.function_dict[len(wires)](self, wires, bomb_info)
                    break
                except KeyError:
                    print("Invalid number of wires")
                except FormatError:
                    print("Invalid format for wire string")

    def dict_function(key):
        def decorate(fn):
            _PRIVATE_DICT[key] = fn
            return fn
        return decorate

    def num_of_color(self, wires, color):
        return len(list(filter(lambda c: c == color, wires)))

    def last_digit_odd(self, bomb_info):
        try:
            last_digit = int(bomb_info.serial_number[-1])
            return last_digit % 2 == 1
        except ValueError:
            return False

    @dict_function(3)
    def three(self, wires, bomb_info):
        if self.num_of_color(wires, 'r') == 0:
            print("--> Cut the second wire")
        elif wires[-1] == 'w':
            print("--> Cut the last wire")
        elif self.num_of_color(wires, 'b') > 1:
            print("--> Cut the last blue wire")
        else:
            print("--> Cut the last wire")

    @dict_function(4)
    def four(self, wires, bomb_info):
        if self.num_of_color(wires, 'r') > 1 and self.last_digit_odd(bomb_info):
            print("--> Cut the last wire")
        elif self.num_of_color(wires, 'r') == 0 and wires[-1] == 'y':
            print("--> Cut the first wire")
        elif self.num_of_color(wires, 'b') == 1:
            print("--> Cut the first wire")
        elif self.num_of_color(wires, 'y') > 1:
            print("--> Cut the last wire")
        else:
            print("--> Cut the second wire")

    @dict_function(5)
    def five(self, wires, bomb_info):
        if wires[-1] == 'k' and self.last_digit_odd(bomb_info):
            print("--> Cut the fourth wire")
        elif self.num_of_color(wires, 'r') == 1 and self.num_of_color(wires, 'y') > 1:
            print("--> Cut the first wire")
        elif self.num_of_color(wires, 'k') == 0:
            print("--> Cut the second wire")
        else:
            print("--> Cut the first wire")

    @dict_function(6)
    def six(self, wires, bomb_info):
        if self.num_of_color(wires, 'y') == 0 and self.last_digit_odd(bomb_info):
            print("--> Cut the third wire")
        elif self.num_of_color(wires, 'y') == 1 and self.num_of_color(wires, 'w') > 1:
            print("--> Cut the fourth wire")
        elif self.num_of_color(wires, 'r') == 0:
            print("--> Cut the last wire")
        else:
            print("--> Cut the fourth wire")
