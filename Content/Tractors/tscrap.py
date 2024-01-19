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

buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
if buttonText == 'Load More Tractors':
    print('enter if--')
    load_more = wait.until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
    # load_more.click()
    # print('clicked1//...')
    # time.sleep(1)
    # load_more.click()

    # time.sleep(1)
    # load_more.click()
    # time.sleep(1)
    # load_more.click()
    # time.sleep(1)
    # load_more.click()
    # time.sleep(1)
    # load_more.click()
    # time.sleep(1)
    # load_more.click()
    # time.sleep(1)
    # load_more.click()
    # time.sleep(1)
    # load_more.click()

    count=0
    buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
    while buttonText == 'Load More Tractors':
        buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')    
        if buttonText != 'Load More Tractors':
            break
        else:  
            count +=1
            print('count-', count)
            load_more = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
            driver.execute_script("arguments[0].click();", load_more)
            print('clicked on load')  
    print('click3',count)


    for i in range(100, 180):
        print('looping start...i-', i)

        try:
            try:

                print('click on image..///')
                new_tractor = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                "div#tractorMoreData div:nth-child("+str(i)+")>div.new-tractor-main>div.new-tractor-img>a>img")))
                new_tractor.click()
                time.sleep(2)

                modal=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                close_modal= WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                close_modal.click()

                # modal_= WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.modal-dialog div.modal-content>span.close")))
                # modal_close= WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.modal-dialog div.modal-content>span.close")))
                # modal_close.click()

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


            feature = driver.find_elements(By.CSS_SELECTOR, "div.product-single-features-inner")
            feature_list =['','','']
            feature_ans_list=['','','']

            print('feature l-',len(feature))

            for jj in range(3, len(feature)+2):
                ele = driver.find_element(By.CSS_SELECTOR,
                    "div.product-single-features-inner:nth-child("+str(jj)+")>h5").text
                feature_list.append(ele)
                element = driver.find_element(By.CSS_SELECTOR,
                        "div.product-single-features-inner:nth-child("+str(jj)+")>p").text
                feature_ans_list.append(element)
            print('feature_list-',feature_list) 
            try:
                if 'No. Of Cylinder'  in  feature_list:
                    index=feature_list.index('No. Of Cylinder')
                    cylinder.append(feature_ans_list[index]) 
                else:
                    cylinder.append('')

                if 'HP Category'  in  feature_list:
                    index=feature_list.index('HP Category')
                    hp_category.append(feature_ans_list[index])  
                else:
                    hp_category.append('')

                if 'PTO HP'  in  feature_list:
                    index=feature_list.index('PTO HP')
                    pto_hp.append(feature_ans_list[index])  
                else:
                    pto_hp.append('') 

                if 'Gear Box'  in  feature_list:
                    index=feature_list.index('Gear Box')
                    gear_box.append(feature_ans_list[index]) 
                else:
                    gear_box.append('')

                if 'Brakes'  in  feature_list:
                    index=feature_list.index('Brakes')
                    brakes.append(feature_ans_list[index]) 
                else:
                    brakes.append('')   

                if 'Warranty' in  feature_list:
                    index=feature_list.index('Warranty')
                    warranty.append(feature_ans_list[index])  
                else:
                    warranty.append('')   

                if 'Price' in  feature_list:
                    index=feature_list.index('Price')
                    price.append(feature_ans_list[index])  
                else:
                    price.append('')
            except NoSuchElementException as e:
                print('no features..') 

            about=driver.find_element(By.CSS_SELECTOR, 'div.product_description_main').text
            about_list.append(about)

            
            tab_ele =driver.find_elements(By.CSS_SELECTOR,"div.acc-container div.acc")
            tab_text_list=['','']   

            print('tab_ele-', len(tab_ele)) 

            for ii in range(2, len(tab_ele)+2):
                print('i-', i, ii)
                tab_text =  driver.find_element(By.CSS_SELECTOR,
                    "div.acc-container div.acc:nth-child("+str(ii)+")").text
                tractor_model = model_name[0]+' ' 
                print('tab_text-',tractor_model,  tab_text, re.split(tractor_model, tab_text))
                t=re.split(tractor_model, tab_text)[1]
                tab_text_list.append(t)

            print('tab_text_list-', tab_text_list)

            if 'Engine' in tab_text_list:
                el_index = tab_text_list.index('Engine')
                print('in-', el_index)
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                    "div.acc-container div.acc:nth-child("+str(el_index)+")")))
                element.click()
                time.sleep(.5)
                ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")     
                tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")

                child_text_list =['','','']
                chlid_ans_list=['','','']
                for ll in range(1,(len(tr)+1)):
                    print('ll-', ll)
                    text1=ele.find_element(By.CSS_SELECTOR, 
                    "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    child_text_list.append(text1)
                    text = ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    chlid_ans_list.append(text)
                print('engine child_text_list-', child_text_list,chlid_ans_list)

                try:
                    if('Capacity CC' in child_text_list):
                        index =  child_text_list.index('Capacity CC')
                        engine_capaity.append(chlid_ans_list[index])
                    else:
                        engine_capaity.append('')

                    if('Engine Rated RPM' in child_text_list):
                        index =  child_text_list.index('Engine Rated RPM')
                        engine_rpm.append(chlid_ans_list[index])
                    else:
                        engine_rpm.append('')

                    if('Cooling' in child_text_list):
                        index =  child_text_list.index('Cooling')
                        engine_cooling.append(chlid_ans_list[index])
                    else:
                        engine_cooling.append('')

                    if('Air Filter' in child_text_list):
                        index =  child_text_list.index('Air Filter')
                        engine_airfilter.append(chlid_ans_list[index]) 
                    else:
                        engine_airfilter.append('')  

                    if('Fuel Pump' in child_text_list):
                        index =  child_text_list.index('Fuel Pump')
                        engine_fuelpump.append(chlid_ans_list[index])
                    else:
                        engine_fuelpump.append('')

                    if('Torque' in child_text_list):
                        index =  child_text_list.index('Torque')
                        engine_torque.append(chlid_ans_list[index]) 
                    else:
                        engine_torque.append('')  
                except NoSuchElementException as e:
                    print('no engine')
            else:
                print('else engine')

            if 'Transmission' in tab_text_list:
                el_index = tab_text_list.index('Transmission')
                print('in-', el_index)
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")))
                element.click()
                time.sleep(.5)
                ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")     
                tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")
                
                child_text_list =[]
                chlid_ans_list=[]
                for ll in range(1,(len(tr)+1)):
                    print('ll-', ll)
                    text1=ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    child_text_list.append(text1)
                    text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    chlid_ans_list.append(text)
                print('transmission child_text_list-', child_text_list)

                try:
                    if('Type' in child_text_list):
                        index =  child_text_list.index('Type')
                        transmission_type.append(chlid_ans_list[index])
                    else:
                        transmission_type.append('')

                    if('Clutch' in child_text_list):
                        index =  child_text_list.index('Clutch')
                        transmission_clutch.append(chlid_ans_list[index])
                    else:
                        transmission_clutch.append('')

                    if('Gear Box' in child_text_list):
                        index =  child_text_list.index('Gear Box')
                        transmission_gear.append(chlid_ans_list[index])
                    else:
                        transmission_gear.append('')

                    if('Battery' in child_text_list):
                        index =  child_text_list.index('Battery')
                        transmission_battery.append(chlid_ans_list[index]) 
                    else:
                        transmission_battery.append('')  

                    if('Alternator' in child_text_list):
                        index =  child_text_list.index('Alternator')
                        transmission_alternator.append(chlid_ans_list[index])
                    else:
                        transmission_alternator.append('')

                    if('Forward Speed' in child_text_list):
                        index =  child_text_list.index('Forward Speed')
                        transmission_fspeed.append(chlid_ans_list[index]) 
                    else:
                        transmission_fspeed.append('')
                        
                    if('Reverse Speed' in child_text_list):
                        index =  child_text_list.index('Reverse Speed')
                        transmission_rspeed.append(chlid_ans_list[index]) 
                    else:
                        transmission_rspeed.append('')
                except NoSuchElementException as e:
                    print('no engine')
            else:
                print('else transmission..')

            if 'Steering' in tab_text_list:
                el_index = tab_text_list.index('Steering')
                print('in-', el_index)
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")))
                element.click()
                time.sleep(.5)
                ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")     
                tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")
                
                child_text_list =[]
                chlid_ans_list=[]
                for ll in range(1,(len(tr)+1)):
                    print('ll-', ll)
                    text1=ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    child_text_list.append(text1)
                    text= ele.find_element(By.CSS_SELECTOR,"div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    chlid_ans_list.append(text)
                print('steering child_text_list-', child_text_list,chlid_ans_list)

                try:
                    if('Type' in child_text_list):
                        index =  child_text_list.index('Type')
                        steering_type.append(chlid_ans_list[index])
                    else:
                        steering_type.append('')
                    if('Steering Column' in child_text_list):
                        index =  child_text_list.index('Steering Column')
                        steering_column.append(chlid_ans_list[index])
                    else:
                        steering_column.append('')

                except NoSuchElementException as e:
                    print('no steering')
            else:
                print('else steering...')    

            if 'Power Take Off' in  tab_text_list:
                el_index = tab_text_list.index('Power Take Off')
                print('in-', el_index)
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")))
                element.click()
                time.sleep(.5)
                ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")     
                tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")
                
                child_text_list =[]
                chlid_ans_list=[]
                for ll in range(1,(len(tr)+1)):
                    print('ll-', ll)
                    text1=ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    child_text_list.append(text1)
                    text= ele.find_element(By.CSS_SELECTOR,"div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    chlid_ans_list.append(text)
                print('power child_text_list-', child_text_list)

                try:
                    if('Type' in child_text_list):
                        index =  child_text_list.index('Type')
                        power_take_type.append(chlid_ans_list[index])
                    else:
                        power_take_type.append('')

                    if('RPM' in child_text_list):
                        index =  child_text_list.index('RPM')
                        power_take_rpm.append(chlid_ans_list[index])
                    else:
                        power_take_rpm.append('')
                except NoSuchElementException as e:
                    print('no steering')
            else:
                power_take_type.append('')
                power_take_rpm.append('')

            if 'Dimensions And Weight Of Tractor' in  tab_text_list:
                el_index = tab_text_list.index('Dimensions And Weight Of Tractor')
                print('in-', el_index)
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")))
                element.click()
                time.sleep(.5)
                ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")     
                tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")
                child_text_list =[]
                chlid_ans_list=[]
                for ll in range(1,(len(tr)+1)):
                    print('ll-', ll)
                    text1=ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    child_text_list.append(text1)
                    text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    chlid_ans_list.append(text)
                print('dimension child_text_list-', child_text_list)

                try:
                    if('Total Weight' in child_text_list):
                        index =  child_text_list.index('Total Weight')
                        total_weight.append(chlid_ans_list[index])
                    else:
                        total_weight.append('')

                    if('Wheel Base' in child_text_list):
                        index =  child_text_list.index('Wheel Base')
                        wheel_base.append(chlid_ans_list[index])
                    else:
                        wheel_base.append('')

                    if('Overall Length' in child_text_list):
                        index =  child_text_list.index('Overall Length')
                        overall_length.append(chlid_ans_list[index])
                    else:
                        overall_length.append('') 

                    if('Overall Width' in child_text_list):
                        index =  child_text_list.index('Overall Width')
                        overall_width.append(chlid_ans_list[index])
                    else:
                        overall_width.append('') 

                    if('Ground Clearance' in child_text_list):
                        index =  child_text_list.index('Ground Clearance')
                        ground_clearance.append(chlid_ans_list[index])
                    else:
                        ground_clearance.append('') 

                    if('Turning Radius With Brakes' in child_text_list):
                        index =  child_text_list.index('Turning Radius With Brakes')
                        turning_radius.append(chlid_ans_list[index])
                    else:
                        turning_radius.append('') 
                except NoSuchElementException as e:
                    print('no dimension')
            else:
                total_weight.append('')
                wheel_base.append('')
                overall_length.append('')
                overall_width.append('')
                ground_clearance.append('')
                turning_radius.append('')  

            if 'Hydraulics' in  tab_text_list:
                el_index = tab_text_list.index('Hydraulics')
                print('in-', el_index)
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")))
                element.click()
                time.sleep(.5)
                ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")     
                tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")
                child_text_list =[]
                chlid_ans_list=[]
                for ll in range(1,(len(tr)+1)):
                    print('ll-', ll)
                    text1=ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    child_text_list.append(text1)
                    text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    chlid_ans_list.append(text)
                print('hy child_text_list-', child_text_list)

                try:
                    if('Lifting Capacity' in child_text_list):
                        index =  child_text_list.index('Lifting Capacity')
                        hydraulics_cap.append(chlid_ans_list[index])
                    else:
                        hydraulics_cap.append('')

                    if('3 point Linkage' in child_text_list):
                        index =  child_text_list.index('3 point Linkage')
                        hydraulics_linkage.append(chlid_ans_list[index])
                    else:
                        hydraulics_linkage.append('')

                except NoSuchElementException as e:
                    print('no hydraulics')
            else:
                hydraulics_cap.append('') 
                hydraulics_linkage.append('')

            if 'Wheels And Tyres' in  tab_text_list:
                el_index = tab_text_list.index('Wheels And Tyres')
                print('in-', el_index)
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")))
                element.click()
                time.sleep(.5)
                ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")     
                tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")
                child_text_list =[]
                chlid_ans_list=[]
                for ll in range(1,(len(tr)+1)):
                    print('ll-', ll)
                    text1=ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    child_text_list.append(text1)
                    text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    chlid_ans_list.append(text)
                print('wheel child_text_list-', child_text_list)

                try:
                    if('Wheel drive' in child_text_list):
                        index =  child_text_list.index('Wheel drive')
                        wheel_drive.append(chlid_ans_list[index])   
                    else:
                        wheel_drive.append('')  

                    if('Front' in child_text_list):
                        index =  child_text_list.index('Front')
                        front_tyres.append(chlid_ans_list[index])
                    else:
                        front_tyres.append('')

                    if('Rear' in child_text_list):
                        index =  child_text_list.index('Rear')
                        rear_tyres.append(chlid_ans_list[index])
                    else:
                        rear_tyres.append('')    

                except NoSuchElementException as e:
                    print('no wheel')
            else:
                wheel_drive.append('')    
                front_tyres.append('')
                rear_tyres.append('')

            if 'Other Information' in  tab_text_list:
                el_index = tab_text_list.index('Other Information')
                print('in-', el_index)
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")))
                element.click()
                time.sleep(.5)
                ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(el_index)+")")     
                tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")
                child_text_list =[]
                chlid_ans_list=[]
                for ll in range(1,(len(tr)+1)):
                    print('ll-', ll)
                    text1=ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    child_text_list.append(text1)
                    text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    chlid_ans_list.append(text)
                print('other child_text_list-', child_text_list)

                try:
                    if('Accessories' in child_text_list):
                        index =  child_text_list.index('Accessories')
                        accessories_list.append(chlid_ans_list[index])   
                    else:
                        accessories_list.append('') 

                    if('Additional Features' in child_text_list):
                        index =  child_text_list.index('Additional Features')
                        additional_feature.append(chlid_ans_list[index]) 
                    else:
                        additional_feature.append('') 

                    if('Warranty' in child_text_list):
                        index =  child_text_list.index('Warranty')
                        warranty_status.append(chlid_ans_list[index])
                    else:
                        warranty_status.append('')

                    if('Status' in child_text_list):
                        index =  child_text_list.index('Status')
                        status.append(chlid_ans_list[index])
                    else:
                        status.append('')        
                except NoSuchElementException as e:
                    print('no other')
            else:
                accessories_list.append('')
                additional_feature.append('') 
                warranty_status.append('')
                status.append('')

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
                close_modal= WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                close_modal.click()
                time.sleep(2)

                load_more = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
                # load_more.click()
                # time.sleep(1)
                # load_more.click()
                # time.sleep(1)
                # load_more.click()
                # time.sleep(1)
                # load_more.click()
                # time.sleep(1)
                # load_more.click()
                # time.sleep(1)
                # load_more.click()
                # time.sleep(1)
                # load_more.click()
                buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
                while buttonText == 'Load More Tractors':
                    buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')    
                    if buttonText != 'Load More Tractors':
                        break
                    else:  
                        load_more = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
                        # time.sleep(1)
                        driver.execute_script("arguments[0].click();", load_more)
                        # load_more.click()
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
print('brand_list-', brand_list, model_list,cylinder)
data_dict = {
    'Brand':brand_list,
    'Model':model_list,
    'No_of_Cylinder':cylinder,
    'HP_Category':hp_category,
    'PTO_HP':pto_hp,
    'Gear_Box':gear_box,
    'Brakes':brakes,
    'Warranty':warranty,
    'Price':price,
    # 'Features':feature_list,
    'About':about_list,
    'Engine_Capacity':engine_capaity,
    'Engine_RPM':engine_rpm,
    'Engine_Cooling':engine_cooling,
    'Engine_AirFilter':engine_airfilter,
    'Engine_FuelPump':engine_fuelpump,
    'Engine_Torque':engine_torque,
    'Transmission_Type':transmission_type,
    'Transmission_Clutch':transmission_clutch,
    'Transmission_Gear_Box':transmission_gear,
    'Transmission_Battery':transmission_battery,
    'Transmission_Alternator':transmission_alternator,
    'Transmission_Forward_Speed':transmission_fspeed,
    'Transmission_Reverse_Speed':transmission_rspeed,
    'Steering_type':steering_type,
    'Steering_Column':steering_column,
    'Power_Take_Off_Type':power_take_type,
    'Power_Take_Off_RPM':power_take_rpm,
    'Total_Weight':total_weight,
    'Wheel_Base':wheel_base,
    'Overall_Length':overall_length,
    'Overall_Width':overall_width,
    'Ground_Clearance':ground_clearance,
    'Turning_Radius':turning_radius,
    'Hydraulics_Lifting_Capacity':hydraulics_cap,
    'Hydraulics_Linkage':hydraulics_linkage,
    'Wheel_Drive':wheel_drive,
    'Front_Tyres':front_tyres,
    'Rear_Tyres':rear_tyres,
    'Accessories':accessories_list,
    'Additional_Feature':additional_feature,
    'Warranty_status':warranty_status,
    'Status':status
}
df=pd.DataFrame.from_dict(data_dict, orient="index")
df= df.transpose()

writer = pd.ExcelWriter('Tractor_Infos2.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()
