from selenium import webdriver

chrome_driver_path = "F:\Download\Drivers\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))

driver.quit()
