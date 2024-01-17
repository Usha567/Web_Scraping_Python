import time
import urllib
import os
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

os.mkdir('Bullz_Power')


driver = webdriver.Chrome()

driver.get('https://www.tractorjunction.com/tractor-implements/?shortBy=&brands=217&impType=&impCat=')

wait = WebDriverWait(driver, 10)

driver.execute_script('window.scrollTo(0, 1200)')

# close_modal= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.tj-product-list-popup span.list_close")))
# close_modal.click()

# buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
# while buttonText == 'Load More Implements':
#     buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
#     if buttonText != 'Load More Implements':
#         break
#     else:    
#         try:
#             load_more = wait.until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
#             load_more.click()
#             images = driver.find_elements(By.CSS_SELECTOR, "div.implement-img>a>img.img-fluid")
#             print('images-', type(images), len(images)) 
#             time.sleep(.5)
#         except ElementClickInterceptedException:
#             print('Tring to click on button again')
#             driver.execute_script("arguments[0].click()", load_more)
#             time.sleep(.5)

images = driver.find_elements(By.CSS_SELECTOR, "div.implement-img>a>img.img-fluid")
print('images-', type(images), len(images))  

print('image_list-', len(images))
src = [] 
for img in images:
    src.append(img.get_attribute('src'))    

print('src-', len(src)) 
for i in range((len(src))):
    # print('src[i]-',i,  src[i])
    if(src[i] != ''):
        path = urlparse(src[i]).path
        extension = os.path.splitext(path)[1]
        name = os.path.splitext(path)[0]
        img_name = "img"+str(i)+"-"+name[name.rfind("/") + 1:]
        urllib.request.urlretrieve(str(src[i]), "Bullz_Power/"+img_name+extension.format(i))
    
   