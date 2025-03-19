import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class Driver:
    def __init__(self, url):
        self.driver = self._create_driver(url)

    def navigate(self, url, wait=3):
        self.driver.get(url)
        time.sleep(wait)

    def scroll_to_bottom(self, wait=3):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait)

    def get_element(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def get_elements(self, selector):
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def fill_text_field(self, selector, text):
        element = self.get_element(selector)
        element.clear()
        element.send_keys(text)

    def click_button(self, selector):
        element = self.get_element(selector)
        element.click()

    def _create_driver(self, url):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        return driver

    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def get_cookies(self):
        return self.driver.get_cookies()

    def close(self):
        self.driver.close()
