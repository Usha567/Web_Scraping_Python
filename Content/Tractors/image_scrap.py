import time
import urllib
import os
import re
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

driver.get('https://www.tractorjunction.com/')

wait = WebDriverWait(driver, 15)
driver.execute_script('window.scrollTo(0, 500)')

nav_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.navbar-nav>li>a#navbarDropdown1')))
nav_bar.click()
time.sleep(1)

dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-labelledby='navbarDropdown1']/ul/li/a[@title='All Tractors']")))
dropdown_menu.click()
time.sleep(2)

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
cylinder=[]
hp_category=[]
pto_hp=[]
gear_box=[]
brakes=[]
warranty=[]
price=[]
about_list=[]
# feature_list=[]

engine_capaity=[]
engine_rpm=[]
engine_cooling=[]
engine_airfilter=[]
engine_fuelpump=[]
engine_torque=[]

transmission_type=[]
transmission_clutch=[]
transmission_fspeed=[]
transmission_rspeed=[]
transmission_gear=[]
transmission_battery=[]
transmission_alternator=[]

steering_type=[]
steering_column=[]

power_take_type =[]
power_take_rpm=[]

total_weight=[]
wheel_base=[]
overall_length=[]
overall_width =[]
ground_clearance=[]
turning_radius=[]

hydraulics_cap=[]
hydraulics_linkage=[]

wheel_drive = []
front_tyres=[]
rear_tyres=[]

accessories_list=[]
additional_feature=[]
warranty_status =[]
status=[]
image_list=[]
images_name=[]

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

   #100-180
#    122
    for i in range(50,100):
        print('looping start...i-', i)

        try:
            try:
                print('click on image..///')
                new_tractor = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                "div#tractorMoreData div:nth-child("+str(i)+")>div.new-tractor-main>div.new-tractor-img>a>img")))
                new_tractor.click()
                time.sleep(2)

                modal=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                close_modal= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                close_modal.click()
            except TimeoutException as e:
                print('TimeoutException for close btn..///..//')   

            brand = driver.find_element(By.CSS_SELECTOR, "div.product-single-features-inner>p>a").text
            brand_list.append(brand)

            model_name=[]
            model = driver.find_element(By.XPATH, "//li[@itemprop='itemListElement']/span[@itemprop='name']").text
            model_list.append(model)

            model_name_ = driver.find_element(By.CSS_SELECTOR, 
            "div.product-single-top>div.product-tooltip>h1").text
            model_name.append(model_name_)

            # image_list
            tractor_images = driver.find_elements(By.CSS_SELECTOR, "div.slider div.slick-list div.slick-track div.slick-slide>img")
            src =[]

            for img in tractor_images:
                if len(src) < 4:
                    src.append(img.get_attribute('src'))
            image_list.append(src)

            dirname = (((brand.split('Tractors')[0]).capitalize()).strip())+"_"+str(i)+"_"+model
            print('dirname-', dirname)
            os.mkdir(dirname) 

            imagename_list=[]
            for i in range((len(src))):
                if(src[i] != ''):
                    path = urlparse(src[i]).path
                    extension = os.path.splitext(path)[1]
                    name = os.path.splitext(path)[0]
                    img_name = "img"+str(i)+"-"+name[name.rfind("/") + 1:]
                    imagename_list.append(img_name+'.png'.format(i))
                    urllib.request.urlretrieve(str(src[i]), dirname+"/"+img_name+'.png'.format(i))
        
            images_name.append(imagename_list)
            # driver.back()
            time.sleep(2)

            nav_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.navbar-nav>li>a#navbarDropdown1')))
            nav_bar.click()
            time.sleep(1)

            dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-labelledby='navbarDropdown1']/ul/li/a[@title='All Tractors']")))
            dropdown_menu.click()
            time.sleep(2)

            try:
                print('load_more_again..')
                close_modal= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                close_modal.click()
                time.sleep(2)

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

            except TimeoutException as e:
                print('TimeoutException for load more btn..//')    

        except ElementClickInterceptedException:
            print('ElementClickInterceptedException+++....')
        except TimeoutException as e:
            print('TimeoutException for loop-///+++')

    time.sleep(1) 

print('images_name//////-', images_name)

data_dict = {
    'Brand':brand_list,
    'Model':model_list,
    'Images':images_name
}
df=pd.DataFrame.from_dict(data_dict, orient="index")
df= df.transpose()

writer = pd.ExcelWriter('Tractor_Image_Infos.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()