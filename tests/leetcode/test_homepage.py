import allure
import pytest

from pages.leetcode.leetcode_page import LeetcodePage
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from core.base.base_test import BaseTest


@pytest.mark.leetcode
@pytest.mark.homepage
@allure.feature("Leetcode: Homepage")
class TestHomepage(BaseTest):

    @allure.title("Leetcode: Test homepage card titles")
    def test_homepage_cards_title(self, driver):

        leetcode = LeetcodePage(driver)
        leetcode.open_leetcode_site()

        leetcode.verify_total_cards(21)

        cards_title_list = ['POM', 'Input', 'Button', 'Select',
                            'Alert', 'Frame', 'Radio', 'Window',
                            'Elements', 'Drag', 'Drop', 'Sort',
                            'Multi-Select', 'Slider', 'Waits', 'Table',
                            'Table', 'Calendar', 'Forms', 'File',
                            'Shadow']
        leetcode.verify_cards_title(cards_title_list)


    @allure.title("Leetcode: Test homepage cards description")
    def test_homepage_cards_description(self, driver):
        leetcode = LeetcodePage(driver)
        leetcode.open_leetcode_site()

        leetcode.verify_total_cards(21)

        cards_title_list = ['POM', 'Input', 'Button', 'Select',
                            'Alert', 'Frame', 'Radio', 'Window',
                            'Elements', 'Drag', 'Drop', 'Sort',
                            'Multi-Select', 'Slider', 'Waits', 'Table',
                            'Table', 'Calendar', 'Forms', 'File',
                            'Shadow']
        leetcode.verify_cards_title(cards_title_list)

        cards_titles_descriptions_dict = {
            'POM': 'Practice Page Object Model with fakestore',
            'Input': 'Interact with different types of input fields',
            'Button': 'Interact with different types of buttons',
            'Select': 'Interact with different types of drop-down',
            'Alert': 'Interact with different types of dialog boxes',
            'Frame': 'Interact with different types of frames/iframes',
            'Radio': 'Interact with different types of radio & check boxes',
            'Window': 'Switch different types of tabs or windows',
            'Elements': 'Play with element and smash them',
            'Drag': 'Drag me here and there',
            'Drop': 'Feel free to bounce me',
            'Sort': 'Sort out the problem quickly',
            'Multi-Select': 'Be a multi-tasker',
            'Slider': 'Hmm.. Can you slide me?',
            'Waits': 'It\'s ok to wait but you know..',
            'Table': 'It\'s all about rows & columns',
            'Table': 'It\'s little complicated but give a try',
            'Calendar': 'My time is precious & your?',
            'Forms': 'Interact with everything',
            'File': 'All your data is secured!',
            'Shadow': 'Shadow never leaves us alone'
        }
        leetcode.verify_cards_description(cards_titles_descriptions_dict)

