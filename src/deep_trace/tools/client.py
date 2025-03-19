import os
import time
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from .driver import Driver

class LinkedinClient:
    def __init__(self):
        self.url = "https://linkedin.com/"
        self.cookie_name = "li_at"
        self.username = os.environ.get("LINKEDIN_USERNAME")
        self.password = os.environ.get("LINKEDIN_PASSWORD")
        self.driver = Driver(self.url)
        self.cookie = self._get_or_create_cookie()
        self.driver.add_cookie(self.cookie)

    def _get_or_create_cookie(self):
        if os.environ.get("LINKEDIN_COOKIE"):
            return {"name": self.cookie_name,
                    "value": os.environ["LINKEDIN_COOKIE"]}
        elif self._check_existing_cookie():
            return self._check_existing_cookie()
        else:
            return self.login_and_get_cookie()

    def _check_existing_cookie(self):
        cookies = self.driver.get_cookies()
        return next(
            (cookie for cookie in cookies if cookie["name"] == self.cookie_name),
            None,
        )

    def _login_and_get_cookie(self):
        try:
            self.driver.navigate("https://www.linkedin.com/login?fromSignIn=true&amp;trk=guest_homepage-basic_nav-header-signin")
            time.sleep(1)

            username_field = self.driver.get_element("#username")
            password_field = self.driver.get_element("#password")
            login_button = self.driver.get_element("button[type='submit']")
            time.sleep(1)
            username_field.send_keys(self.username)
            password_field.send_keys(self.password)
            login_button.click()

            time.sleep(1)

            cookies = self.driver.get_cookies()
            for cookie in cookies:
                if cookie["name"] == self.cookie_name:
                    return cookie
        except Exception as e:
            raise Exception(f"Failed to retrieve LinkedIn cookie. Error: {e}")

    def find_people(self, name):
        search = name
        encoded_string = urllib.parse.quote(search.lower())
        url = f"https://www.linkedin.com/search/results/people/?keywords={encoded_string}"
        self.driver.navigate(url)

        people = self.driver.get_elements("ul li div div.linked-area")
        results = []
        for person in people:
            try:
                result = {
                    "profile_photo": person.find_element(By.CSS_SELECTOR, "img.presence-entity__image").get_property('src'),
                    "name": person.find_element(By.CSS_SELECTOR, "a[data-test-app-aware-link] > span > span").text,
                    "position": person.find_elements(By.CSS_SELECTOR, "div.t-14.t-normal")[0].text,
                    "location": person.find_elements(By.CSS_SELECTOR, "div.t-14.t-normal")[1].text,
                    "profile_link": person.find_element(By.CSS_SELECTOR, "a[data-test-app-aware-link]").get_attribute("href")
                }
                results.append(result)
            except Exception:
                continue
        return results

    def close(self):
        self.driver.close()
