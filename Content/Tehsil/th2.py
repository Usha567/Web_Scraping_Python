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
from selenium.common.exceptions import ElementClickInterceptedException,StaleElementReferenceException, NoSuchElementException,TimeoutException 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome()

driver.get('https://igod.gov.in/district/jr6_uIsBC8DLsKxJUVLd/sub_districts')

wait = WebDriverWait(driver, 10)
state_list=[]
district_list=[]
tehsil_list =[]
# state_divs = driver.find_elements(By.CSS_SELECTOR, 'div.grid-content div.cat-box.state>ul>li')

# for div in state_divs:
#     state_item = div.find_element(By.CSS_SELECTOR, 'a').text
#     state_list.append(state_item)

# print('length-', len(state_divs))
for i in  range(1,2):
    print('i--', i)
    try:
        # st=driver.find_element(By.CSS_SELECTOR, "div.grid-content div.cat-box.state>ul>li:nth-child("+str(i)+")>a").text
        # print('enter state..', st)
        # state_item=WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.grid-content div.cat-box.state>ul>li:nth-child("+str(i)+")>a")))
        # # state_item = div.find_element(By.CSS_SELECTOR, 'a')
        # state_item.click()
        # print('clicked state..')

   
        # div_text = driver.find_element(By.CSS_SELECTOR, "div.cat-post-container div.row>div:nth-child(5)>div.cat-box a>strong").text
        # print('div_text- ', div_text) 
        # state_divs = driver.find_elements(By.CSS_SELECTOR, "div.cat-post-container>div.row>div")
        # print(' len(state_divs)-- ',  len(state_divs))
        # for i in range(1, len(state_divs)):
        #     div_h3=driver.find_element(By.CSS_SELECTOR, "div.cat-post-container div.row>div:nth-child("+str(i)+")>div.cat-box>h3").text
        #     print('div_h3-/// ', div_h3)
        #     if div_h3 == 'Districts':
        #         print('div_h3 dist here...', i)
        #         try:
        #             a_tag = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.cat-post-container div.row>div:nth-child("+str(i)+")>div.cat-box a>strong")))
        #             a_tag.click() 
        #         except NoSuchElementException as e:
        #             print('no view all +++....') 
        #         except TimeoutException as e:
        #             print('TimeoutException for button a_tag..///..//')         
        # # state_divs.click()  

        # print('clicked cate////') 

        # dist_divs = driver.find_elements(By.CSS_SELECTOR, 'div.grid-content div.search-content>div.search-row')          
        # print('distDivs...')
        # distlist=[]
        # for div2 in dist_divs:    
        #     try:    
        #         dist = div2.find_element(By.CSS_SELECTOR, "div.search-result-row>a").text
        #         print('each dist-', dist) 
        #         district_list.append(dist)
        #         tensil_div = div2.find_element(By.CSS_SELECTOR, "div.search-result-row div.search-opts>a:nth-child(1)")
        #         tensil_div.click()

        tehsil_divs = driver.find_elements(By.CSS_SELECTOR, 'div.grid-content div.search-content>div.search-row')
        print('tehsilDivs//')
        tehsillist=[]
        for tehsil_div in tehsil_divs:        
            tehsil_ = tehsil_div.find_element(By.CSS_SELECTOR, "div.search-result-row>div.search-title").text
            print('each tehsil-', tehsil_) 
            tehsillist.append(tehsil_)
        tehsil_list.append(tehsillist)    
        # driver.back() 
        time.sleep(2)
            # except NoSuchElementException as e:
            #     print('no such element.///..//')    
          

            # print('length===', len(state_list), len(distlist))
            # time.sleep(2)
            # driver.back() 
            # time.sleep(2)
            # driver.back() 
            # time.sleep(2)
       
            # except TimeoutException as e:
            #     print('TimeoutException for state_item btn..///..//') 
            # except ElementClickInterceptedException:
            #     print('ElementClickInterceptedException+++....')
            # except StaleElementReferenceException as e:
            #     print('Exception occurred during object identification.')

    except TimeoutException as e:
        print('TimeoutException for state_item btn..///..//') 
    except ElementClickInterceptedException:
        print('ElementClickInterceptedException+++....')
    except StaleElementReferenceException as e:
        print('Exception occurred during object identification.')
    # print('clicked on state...')
  
time.sleep(2)

# print('district_list//////-', district_list, len(district_list), len(tehsil_list))
data_dict = {
    # 'state':state_list,
    'district':district_list,
    'tehsil':tehsil_list
}
df=pd.DataFrame.from_dict(data_dict, orient="index")
df= df.transpose()

writer = pd.ExcelWriter('tehsil22.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()
