
from AnalogCSS.tools import NUMBERS, NUMERICAL, STRING

class ShorthandValue:
    def __init__(self, value):
        self.raw_value = value # This value will be unchanged. The other one will be parsed if it's a fraction.
        self.value = value
        self.type = self.get_value_type()
        self.unit = self.get_unit_from_value()
        self.parse_fraction()

    def is_fraction(self):
        return "/" in self.value
             
    def get_value_type(self):
        if self.value[0] in NUMBERS:
            return NUMERICAL
        else:
            return STRING

    def parse_fraction(self):
        if self.is_fraction() and self.type == NUMERICAL:
            if self.value[-1] not in NUMBERS:
                # This means the user is using a custom unit in their class name, so we need to do some parsing.
                slash_index = self.value.index("/")
                for i in range(slash_index + 1, len(self.value)):
                    if self.value[i] not in NUMBERS:
                        expression = self.value[:i]
                        self.value = str(round(int(expression.split("/")[0]) / int(expression.split("/")[1]), 2))
                        if self.unit:
                            self.value += self.unit

                        # STOP THE LOOP HERE
                        return
            else:
                # This means the user did not provide a unit in their class name, so we can just evaluate the raw expression.
                self.value = str(round(int(self.value.split("/")[0]) / int(self.value.split("/")[1]), 2))
                # If there is no unit defined, set a percentage as the default unit.
                if not self.unit:
                    self.unit = "%"
                    self.value += self.unit

    def get_unit_from_value(self):
        for i, char in enumerate(self.value):
            if char not in NUMBERS and char not in "/.":
                if i == 0:
                    return None
                return self.value[i:]

        