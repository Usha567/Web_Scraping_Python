import time
import urllib
import os
from urllib.parse import urlparse
import xlsxwriter
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


title_list =[]
price_list=[]
description_list = []
rating_list=[]

page_url = 'https://www.tractorjunction.com/tractors/'

driver = webdriver.Chrome()
driver.get(page_url)

title = driver.find_element(By.CSS_SELECTOR, 'div.product-single-top>div.section-heading>h1')
.text

# price = driver.find_elements(By.CLASS_NAME, 'price') 
# description = driver.find_elements(By.CLASS_NAME, 'description')
# rating = driver.find_elements(By.CLASS_NAME, 'ratings')

# print('title-', title)
# for i in range(len(title)):
#     title_list.append(title[i].text) 
    # price_list.append(price[i].text) 
    # description_list.append(description[i].text)
    # rating_list.append(rating[i].text)
    # element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

df = pd.DataFrame({
    'title':[title],
    # 'price':price_list,
    # 'description':description_list,
    # 'ratings':rating_list
})
print('df-', df)

writer = pd.ExcelWriter('Tractor_Info.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook=writer.book
worksheet = writer.sheets['Sheet1']

#header_format
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

#write column header with define format
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    

driver.close()


