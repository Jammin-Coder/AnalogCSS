from AnalogCSS.ShorthandValue import ShorthandValue
from AnalogCSS.get_config import get_class_mappings
from AnalogCSS.tools import NUMERICAL

class ShorthandProperty:
    def __init__(self, property_abbreviation, full_property_value):
        self.prop_abbr = property_abbreviation
        self.full_prop_value = ShorthandValue(full_property_value)
        

        # Gets the class mappings from analog_config.json
        self.class_mappings = get_class_mappings()

        self.prop_unit = None
        self.defined_unit = self.get_defined_unit()
        self.prop_value = self.full_prop_value.value

        self.attributes = self.get_prop_attributes()
        self.set_unit()
        
    def get_prop_attributes(self):
        if self.prop_abbr in self.class_mappings.keys():
            return self.class_mappings[self.prop_abbr]["property"]

    def get_defined_unit(self):
        if "unit" in self.class_mappings[self.prop_abbr].keys():
            return self.class_mappings[self.prop_abbr]["unit"]
        return None

    def set_unit(self):
        if self.full_prop_value.type == NUMERICAL:
            if self.full_prop_value.unit:
                self.prop_unit = self.full_prop_value.unit
            else:
                self.prop_unit = self.defined_unit
    

    def info(self):
        print("[+] INFO: self.prop_value:" + self.prop_value)
        print("[+] INFO: self.prop_unit:" + self.prop_unit)
                
    


