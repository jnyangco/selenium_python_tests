import configparser
import os

def read_config(section, key):
    # Define the path to the config.ini file
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "../config.ini")
    config.read(config_path)

    return config.get(section, key)