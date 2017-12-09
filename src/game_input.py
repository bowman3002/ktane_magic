class EscapeException(Exception):
    pass

def game_input(message):
    response = input(message)
    if response == "~":
        raise EscapeException
    else:
        return response

class game_loop:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("==============================")
        print(self.name.upper())
        print("==============================")

    def __exit__(self, type, value, traceback):
        if isinstance(value, EscapeException):
            print("GAME ABORTED")
        elif isinstance(value, Exception):
            return False
        print("\n")
        return True