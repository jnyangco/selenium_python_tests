import configparser
import os

def get_data(section, key):
    # Define the path to the data.ini file
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "../config/data.ini")
    config.read(config_path)

    return config.get(section, key)