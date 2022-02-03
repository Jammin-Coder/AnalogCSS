class CSSClass:
    """
    This class is used to store CSS classes neatly.
    You can access property values like this:
    >>> css_class.get("property_name")  # Returns property value

    And you can set property values like this:
    >>> css_class.set("property_name", "property_value")  # Sets specified property name to specified value

    You can generate a full CSS class that contains all of the properties you set in this class using:
    >>> css_class.compile()  # Returns a valid CSS class as a string.

    You can generate a breakpoint media query using:
    >>> css_class.create_media_query("mq_type", "breakpoint")  # Returns a CSS class string inside of a media query 
    """

    def __init__(self, name, attr_str = None):
        self.name = name
        self.attr_str = attr_str
        self.attributes = dict()
        if attr_str:
            self.parse_attr_str()

    def parse_attr_str(self):
        """
        Loops through the attribute string and identifies properties and their value.
        Once properties and values are found, add them to self.attributes
        """

        # This splits the attribute string into individiual attributes since a CSS attribute is defined as <attribute-name>: <value>;
        attrs = self.attr_str.split(";")

        # Loop over each of the attributes and get the attribute name and value.
        for line in attrs:
            if line != "":
                property = line.split(":")[0].strip()  # 
                value = line.split(":")[1].strip()
                self.set(property, value)  # Set the new property name to the new value.
    
    def get(self, property_name):
        """
        Returns the value of the property within self.attributes
        """
        return self.attributes[property_name]
    
    def set(self, property_name, value):
        """
        Sets the value of property_name to value within self.attributes.
        """
        self.attributes[property_name] = value

    def create_media_query(self, mq_type, breakpoint):
        """
        Generates a media query breakpoint with the current class attributes within self.attributes.
        """
        compiled_class = self.compile()
        return f"@media ({mq_type}: {breakpoint}) {{\n.{compiled_class[1:]}}}\n"  # use [1:] because otherwise the CSS class would start with 2 dots instead of one

    def compile(self):
        """
        Generates a valid CSS class using the information provided in self.attributes and return it as a string.
        """
        output_string = f".{self.name} {{\n"

        for key in self.attributes.keys():
            # Loop over all of the set attributes and add them to the output_string.
            value = self.get(key)
            output_string += f"\t{key}: {value};\n"
        return output_string + "}\n"

        



    