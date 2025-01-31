"""
@package utils

Util class implementation
All most commonly used utils should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import os
import time
import traceback
import random, string
import utils.custom_logger as cl
import logging
# from base.base_page import BasePage
from faker import Faker


class Util(object):
# class Util:

    log = cl.custom_logger(logging.INFO)


    # def wait_seconds(self, seconds):
    #     time.sleep(seconds)

    @staticmethod
    def generate_random_names():
        # initialize faker
        fake = Faker()

        # generate single random name
        random_name = fake.name()
        print(f">>> generated name = {random_name}")
        return random_name






    # def get_alpha_numeric(self, length, type='letters'):
    #     """
    #     Get random string of characters
    #
    #     Parameters:
    #         length: Length of string, number of characters string should have
    #         type: Type of characters string should have. Default is letters
    #         Provide lower/upper/digits for different types
    #     """
    #     alpha_num = ''
    #     if type == 'lower':
    #         case = string.ascii_lowercase
    #     elif type == 'upper':
    #         case = string.ascii_uppercase
    #     elif type == 'digits':
    #         case = string.digits
    #     elif type == 'mix':
    #         case = string.ascii_letters + string.digits
    #     else:
    #         case = string.ascii_letters
    #     return alpha_num.join(random.choice(case) for i in range(length))
    #
    #
    # # another wrapper method of getAlphaNumeric
    # def get_unique_name(self, char_count=10):
    #     """
    #     Get a unique name
    #     """
    #     return self.get_alpha_numeric(char_count, 'lower')
    #
    #
    # # another wrapper method of getAlphaNumeric
    # def get_unique_name_list(self, list=5, item_length=None):
    #     """
    #     Get a list of valid email ids
    #
    #     Parameters:
    #         list: Number of names. Default is 5 names in a list
    #         item_length: It should be a list containing number of items equal to the listSize
    #                     This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
    #     """
    #     name_list = []
    #     for i in range(0, list):
    #         name_list.append(self.get_unique_name(item_length[i]))
    #     return name_list
    

    # def screenshot(self, result_message):
    #     """
    #     Takes the screenshot of the current open web
    #     """
    #     print()
    #     filename = result_message + "." + str(round(time.time() * 1000)) + ".png" #png is more compressed / smaller file
    #     screenshot_directory = "../reports/"
    #     relative_filename = screenshot_directory + filename  # this is the filepath
    #
    #     current_directory = os.path.dirname(__file__)
    #
    #     destination_file = os.path.join(current_directory, relative_filename)
    #     destination_directory = os.path.join(current_directory, screenshot_directory)
    #
    #     try:
    #         # if "reports" folder not exist, create a folder
    #         if not os.path.exists(destination_directory):
    #             os.makedirs(destination_directory)
    #         self.driver.save_screenshot(destination_file)
    #         self.log.info("Screenshot save to directory: " + destination_file)
    #     except:
    #         self.log.error("### Exception Occurred ###")
    #         traceback.print_stack()



