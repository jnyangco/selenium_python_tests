import allure
from selenium.webdriver.common.by import By
from core.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step


class LeetcodePage(BasePage):

    # ============================================================================
    # LOCATORS - All locators from all Leetcode pages
    # ============================================================================
    # HOME PAGE (HP)
    HP_EDIT_BUTTON = (By.XPATH, "//a[@href='/edit']")
    HP_CARDS_OBJECT = (By.XPATH, "//div[@class='columns is-multiline']/div[@class='column is-3-desktop is-6-tablet']")
    HP_CARDS_TITLE = (By.XPATH, "//div/div[@class='column is-3-desktop is-6-tablet']//header/p")
    HP_CARDS_DESCRIPTION = (By.XPATH, "//div/div[@class='column is-3-desktop is-6-tablet']//div/p")

    # EDIT PAGE
    EP_FULL_NAME_TEXTBOX = (By.XPATH, "//input[@id='fullName']")
    EP_INSIDE_TEXTBOX = (By.XPATH, "//input[@id='getMe']")
    EP_CLEAR_TEXTBOX = (By.XPATH, "//input[@id='clearMe']")
    EP_DISABLED_TEXTBOX = (By.XPATH, "//input[@id='noEdit']")
    EP_READ_ONLY_TEXTBOX = (By.XPATH, "//input[@id='dontwrite']")


    # ****************************************************************************




    # ============================================================================
    # COMMON METHODS
    # ============================================================================
    @allure_step("Opening leetcode website")
    def open_leetcode_site(self):
        url = data("leetcode", "base_url")
        self.open_url(url)



    # ============================================================================
    # HOMEPAGE METHODS
    # ============================================================================
    @allure_step("Click Edit button")
    def click_edit_button(self):
        self.click_element(self.HP_EDIT_BUTTON)


    @allure_step("Verify total cards: {expected_total}")
    def verify_total_cards(self, expected_total):
        cards_object = self.find_web_elements(self.HP_CARDS_OBJECT)
        total_cards = len(cards_object)
        self.log.info(f"total_cards = {total_cards}")
        assert total_cards == expected_total, \
            f"Total cards mismatch: Expected '{expected_total}', but found '{total_cards}'"

    @allure_step("Verify cards title: {expected_list}")
    def verify_cards_title(self, expected_list):
        cards_object = self.find_web_elements(self.HP_CARDS_TITLE)
        cards_title_list = []
        for card in cards_object:
            # self.log.info(card.text.strip())
            cards_title_list.append(card.text.strip())
        self.log.info(f"cards_title_list = {cards_title_list}")

        assert cards_title_list == expected_list, \
            f"Cards title mismatch: Expected = {expected_list}, but found {cards_title_list}"


    @allure_step("Verify cards description: {expected_dict}")
    def verify_cards_description(self, expected_dict):
        # get cards title -> list
        titles = self.find_web_elements(self.HP_CARDS_TITLE)
        title_list = []
        for card in titles:
            # self.log.info(card.text.strip())
            title_list.append(card.text.strip())
        self.log.info(f"title_list = {title_list}")

        # get cards description -> list
        descriptions = self.find_web_elements(self.HP_CARDS_DESCRIPTION)
        description_list = []
        for description in descriptions:
            self.log.info(description.text.strip())
            description_list.append(description.text.strip())

        # CONVERT two lists into a dictionary (keys and values) pair
        # GET value from dictionary -> dict_object['key_here']}")
        actual_dict = dict(zip(title_list, description_list))

        # Loop through dictionary itesm -> for key, value in dict.items():
        for key, value in actual_dict.items():
            self.log.info(f"> k:{key}, v:{value}")

        # Report mismatch <key> or <value>
        for key in expected_dict:
            if key in actual_dict:
                if expected_dict[key] != actual_dict[key]:
                    raise AssertionError(f"Value mismatch: Expected description '{key}: {expected_dict[key]}', but found '{key}: {actual_dict[key]}'")
            else:
                raise AssertionError(f"Key '{key}' not present in actual_dict: -> {title_list}")







        assert actual_dict == expected_dict, \
            f"Titles and description mismatch: Expected {expected_dict}, but found {actual_dict}"












    # ============================================================================
    # EDIT METHODS
    # ============================================================================
    @allure_step("Verify full name placeholder text: '{expected_text}'")
    def verify_full_name_placeholder_text(self, expected_text):
        actual_text = self.find_web_element(self.EP_FULL_NAME_TEXTBOX).get_attribute('placeholder')
        assert actual_text == expected_text, \
            f"Placeholder text mismatch: Expected text '{expected_text}', but found '{actual_text}'"


    @allure_step("Enter text to full name textbox: '{text}'")
    def enter_text_to_full_name_textbox(self, text):
        self.enter_text(self.EP_FULL_NAME_TEXTBOX, text)


    @allure_step("Verify text inside the textbox: '{expected_text}'")
    def verify_text_inside_the_textbox(self, expected_text):
        actual_text = self.find_web_element(self.EP_INSIDE_TEXTBOX).get_attribute('value')
        assert actual_text == expected_text, \
            f"Text mismatch: Expected text '{expected_text}', but found '{actual_text}'"


    @allure_step("Clear textbox")
    def clear_textbox(self):
        textbox = self.find_web_element(self.EP_CLEAR_TEXTBOX)
        text_value = textbox.get_attribute('value')
        self.log.info(f"Before clearing text: text_value = {text_value}")
        assert text_value != "", f"Textbox is empty"

        textbox.clear()
        text_value = textbox.get_attribute('value')
        self.log.info(f"After clearing text: text_value = {text_value}")
        assert text_value == "", f"Textbox should be empty, but found '{text_value}'"


    @allure_step("Verify textbox is disabled")
    def verify_textbox_is_disabled(self):
        textbox = self.find_web_element(self.EP_DISABLED_TEXTBOX)
        is_textbox_disabled = textbox.get_attribute('disabled')
        self.log.info(f"is_textbox_disabled = {is_textbox_disabled}")
        assert is_textbox_disabled, f"Textbox should be disabled: is_textbox_disabled '{is_textbox_disabled}'"


    @allure_step("Verify textbox is read only")
    def verify_textbox_is_read_only(self):
        textbox = self.find_web_element(self.EP_READ_ONLY_TEXTBOX)
        is_textbox_readonly = textbox.get_attribute('readonly')
        self.log.info(f"is_textbox_readonly = {is_textbox_readonly}")
        assert is_textbox_readonly, f"Textboxt should be read only: is_textbox_readonly = {is_textbox_readonly}"


