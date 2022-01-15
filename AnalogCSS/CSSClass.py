class CSSClass:
    """
    This class is used to store CSS classes neatly.
    You can access property values like this:
    >>> css_class.get("property_name")
    >>> <property-value>
    """
    def __init__(self, name, attr_str = None):
        self.name = name
        self.attr_str = attr_str
        self.attributes = dict()
        if attr_str:
            self.parse_attr_str()

    def parse_attr_str(self):
        attrs = self.attr_str.split(";")
        for line in attrs:
            if line != "":
                property = line.split(":")[0].strip()
                value = line.split(":")[1].strip()
                self.attributes[property] = value
    
    def get(self, property_name):
        return self.attributes[property_name]
    
    def set(self, property_name, value):
        self.attributes[property_name] = value

    def create_media_query(self, mq_type, breakpoint):
        return f"@media ({mq_type}: {breakpoint}) {{\n{self.compile()[1:]}}}\n"

    def compile(self):
        output = f".{self.name} {{\n"

        for key in self.attributes.keys():
            value = self.attributes[key]
            output += f"\t{key}: {value};\n"
        return output + "}\n"

        



    