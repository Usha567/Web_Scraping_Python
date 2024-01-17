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
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException,TimeoutException 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome()

driver.get('https://www.tractorjunction.com/powertrac-tractor/euro-439/')

wait = WebDriverWait(driver, 15)
# driver.execute_script('window.scrollTo(0, 500)')

# nav_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.navbar-nav>li>a#navbarDropdown1')))
# nav_bar.click()
# time.sleep(1)

# dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-labelledby='navbarDropdown1']/ul/li/a[@title='All Tractors']")))
# dropdown_menu.click()
# time.sleep(2)


# WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
# close_modal= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
# close_modal.click()
# time.sleep(2)

# new_tractors = driver.find_elements(By.CSS_SELECTOR,'div#tractorMoreData div.new-tractor-main>div.new-tractor-img>a>img')

# div#tractorMoreData  div.new-tractor-main>div.new-tractor-img>a>img')
# print('new_tractors-',new_tractors,  len(new_tractors))
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

try:
    close_modal= WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal.click()

    # time.sleep(1)
    brand = driver.find_element(By.CSS_SELECTOR, "div.product-single-features-inner>p>a").text
    brand_list.append(brand)

    print('clicking brand_list..///', brand_list)

    model = driver.find_element(By.XPATH, "//li[@itemprop='itemListElement']/span[@itemprop='name']").text
    model_list.append(model)
    print('title-', brand_list, model_list)

    for j in range(3, 10):
        # print('j-', j)
        element = driver.find_element(By.CSS_SELECTOR,
            "div.product-single-features-inner:nth-child("+str(j)+")>p").text
        # print('element-',element)     
        if( j == 3):
            # print('cylinder')
            cylinder.append(element)
            # hp_category.append(element) 
        if( j == 4):
            # print('hp_category')
            hp_category.append(element) 
            # pto_hp.append(element)
        if( j ==5):
            # print('pto_hp')
            pto_hp.append(element)
            # gear_box.append(element)
        if( j == 6):
            # print('gear_box')
            # brakes.append(element)
            gear_box.append(element)
        if( j == 7):
            # print('brakes')
            brakes.append(element)
            # warranty.append(element) 
        if( j == 8):
            # print('warranty')
            warranty.append(element) 
            # price.append(element)
        if( j == 9):
            # print('price')
            price.append(element)

    # fe_list=[]
    # for k in range(1, 6):
    #     # print('k-', k)
    #     feature = driver.find_element(By.CSS_SELECTOR, 
    #     "div.tractor-other-features-main:nth-child("+str(k)+")>div.tractor-other-features-inner>p.tractor-other-features-property").text + '-'+ driver.find_element(By.CSS_SELECTOR, 
    #     "div.tractor-other-features-main:nth-child("+str(k)+")>div.tractor-other-features-inner>p.tractor-other-features-value").text
    #     fe_list.append(feature)
    # feature_list.append(fe_list)

    about=driver.find_element(By.CSS_SELECTOR, 'div.product_description_main').text
    about_list.append(about)

    tab_ele =driver.find_elements(By.CSS_SELECTOR,"div.acc-container div.acc")

    for l in range(2, 12):
        # try:
        print('l-', l)
        print('text-', driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(l)+")").text)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(l)+")")))
        element.click()
        time.sleep(.5)
        ele= driver.find_element(By.CSS_SELECTOR,"div.acc-container div.acc:nth-child("+str(l)+")")     
        tr=  ele.find_elements(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr")

        if(l == 2):
            print('tr-len', len(tr))
            for ll in range(3,len(tr)+1):
                try:
                # if ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+")"):
                    text1=   ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    print('ll-', ll, text1)
                    if(ll==3):
                        if(text1=='Capacity CC'):
                            engine_capaity.append(text)
                    if(ll==4):
                        if(text1=='Engine Rated RPM'):
                            engine_rpm.append(text)
                    if(ll==5):
                        if(text1=='Cooling'):
                            engine_cooling.append(text)
                    if(ll==6):
                        if(text1=='Air Filter'):
                            engine_airfilter.append(text) 
                    if(len(tr) == 8):
                        if(ll==8):
                            if(text1=='Fuel Pump'):
                                print('f-')
                                engine_fuelpump.append(text)
                            else: 
                                print('else f-')
                                engine_fuelpump.append('')  

                            if(text1=='Torque'):
                                print('t-')
                                engine_torque.append(text)
                            else: 
                                print('else t-')
                                engine_torque.append('') 
                    else:
                        if(ll==8):
                            if(text1=='Fuel Pump'):
                                engine_fuelpump.append(text)
                    if(ll==9):
                        if(text1=='Torque'):
                            print('t-')
                            engine_torque.append(text)
                        else: 
                            print('else t-')
                            engine_torque.append('') 
                except NoSuchElementException as e:
                    print('no such element',text1)  
                    # if(text1=='Fuel Pump'):engine_fuelpump.append('')
                    # if(text1=='Torque'):engine_torque.append('')  
            if(len(tr)==7):
                print('length is 7')
                engine_fuelpump.append('') 
                engine_torque.append('') 
                
        if(l==3):
            print('transmission--lengthtr// ',len(tr))
            for ll in range(1,len(tr)+1):
                print('ll//-', ll)
                text1=   ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                if(ll==1):
                    if(len(tr)==6): 
                        if(text1 == 'Clutch'):
                            transmission_type.append('')
                            transmission_clutch.append(text)
                        else:
                            transmission_type.append(text)    
                    else: 
                        transmission_type.append(text)           
                if( ll == 2):
                    if(len(tr)==6):
                        if(text1 == 'Gear Box'): 
                            transmission_gear.append(text)
                        else:
                            transmission_clutch.append(text)    
                    else: 
                        if(text1 == 'Clutch'):
                            transmission_clutch.append(text)
                        else:
                            transmission_clutch.append(text)
                if( ll ==3):
                    if(len(tr)==6):
                        if(text1 == 'Battery'): 
                            transmission_battery.append(text)
                        else:
                            transmission_gear.append(text) 
                    else:        
                        if(text1 == 'Gear Box'):
                            transmission_gear.append(text)
                        else:
                            transmission_gear.append(text)    
                if(len(tr)==7):
                    print('trlength-7')
                    if( ll == 4):
                        if(text1=='Battery'):
                            transmission_battery.append(text)
                    if( ll == 5):
                        if(text1=='Alternator'):
                            transmission_alternator.append(text)
                    if( ll == 6):
                        if(text1 == 'Forward Speed'):
                            transmission_fspeed.append(text)
                    if( ll == 7):
                        if(text1 == 'Reverse Speed'):
                            transmission_rspeed.append(text)
                if(len(tr)==6): 
                    print('trlength-6')
                    if(ll == 4):
                        if(ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child(3) td:nth-child(1)").text == 'Battery'):
                            print('here----2')
                        else:    
                            print('here///---')
                            if(text1=='Battery'):
                                transmission_battery.append(text)
                            else:
                                transmission_battery.append('')

                        if(text1=='Alternator'):
                            transmission_alternator.append(text)
                        else:
                            transmission_alternator.append('')

                    if(ll == 5 and text1 == 'Forward Speed'):
                        transmission_fspeed.append(text)
                    if(ll == 6 and text1 == 'Reverse Speed'):
                        transmission_rspeed.append(text)    

                if(len(tr)==5):
                    print('trlength-5')
                    if( ll == 4):
                        if(text1 == 'Forward Speed'):
                            transmission_fspeed.append(text)
                            transmission_battery.append('')
                    if( ll == 5):
                        if(text1 == 'Reverse Speed'):
                            transmission_rspeed.append(text)
                            transmission_alternator.append('')
        
        if(l==5):
            for ll in range(1,len(tr)+1):
                print('ll-', ll)
                try:
                    text= ele.find_element(By.CSS_SELECTOR,"div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    if(ll==1):
                        steering_type.append(text)    
                    if( ll == 2):
                        steering_column.append(text)
                except NoSuchElementException as e:
                    print('no such steering//')         
        if(l==6):
            for ll in range(1,len(tr)+1):
                print('ll-', ll)
                try:
                    text1=  ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                    text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    if(len(tr)==1):
                        print('powertake-length1--')
                        if(text1 == 'Type'):
                            power_take_type.append(text)
                        else:
                            power_take_type.append('')
                            power_take_rpm.append('')

                            total_weight.append('')
                            wheel_base.append('')
                            overall_length.append('')
                            overall_width.append('')
                            ground_clearance.append('')
                            turning_radius.append('')

                            hydraulics_cap.append(text) 
                            hydraulics_linkage.append('')
                    else:
                        print('powertake-length>1--')
                        if(ll==1):
                            power_take_type.append(text)
                        if(ll == 2):
                            power_take_rpm.append(text)

                            # total_weight.append('')
                            # wheel_base.append('')
                            # overall_length.append('')
                            # overall_width.append('')
                            # ground_clearance.append('')
                            # turning_radius.append('')

                except NoSuchElementException as e:
                    print('no poer teck...')
        
        # if(l==7):
        #     for ll in range(1,len(tr)+1):
        #         print('ll-', ll)
        #         text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
        #         if(ll==1):
        #             hydraulics_cap.append(text)    
        #         if( ll == 2):
        #             hydraulics_linkage.append(text)
        # if(l==7):
        #     for ll in range(1,len(tr)+1):
        #         print('ll-', ll)
        #         try:
        #             text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
        #             if(len(tr)==1):
        #                 wheel_drive.append(text)
        #                 front_tyres.append('')
        #                 rear_tyres.append('')
        #             else:    
        #                 if(ll==1):
        #                     wheel_drive.append(text)    
        #                 if( ll == 2):
        #                     front_tyres.append(text)
        #                 if( ll == 3):
        #                     rear_tyres.append(text)
        #         except NoSuchElementException as e:
        #             print('No such driver')     

        if(l==8):
            print('l is 8////- ', len(tr))
            for ll in range(1,(len(tr)+1)):
                print('ll-', ll)
                try:
                    text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                    if(len(tr)==2):
                        if(ll==1):
                            if(text1=='Lifting Capacity'):
                                total_weight.append('')   
                                wheel_base.append('')
                                overall_length.append('')
                                overall_width.append('')
                                ground_clearance.append('')
                                turning_radius.append('')
                                hydraulics_cap.append(text)
                            elif(text1 == 'Total Weight'):
                                total_weight.append(text)
                            else:
                                total_weight.append('') 
                                wheel_base.append(text)
                        if(ll==2):
                            if(text1=='3 point Linkage'):
                                hydraulics_linkage.append(text)
                            elif(text1=='Wheel Base'):
                                wheel_base.append(text)
                                overall_length.append('')
                                overall_width.append('')
                                ground_clearance.append('')
                                turning_radius.append('')  
                            else:
                                overall_length.append(text)
                                overall_width.append('')
                                ground_clearance.append('')
                                turning_radius.append('')
                            # hydraulics_cap.append(text) 
                            # hydraulics_linkage.append(text)

                            # accessories_list.append('')
                            # additional_feature.append('')
                            # warranty_status.append('')
                            # status.append(text) 
                    elif(len(tr)==1):
                        total_weight.append('')   
                        wheel_base.append('')
                        overall_length.append('')
                        overall_width.append('')
                        ground_clearance.append('')
                        turning_radius.append('')
                        hydraulics_cap.append(text) 
                        hydraulics_linkage.append('')
                    else:
                        if(ll==1):
                            total_weight.append(text)    
                        if( ll == 2):
                            wheel_base.append(text)
                        if(len(tr)==5):
                            if( ll == 3):
                                overall_length.append(text)
                            if(ll== 4):
                                overall_width.append(text)
                            if(ll==5):	
                                ground_clearance.append(text)
                                turning_radius.append('')
                        if(len(tr)==6):
                            if( ll == 3):
                                overall_length.append(text)
                            if(ll== 4):
                                overall_width.append(text)
                            if(ll==5):	
                                ground_clearance.append(text)
                            if(ll==6):    
                                turning_radius.append(text) 
                        if(len(tr)==3):
                            if(ll == 3):
                                overall_length.append('')
                                overall_width.append('')
                                ground_clearance.append(text)
                                turning_radius.append('')  
                        if(len(tr)==2):
                            if(ll == 2):
                                overall_length.append('')
                                overall_width.append('')
                                ground_clearance.append('')
                                turning_radius.append('')              
                except NoSuchElementException as e:
                    total_weight.append('')
                    wheel_base.append('')
                    overall_length.append('')
                    overall_width.append('')
                    ground_clearance.append('')
                    turning_radius.append('')

        if(l==9):
            for ll in range(1,len(tr)+1):
                print('ll-', ll)
                text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                if(len(tr) == 1):
                    hydraulics_cap.append(text)    
                    hydraulics_linkage.append('')
              
                else:    
                    if(ll==1):
                        # total_weight.append('')   
                        # wheel_base.append('')
                        # overall_length.append('')
                        # overall_width.append('')
                        # ground_clearance.append('')
                        # turning_radius.append('')
                        hydraulics_cap.append(text)    
                    if( ll == 2):
                        hydraulics_linkage.append(text)

        if(l==10):
            for ll in range(1,len(tr)+1):
                print('ll-', ll)
                text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                if(len(tr)==1):
                    wheel_drive.append(text)    
                    front_tyres.append('')
                    rear_tyres.append('')
                else:    
                    if(ll==1):
                        wheel_drive.append(text)    
                    if( ll == 2):
                        front_tyres.append(text)
                    if( ll == 3):
                        rear_tyres.append(text)
        
        if(l==11):
            print('Otherinfo---')
            for ll in range(1, (len(tr)+1)):
                print('ll-', ll)
                text1=   ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(1)").text
                text= ele.find_element(By.CSS_SELECTOR, "div.acc-content>table>tbody>tr:nth-child("+str(ll)+") td:nth-child(2)").text
                if(len(tr)==4):
                    if(ll==1):
                        if(text1 == 'Accessories'):
                            accessories_list.append(text)
                        else: 
                            additional_feature.append(text)   
                        # print('ac...')
                        # accessories_list.append(text)
                    if(ll==2):
                        print('ad...')
                        if(text1 == 'Additional Features'):
                            print('ad///')
                            additional_feature.append(text)
                        elif(text1 == 'Options'):
                            print('option--///')  
                            additional_feature.append('')
                        elif(text1 == 'Warranty'):
                            warranty_status.append(text)
                        else:
                            print('ad st///')
                            additional_feature.append('')
                            warranty_status.append(text)
                    if(ll==3):
                        print('w///')
                        if(text1 == 'Warranty'):
                            print('w-///')
                            warranty_status.append(text)
                        else:
                            print('w-st///')
                            status.append(text)        
                    if(ll==4):
                        print('st///')
                        if(text1 == 'Status'):
                            print('st-s///')
                            status.append(text)  
                if(len(tr) == 3):  
                    if(ll==1):
                        if(text1== 'Accessories'):
                            accessories_list.append(text)
                            additional_feature.append('') 
                        else:
                            accessories_list.append('')
                            additional_feature.append('')
                            warranty_status.append(text)   
                    if(ll==2):
                        if(text1== 'Warranty'):
                            warranty_status.append(text)
                        else:
                            status.append(text)  
                    if(ll==3):
                        if(text1== 'Status'):
                            status.append(text)
                
                if(len(tr) == 2):  
                    if(ll==1):
                        if(text1== 'Accessories'):
                            accessories_list.append(text)
                            additional_feature.append('') 
                        else:
                            accessories_list.append('')
                            additional_feature.append('')
                            warranty_status.append(text)   
                    if(ll==2):
                        if(text1== 'Warranty'):
                            warranty_status.append(text)
                        else:
                            status.append(text) 

                if(len(tr)==5):
                    if(ll==1):
                        accessories_list.append(text)
                    if(ll==3):
                        if(text1 == 'Additional Features'):
                            additional_feature.append(text)
                    if(ll==4):
                        warranty_status.append(text)
                    if(ll==5):
                        if(text1 == 'Status'):
                            status.append(text)  
    
        # except ElementClickInterceptedException:
        #     print('Tring to click on button again')
        #     # driver.execute_script("arguments[0].click()", element)

    driver.back()
    time.sleep(2)

    # driver.close()

    # load_more = wait.until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
    # load_more.click()
    # try:
    #     modal=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    #     close_modal= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    #     close_modal.click()

        # print('click on loadmore btn')
        # modal=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
        # close_modal= WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
        # close_modal.click()

    #     load_more = wait.until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
    #     load_more.click()
    #     print('clicked on modal...///')

    # except ElementClickInterceptedException as e:
    #     print('ElementClickInterceptedException---///')

except TimeoutException as e:
    print('TimeoutException for loop-///+++')

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
    'Overall_Base':overall_length,
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

writer = pd.ExcelWriter('Tractor_Infos3.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()
