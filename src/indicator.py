from format_error import FormatError

class Indicator:
    """ Defines a three letter indicator with light """
    def __init__(self, light, text):
        """ 
        Constructs an Indicator
        :param light: boolean representing if the light is on
        :param text:  three letter text on indicator
        """
        self.light = light
        self.text = text

    @classmethod
    def Make_Indicator(cls, encoded_string):
        """
        Returns an Indicator by decoding the string given
        :param encoded_string: Indicator encoded by [t|f][A-Z]{3}
        :returns: Indicator matching the encoded_string
        :raises FormatError: if encoded_string is not formatted correctly
        """
        def bool_char_to_str(char):
            if char.lower() == 't':
                return True
            elif char.lower() == 'f':
                return False
            else:
                raise FormatError(encoded_string)

        if len(encoded_string) != 4:
            raise FormatError(encoded_string)

        return Indicator(bool_char_to_str(encoded_string[0]), encoded_string[1:].lower())