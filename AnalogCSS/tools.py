"""
This file contains a bunch of generic functions.
"""

# import argparse
import json

from bs4 import BeautifulSoup
from AnalogCSS.syntax import *

NUMBERS = "0123456789"

# def get_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-o", help="Output CSS file.", dest="outfile")
#     args = parser.parse_args()
    
#     if not args.outfile:
#         return "analog.css"
#     return args.outfile

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w") as f:
        return f.write(content)

def append_to_file(path, content):
    with open(path, "a") as f:
        return f.write(content)

def read_json(path):
    """
    Reads a JSON file and returns the contents as a dictionary
    """
    with open(path, "r") as f:
        return json.loads(f.read())

def get_classes_from_file(file):
    file_contents = read_file(file)
    """
    Finds all classes in the provided file contents and returns them as a list.
    ['class-1', 'class-2', class-3', etc...]
    """
    soup = BeautifulSoup(file_contents, "html.parser")
    class_list = list()  # A list of class names that the parser found

    for element in soup.find_all():
        # If there is a class attribute in this element, extract all the class names from it.
        if element.has_attr("class"):
            for _class in element["class"]:
                if _class not in class_list:
                    class_list.append(_class)
    return class_list