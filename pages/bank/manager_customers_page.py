import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.bank.header_page import HeaderPage
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step


class ManagerCustomersPage(HeaderPage):

    # Locators
    CUSTOMERS_TABLE = (By.XPATH, "//table/tbody/tr")




    # Functions
    # Helper method for is_customer_exists
    def get_all_customers(self):
        table_customer = self.find_web_elements(self.CUSTOMERS_TABLE)

        all_customers = []

        for row_customer in table_customer:
            cells = row_customer.find_elements(By.TAG_NAME, "td")
            customer = {
                'first_name': cells[0].text,
                'last_name': cells[1].text,
                'post_code': cells[2].text,
                'account_number': cells[4].text,
            }
            all_customers.append(customer)
            # self.log.info(f"customer: {customer}")

        return all_customers


    @allure_step("Check new customer record is in the table")
    def is_customer_exists(self, first_name, last_name, post_code):
        all_customers = self.get_all_customers()
        for customer in all_customers:
            if (first_name in customer['first_name']
                    and last_name in customer['last_name']
                    and post_code in customer['post_code']):
                self.log.info(f"Customer exists: {first_name}, {last_name}, {post_code}")
                return True
        self.log.error(f"Customer not exists")
        return False













