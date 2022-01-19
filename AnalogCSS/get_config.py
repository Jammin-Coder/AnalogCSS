from AnalogCSS.tools import read_json

config_file = "analog_config.json"

def get_breakpoint_values() -> dict:
    return read_json(config_file)["breakpoint_values"]

def get_class_mappings() -> dict:
    return read_json(config_file)["class_mappings"]

def get_custom_values() -> dict:
    return read_json(config_file)["custom_values"]

def get_media_query_type() -> dict:
    return read_json(config_file)["media_query_type"]

def get_user_css_file_paths() -> dict:
    return read_json(config_file)["user_css_file_paths"]

def get_output_css_path() -> str:
    return read_json(config_file)["output_css_file_path"]

def get_input_paths():
    return read_json(config_file)["input_paths"]

def get_input_extensions():
    return read_json(config_file)["input_extensions"]


