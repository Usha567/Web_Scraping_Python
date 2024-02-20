import time
import urllib
import os
import shutil
from glob import glob
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
from selenium.common.exceptions import ElementClickInterceptedException,ElementNotInteractableException, NoSuchElementException,TimeoutException 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome()

driver.get('https://www.tractorjunction.com/escort-tractor/')

wait = WebDriverWait(driver, 15)

try:
    cross_model=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal.click()
    time.sleep(2)
except TimeoutException as e:
    print('timeoutException for close external modal...')    

new_tractors = driver.find_elements(By.CSS_SELECTOR,'div#tractorMoreData div.new-tractor-main>div.new-tractor-img>a>img')

# div#tractorMoreData  div.new-tractor-main>div.new-tractor-img>a>img')
print('new_tractors-',new_tractors,  len(new_tractors))
brand_list=[]
model_list=[]
tractor_price=[]

buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
if buttonText == 'Load More Tractors':
    print('enter if--')
    load_more = wait.until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))

    count=0
    buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
    while buttonText == 'Load More Tractors':
        buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')    
        if buttonText != 'Load More Tractors':
            break
        else:  
            try:
                count +=1
                print('count-', count)
                load_more = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
                driver.execute_script("arguments[0].click();", load_more)
                print('clicked on load')  
            except TimeoutException as e:
                print('TimeoutException for load more..')
    print('click3',count)

    # 140-150 left
    # Need to run this loop again file name is same 
    for i in range(1,2):
        print('looping start...i-', i)

        try:
            try:
                print('click on image..///')
                new_tractor = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                "div#tractorMoreData div:nth-child("+str(i)+")>div.new-tractor-main>div.new-tractor-img>a>img")))
                new_tractor.click()
                time.sleep(2)

                # modal=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                # close_modal= WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                # close_modal.click()
            except TimeoutException as e:
                print('TimeoutException for close btn..///..//')

            except ElementClickInterceptedException:
                print('ElementClickInterceptedException+++....')
                driver.execute_script("arguments[0].click();", new_harvester)     

            brand = driver.find_element(By.CSS_SELECTOR, "div.product-single-features-inner>p>a").text
            brand_list.append(brand)

            model_name=[]
            model = driver.find_element(By.XPATH, "//li[@itemprop='itemListElement']/span[@itemprop='name']").text
            model_list.append(model)

            print('brand_list-.... ', brand_list, model_list)
            #checking price
            print('checkpricebtn-', driver.find_element(By.CSS_SELECTOR,"div.new-right-cls div:nth-child(5)>div>div>span.requestModal").text)
            check_price = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.new-right-cls div:nth-child(5)>div>div>span.requestModal")))
            check_price.click()
            time.sleep(2)

            try:
                inputElement = driver.find_element(By.XPATH,"//form[@id='tractor_submit_form']/input[@placeholder='Enter Your Name']")
                inputElement.send_keys('1')
            except  ElementNotInteractableException as e:
                print('ElementNotInteractableException....++++ ')   

          
            driver.back()
            time.sleep(2)
            try:
                print('load_more_again..')
                load_more = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
                buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
                while buttonText == 'Load More Tractors':
                    buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')    
                    if buttonText != 'Load More Tractors':
                        break
                    else:  
                        load_more = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
                        driver.execute_script("arguments[0].click();", load_more)
                print('clicked on modal...///')
            except ElementClickInterceptedException as e:
                print('ElementClickInterceptedException---///')
                driver.execute_script("arguments[0].click()", load_more)
            except TimeoutException as e:
                print('TimeoutException for load more btn..//')
        except ElementClickInterceptedException:
            print('ElementClickInterceptedException+++....')
        except TimeoutException as e:
            print('TimeoutException for loop-///+++')
    time.sleep(1)
print('images_name//////-', model_list)

data_dict = {
    'Brand':brand_list,
    'Model':model_list,
    'Tractor_price':tractor_price
}
df=pd.DataFrame.from_dict(data_dict, orient="index")
df= df.transpose()

writer = pd.ExcelWriter('TractorPrice.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()




