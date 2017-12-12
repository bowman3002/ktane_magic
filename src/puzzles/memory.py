from game_input import game_input
from game_input import game_loop
from puzzle import puzzle

LABEL = 0
POSITION = 1

@puzzle("Memory")
class Memory:
    def __init__(self):
        self.name = "Memory"

    def run(self, bomb_info):
        with game_loop(self.name) as loop:
            memory = []

            while True:
                try:
                    print("Stage 1:")
                    display_number = int(game_input("Enter the number on the display: "))
                    position_number = -1
                    button_number = -1
                    if display_number == 1:
                        memory.append(self.prompt_press_position(2))
                    elif display_number == 2:
                        memory.append(self.prompt_press_position(2))
                    elif display_number == 3:
                        memory.append(self.prompt_press_position(3))
                    elif display_number == 4:
                        memory.append(self.prompt_press_position(4))
                    else:
                        print("Not a valid number\n")
                        continue
                    print("")
                    break
                except ValueError:
                    print("Not a number")

            while True:
                try:
                    print("Stage 2:")
                    display_number = int(game_input("Enter the number on the display: "))
                    position_number = -1
                    button_number = -1
                    if display_number == 1:
                        memory.append(self.prompt_press_label(4))
                    elif display_number == 2:
                        memory.append(self.prompt_press_position(memory[0][POSITION]))
                    elif display_number == 3:
                        memory.append(self.prompt_press_label(1))
                    elif display_number == 4:
                        memory.append(self.prompt_press_position(memory[0][POSITION]))
                    else:
                        print("Not a valid number")
                        continue
                    print("")
                    break
                except ValueError:
                    print("Not a number")

            while True:
                try:
                    print("Stage 3:")
                    display_number = int(game_input("Enter the number on the display: "))
                    position_number = -1
                    button_number = -1
                    if display_number == 1:
                        memory.append(self.prompt_press_label(memory[1][LABEL]))
                    elif display_number == 2:
                        memory.append(self.prompt_press_label(memory[0][LABEL]))
                    elif display_number == 3:
                        memory.append(self.prompt_press_position(3))
                    elif display_number == 4:
                        memory.append(self.prompt_press_label(4))
                    else:
                        print("Not a valid number")
                        continue
                    print("")
                    break
                except ValueError:
                    print("Not a number")

            while True:
                try:
                    print("Stage 4:")
                    display_number = int(game_input("Enter the number on the display: "))
                    position_number = -1
                    button_number = -1
                    if display_number == 1:
                        memory.append(self.prompt_press_position(memory[0][POSITION]))
                    elif display_number == 2:
                        memory.append(self.prompt_press_position(1))
                    elif display_number == 3:
                        memory.append(self.prompt_press_position(memory[1][POSITION]))                        
                    elif display_number == 4:
                        memory.append(self.prompt_press_position(memory[1][POSITION]))
                    else:
                        print("Not a valid number")
                        continue
                    print("")
                    break
                except ValueError:
                    print("Not a number")

            while True:
                try:
                    print("Stage 5:")
                    display_number = int(game_input("Enter the number on the display: "))
                    position_number = -1
                    button_number = -1
                    if display_number == 1:
                        memory.append(self.prompt_press_label(memory[0][LABEL]))
                    elif display_number == 2:
                        memory.append(self.prompt_press_label(memory[1][LABEL]))
                    elif display_number == 3:
                        memory.append(self.prompt_press_label(memory[3][LABEL]))
                    elif display_number == 4:
                        memory.append(self.prompt_press_label(memory[2][LABEL]))
                    else:
                        print("Not a valid number")
                        continue
                    print("")
                    break
                except ValueError:
                    print("Not a number")

    def prompt_press_label(self, label):
        position = int(game_input("Enter the position of button labeled {}: ".format(label)))
        print("Press button labeled {}".format(label))
        return [label, position]

    def prompt_press_position(self, position):
        label = int(game_input("Enter the label on button in position {}: ".format(position)))
        print("Press button at position {}".format(position))
        return [label, position]