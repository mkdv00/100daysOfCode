from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "F:\Download\Drivers\chromedriver"
TWITTER_PHONE = "89197834756"
TWITTER_PASSWORD = "DickHead_228"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        sleep(3)
        start_btn = self.driver.find_element_by_class_name("start-button")
        start_btn.click()

        sleep(60)
        self.down = self.driver.find_element_by_class_name("download-speed").text
        self.up = self.driver.find_element_by_class_name("upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")

        sleep(2)
        login_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main'
                                                        '/div/div/div[2]/form/div/div[1]')
        login_input.send_keys(TWITTER_PHONE)
        pass_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div'
                                                       '/div/div[2]/form/div/div[2]')
        pass_input.send_keys(TWITTER_PASSWORD)
        sleep(2)
        pass_input.send_keys(Keys.ENTER)

        sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/di'
            'v/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when " \
                f"I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]'
            '/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
