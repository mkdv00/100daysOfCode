from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

facebook_email = "maksim.cudaew@gmail.com"
facebook_password = "needforspeed10012000"

chrome_driver_path = "F:\Download\Drivers\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://tinder.com/")

sleep(2)
# Find and click to login button
login_button = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                            'header/div/div[2]/div[2]/button')
login_button.click()

sleep(2)
# Find and click to facebook login
facebook_login = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login.click()
base_window = driver.window_handles[0]
facebook_window_handle = driver.window_handles[1]
driver.switch_to.window(facebook_window_handle)

# Add value ti inputs
facebook_login_entry = driver.find_element_by_id("email")
facebook_login_entry.send_keys(facebook_email)
facebook_password_entry = driver.find_element_by_id("pass")
facebook_password_entry.send_keys(facebook_password)
facebook_password_entry.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

sleep(5)

# Apply button find and click
apply_button = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[1]')
apply_button.click()

# Next apply button find and click
apply_button_two = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[2]')
apply_button_two.click()

# Agree button find and click
agree_button = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[2]/div/div/div[1]/button')
agree_button.click()

bot_on = True
while bot_on:
    sleep(1)
    try:
        # find like button
        like_button = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[1]/div/main/div'
                                                   '[1]/div/div/div[1]/div[1]/div[2]/div[4]')
        like_button.click()
    except NoSuchElementException:
        sleep(2)
    except ElementClickInterceptedException:
        try:
            driver.find_element_by_css_selector(".itsAMatch a").click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
