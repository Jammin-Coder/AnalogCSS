from AnalogCSS.get_config import *
from AnalogCSS.syntax import *
from AnalogCSS.CSSClass import CSSClass
from AnalogCSS.tools import NUMBERS
from AnalogCSS.get_user_css import GetUserCSS

class ShorthandClass:
    """
    This class determines how to interpret a shorthand CSS class.
    I.E If the inputed shorthand class is 'p-2em', then GenerateClass would generate a CSS class that gives a padding of 2em.
    If the inputed shorthand class is 'md:py-4em', then GenerateClass would generate a CSS class that gives a padding of 4em to 
    the top and bottom of the element, only after the medium (md) breakpoint is reached.
    
    The syntax for a shorthand CSS class is [optional breakpoint:]<property>-<value>
    So if you wanted a CSS class to give a margin of 1rem to an element,
    the shorthand CSS class would be: 'm-1rem'. If you wanted that class to only have an effect
    at the small (sm) breakpoint, you would prepend 'sm:' to the shorthand class, like this: 'sm:m-1rem'.
    """

    def __init__(self, shorthand_class: str):

        # The shorthand CSS class/class name
        self.shorthand_class = shorthand_class
        self.parsed_name = self.parse_name(shorthand_class)

        # Gets the defined breakpoint values from analog_config.json
        self.breakpoint_values = get_breakpoint_values()

        # Gets the class mappings from analog_config.json
        self.class_mappings = get_class_mappings()

        # Gets any custom values the user made in analog_config.json
        self.custom_values = get_custom_values()

        # Gets the predefined CSS that the user wrote.
        self.user_css_classes = GetUserCSS(get_user_css_file_paths()).get_classes()

        self.media_queries = dict()  # {"breakpoint": list(<all classes fro this breakpoint>)}


    def is_shorthand_class(self):
        return PROPTERTY_SEPERATOR in self.shorthand_class
    
    def breakpoint_exists(self):
        return BREAKPOINT_SEPERATOR in self.shorthand_class

    def parse_name(self, name):
        """
        Prepends any special characters with a backslash to escape them
        """
        parsed_name = ""
        for char in name:
            if char in SPECIAL_CHARS:
                parsed_name += f"\{char}"
            else:
                parsed_name += char
        return parsed_name

    def get_breakpoint(self):
        """
        Gets the breakpoint of the shorthand class, if any, and returns its value.
        """
        if self.breakpoint_exists():
            breakpoint_index = self.shorthand_class.index(BREAKPOINT_SEPERATOR)
            breakpoint_shorthand = self.shorthand_class[:breakpoint_index]  # Evaluates to xs, sm, md, lg, xl or custom values.
            if breakpoint_shorthand in self.breakpoint_values.keys():
                return self.breakpoint_values[breakpoint_shorthand]
            else:
                return breakpoint_shorthand

        return None
    
    def get_shorthand_property(self):
        """
        Gets the CSS property from the shorthand CSS class and returns its mapped value.
        """
        property_shorthand = self.shorthand_class.split(PROPTERTY_SEPERATOR)[0]
        if BREAKPOINT_SEPERATOR in property_shorthand:
            property_shorthand = property_shorthand[property_shorthand.index(BREAKPOINT_SEPERATOR) + 1:]
        
        return property_shorthand

    def get_real_property(self, prop_shorthand):
        if prop_shorthand in self.class_mappings.keys():
            return self.class_mappings[prop_shorthand]["property"]

    def get_shorthand_value(self):
        """
        Gets the value from the shorthand class and returns it.
        """
        if self.is_shorthand_class():
            value = self.shorthand_class.split(PROPTERTY_SEPERATOR)[1]

            # If the value was assigned in the "custom_values", then use the assigned value.
            if value in self.custom_values:
                value = self.custom_values[value]

            return value

    def get_unit(self, value):
        for i, char in enumerate(value):
            if char not in NUMBERS:
                return value[i + 2:]

    def get_value(self, value):
        # Evaluate fractions
        if "/" in value:
            slash_index = value.index("/")
            for i in range(slash_index + 1, len(value)):
                if value[i] not in NUMBERS:
                    expression = value[:i]
                    evaluated_value = round(int(expression.split("/")[0]) / int(expression.split("/")[1]), 2)
                    unit = self.get_unit(value)
                    value = str(evaluated_value) + unit
                    break
        
        # Otherwise the value is good
        return value

    def generate(self):

        output = ""
        is_media_query = False

        if self.breakpoint_exists():
            is_media_query = True
            mq_type = get_media_query_type()
            breakpoint = self.get_breakpoint()
            
            # This means the breakpoint is a custom one
            if breakpoint[0] == "@" and breakpoint not in self.breakpoint_values.keys():
                breakpoint = self.get_value(breakpoint[1:])


            # self.media_queries[breakpoint].append()
            output += f"@media ({mq_type}: {breakpoint}) {{\n"

            if self.get_shorthand_property() in self.user_css_classes.keys():
                # This means the user is adding a breakpoint to one of their own predefined classes.
                user_class_name = self.get_shorthand_property()
                user_css_class = self.user_css_classes[user_class_name]
                user_css_class.name = self.parse_name(user_class_name)
                return user_css_class.create_media_query(mq_type, breakpoint)

                

        if not self.is_shorthand_class():
            return ""
        
        shorthand_prop = self.get_shorthand_property()
        attributes = self.get_real_property(shorthand_prop)
        if not attributes:
            attributes = shorthand_prop
        value = self.get_value(self.get_shorthand_value())

        css_class = CSSClass(self.parsed_name)

        if type(attributes) == list:
            for attr in attributes:
                css_class.set(attr, value)
        else:
            css_class.set(attributes, value)

        compiled_class = css_class.compile()
        output += compiled_class


        if is_media_query == True:
            output += "}\n"

        return output
