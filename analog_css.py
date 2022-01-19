from AnalogCSS.tools import get_classes_from_file, append_to_file, write_file
from AnalogCSS.FindFiles import find_files
from AnalogCSS.get_config import get_output_css_path

import time

from AnalogCSS.ShorthandClass import ShorthandClass
print("[+] Watching files")

while True:
    output_path = get_output_css_path()
    try:
        files = find_files() # Find all the files the user wants the program to track.

        generated_classes = list() # A list to store the generated CSS classes.

        for file in files:
            class_names = get_classes_from_file(file)  # Gets the CSS classes the user used in their markup.

            # Loop over all the found class names and generate a CSS class with them.
            for _class in class_names:
                shorthand_class = ShorthandClass(_class)
                generated_classes.append(shorthand_class.generate())


        write_file(output_path, "") # Delete the contents of the output file.

        # Append all the generated classes to the output file
        for _class in generated_classes:
            append_to_file(output_path, _class)
        time.sleep(1)

    except KeyboardInterrupt:
        # Make sure the program generates all the classes again before quitting.
        print("[+] Generating classes one more time.")
        for _class in generated_classes:
            append_to_file(output_path, _class)

        print("\n[+] Done. Stopped watching files")
        exit()
        

    
