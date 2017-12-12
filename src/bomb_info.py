from indicator import Indicator
from format_error import FormatError
from port import PortEnum

class BombInfo:
    """
    Stores all information for the bomb itself
    """
    def __init__(self):
        self.indicators = []
        self.batteries = 0
        self.ports = set()
        self.serial_number = ""
        self.strikes = 0

    def read_data(self):
        """
        Reads in all data from the bomb itself
        """
        self.print_divider()
        self.serial_number = self.read_serial_number()
        self.print_divider()
        self.batteries = self.read_batteries()
        self.print_divider()
        self.ports = self.read_ports()
        self.print_divider()
        self.indicators = self.read_indicators()
        self.print_divider()

    def print_divider(self):
        print("\n--------------------------------------------------------------------------------\n")

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

    def read_ports(self):
        """
        Shows user numbered list of ports
        Prompts user to enter matching numbers to what ports are on the bomb
        """
        port_list = list(PortEnum)
        current_ports = set()
        for i in range(0, len(port_list)):
            print("{0}: {1}".format(i, port_list[i].value))

        while True:
            value_str = input("Enter number matching a port on the bomb or blank for end: ")

            if value_str == "":
                break

            try:
                value = int(value_str)
                if value > len(port_list):
                    print("Number out of range")
                    continue
                current_ports.add(port_list[value])
            except ValueError:
                print("Not an integer")

        return current_ports

    def read_serial_number(self):
        return input("Enter the serial number for the bomb: ").lower()

    def exists_indicator(self, ind_string):
        """
        Raises FormatError if ind_string is not formatted correctly
        """
        ind = Indicator.Make_Indicator(ind_string)
        return len(filter(lambda i: i.light == ind.light and i.text == ind.text, self.indicators)) > 0

    def add_strike(self):
        self.strikes += 1