import imp
from AnalogCSS.tools import read_json
from AnalogCSS.get_config import get_input_extensions, get_input_paths
import os


def find_files():
    input_paths = get_input_paths()
    extensions = get_input_extensions()
    for dir in input_paths:
        for root, dirs, files in os.walk(dir):
            for file in files:
                file_ext = "." + file.split(".")[-1]
                if file_ext in extensions:
                    file_path = os.path.join(root, file)
                    yield file_path