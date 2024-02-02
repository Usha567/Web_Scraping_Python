import time
import urllib
import os
import errno
import re
from urllib.parse import urlparse
import xlsxwriter
import pandas as pd
from PIL import Image , ImageFont, ImageDraw
from rembg import remove 
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

nav_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.navbar-nav>li>a#navbarDropdown5')))
nav_bar.click()
time.sleep(1)

dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@aria-labelledby='navbarDropdown5']/li/a[@title='Harvester']")))
dropdown_menu.click()
time.sleep(2)

# try:
#     cross_model=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
#     close_modal= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
#     close_modal.click()
#     time.sleep(2)
# except TimeoutException as e:
#     print('timeoutException for close external modal...')    

new_harvester = driver.find_elements(By.CSS_SELECTOR,'div#harvesterMoreData div.implement-main>div.implement-img>a>img')

# div#tractorMoreData  div.new-tractor-main>div.new-tractor-img>a>img')
print('new_tractors-',new_harvester,  len(new_harvester))
brand_list=[]
model_list=[]
cylinder=[]
power=[]
cutterwidth=[]
powersource=[]
crop=[]

hp_power =[]
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
no_of_cylinder=[]
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

engine_type=[]
cutter_width = []
cutter_min_height =[]
cutter_max_height =[]
cutter_height_adj=[]
reel_height_adj = []
reel_type=[]
reel_dia=[]
speed_adjustment =[]
max_revolution=[]
min_revolution=[]
images_name=[]
image_list=[]
cooling_sys=[]
cooling_cap=[]
threshing_width=[]
threshing_length=[]
threshing_diameter=[]
threshing_adjusment=[]
concave_clearance=[]
grain_tank_capacity=[]
transmission_gear=[]
transmission_clutch_type=[]
tyre_size_front=[]
tyre_size_rear=[]
fuel_tank_capacity=[]
dimensions_length=[]
dimensions_height=[]
dimensions_width=[]

buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
if buttonText == 'Load More Harvesters':
    print('enter if--')
    load_more = wait.until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
    # load_more.click()
    # time.sleep(1)

    # For load more harvester 
    # count=0
    # buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
    # while buttonText == 'Load More Tractors':
    #     buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')    
    #     if buttonText != 'Load More Tractors':
    #         break
    #     else:  
    #         count +=1
    #         print('count-', count)
    #         load_more = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
    #         driver.execute_script("arguments[0].click();", load_more)
    #         print('clicked on load')  
    # print('click3',count)


    for i in range(3,4):
        print('looping start...i-', i)

        try:
            try:
                print('click on image..///')
                new_harvester = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div#harvesterMoreData div:nth-child("+str(i)+")>div.implement-main>div.implement-img>a>img")))
                new_harvester.click()
                time.sleep(2)

                # modal=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                # close_modal= WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                # close_modal.click()

            except TimeoutException as e:
                print('TimeoutException for close btn..///..//') 

            brand = driver.find_element(By.CSS_SELECTOR, "div.product-single-features-inner>p>a").text
            brand_list.append(brand)

            model_name=[]
            model = driver.find_element(By.XPATH, "//li[@itemprop='itemListElement']/span[@itemprop='name']").text
            model_list.append(model)

            print('brand_list-.... ', brand_list, model_list)

            model_name_ = driver.find_element(By.CSS_SELECTOR, 
            "div.product-single-top>div.section-heading>h1").text
            model_name.append(model_name_)

            # image_list
            tractor_images = driver.find_elements(By.CSS_SELECTOR, "div.slider div.slick-list div.slick-track div.slick-slide>img")
            src =[]

            for img in tractor_images:
                if img not in src:
                    if len(src) < 4:
                        src.append(img.get_attribute('src'))
            image_list.append(src)

        
            if '/' in model:
                print('if model//..')
                m= model.split('/')
                dirname = "Harvester_Images/"+((brand.capitalize()).strip())+"_"+str(i)+"_"+m[0]+"_"+m[1]
                print('dirname-', dirname)
            else:
                print('if model...')
                dirname = "Harvester_Images/"+((brand.capitalize()).strip())+"_"+str(i)+"_"+model
                print('dirname-', dirname)     
            try:
                os.mkdir(dirname)
            except OSError as e:
                print(' e-',  e)
                if e.errno == errno.EEXIST:
                    print('Dir not created')
                else:
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
                
            files = os.listdir(dirname)
            for file in files:
                print('file-',file)
                im = Image.open(os.path.join(dirname+"/", file))
                output_path = dirname+"/"+file 

                output = remove(im,  bgcolor=(255, 255, 255, 255)) 
                output.save(output_path, quality=95) 

            print('dirname/', dirname)
            rem_bgfiles = os.listdir(dirname)
            for file in rem_bgfiles:
                print('file///-', file)
                with Image.open(dirname+"/"+file) as img:
                    width, height = img.size
                    txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
                    
                    d = ImageDraw.Draw(txt)
                    _, _, w, h = d.textbbox((0, 0), "Bharatagrimart")
                    fontsize = 1

                    img_fraction = 0.25
                    font = ImageFont.truetype("BerkshireSwash-Regular.ttf", fontsize)
                    while d.textbbox((0, 0), "Bharatagrimart", font=font)[2] < img_fraction * width:
                        fontsize += 1
                        font = ImageFont.truetype("BerkshireSwash-Regular.ttf", fontsize)
                    fontsize -= 1
                    font = ImageFont.truetype("BerkshireSwash-Regular.ttf", fontsize)
                    print('width-',width, height, w,h) 
                    if(width > 450 and height>180):
                        print('if...')
                        d.text(((width/2+157),(height-h-12)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    elif(width==320 and height==180):
                        print('elif...')
                        d.text(((width/2+(w*1.20)),(height/2+(height/3)+h*1.3)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    else:
                        print('else//..')
                        d.text(((width/2+70),(height-h-5)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    
                    out = Image.alpha_composite(img.convert("RGBA"), txt)
                    output_path = dirname+"/"+file
                    out.save(output_path)

            images_name.append(imagename_list)

            feature = driver.find_elements(By.CSS_SELECTOR, "div.product-single-features-inner")
            feature_list =['','']
            feature_ans_list=['','']

            # print('feature l-',len(feature))

            for jj in range(2, len(feature)+1):
                ele = driver.find_element(By.CSS_SELECTOR,
                    "div.product-single-features-inner:nth-child("+str(jj)+")>h5").text
                feature_list.append(ele)
                element = driver.find_element(By.CSS_SELECTOR,
                        "div.product-single-features-inner:nth-child("+str(jj)+")>p").text
                feature_ans_list.append(element)
            # print('feature_list//-',feature_list, feature_ans_list) 

            try:
                if 'Power'  in  feature_list:
                    index=feature_list.index('Power')
                    power.append(feature_ans_list[index]) 
                else:
                    power.append('')

                if "Cutter Bar – Width"  in  feature_list:
                    index=feature_list.index("Cutter Bar – Width")
                    cutterwidth.append(feature_ans_list[index])  
                else:
                    cutterwidth.append('')

                if 'No Of Cylinder'  in  feature_list:
                    index=feature_list.index('No Of Cylinder')
                    cylinder.append(feature_ans_list[index])  
                else:
                    cylinder.append('') 

                if 'Power Source'  in  feature_list:
                    index=feature_list.index('Power Source')
                    powersource.append(feature_ans_list[index]) 
                else:
                    powersource.append('')

                if 'Crop'  in  feature_list:
                    index=feature_list.index('Crop')
                    crop.append(feature_ans_list[index]) 
                else:
                    crop.append('')
            except NoSuchElementException as e:
                print('no features..') 

            about=driver.find_element(By.CSS_SELECTOR, 'div.product_description_main').text
            about_list.append(about)
            
            tr_list =driver.find_elements(By.CSS_SELECTOR,"div.product-single-content div.text-editor-block div.table-block table>tbody tr")
            tr_text_list=[]
            tr_text_list_withcolon=[]
            tab_ans_list=['','']

            for tr in tr_list:
                tr_text = tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
                text = (tr_text.text).lstrip()
                tr_text_list_withcolon.append(text)
                if ':' in text:
                    tr_text_list.append(text[:-1])
                else:    
                    tr_text_list.append(text)

            # print('tr_text_list-', tr_text_list)    
             
            if 'TYPE'.capitalize() in [(i.capitalize()).strip() for i in tr_text_list]:
                print('Type in tr_text_list')
                index_of = [(i.capitalize()).strip() for i in tr_text_list].index('TYPE'.capitalize())
               
                zero_index_tr_text =(tr_list[0].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                parent_tr_text=(tr_list[index_of-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()

                print('parent_tr_text-', parent_tr_text)

                if (parent_tr_text.capitalize()).strip() == 'Engine':
                    print('if Engine is parent....')
                    for tr in tr_list:

                        parent_tr_index = tr_list.index(tr)
                        parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        # print('parent_tr_text--',parent_tr_text)
                        tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                        if ':' in tr_text:
                            tr_text = tr_text[:-1]
                        if  (parent_tr_text.capitalize()).strip() == 'Engine':   
                            if (tr_text.capitalize()).strip() == 'TYPE'.capitalize():
                                try:
                                    ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                    print('engine ans_texttype--/-', ans_text)
                                    engine_type.append(ans_text)
                                except NoSuchElementException as e:
                                    print('no weight')  
                                    engine_type.append('')       

                elif (parent_tr_text.capitalize()).strip() != 'Engine' and 'Engine'.capitalize() in [(i.capitalize()).strip() for i in tr_text_list]:
                    print('if Engine is not parent....')
                    for tr in tr_list:
                        tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                        if ':' in tr_text:
                            tr_text = tr_text[:-1]
                        if (tr_text.capitalize()).strip() == 'Engine'.capitalize():
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('engine ans_texttype--/-', ans_text)
                                engine_type.append(ans_text)
                            except NoSuchElementException as e:
                                print('no such element--/-') 
                                engine_type.append('') 
                else:
                    print('else-no engine_type...')
                    engine_type.append('')

            if 'TYPE'.capitalize() not in [(i.capitalize()).strip() for i in tr_text_list] and 'Engine'.capitalize() in [(i.capitalize()).strip() for i in tr_text_list]:
                print('type is not and if Engine is parent....')
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if (tr_text.capitalize()).strip() == 'Engine'.capitalize():

                        zero_index_tr_text = (tr_list[0].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        parent_tr_index = tr_list.index(tr)
                        parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        
                        if (parent_tr_text).strip() == (zero_index_tr_text).strip():
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('ans_texttype--/-', ans_text)
                                engine_type.append(ans_text)
                            except NoSuchElementException as e:
                                print('no such element--/-') 
                                engine_type.append('') 
            
            if 'Engine Rated RPM' in [i for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]  
                    if tr_text.strip() == 'Engine Rated RPM':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('rpm ans_texttype--/-', ans_text)
                            engine_rpm.append(ans_text)
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            engine_rpm.append('')     
            else:
                print('else-no engine_rpm...')
                engine_rpm.append('') 

            # if 'HP Power' in [i.strip() for i in tr_text_list]:
            #     for tr in tr_list:
            #         tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
            #         if ':' in tr_text:
            #             tr_text = tr_text[:-1]  
            #         if tr_text.strip() == 'HP Power':
            #             ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
            #             print('hp ans_texttype--/-', ans_text)
            #             hp_power.append(ans_text)
            # else:
            #     hp_power.append('') 

            if 'Air Filter' in [i.strip() for i in tr_text_list] or 'Air Cleaner' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]  
                    if tr_text.strip() == 'Air Filter' or tr_text.strip() == 'Air Cleaner':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('air_filter ans_texttype--/-', ans_text)
                            engine_airfilter.append(ans_text)
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            engine_airfilter.append('')    
            else:
                print('else-no engine_airfilter...')
                engine_airfilter.append('')

            if 'Cutting Height Min' in [i.strip() for i in tr_text_list] or 'Cutting Height' in [i.strip() for i in tr_text_list] or 'Cutting Height (mm)' in [i.strip() for i in tr_text_list] or 'Cutting Height Range (mm)' in [i.strip() for i in tr_text_list]:
                print('inner cutter height...')
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Cutting Height Min' or tr_text.strip() == 'Cutting Height (mm)'or tr_text.strip() == 'Cutting Height Range (mm)' or tr_text.strip() == 'Cutting Height':    
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('cutting_height_min ans_texttype--/-', ans_text)
                            cutter_min_height.append(ans_text)
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            cutter_min_height.append('')        
            else:
                print('else-no cutter_min_height...')
                cutter_min_height.append('')

            if 'Cutting Height Max' in [i.strip() for i in tr_text_list]:
                print('inner cutter height max ...')
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Cutting Height Max':    
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('cutting_height_max ans_texttype--/-', ans_text)
                            cutter_max_height.append(ans_text)
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            cutter_max_height.append('')           
            else:
                print('else-no cutter_max_height...')
                cutter_max_height.append('') 

            if 'Height Adjustment' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    print('tr_text////', tr_text)

                    if tr_text.strip() == 'Height Adjustment': 
                        ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                        print('height_adj ans_texttype--/-', ans_text)
                        if(ans_text not in cutter_height_adj):
                            cutter_height_adj.append(ans_text) 
            else:
                print('else-no cutter_height_adj...')
                cutter_height_adj.append('')       

            if 'Reel'.capitalize() in [(i.capitalize()).strip() for i in tr_text_list] or 'Reel Assembly' in [(i.capitalize()).strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if (tr_text.capitalize()).strip() == 'Type'.capitalize():
                        index_of = [(i.capitalize()).strip() for i in tr_text_list_withcolon].index('TYPE:'.capitalize())
                        parent_tr_text=(tr_list[index_of-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        
                        print('reel parent_tr_text-', parent_tr_text)

                        if (parent_tr_text.capitalize()).strip() == 'Reel'.capitalize():
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('reel_type ans_texttype--/-', ans_text)
                                reel_type=[]
                                reel_type.append(ans_text)
                            except NoSuchElementException as e:
                                print('no such element--/-') 
                                reel_type.append('') 
            else:
                print('else-no reel_type...')
                reel_type.append('')   
            
            if 'Reel Diameter (mm)' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Reel Diameter (mm)':    
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('reel_dia ans_texttype--/-', ans_text)
                            reel_dia.append(ans_text)
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            reel_dia.append('')      
            else:
                print('else-no reel_dia...')
                reel_dia.append('')    

            if 'Speed Adjustment' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Speed Adjustment':    
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('speed_adjustment- ', ans_text)
                            speed_adjustment.append(ans_text)
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            speed_adjustment.append('')           
            else:
                print('else-no speed_adjustment...')
                speed_adjustment.append('')

            # if 'Height Adjustment' in [i.strip() for i in tr_text_list]:
            #     for tr in tr_list:
            #         tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
            #         if ':' in tr_text:
            #             tr_text = tr_text[:-1]

            #         if tr_text.strip() == 'Height Adjustment': 
            #             parent_tr_index = tr_list.index(tr)
            #             parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, 
            #                "td:nth-child(1)").text).lstrip()
            #             if 'Reel' in (parent_tr_text.capitalize()).strip():
            #                 ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
            #                 print('air ans_texttype--/-', ans_text)
            #                 reel_height_adj.append(ans_text) 
            # else:
            #     reel_height_adj.append('')

            if 'Cooling System' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    if tr_text.strip() == 'Cooling System': 
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('cooling_sys --/-', ans_text)
                            cooling_sys.append(ans_text)
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            cooling_sys.append('')         
            else:
                print('else-no cooling_sys...')
                cooling_sys.append('') 

            if 'Coolant Capacity' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    if tr_text.strip() == 'Coolant Capacity': 
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('cooling_cap --/-', ans_text)
                            cooling_cap.append(ans_text) 
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            cooling_cap.append('')    
            else:
                print('else-no cooling_cap...')
                cooling_cap.append('')

            if 'Width (mm)' in [i.strip() for i in tr_text_list] or 'SieveCase Length x Width (mm)' in [i.strip() for i in tr_text_list] or 'Threshing Drum Width' in [i.strip() for i in tr_text_list] or 'Drum Width' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    if tr_text.strip() == 'Width (mm)' or tr_text.strip() == 'SieveCase Length x Width (mm)' or tr_text.strip() == 'Threshing Drum Width' or tr_text.strip() == 'Drum Width': 
                        if tr_text.strip() == 'Width (mm)': 
                            parent_tr_index = tr_list.index(tr)
                            parent_tr_text=(tr_list[parent_tr_index-2].find_element(By.CSS_SELECTOR, 
                            "td:nth-child(1)").text).lstrip()
                            parent_tr_splitted_text = parent_tr_text.split()
                            print('thresh parent_tr_splitted_text-- ', parent_tr_splitted_text)
                            if 'Threshing' in parent_tr_splitted_text:
                                try:
                                    ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                    print('not cutter threshing_width --/-', ans_text)
                                    threshing_width.append(ans_text)
                                except NoSuchElementException as e:
                                    print('no such element--/-') 
                                    threshing_width.append('')         
                        else:
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('threshing_width --/-', ans_text)
                                threshing_width.append(ans_text)
                            except NoSuchElementException as e:
                                print('no such element--/-') 
                                threshing_width.append('')            
            else:        
                print('else-no threshing_width...')
                threshing_width.append('')  

            if 'Width' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    if tr_text.strip() == 'Width': 
                        parent_tr_index = tr_list.index(tr)
                        parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()

                        print('Threshing parent_tr_text--', parent_tr_text)

                        parent_tr_splitted_text = parent_tr_text.split()
                        if 'Threshing' in parent_tr_splitted_text:
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('threshing_width ans_texttype--/-', ans_text)
                                threshing_width.append(ans_text) 
                            except NoSuchElementException as e:
                                print('no such element--/-') 
                                threshing_width.append('')    
            else:
                print('else-no threshing_width...')
                threshing_width.append('')       

            if 'Length of Drum' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    if tr_text.strip() == 'Length of Drum': 
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('threshing_length --/-', ans_text)
                            threshing_length.append(ans_text) 
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            threshing_length.append('')      
            else:
                print('else-no threshing_length...')
                threshing_length.append('')   

            if 'Drum Diameter' in [i.strip() for i in tr_text_list] or 'Dia of Drum' in [i.strip() for i in tr_text_list] or 'Diameter of Thresher Drum (mm)' in [i.strip() for i in tr_text_list] or 'Outside dia (mm)' in [i.strip() for i in tr_text_list] or 'Diameter' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    if tr_text.strip() == 'Drum Diameter' or tr_text.strip() == 'Dia of Drum' or tr_text.strip() == 'Diameter of Thresher Drum (mm)' or tr_text.strip() == 'Outside dia (mm)' or tr_text.strip() == 'Diameter': 
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('threshing_diameter --/-', ans_text)
                            threshing_diameter.append(ans_text) 
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            threshing_diameter.append('')     
            else:
                print('else-no threshing_diameter...')
                threshing_diameter.append('')

            if 'Adjustment' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Adjustment': 
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('threshing_adjusment --/-', ans_text)
                            if(ans_text not in threshing_adjusment):
                                threshing_adjusment.append(ans_text)
                        except NoSuchElementException as e:
                            print('no such element--/-') 
                            threshing_adjusment.append('')         
            else:
                print('else-no threshing_adjusment...')
                threshing_adjusment.append('')

            if 'Clearance' in [i.strip() for i in tr_text_list] or 'Clearance Between' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Clearance' or tr_text.strip() == 'Clearance Between': 
                        parent_tr_index = tr_list.index(tr)
                        parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        
                        print('clearance parent_tr_text-- ', parent_tr_text)
                        if parent_tr_text == 'Concave':
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('concave_clearance--/-', ans_text)
                                concave_clearance.append(ans_text)
                            except NoSuchElementException as e:
                                print('no such element--/-') 
                                concave_clearance.append('')     
            else:
                print('else-no concave_clearance...')
                concave_clearance.append('') 

            if 'Grain Tank' in [i.strip() for i in tr_text_list] or 'Capacity (L)' in [i.strip() for i in tr_text_list] or 'Grain Tank (m2)' in [i.strip() for i in tr_text_list] or  'Grain Tank Capacity (m3)' in [i.strip() for i in tr_text_list] or 'Capacity' in [i.strip() for i in tr_text_list] or 'Unload capacity (l/sec)' in [i.strip() for i in tr_text_list] or 'Grain Tank (M2)' in [i.strip() for i in tr_text_list] or 'Grain Tank Capacity (m3)' in [i.strip() for i in tr_text_list] or 'Capacity: Volume Basis (m3)' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    if tr_text.strip() == 'Capacity':
                        parent_tr_index = tr_list.index(tr)
                        parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        
                        print('Grain parent_tr_text-- ', parent_tr_text)

                        if parent_tr_text == 'Grain Tank':    
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('grain_tank_capacity --/-', ans_text)
                                grain_tank_capacity.append(ans_text)
                            except NoSuchElementException as e:
                                print('no such element--/-') 
                                grain_tank_capacity.append('')       
                    else:
                        if tr_text.strip() == 'Grain Tank' or tr_text.strip() == 'Capacity (L)' or tr_text.strip() == 'Grain Tank (m2)' or tr_text.strip() == 'Grain Tank Capacity (m3)' or  tr_text.strip() == 'Capacity' or tr_text.strip() == 'Unload capacity (l/sec)' or tr_text.strip() == 'Grain Tank (M2)':
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('else grain_tank_capacity --/-', ans_text)
                                grain_tank_capacity.append(ans_text)
                            except NoSuchElementException as e:
                                print('no such element--/-') 
                                grain_tank_capacity.append('')          
            else:
                print('else-no grain_tank_capacity...')
                grain_tank_capacity.append('')


            if 'No. Of Gears' in [i.strip() for i in tr_text_list] or 'Transmission' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'No. Of Gears' or  tr_text.strip() == 'Transmission':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('transmission_gear --/-', ans_text)
                            transmission_gear.append(ans_text)
                        except NoSuchElementException as e:
                            print('no gear')  
                            transmission_gear.append('')    
            else:
                print('else-no transmission_gear...')
                transmission_gear.append('')

            if 'Clutch Type' in [i.strip() for i in tr_text_list] or 'Type' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Type':
                        parent_tr_index = tr_list.index(tr)
                        parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        
                        print('Clutch parent_tr_text-- ', parent_tr_text)

                        if (parent_tr_text.capitalize()).strip() == 'Clutch':
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('transmission_clutch_type --/-', ans_text)
                                transmission_clutch_type.append(ans_text)
                            except NoSuchElementException as e:
                                print('no clutch')  
                                transmission_clutch_type.append('')       
                    else:    
                        if tr_text.strip() == 'Clutch Type':
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('transmission_clutch_type --/-', ans_text)
                                transmission_clutch_type.append(ans_text)
                            except NoSuchElementException as e:
                                print('no clutch')  
                                transmission_clutch_type.append('')          
            else:
                print('else-no transmission_clutch_type...')
                transmission_clutch_type.append('')

            if 'Front' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]
                    if tr_text.strip() == 'Front':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('tyre_size_front --/-', ans_text)
                            tyre_size_front.append(ans_text) 
                        except NoSuchElementException as e:
                            print('no front')  
                            tyre_size_front.append('')        
            else:
                print('else-no tyre_size_front...')
                tyre_size_front.append('') 

            if 'Rear/Trolley' in [i.strip() for i in tr_text_list] or 'Rear & Trolley' in [i.strip() for i in tr_text_list] or 'Rear' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Rear/Trolley' or tr_text.strip() == 'Rear & Trolley' or tr_text.strip() == 'Rear':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('tyre_size_rear --/-', ans_text)
                            tyre_size_rear.append(ans_text)
                        except NoSuchElementException as e:
                            print('no rear')  
                            tyre_size_rear.append('') 
            else:
                print('else-no tyre_size_rear...')
                tyre_size_rear.append('')    


            if 'Fuel tank' in [i.strip() for i in tr_text_list] or 'Fuel Tank Capacity (L)' in [i.strip() for i in tr_text_list] or 'Fuel Tank (ltr.)' in [i.strip() for i in tr_text_list] or 'Fuel Tank Capacity' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Fuel tank' or tr_text.strip() == 'Fuel Tank Capacity (L)' or tr_text.strip() == 'Fuel Tank (ltr.)' or tr_text.strip() == 'Fuel Tank Capacity':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('fuel_tank_capacity --/-', ans_text)
                            fuel_tank_capacity.append(ans_text) 
                        except NoSuchElementException as e:
                            print('no fuelcap')  
                            fuel_tank_capacity.append('')     
            else:
                print('else-no fuel_tank_capacity...')
                fuel_tank_capacity.append('')

            if 'Weight' in [i.strip() for i in tr_text_list] or 'Total Weight (kg)' in [i.strip() for i in tr_text_list] or 'Weight (kg)' in [i.strip() for i in tr_text_list] or 'Machine Weight' in [i.strip() for i in tr_text_list] or'Total Weight without Grain' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Weight' or tr_text.strip() == 'Total Weight (kg)' or tr_text.strip() == 'Weight (kg)'or tr_text.strip() == 'Machine Weight' or tr_text.strip() == 'Total Weight without Grain':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('total_weight --/-', ans_text)
                            total_weight.append(ans_text)
                        except NoSuchElementException as e:
                            print('no weight')  
                            total_weight.append('')         
            else:
                print('else-no total_weight...')
                total_weight.append('') 

            
            if 'Length' in [i.strip() for i in tr_text_list] or 'Length (mm)' in [i.strip() for i in tr_text_list] or 'Length (including cutterbar )' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Length (mm)':
                        parent_tr_index = tr_list.index(tr)
                        parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        if parent_tr_text == 'Main Dimensions(Approx)' or parent_tr_text == 'Overall Dimension': 
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('dimensions_length --/-', ans_text)
                                dimensions_length.append(ans_text)
                            except NoSuchElementException as e:
                                print('no weight')  
                                dimensions_length.append('')       
                    else:
                        if tr_text.strip() == 'Length' or tr_text.strip() == 'Length (including cutterbar )':
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('dimensions_length --/-', ans_text)
                                dimensions_length.append(ans_text)
                            except NoSuchElementException as e:
                                print('no weight')  
                                dimensions_length.append('')         
            else:
                print('else-no dimensions_length...')
                dimensions_length.append('')

            if 'Height' in [i.strip() for i in tr_text_list] or 'Height (mm)' in [i.strip() for i in tr_text_list] or 'Height (With Canopy Stored) (mm)' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Height' or tr_text.strip() == 'Height (mm)' or tr_text.strip() == 'Height (With Canopy Stored) (mm)':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('dimensions_height--/-', ans_text)
                            dimensions_height.append(ans_text)  
                        except NoSuchElementException as e:
                            print('no weight')  
                            dimensions_height.append('')         
            else:
                print('else-no dimensions_height...')
                dimensions_height.append('')  

             
            if 'Width' in [i.strip() for i in tr_text_list] or 'Width (mm)' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Width (mm)':
                        parent_tr_index = tr_list.index(tr)
                        parent_tr_text=(tr_list[parent_tr_index-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                        if parent_tr_text != 'Threshing Drum': 
                            try:
                                ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                print('dimensions_width --/-', ans_text)
                                dimensions_width.append(ans_text)
                            except NoSuchElementException as e:
                                print('no weight')  
                                dimensions_width.append('')            
                    else:
                        if tr_text.strip() == 'Width':
                            try:                               
                                index_of = [(i.capitalize()).strip() for i in tr_text_list_withcolon].index('Width:'.capitalize())
                                parent_tr_text=(tr_list[index_of-1].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).lstrip()
                            
                                print('dimension w parent_tr_text-', parent_tr_text)
                                parent_tr_text_splitted = parent_tr_text.split()
                            except Exception as e:
                                print('exception....')
                                parent_tr_text_splitted=[]    
                            if 'Cutter' in parent_tr_text_splitted:
                                print('no dimension width its cutter width')
                            else:   
                                try: 
                                    ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                                    print('dimensions_width --/-', ans_text)
                                    dimensions_width.append(ans_text)
                                except NoSuchElementException as e:
                                    print('no weight')  
                                    dimensions_width.append('')    
            else:
                print('else-no dimensions_width...')
                dimensions_width.append('')      

              
            if 'Min Ground Clearance' in [i.strip() for i in tr_text_list] or 'Ground Clearance (mm)' in [i.strip() for i in tr_text_list] or 'Ground Clearance' in [i.strip() for i in tr_text_list]:
                for tr in tr_list:
                    tr_text = ((tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")).text).lstrip()
                    if ':' in tr_text:
                        tr_text = tr_text[:-1]

                    if tr_text.strip() == 'Min Ground Clearance' or tr_text.strip() == 'Ground Clearance (mm)' or tr_text.strip() == 'Ground Clearance':
                        try:
                            ans_text = (tr.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text).lstrip()
                            print('ground_clearance --/-', ans_text)
                            ground_clearance.append(ans_text) 
                        except NoSuchElementException as e:
                            print('no weight')  
                            ground_clearance.append('')              
            else:
                print('else-no ground_clearance...')
                ground_clearance.append('')

            # print('tr_text_list- ', engine_type, engine_rpm)
            
            # driver.back()
            time.sleep(2)

            nav_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.navbar-nav>li>a#navbarDropdown5')))
            nav_bar.click()
            time.sleep(1)

            dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@aria-labelledby='navbarDropdown5']/li/a[@title='Harvester']")))
            dropdown_menu.click()
            time.sleep(2)

            try:
                print('load_more_again..')
                # close_modal= WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                # close_modal.click()
                # time.sleep(2)

                load_more = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
                
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
print('\n\reel_type.......-', reel_type)


data_dict = {
    'Brand':brand_list,
    'Model':model_list,
    'images_name':images_name,
    # 'Power':power,
    'Cutter_Width':cutterwidth,
    'No_of_Cylinder':cylinder,
    'Power_Sorce':powersource,
    'Crop':crop,
    'About':about_list,
    'Engine_Type':engine_type,
    'Engine_Rated_RPM':engine_rpm,
    'Hp_Power':power,
    'Engine_Air_Filter':engine_airfilter,

    'Minimum_Cutting_Height':cutter_min_height,
    'Maximum_Cutting_Height':cutter_max_height,
    'Cutter_Height_Adjusment':cutter_height_adj,

    'Reel_Type':reel_type,
    'Reel_Diameter':reel_dia,
    'Reel_Speed_Adjustment':speed_adjustment,
    'Max_Revolution':max_revolution,
    'Min_Revolution':min_revolution,
    'Reel_Height_Adjustment':reel_height_adj,

    'Cooling_System':cooling_sys,
    'Colling_Cap':cooling_cap,

    'Threshing_Width':threshing_width,
    'Threshing_Length':threshing_length,
    'Threshing_Diameter':threshing_diameter,
    'Threshing_Drum_Speed_Adjustment':threshing_adjusment,
    'Clearance_Concave':concave_clearance,

    'Grain_Tank_Capacity':grain_tank_capacity,

    'Transmission_Gear':transmission_gear,
    'Transmission_Clutch_Type':transmission_clutch_type,
    'Front_Tyre_Size':tyre_size_front,
    'Rear_Tyre_Size':tyre_size_rear,

    'Fuel_Tank_Capacity':fuel_tank_capacity,
    
    'Total_Weight':total_weight,
    'Dimensions_Length':dimensions_length,
    'Dimensions_Height':dimensions_height,
    'Dimensions_Width':dimensions_width,
    'Ground_Clearance':ground_clearance,
    'Image_Type_Nmae':['product']
}
df=pd.DataFrame.from_dict(data_dict, orient="index")
df= df.transpose()

writer = pd.ExcelWriter('Harvester_Infos1.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()
