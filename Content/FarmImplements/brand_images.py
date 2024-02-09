import time
import urllib
import os
import errno
import re
from rembg import remove 
from PIL import Image , ImageFont, ImageDraw
from urllib.parse import urlparse
import xlsxwriter
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException,TimeoutException 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome()

driver.get('https://www.tractorjunction.com/all-brands/')

wait = WebDriverWait(driver, 30)
try:
    tab = driver.find_element(By.CSS_SELECTOR, "ul#tractorbrands  li>a#Implements-tab")
    print('tab-', tab)
    driver.execute_script("arguments[0].scrollIntoView(true);", tab)
except ElementClickInterceptedException as e:
    print('intercepted...',e)
    # driver.execute_script("arguments[0].click();", brand_btn)   


# try:
#     harvester_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul#tractorbrands  li>a#Harvesters-tab")))
#     harvester_tab.click()
# except ElementClickInterceptedException as e:
#     print('interexception...')
#     driver.execute_script("arguments[0].click();", harvester_tab)
# except TimeoutException as e:
#     print('timeoutException for close external modal++++++...')     

try:
    brand_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Brand Button']")))
    brand_btn.click()
except ElementClickInterceptedException as e:
    print('exception...')
    driver.execute_script("arguments[0].click();", brand_btn)
except TimeoutException as e:
    print('timeoutException for close external modal///...')      


try:
    cross_model=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal.click()
    time.sleep(2)
except TimeoutException as e:
    print('timeoutException for close external modal...')    

brand_list=[]
image_list=[]
images_name=[]

# brand_divs = driver.find_elements(By.CSS_SELECTOR, 'div#brandstabcontent>div#Implements>div.section-css-slider div.tjcol.states-block')
# print('length-', len(brand_divs))
# for div in  brand_divs:
#     brand = div.find_element(By.CSS_SELECTOR, "div.brand-main>a p").text 
#     print('each brand-', brand) 
#     brand_list.append(brand)   
# print('brand_list-///',brand_list)      
tractor_images = driver.find_elements(By.CSS_SELECTOR, "div#brandstabcontent>div#Implements>div.section-css-slider div.tjcol.states-block div.brand-main>a")
src =[]

print('farmimplements_brnd_images-', len(tractor_images))
for a in tractor_images:
    img = a.find_element(By.CSS_SELECTOR, 'img.img-fluid')
    if img not in src:
        src.append(img.get_attribute('src'))
    brand = a.find_element(By.CSS_SELECTOR, 'p').text
    brand_list.append(brand)
image_list.append(src)

for i in range((len(src))):
    imagename_list=[]
    if(src[i] != ''):
        path = urlparse(src[i]).path
        extension = os.path.splitext(path)[1]
        name = os.path.splitext(path)[0]
        img_name = "img"+str(i)+"-"+name[name.rfind("/") + 1:]
        imagename_list.append(img_name+'.png'.format(i))
        images_name.append(imagename_list)
        urllib.request.urlretrieve(str(src[i]), "Images/"+img_name+'.png'.format(i))

time.sleep(1) 

print('brand_list//////-', brand_list, len(brand_list), len(images_name))

data_dict = {
    'Brand':brand_list,
    # 'Model':model_list,
    'Images':images_name
}
df=pd.DataFrame.from_dict(data_dict, orient="index")
df= df.transpose()

writer = pd.ExcelWriter('implements_brand_Images.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()
