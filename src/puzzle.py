_PUZZLE_CLASS_DICT = {}

def puzzle(name):
    def decorator(cls):
        _PUZZLE_CLASS_DICT[name] = cls
        return cls
    return decorator