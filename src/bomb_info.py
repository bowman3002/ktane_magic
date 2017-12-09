from indicator import Indicator
from format_error import FormatError

class BombInfo:
    """
    Stores all information for the bomb itself
    """
    def __init__(self):
        self.indicators = []
        self.batteries = 0

    def read_data(self):
        """
        Reads in all data from the bomb itself
        """
        self.indicators = self.read_indicators()
        self.batteries = self.read_batteries()

    def read_indicators(self):
        """
        Prompts user to enter string for indicators
        Enter nothing to exit loop of input
        """
        inds = []
        while True:
            ind_string = input("Enter indicator string ([t|f][A-Z]{3}) or blank for end: ")
            if ind_string == "":
                break

            try:
                ind = Indicator.Make_Indicator(ind_string)
                inds.append(ind)
            except FormatError:
                print("INCORRECT FORMATTING")
                continue

        return inds

    def read_batteries(self):
        """
        Prompts user to enter number of batteries
        Loops until number is inputted
        """
        while True:
            num_batteries = input("Enter number of batteries: ")
            try:
                return int(num_batteries)
            except ValueError:
                print("Not a number!")