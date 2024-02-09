import time
import urllib
import os
import errno
import re
from urllib.parse import urlparse
import xlsxwriter
import pandas as pd
from PIL import Image , ImageFont, ImageDraw
import rembg
from rembg import remove 
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

# driver.get('https://www.tractorjunction.com/')
driver.get('https://www.tractorjunction.com/latest/tyres/')

wait = WebDriverWait(driver, 15)
# driver.execute_script('window.scrollTo(0, 500)')

# nav_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.navbar-nav>li>a#navbarDropdown8')))
# nav_bar.click()
# time.sleep(1)

# dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@aria-labelledby='navbarDropdown8']/li/a[@title='Tyres']")))
# dropdown_menu.click()
# time.sleep(2)

try:
    cross_model=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal.click()
    time.sleep(2)
except TimeoutException as e:
    print('timeoutException for close external modal...')    

# new_harvester = driver.find_elements(By.CSS_SELECTOR,'div#harvesterMoreData div.implement-main>div.implement-img>a>img')

# div#tractorMoreData  div.new-tractor-main>div.new-tractor-img>a>img')
# print('new_tractors-',new_harvester,  len(new_harvester))
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

category_list=[]
tyre_position=[]
tyre_dia=[]
tyre_width=[]

buttonText = driver.find_element(By.CSS_SELECTOR, "div.container-mid p#loadMoreDiv a#loadmorebtn").get_attribute('innerHTML')
if buttonText == 'Load More Tyres':
    print('enter if--')
    load_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.container-mid p#loadMoreDiv a#loadmorebtn")))
    
    # Above if load more btn available

    load_more.click()
    time.sleep(1)
    load_more.click()
    load_more.click()
    load_more.click()
    load_more.click()

    # For load more harvester 
    count=0
    # buttonText = driver.find_element(By.CSS_SELECTOR, "div.container-mid p#loadMoreDiv>a#loadmorebtn").get_attribute('innerHTML')
    # while buttonText == 'Load More Tyres':
    #     buttonText = driver.find_element(By.CSS_SELECTOR, "div.container-mid p#loadMoreDiv>a#loadmorebtn").get_attribute('innerHTML')    
    #     if buttonText != 'Load More Tyres':
    #         break
    #     else:  
    #         count +=1
    #         print('count-', count)
    #         try:
    #             load_more = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.container-mid p#loadMoreDiv a#loadmorebtn")))
    #             driver.execute_script("arguments[0].click();", load_more)
    #             print('clicked on load')  
              
    #             modal=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.modal-dialog div.modal-content span.close")))
    #             close_modal= WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.modal-dialog div.modal-content span.close")))
    #             close_modal.click()
    #         except TimeoutException as e:
    #             print('timeoutException for loadmore...') 
    #         except ElementNotInteractableException as e:
    #             print('intercepted exception for loadmore...') 
    print('click3',count)


    for i in range(10,50):
        print('looping start...i-', i)

        try:
            try:
                print('click on image..///')
                new_harvester = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div#loadMoreTyre div:nth-child("+str(i)+")>div.implement-main>div.implement-img>a>img")))
                new_harvester.click()
                time.sleep(2)
            except TimeoutException as e:
                print('TimeoutException for close btn..///..//')

            except ElementClickInterceptedException:
                print('ElementClickInterceptedException+++....')
                driver.execute_script("arguments[0].click();", new_harvester)     

            brand = driver.find_element(By.CSS_SELECTOR, "div.product-single-features div.product-single-features-inner p>a").text
            brand_list.append(brand)

            model_name=[]
            model = driver.find_element(By.XPATH, "//li[@itemprop='itemListElement']/span[@itemprop='name']").text
            model_list.append(model)

            print('brand_list-.... ', brand_list, model_list)

            model_name_ = driver.find_element(By.CSS_SELECTOR, 
            "div.product-single-top>div.section-heading>h1").text
            model_name.append(model_name_)

            category =[]
            category = driver.find_element(By.CSS_SELECTOR, "div.product-single-top span.rateTractor").text
            category_list.append(category)

            # image_list
            tractor_images = driver.find_elements(By.CSS_SELECTOR, "div.slider div.slick-list div.slick-track div.slick-slide>img")
            src =[]

            print('leng-', len(tractor_images))

            for img in tractor_images:
                if img not in src:
                    src.append(img.get_attribute('src'))
            image_list.append(src)
        
            dirname = "imgaes/"
            imagename_list=[]
            for i in range((len(src)-1)):
                if(src[i] != ''):
                    path = urlparse(src[i]).path
                    extension = os.path.splitext(path)[1]
                    name = os.path.splitext(path)[0]
                    img_name = "img"+str(i)+"-"+name[name.rfind("/") + 1:]
                    imagename_list.append(img_name+'.png'.format(i))
                    urllib.request.urlretrieve(str(src[i]), dirname+img_name+'.png'.format(i))
                
            # files = os.listdir(dirname)
            # for file in files:
            #     print('file-',file)
            #     im = Image.open(os.path.join(dirname+file))
            #     output_path = dirname+file 

            #     output = remove(im,  bgcolor=(255, 255, 255, 255)) 
            #     output.save(output_path, quality=95) 

            print('dirname/', dirname)
            #Adding Watermark
            rem_bgfiles = os.listdir(dirname)
            for file in rem_bgfiles:
                print('file///-', file)
                with Image.open(dirname+file) as img:
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
                        d.text(((width/2+157),(height-h-20)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    elif(width==320 and height==180):
                        print('elif...')
                        d.text(((width/2+(w*1.20)),(height/2+(height/3)+h*1.3)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    else:
                        print('else//..')
                        d.text(((width/2+70),(height-h-5)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    
                    out = Image.alpha_composite(img.convert("RGBA"), txt)
                    output_path = dirname+file
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
                if 'Tyre Position'  in  feature_list:
                    index=feature_list.index('Tyre Position')
                    tyre_position.append(feature_ans_list[index]) 
                else:
                    tyre_position.append('')

                if "Tyre Diameter"  in  feature_list:
                    index=feature_list.index("Tyre Diameter")
                    tyre_dia.append(feature_ans_list[index])  
                else:
                    tyre_dia.append('')

                if 'Tyre Width'  in  feature_list:
                    index=feature_list.index('Tyre Width')
                    tyre_width.append(feature_ans_list[index])  
                else:
                    tyre_width.append('') 
            except NoSuchElementException as e:
                print('no features..') 

            about=driver.find_element(By.CSS_SELECTOR, 'div.product-single-content div.text-editor-block').text
            about_list.append(about)

            driver.back()
            time.sleep(2)

            # nav_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.navbar-nav>li>a#navbarDropdown5')))
            # nav_bar.click()
            # time.sleep(1)

            # dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@aria-labelledby='navbarDropdown5']/li/a[@title='Harvester']")))
            # dropdown_menu.click()
            # time.sleep(2)

            try:
                print('load_more_again..')
                count=0
                buttonText = driver.find_element(By.CSS_SELECTOR, "div.container-mid p#loadMoreDiv a#loadmorebtn").get_attribute('innerHTML')
                while buttonText == 'Load More Tyres':
                    buttonText = driver.find_element(By.CSS_SELECTOR, "div.container-mid p#loadMoreDiv a#loadmorebtn").get_attribute('innerHTML')    
                    if buttonText != 'Load More Tyres':
                        break
                    else:  
                        count +=1
                        print('count-', count)
                        load_more = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.container-mid p#loadMoreDiv a#loadmorebtn")))
                        driver.execute_script("arguments[0].click();", load_more)
                        print('clicked on load') 
                print('clicked on modal...///')
            except ElementClickInterceptedException as e:
                print('ElementClickInterceptedException---///')

            except TimeoutException as e:
                print('TimeoutException for load more btn..//')    

        except ElementClickInterceptedException:
            print('ElementClickInterceptedException+++....')
            driver.execute_script("arguments[0].click();", new_harvester)
        except TimeoutException as e:
            print('TimeoutException for loop-///+++')

    time.sleep(1) 
print('\n\category_list.......-', category_list)


data_dict = {
    'Brand':brand_list,
    'Model':model_list,
    'images_name':images_name,
    'category_list':category_list,
    'tyre_position':tyre_position,
    'tyre_dia':tyre_dia,
    'tyre_width':tyre_width,
    'About':about_list,
    'Image_Type_Nmae':['product']
}
df=pd.DataFrame.from_dict(data_dict, orient="index")
df= df.transpose()

writer = pd.ExcelWriter('tyre.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()