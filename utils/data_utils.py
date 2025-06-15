import configparser
import os
from config.test_config import TestConfig

def get_data(section, key):
    # get test_data.ini path
    test_config = TestConfig()

    # Define the path to the test_data.ini file
    config_parser = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), test_config.DATA_DIR)
    config_parser.read(config_path)

    return config_parser.get(section, key)