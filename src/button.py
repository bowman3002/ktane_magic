from game_input import game_input
from game_input import game_loop
from puzzle import puzzle

@puzzle("Button")
class Button:
    def __init__(self):
        self.name

    def run(self, bomb_info):
        with game_loop(self.name) as loop:
            while True:
                color = game_input("Please input color character [b|k|r|w|y]: ").lower()
                if not(set('bkrwy') >= set(color)) or len(color) > 1:
                    print("Incorrect format")
                    continue

                text = game_input("Please enter text on the button: ").lower()

                if color == 'b' and text == "abort":
                    self.holdButton()
                elif bomb_info.batteries > 1 and text == "Detonate":
                    print("Click the button")
                elif color == 'w' and bomb_info.exists_indicator("tcar"):
                    self.holdButton()
                elif bomb_info.batteries > 2 and bomb_info.exists_indicator("tfrk"):
                    print("Click the button")
                elif color = 'y':
                    self.holdButton()
                elif color == 'r' and text == "hold":
                    print("Click the button")
                else:
                    self.holdButton()

    def holdButton(self):
        print("Hold the button")
        color = game_input("Please enter the color character [b|k|r|w|y] of the strip: ").lower()
        if color == 'b':
            print("Release on: 5")
        elif color == 'y':
            print("Release on: 4")
        else:
            print("Release on: 1")
