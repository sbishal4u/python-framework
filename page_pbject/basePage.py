import string
from random import *

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 120)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def clear_the_box(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys()

    def send_keys(self, by_locator, value):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def wait_for_element(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator))

    def get_element_height(self, by_locator):
        elm = self.wait.until(EC.presence_of_element_located(by_locator))
        return elm.size['height']

    def getEls(self, by_locator):
        return len(self.wait.until(EC.presence_of_all_elements_located(by_locator)))

    def get_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def wait_for(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_Element_Base_on_text(self, text):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'" + text + "')]")

    def clear_box(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()

    def scroll_the_page_down(self):
        self.driver.execute_script(
            "var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")

    def scroll_the_page_up(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

    def scroll_hal(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_the_page_to_element(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def enter_keys(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def escape_keys(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ESCAPE)

    def go_to_action(self, by_locator):
        action = ActionChains(self.driver)
        action.move_to_element(by_locator).click()

    def go_to_hover(self, byLocator):
        actions = ActionChains(self.driver)
        actions.move_to_element(byLocator)

    def click_java_script(self, by_locator):
        self.driver.execute_script("arguments[0].click();", by_locator)

    def get_random_string(self, length):
        result_str = ''.join(choice(string.ascii_letters) for i in range(length))
        return result_str
