import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from core.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step
from selenium.webdriver.support.color import Color


class LeetcodePage(BasePage):

    # ============================================================================
    # LOCATORS - All locators from all Leetcode pages
    # ============================================================================
    # HOME PAGE (HP)
    HP_INPUT_BUTTON = (By.XPATH, "//a[@href='/edit']")
    HP_CARDS_OBJECT = (By.XPATH, "//div[@class='columns is-multiline']/div[@class='column is-3-desktop is-6-tablet']")
    HP_CARDS_TITLE = (By.XPATH, "//div/div[@class='column is-3-desktop is-6-tablet']//header/p")
    HP_CARDS_DESCRIPTION = (By.XPATH, "//div/div[@class='column is-3-desktop is-6-tablet']//div/p")
    HP_BUTTON = (By.XPATH, "//a[@href='/button']")
    HP_SELECT_BUTTON = (By.XPATH, "//a[@href='/dropdowns']")
    HP_ALERT_BUTTON = (By.XPATH, "//a[@href='/alert']")
    HP_FRAME_BUTTON = (By.XPATH, "//a[@href='/frame']")
    HP_RADIO_BUTTON = (By.XPATH, "//a[@href='/radio']")
    HP_WINDOW_BUTTON = (By.XPATH, "//a[@href='/window']")
    HP_ELEMENTS_BUTTON = (By.XPATH, "//a[@href='/window']")

    # INPUT PAGE
    IP_FULL_NAME_TEXTBOX = (By.XPATH, "//input[@id='fullName']")
    IP_INSIDE_TEXTBOX = (By.XPATH, "//input[@id='getMe']")
    IP_CLEAR_TEXTBOX = (By.XPATH, "//input[@id='clearMe']")
    IP_DISABLED_TEXTBOX = (By.XPATH, "//input[@id='noEdit']")
    IP_READ_ONLY_TEXTBOX = (By.XPATH, "//input[@id='dontwrite']")

    # BUTTON PAGE
    BP_GOTO_HOME_BUTTON = (By.XPATH, "//button[@id='home']")
    BP_FIND_LOCATION_BUTTON = (By.XPATH, "//button[@id='position']")
    BP_WHAT_IS_MY_COLOR_BUTTON = (By.XPATH, "//button[@id='color']")
    BP_HOW_TALL_AND_FAT_I_AM_BUTTON = (By.XPATH, "//button[@id='property']")
    BP_DISABLED_BUTTON = (By.XPATH, "//button[text()='Disabled']")
    BP_HOLD_BUTTON = (By.XPATH, "//button[contains(.,'Button Hold')]")

    # ALERT PAGE
    AP_SIMPLE_ALERT_BUTTON = (By.XPATH, "//button[text()='Simple Alert']")
    AP_CONFIRM_ALERT_BUTTON = (By.XPATH, "//button[text()='Confirm Alert']")
    AP_PROMPT_ALERT_BUTTON = (By.XPATH, "//button[text()='Prompt Alert']")
    AP_YOUR_NAME_TEXT = (By.XPATH, "//p[@id='myName']")
    AP_MODERN_ALERT_BUTTON = (By.XPATH, "//button[text()='Modern Alert']")
    AP_MODERN_ALERT_TEXT = (By.XPATH, "//div[@class='card-content']/p")
    AP_MODERN_ALERT_CLOSE_BUTTON = (By.XPATH, "//button[@class='modal-close is-large']")

    # SELECT PAGE
    SP_SELECT_FRUIT_DROPDOWN = (By.XPATH, "//select[@id='fruits']")
    SP_SELECT_FRUIT_TEXT = (By.XPATH, "//select[@id='fruits']//following::p[1]")
    SP_SELECT_MULTIPLE = (By.XPATH, "//select[@id='superheros']")
    SP_SELECT_MULTIPLE_TEXT = (By.XPATH, "//select[@id='superheros']//following::p[1]")






    # ****************************************************************************


    # ============================================================================
    # COMMON METHODS
    # ============================================================================
    @allure_step("Opening leetcode website")
    def open_leetcode_site(self):
        url = data("leetcode", "base_url")
        self.open_url(url)

    @allure_step("Verify current url: {expected_url}")
    def verify_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Incorrect url: Expected {expected_url}, but found {current_url}"

    @allure_step("Navigate back")
    def navigate_back(self):
        self.driver.back()

    # ============================================================================
    # HOMEPAGE BUTTON CLICKS
    # ============================================================================
    @allure_step("Click [Input] button")
    def click_input_button(self):
        self.click_element(self.HP_INPUT_BUTTON)

    @allure_step("Click [Button]")
    def click_button(self):
        self.click_element(self.HP_BUTTON)

    @allure_step("Click [Select] button")
    def click_select_button(self):
        self.click_element(self.HP_SELECT_BUTTON)

    @allure_step("Click [Alert] button")
    def click_alert_button(self):
        self.click_element(self.HP_ALERT_BUTTON)


    # ============================================================================
    # HOMEPAGE METHODS
    # ============================================================================
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
    # INPUT METHODS
    # ============================================================================
    @allure_step("Verify full name placeholder text: '{expected_text}'")
    def verify_full_name_placeholder_text(self, expected_text):
        actual_text = self.find_web_element(self.IP_FULL_NAME_TEXTBOX).get_attribute('placeholder')
        assert actual_text == expected_text, \
            f"Placeholder text mismatch: Expected text '{expected_text}', but found '{actual_text}'"


    @allure_step("Enter text to full name textbox: '{text}'")
    def enter_text_to_full_name_textbox(self, text):
        self.enter_text(self.IP_FULL_NAME_TEXTBOX, text)


    @allure_step("Verify text inside the textbox: '{expected_text}'")
    def verify_text_inside_the_textbox(self, expected_text):
        actual_text = self.find_web_element(self.IP_INSIDE_TEXTBOX).get_attribute('value')
        assert actual_text == expected_text, \
            f"Text mismatch: Expected text '{expected_text}', but found '{actual_text}'"


    @allure_step("Clear textbox")
    def clear_textbox(self):
        textbox = self.find_web_element(self.IP_CLEAR_TEXTBOX)
        text_value = textbox.get_attribute('value')
        self.log.info(f"Before clearing text: text_value = {text_value}")
        assert text_value != "", f"Textbox is empty"

        textbox.clear()
        text_value = textbox.get_attribute('value')
        self.log.info(f"After clearing text: text_value = {text_value}")
        assert text_value == "", f"Textbox should be empty, but found '{text_value}'"


    @allure_step("Verify textbox is disabled")
    def verify_textbox_is_disabled(self):
        textbox = self.find_web_element(self.IP_DISABLED_TEXTBOX)
        is_textbox_disabled = textbox.get_attribute('disabled')
        self.log.info(f"is_textbox_disabled = {is_textbox_disabled}")
        assert is_textbox_disabled, f"Textbox should be disabled: is_textbox_disabled '{is_textbox_disabled}'"


    @allure_step("Verify textbox is read only")
    def verify_textbox_is_read_only(self):
        textbox = self.find_web_element(self.IP_READ_ONLY_TEXTBOX)
        is_textbox_readonly = textbox.get_attribute('readonly')
        self.log.info(f"is_textbox_readonly = {is_textbox_readonly}")
        assert is_textbox_readonly, f"Textboxt should be read only: is_textbox_readonly = {is_textbox_readonly}"


    # ============================================================================
    # BUTTON METHODS
    # ============================================================================
    @allure_step("Verify Goto Home button")
    def click_goto_home_button(self):
        self.click_element(self.BP_GOTO_HOME_BUTTON)


    @allure_step("Verify button location")
    def verify_button_location(self):
        element = self.find_web_element(self.BP_FIND_LOCATION_BUTTON)
        location = element.location
        x = location['x']
        y = location['y']
        self.log.info(f"Location x:{x}, y:{y}")

        # attach additional info
        allure.attach(
            f"Location x:{x}, y:{y}",
            name="Location Info",
            attachment_type=allure.attachment_type.TEXT
        )


    @allure_step("Verify button color: {color}")
    def verify_button_color(self, expected_color):
        button = self.find_web_element(self.BP_WHAT_IS_MY_COLOR_BUTTON)
        bg_color = button.value_of_css_property("background-color")
        hex_color = Color.from_string(bg_color).hex

        self.log.info(f"Background Color (Rgb): {bg_color}")
        self.log.info(f"Background Color (Hex): {hex_color}")

        assert hex_color == expected_color.lower(), \
            f"Button background color mismatch: Expected '{expected_color}', but found '{hex_color}'"


    @allure_step("Verify button size")
    def verify_button_size(self):
        button = self.find_web_element(self.BP_HOW_TALL_AND_FAT_I_AM_BUTTON)
        size = button.size
        self.log.info(f"Button size: width: {size['width']}, height: {size['height']}")
        assert size['width'] > 0, f"Button width should be greater than 0"
        assert size['height'] > 0, f"Button height should be greater than 0"

        allure.attach(
            f"Button size: width:{size['width']}, height:{size['height']}",
            name="Button size info",
            attachment_type=allure.attachment_type.TEXT
        )


    @allure_step("Verify button is disabled")
    def verify_button_is_disabled(self):
        button = self.find_web_element(self.BP_DISABLED_BUTTON)
        assert not button.is_enabled(), f"Button should be disabled"


    @allure_step("Verify button click and hold: text_before '{text_before}', text_after '{text_after}'")
    def verify_button_click_and_hold(self, text_before, text_after):
        button = self.find_web_element(self.BP_HOLD_BUTTON)
        assert button.text == text_before, f"Button text should be '{text_before}'"

        actions = ActionChains(self.driver)
        actions.click_and_hold(button).perform()
        self.wait_seconds(2)
        actions.release(button).perform()
        assert button.text == text_after, f"Button text should be '{text_after}'"


    # ============================================================================
    # SELECT METHODS
    # ============================================================================
    @allure_step("Verify dropdown option list: {option_list}")
    def verify_dropdown_option_list(self, option_list=""):
        dropdown = self.find_web_element(self.SP_SELECT_FRUIT_DROPDOWN)
        dropdown_options = dropdown.find_elements(By.TAG_NAME, 'option')

        # for option in dropdown_options:
        #     self.log.info(f"option: {option.text}")

        # for i in range(len(dropdown_options)):
        #     self.log.info(f"option[{i+1}]: {dropdown_options[i+1].text}")

        for index, option in enumerate(dropdown_options, start=0):
            self.log.info(f"Assert options[{index}]: {option.text}")
            # self.log.info(f"Assert options[{index}]: {option.text} == {option_list[index]}")
            # assert option.text == option_list[index-1], f"Option mismatch: Expected '{option.text}', but found '{option_list[index-1]}'"





    @allure_step("Verify dropdown select by visible text: option='{option}', message='{message}'")
    def verify_dropdown_select_by_visible_text(self, option, message):
        select = self.find_web_element(self.SP_SELECT_FRUIT_DROPDOWN)
        dropdown = Select(select)
        dropdown.select_by_visible_text(option)

        fruit_message = self.find_web_element(self.SP_SELECT_FRUIT_TEXT).text
        assert fruit_message == message, f"Message mismatch. Expected '{message}', but found '{fruit_message}'"

    @allure_step("Verify dropdown select multiple: option='{option}', message='{message}'")
    def verify_dropdown_select_multiple(self, option, message):
        select = self.find_web_element(self.SP_SELECT_MULTIPLE)
        dropdown = Select(select)
        dropdown.select_by_visible_text(option)

        multiple_text = self.find_web_element(self.SP_SELECT_MULTIPLE_TEXT).text
        assert multiple_text == message, f"Message mismatch. Expected '{message}', but found '{multiple_text}'"




    # ============================================================================
    # ALERT METHODS
    # ============================================================================
    @allure_step("Verify Alert - Accept: '{expected_text}'")
    def verify_alert_accept(self, expected_text):
        self.click_element(self.AP_SIMPLE_ALERT_BUTTON)

        # wait for alert popup
        self.wait.until(EC.alert_is_present())

        # switch to alert popup
        alert = self.driver.switch_to.alert

        # get alert text
        alert_text = alert.text
        self.log.info(f"Alert text: {alert_text}")

        assert alert_text == expected_text, f"Alert text mismatch. Expected '{expected_text}', but found '{alert_text}'"
        self.wait_seconds(1)

        alert.accept()


    @allure_step("Verify Alert - Confirm")
    def verify_alert_confirm(self):
        self.click_element(self.AP_CONFIRM_ALERT_BUTTON)
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.wait_seconds(1)
        alert.accept()


    @allure_step("Verify Alert - Dismiss")
    def verify_alert_dismiss(self):
        self.click_element(self.AP_CONFIRM_ALERT_BUTTON)
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.wait_seconds(1)
        alert.dismiss()

    @allure_step("Verify Alert - Textbox")
    def verify_alert_textbox(self, name):
        self.click_element(self.AP_PROMPT_ALERT_BUTTON)
        alert = self.driver.switch_to.alert
        self.wait_seconds(1)

        alert.send_keys(name)
        self.wait_seconds(1)
        alert.accept()

        your_name_text = self.find_web_element(self.AP_YOUR_NAME_TEXT).text
        expected_text = f"Your name is: {name}"
        assert your_name_text == expected_text, \
            f"Text mismatch. Expected '{expected_text}', but found '{your_name_text}'"


    @allure_step("Verify Alert - Modern Alert")
    def verify_alert_modern(self, expected_text):
        self.click_element(self.AP_MODERN_ALERT_BUTTON)
        alert_text = self.find_web_element(self.AP_MODERN_ALERT_TEXT).text
        self.log.info(f"Alert text: {alert_text}")

        assert alert_text == expected_text, f"Alert text mismatch. Expected '{expected_text}', but found '{alert_text}'"
        self.click_element(self.AP_MODERN_ALERT_CLOSE_BUTTON)
        self.wait_seconds(1)







