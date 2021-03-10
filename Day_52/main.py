from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = "F:\Download\Drivers\chromedriver"
SIMILAR_ACCOUNT = "python.hub"
USERNAME = ""
PASSWORD = ""


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(3)
        not_now_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_btn.click()

        sleep(1)
        notification_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification_btn.click()

    def find_followers(self, group_name: str):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{group_name}")

        sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(3)

    def follow(self):
        sleep(2)
        follow_buttons = self.driver.find_elements_by_xpath('//button[text()="Follow"]')
        for btn in follow_buttons:
            try:
                btn.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_btn.click()


insta_bot = InstaFollower(CHROME_DRIVER_PATH)
insta_bot.login()
insta_bot.find_followers(SIMILAR_ACCOUNT)
insta_bot.follow()
