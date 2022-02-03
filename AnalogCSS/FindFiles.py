from AnalogCSS.get_config import get_input_extensions, get_input_paths
import os


def find_files():
    """
    Function code inspired by: Stackoverflow user 'muon' https://stackoverflow.com/users/3130926/muon in answer: https://stackoverflow.com/a/41419432
    
    Finds all of the files in the paths that you want AnalogCSS to monitor.
    """
    input_paths = get_input_paths()  # Get the file paths we want to monitor.
    extensions = get_input_extensions()  # Get the extensions of the files we want to grab.
    for dir in input_paths:
        # Walk each path in input_paths and find any file that has an extension set it analog_config.json
        for root, dirs, files in os.walk(dir):
            for file in files:
                # Check to see if the file extension is a valid one to check.
                file_ext = "." + file.split(".")[-1]
                if file_ext in extensions:
                    file_path = os.path.join(root, file)  # Get the full path to the file
                    yield file_path  # Yield the results as a generator.