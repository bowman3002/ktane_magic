class FormatError(Exception):
    def __init__(self, formatted_string, msg=None):
        if msg is None:
            msg = "String ({0}) is formatted incorrectly".format(formatted_string)
        super().__init__(msg)
        self.formatted_string = formatted_string