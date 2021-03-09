from selenium import webdriver

chrome_driver_path = "F:\Download\Drivers\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.python.org")

events_dict = {}

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

driver.quit()
