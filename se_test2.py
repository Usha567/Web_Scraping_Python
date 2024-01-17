import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.tractorjunction.com/tractors/')

# city = driver.find_element(By.XPATH,"//select[@name='state_id']")
# all_option = city.find_elements(By.TAG_NAME, 'option')
# for opt in all_option:
#     print('opt-', opt.get_attribute('innerHTML'))
#     opt.click()
    # district = driver.find_element(BY.XPATH, "//select[@name='dist_id']")
    # all_dist = district.find_elements(BY.TAG_NAME, 'option')
    # for dist in all_dist:
    #     print('\ndist-', dist.get_attribute('innerHTML'))

# time.sleep(120) #sleep that no of second




#AUto SCroll
# button.location_once_scrolled_into_view
# driver.execute_script("return arguments[0].scrollIntoView()", button)