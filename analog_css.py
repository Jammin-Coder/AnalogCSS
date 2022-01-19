from AnalogCSS.tools import get_classes_from_file, append_to_file, write_file
from AnalogCSS.FindFiles import find_files
from AnalogCSS.get_config import get_output_css_path

import time

from AnalogCSS.ShorthandClass import ShorthandClass
print("[+] Watching files")

while True:
    output_path = get_output_css_path()
    try:
        files = find_files()

        generated_classes = list()

        for file in files:
            classes = get_classes_from_file(file)

            for _class in classes:
                shorthand_class = ShorthandClass(_class)
                generated_classes.append(shorthand_class.generate())


        write_file(output_path, "")
        for _class in generated_classes:
            append_to_file(output_path, _class)
        time.sleep(1)

    except KeyboardInterrupt:
        print("\n[+] Stopped watching files")
        exit()
        

    
