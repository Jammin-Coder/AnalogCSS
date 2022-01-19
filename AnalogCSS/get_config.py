from AnalogCSS.tools import read_json

config_file = "analog_config.json"

def get_breakpoint_values() -> dict:
    """
    Gets the user defined breakpoint values
    """
    return read_json(config_file)["breakpoint_values"]

def get_class_mappings() -> dict:
    """
    Gets the class user defined CSS class mappings
    """
    return read_json(config_file)["class_mappings"]

def get_custom_values() -> dict:
    """
    Gets the user defined values
    """
    return read_json(config_file)["custom_values"]

def get_media_query_type() -> dict:
    """
    Gets the main media query type
    """
    return read_json(config_file)["media_query_type"]

def get_user_css_file_paths() -> dict:
    """
    Gets the paths the the user's CSS files.
    """
    return read_json(config_file)["user_css_file_paths"]

def get_output_css_path() -> str:
    """
    Gets the path of the CSS file that the user wants the program to output to
    """
    return read_json(config_file)["output_css_file_path"]

def get_input_paths():
    """
    Gets the paths the user wants the program to monitor
    """
    return read_json(config_file)["input_paths"]

def get_input_extensions():
    """
    Gets the type of file extensions the user wants the program to monitor
    """
    return read_json(config_file)["input_extensions"]


