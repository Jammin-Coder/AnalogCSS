from AnalogCSS.tools import read_file
from AnalogCSS.CSSClass import CSSClass


class GetUserCSS:
    def __init__(self, user_css_files):
        self.user_css_files = user_css_files
        self.user_css_classes = dict()

    def get_class_name_from_line(self, line):
        """
        Gets the class name from this line, provided there is a class definition on this line
        """
        class_name = ""
        for char in line:
            if char == " " or char == "{":
                break

            class_name += char
        return class_name

    def is_class_def_line(self, line):
        """
        Returns True if the provided line is one on which a class is defined, otherwise returns False.
        """
        return line != "" and line[0] == "."


    def get_classes(self):
        """
        Gets all CSS classes from provided file and returns them as a list of CSSClass
        """

        for css_file in self.user_css_files:
            user_css = read_file(css_file)

            """ If parse_class is True, that means the program found a CSS class name, 
                so it should grab all the properties under it (in that class) """
            parse_class = False
            
            current_class_properties = ""
            current_class_name = ""

            for line in user_css.split("\n"):
                
                #  This means the program found a CSS class
                if self.is_class_def_line(line):
                    """ Since the program found a CSS class, set parse_class to True so next 
                        itteration start adding the class properties to the current_class_properties list """
                    parse_class = True
                    current_class_name = self.get_class_name_from_line(line)
                    continue

                if parse_class:
                    for char in line:
                        if char == "}":
                            css_class = CSSClass(current_class_name, current_class_properties)
                            self.user_css_classes[current_class_name[1:]] = css_class

                            # Reset the current class attributes to nothing
                            current_class_properties = ""
                            current_class_name = ""

                            parse_class = False
                            break

                        current_class_properties += char
        
        return self.user_css_classes

