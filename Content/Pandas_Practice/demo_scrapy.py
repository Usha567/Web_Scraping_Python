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
for page in range(1,3,1 ):
    page_url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page='+str(page)

    driver = webdriver.Chrome()
    driver.get(page_url)

    title = driver.find_elements(By.CLASS_NAME, 'title')
    price = driver.find_elements(By.CLASS_NAME, 'price') 
    description = driver.find_elements(By.CLASS_NAME, 'description')
    rating = driver.find_elements(By.CLASS_NAME, 'ratings')

    for i in range(len(title)):
        title_list.append(title[i].text) 
        price_list.append(price[i].text) 
        description_list.append(description[i].text)
        rating_list.append(rating[i].text)
        # element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

df = pd.DataFrame({
    'title':title_list,
    'price':price_list,
    'description':description_list,
    'ratings':rating_list
})

writer = pd.ExcelWriter('pandas_Sample2.xlsx', engine='xlsxwriter')

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













#Using ExcelWrite

# print('element_list-', element_list)

# with xlsxwriter.Workbook('result3.xlsx') as workbook:
#     worksheet = workbook.add_worksheet()

#     header_data = ['Product_Name', 'Price', 'Description', 'Ratings']
#     header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04' })

#     # for col_num, data in enumerate(header_data):
#     #     worksheet.write(0, col_num, data, header_format)

#     for row_num, data in enumerate(element_list):
#         print('row_num-', row_num, data)
#         worksheet.write_row(row_num,1,data)

driver.close()


