from game_input import game_input
from game_input import game_loop
from puzzle import puzzle
from enum import Enum

class Color(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3

@puzzle("Simon")
class Simon:
    Vowel_List = [  [Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN],
                    [Color.YELLOW, Color.GREEN, Color.BLUE, Color.RED],
                    [Color.GREEN, Color.RED, Color.YELLOW, Color.BLUE]]
    No_Vowel   = [  [Color.BLUE, Color.YELLOW, Color.GREEN, Color.RED],
                    [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN],
                    [Color.YELLOW, Color.GREEN, Color.BLUE, Color.RED]]
    Test_List = {False: No_Vowel,
                 True: Vowel_List}
    def __init__(self):
        self.name = "Simon"

    def run(self, bomb_info):
        if bomb_info.strikes >= 3:
            print("\nInvalid number of strikes for this puzzle\n")
            return

        with game_loop(self.name) as loop:
            current_prompt_sequence = []
            while True:
                print("CURRENT SEQUENCE: {0}".format(self.get_sequence(current_prompt_sequence, bomb_info)))

                color_str = game_input("Enter the newest color shown by Simon: ").upper()
                try:
                    current_prompt_sequence.append(Color[color_str])
                except KeyError:
                    print("Not a valid color")

    def get_sequence(self, in_sequence, bomb_info):
        output_list = []
        for color in in_sequence:
            output_list.append(Simon.Test_List[bomb_info.serial_has_vowel()][bomb_info.strikes][color.value].name)
        return output_list