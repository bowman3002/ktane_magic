from game_input import game_input
from game_input import game_loop
from puzzle import puzzle

@puzzle("Who's On First")
class WhosOnFirst:
    position_dict = {"yes": "Middle Left",
                     "first": "Top Right",
                     "display": "Bottom Right",
                     "okay": "Top Right",
                     "says": "Bottom Right",
                     "nothing": "Middle Left",
                     "": "Bottom Left",
                     "blank", "Middle Right",
                     "no": "Bottom Right",
                     "led": "Middle Left",
                     "lead": "Bottom Right",
                     "read": "Middle Right",
                     "red": "Middle Right",
                     "reed": "Bottom Left",
                     "leed": "Bottom Left",
                     "hold on": "Bottom Right",
                     "you": "Middle Right",
                     "you are": "Bottom Right",
                     "your": "Middle Right",
                     "you're": "Middle Right",
                     "ur": "Top Left",
                     "there": "Bottom Right",
                     "they're": "Bottom Left",
                     "their": "Middle Right",
                     "they are": "Middle Left",
                     "see": "Bottom Right",
                     "c": "Top Right",
                     "cee": "Bottom Right"}

    word_dict = {"ready": ["Yes", "Okay", "What", "Middle", "Left", "Press", "Right", "Blank", "Ready"],
                 "first": ["Left", "Okay", "Yes", "Middle", "No", "Right", "Nothing", "Uhhh", "Wait", "Ready", "Blank", "What", "Press", "First"],
                 "no": ["Blank", "Uhhh", "Wait", "First", "What", "Ready", "Right", "Yes", "Nothing", "Left", "Press", "Okay", "No"],
                 "blank": ["Wait", "Right", "Okay", "Middle", "Blank"],
                 "nothing": ["Uhhh", "Right", "Okay", "Middle", "Yes", "Blank", "No", "Press", "Left", "What", "Wait", "First", "Nothing"],
                 "yes": ["Okay", "Right", "Uhhh", "Middle", "First", "What", "Press", "Ready", "Nothing", "Yes"],
                 "what": ["Uhhh", "What"],
                 "uhhh": ["Ready", "Nothing", "Left", "What", "Okay", "Yes", "Right", "No", "Press", "Blank", "Uhhh"],
                 "left": ["Right", "Left"],
                 "right": ["Yes", "Nothing", "Ready", "Press", "No", "Wait", "What", "Right"],
                 "middle": ["Blank", "Ready", "Okay", "What", "Nothing", "Press", "No", "Wait", "Left", "Middle"],
                 "okay": ["Middle", "No", "First", "Yes", "Uhhh", "Nothing", "Wait", "Okay"],
                 "wait": ["Uhhh", "No", "Blank", "Okay", "Yes", "Left", "First", "Press", "What", "Wait"],
                 "press": ["Right", "Middle", "Yes", "Ready", "Press"],
                 "you": ["Sure", "You Are", "Your", "You're", "Next", "Uh Huh", "UR", "Hold", "What?", "You"],
                 "you are": ["Your", "Next", "Like", "Uh Huh", "What?", "Done", "Uh Uh", "Hold", "You", "U", "You're", "Sure", "UR", "You Are"],
                 "you're": ["You", "You're"],
                 "ur": ["Done", "U", "UR"],
                 "u": ["Uh Huh", "Sure", "Next", "What?", "You're", "UR", "Uh Uh", "Done", "U"],
                 "uh huh": ["Uh Huh"],
                 "uh uh": ["UR", "U", "You Are", "You're", "Next", "Uh Uh"],
                 "what?": ["You", "Hold", "You're", "Your", "U", "Done", "Uh Uh", "Like", "You Are", "Uh Huh", "UR", "Next", "What?"],
                 "done": ["Sure", "Uh Huh", "Next", "What?", "Your", "UR", "You're", "Hold", "Like", "You", "U", "You Are", "Uh Uh", "Done"],
                 "next": ["What?". "Uh Huh", "Uh Uh", "Your", "Hold", "Sure", "Next"],
                 "hold": ["You Are", "U", "Done", "Uh Uh", "You", "UR", "Sure", "What?", "You're", "Next", "Hold"],
                 "sure": ["You Are", "Done", "Like", "You're", "You", "Hold", "Uh Huh", "UR", "Sure"],
                 "like": ["You're", "Next", "U", "UR", "Hold", "Done", "Uh Uh", "What?", "Uh Huh", "You", "Like"]}

    def __init__(self):
        self.name = "Who's On First"

    def run(self, bomb_info):
