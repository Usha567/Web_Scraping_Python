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
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException,TimeoutException 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome()

# driver.get('https://www.tractorjunction.com/')
driver.get('https://www.tractorjunction.com/tractor-implements/?shortBy=&brands=&impType=10&impCat=35')

wait = WebDriverWait(driver, 15)
driver.execute_script('window.scrollTo(0, 500)')

# nav_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.navbar-nav>li>a#navbarDropdown5')))
# nav_bar.click()
# time.sleep(1)

# dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@aria-labelledby='navbarDropdown5']/li/a[@title='Harvester']")))
# dropdown_menu.click()
# time.sleep(2)

try:
    cross_model=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
    close_modal.click()
    time.sleep(2)
except TimeoutException as e:
    print('timeoutException for close external modal...')    

new_harvester = driver.find_elements(By.CSS_SELECTOR,'div#implementMoreData div.implement-main>div.implement-img>a>img')

# div#tractorMoreData  div.new-tractor-main>div.new-tractor-img>a>img')
print('new_tractors-',new_harvester,  len(new_harvester))
brand_list=[]
model_list=[]
cylinder=[]
power=[]
powersource=[]
crop=[]

hp_power =[]
pto_hp=[]
warranty=[]
price=[]
about_list=[]
implement_type=[]
# feature_list=[]
category_list=[]
implement_power=[]

buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
if buttonText == 'Load More Implements':
    print('enter if--')
    load_more = wait.until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
    # For load more implements 
    count=0
    buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
    while buttonText == 'Load More Implements':
        buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')    
        if buttonText != 'Load More Implements':
            break
        else:  
            count +=1
            print('count-', count)
            load_more = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
            driver.execute_script("arguments[0].click();", load_more)
            print('clicked on load')  
    print('click3',count)

    for i in range(1,2):
        print('looping start...i-', i)

        try:
            try:
                print('click on image..///')
                new_harvester = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div#implementMoreData div:nth-child("+str(i)+")>div.implement-main>div.implement-img>a>img")))
                new_harvester.click()
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
                m= model.split('/')
                model = m[0]+"_"+m[1]

            dirname = "Fram_Images/"
            imagename_list=[]
            for i in range((len(src))):
                if(src[i] != ''):
                    path = urlparse(src[i]).path
                    extension = os.path.splitext(path)[1]
                    name = os.path.splitext(path)[0]
                    img_name = ''.join(model.split())+"img"+str(i)+"-"+name[name.rfind("/") + 1:]
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
            # Add Watermark
            print('dirname/', dirname)
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
                    
                    if((width > 450 and width != 1400 and width != 600  and width != 500 )  and (height>180 and height!=933 and height!=350 and height!=500)):
                        print('if...')
                        d.text(((width/2+157),(height-h-12)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    if(width==500 and height==500):
                        print('if 500..')
                        d.text(((width/2+157),(height-h-12)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    if(width == 1400 and height==933):
                        print('if.1400..')
                        d.text(((width/2+320),(height-h-64)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    elif(width==320 and height==180):
                        print('elif...')
                        d.text(((width/2+(w*1.20)),(height/2+(height/3)+h*1.3)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    else:
                        print('else//..')
                        d.text(((width/2+70),(height-h-5)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                        # d.text(((width/2+112),(height-h-10)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                        
                    out = Image.alpha_composite(img.convert("RGBA"), txt)
                    output_path = dirname+file
                    out.save(output_path)

            #Moving images
            subfolder_names=[]
            source_folders =[dirname]
            for source_folder in source_folders:
                print('sorce folder-- //')
                items = os.listdir(source_folder)
                subfolders = [item for item in items if os.path.isdir(os.path.join(source_folder, item))]
                subfolder_names.extend(subfolders)
            
            destination_folder = 'Moved_Imgaes'
            for source_folder in source_folders:
                image_files = glob(os.path.join(source_folder, '*.jpg')) + glob(os.path.join(source_folder, '*.png')) + glob(os.path.join(source_folder, '*.jpeg'))
                for image_file in image_files:
                    filename = os.path.basename(image_file)
                    destination_path = os.path.join(destination_folder, filename)
                    # Move the image
                    print('moving images...')
                    shutil.move(image_file, destination_path)
        
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

            try:
                if 'Implement Type'  in  feature_list:
                    index=feature_list.index('Implement Type')
                    implement_type.append((feature_ans_list[index]).upper()) 
                else:
                    implement_type.append('')

                if "Category"  in  feature_list:
                    index=feature_list.index("Category")
                    category_list.append((feature_ans_list[index]).upper())  
                else:
                    category_list.append('')

                if 'Implement Power'  in  feature_list:
                    index=feature_list.index('Implement Power')
                    implement_power.append(feature_ans_list[index])  
                else:
                    implement_power.append('') 
                print('no features..') 

            about=driver.find_element(By.CSS_SELECTOR, 'div.product_description_main').text
            about_list.append(about)
            
            tr_list =driver.find_elements(By.CSS_SELECTOR,"div.product-single-content div.text-editor-block div.table-block table>tbody tr")
            tr_text_list=[]
            tr_text_list_withcolon=[]
            tab_ans_list=['','']

            # for tr in tr_list:
            #     tr_text = tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
            #     text = (tr_text.text).lstrip()
            #     tr_text_list_withcolon.append(text)
            #     if ':' in text:
            #         tr_text_list.append(text[:-1])
            #     else:    
            #         tr_text_list.append(text)

            cancave_text_list=[]
            cancave_ans_list=[]
            

            for tr in tr_list:
                try:
                    tr_text = tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
                    text = (tr_text.text).lstrip()
                    print('text is - ', text)
                    if (text.capitalize()).strip() == 'Standard Fitments Features' or (text.capitalize()).strip() == 'Engine':
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+5):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('rangei-', i, new_tr_text) 
                                if ':' in new_tr_text:
                                    (engine_text_list.append((new_tr_text[:-1]).strip()))
                                else:
                                    engine_text_list.append((new_tr_text).strip())  
                                engine_ans_list.append(new_tr_ans_text)
                            except IndexError as e:
                                print('Index error...')
                            except NoSuchElementException as e:
                                print('No such element')   

                    if  (text).strip() == 'CUTTER BAR' or (text).strip() == 'Cutter Bar' or (text).strip() == 'CUTTER BAR MECHANISM' or (text).strip() == 'Cutter-bar': 
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+6):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('cutter rangei-', i, new_tr_text, new_tr_ans_text) 
                                if ':' in new_tr_text:
                                    cutting_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    cutting_text_list.append((new_tr_text).strip())    
                                cutting_ans_list.append(new_tr_ans_text)
                            except IndexError as e:
                                print('Index error...')
                            except NoSuchElementException as e:
                                print('No such element') 
                    
                    if  (text).strip() == 'Reel Assembly' or (text).strip() == 'REEL' or (text).strip() == 'REAL'  or (text).strip() == 'Reel': 
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+4):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('rangei-', i, new_tr_text)
                                if ':' in new_tr_text:
                                    reel_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    reel_text_list.append((new_tr_text).strip())        
                                reel_ans_list.append(new_tr_ans_text)
                            except IndexError as e:
                                print('Index error...')
                            except NoSuchElementException as e:
                                print('No such element')     

                    if  (text).strip() == 'THRESHING EQUIPMENT' or  (text).strip() == 'THRESHING DRUM' or (text).strip() == 'Threshing System' or (text).strip() == 'Thresher Drum': 
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+7):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('rangei-', i, new_tr_text)
                                if new_tr_text !='':
                                    if ':' in new_tr_text:
                                        threshing_text_list.append((new_tr_text[:-1]).strip())
                                    else:
                                        threshing_text_list.append((new_tr_text).strip())    
                                else:
                                    threshing_text_list.append('')

                                if new_tr_ans_text !='':
                                    threshing_ans_list.append(new_tr_ans_text[:-1])
                                else:
                                    threshing_ans_list.append('') 
                            except IndexError as e:
                                print('Index error...')
                            except NoSuchElementException as e:
                                print('No such element')
                    
                    if  (text).strip() == 'Concave':
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+4):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('rangei-', i, new_tr_text)
                                if new_tr_text !='':
                                    if ':' in new_tr_text:
                                        cancave_text_list.append((new_tr_text[:-1]).strip())
                                    else:
                                        cancave_text_list.append((new_tr_text).strip())    
                                else:
                                    cancave_text_list.append('')

                                if new_tr_ans_text !='':
                                    cancave_ans_list.append(new_tr_ans_text[:-1])
                                else:
                                    cancave_ans_list.append('') 
                            except IndexError as e:
                                print('Index error...')
                            except NoSuchElementException as e:
                                print('No such element')

                    if  (text).strip() == 'Grain Tank': 
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+4):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('rangei-', i, new_tr_text)
                                if new_tr_text !='':
                                    if ':' in new_tr_text:   
                                        graintank_text_list.append((new_tr_text[:-1]).strip())
                                    else:
                                        graintank_text_list.append((new_tr_text).strip())
                                else:
                                    graintank_text_list.append('')

                                if new_tr_ans_text !='':   
                                    graintank_ans_list.append(new_tr_ans_text)
                                else:
                                    graintank_ans_list.append('') 
                            except IndexError as e:
                                print('Index error...') 
                            except NoSuchElementException as e:
                                print('No such element')                                   
                
                    if  (text).strip() == 'CAPACITY' or (text).strip() == 'Capacity (Ltr)' or (text).strip() == 'Capacity': 
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+3):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('rangei-', i, new_tr_text)
                                if new_tr_text !='':
                                    if ':' in new_tr_text:  
                                        capacity_text_list.append((new_tr_text[:-1]).strip())
                                    else:
                                        capacity_text_list.append((new_tr_text).strip())    
                                else:
                                    capacity_text_list.append('')

                                if new_tr_ans_text !='':   
                                    capacity_ans_list.append(new_tr_ans_text)
                                else:
                                    capacity_ans_list.append('') 
                            except IndexError as e:
                                print('Index error...') 
                            except NoSuchElementException as e:
                                print('No such element')                                   
                    
                    if  (text.capitalize()).strip() == 'Clutch': 
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+2):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('rangei-', i, new_tr_text)
                                if new_tr_text !='':
                                    if ':' in new_tr_text:  
                                        clutch_text_list.append((new_tr_text[:-1]).strip())
                                    else:
                                        clutch_text_list.append((new_tr_text).strip())    
                                else:
                                    clutch_text_list.append('')

                                if new_tr_ans_text !='':   
                                    clutch_ans_list.append(new_tr_ans_text)
                                else:
                                    clutch_ans_list.append('')
                            except IndexError as e:
                                print('Index error...')    
                            except NoSuchElementException as e:
                                print('No such element')          

                    if  (text.capitalize()).strip() == 'Tyres' or (text).strip() =='Tyre Sizes' or  (text).strip() =='Tyre Size' or (text).strip() =='TYRE SIZE': 
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+3):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('rangei-', i, new_tr_text)
                                if new_tr_text !='':
                                    if ':' in new_tr_text:  
                                        tyre_text_list.append((new_tr_text[:-1]).strip())
                                    else:
                                        tyre_text_list.append((new_tr_text).strip())    
                                else:
                                    tyre_text_list.append('')

                                if new_tr_ans_text !='':   
                                    tyre_ans_list.append(new_tr_ans_text)
                                else:
                                    tyre_ans_list.append('')
                            except IndexError as e:
                                print('Index error...')            
                            except NoSuchElementException as e:
                                print('No such element')         

                    if  (text).strip() == 'Overall Dimension' or (text).strip() =='Overall dimensions' or (text).strip() == 'Dimensions' or (text).strip() == 'DIMENSIONS' or (text).strip() == 'Overall Dimension (mm)': 
                        index = tr_list.index(tr)
                        print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                        for i in range(index+1, index+7):
                            try:
                                new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                                new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                                print('dimen rangei-', i,new_tr_text, new_tr_ans_text)
                                if new_tr_text !='':
                                    if ':' in new_tr_text: 
                                        dimension_text_list.append((new_tr_text[:-1]).strip())
                                    else:
                                        dimension_text_list.append((new_tr_text).strip())    
                                else:
                                    dimension_text_list.append('')

                                if new_tr_ans_text !='':   
                                    dimension_ans_list.append(new_tr_ans_text)
                                else:
                                    dimension_ans_list.append('')
                            except IndexError as e:
                                print('Index error...')        
                            except NoSuchElementException as e:
                                print('No such element')         
                
                except NoSuchElementException as e:
                    print('NoSuchElementException---')

            print('engine_text_list-', engine_text_list)

            cylinder=[]
            if 'No.of Cylinder' in engine_text_list or 'No.of Cylinders' in engine_text_list or  'No. Of Cylinders' in engine_text_list or 'Cylinders/Displacements' in engine_text_list or 'Cylinders' in engine_text_list:
                print('')
                if 'No.of Cylinder' in engine_text_list:
                    index_of = engine_text_list.index('No.of Cylinder')
                if 'No.of Cylinders' in engine_text_list:
                    index_of = engine_text_list.index('No.of Cylinders')
                if 'No. Of Cylinders' in engine_text_list:
                    index_of = engine_text_list.index('No. Of Cylinders')        
                if 'Cylinders/Displacements' in engine_text_list:
                    index_of = engine_text_list.index('Cylinders/Displacements')   
                if 'Cylinders' in engine_text_list:
                    index_of = engine_text_list.index('Cylinders')       
                text=engine_ans_list[index_of]
                cylinder.append(text)  
            else:
                cylinder.append('')
            if 'Rated Speed' in engine_text_list or 'Rated Engine Speed' in engine_text_list:
                if 'Rated Speed' in engine_text_list:
                    index_of = engine_text_list.index('Rated Speed')
                if 'Rated Engine Speed' in engine_text_list:
                    index_of = engine_text_list.index('Rated Engine Speed')
                text=engine_ans_list[index_of]
                engine_rpm.append(text)  
            else:
                engine_rpm.append('') 

            if 'Air Cleaner' in engine_text_list:
                index_of = engine_text_list.index('Air Cleaner')
                text=engine_ans_list[index_of]
                engine_airfilter.append(text)  
            else:
                engine_airfilter.append('') 

            # engine_airfilter.append('')
            print('cutting_text_list-', cutting_text_list, cutting_ans_list)
            
            if 'Cutting Height Max.' in cutting_text_list or 'Cutting Height Max' in cutting_text_list:
                if 'Cutting Height Max.' in cutting_text_list:
                    index_of = cutting_text_list.index('Cutting Height Max.')
                if 'Cutting Height Max' in cutting_text_list:
                    index_of = cutting_text_list.index('Cutting Height Max')    
                text=cutting_ans_list[index_of]
                cutter_max_height.append(text)  
            else:
                cutter_max_height.append('') 

            if 'Cutting Height Min.' in cutting_text_list or 'Cutting Height Min' in cutting_text_list:
                if 'Cutting Height Min.' in cutting_text_list:
                    index_of = cutting_text_list.index('Cutting Height Min.')
                if 'Cutting Height Min' in cutting_text_list:
                    index_of = cutting_text_list.index('Cutting Height Min')    
                text=cutting_ans_list[index_of]
                cutter_min_height.append(text)  
            else:
                cutter_min_height.append('') 

            if 'Height Adjustment' in cutting_text_list or 'Height Adjustments' in cutting_text_list:
                if 'Height Adjustment' in cutting_text_list:
                    index_of = cutting_text_list.index('Height Adjustment')
                if 'Height Adjustments' in cutting_text_list:
                    index_of = cutting_text_list.index('Height Adjustments')    
                text=cutting_ans_list[index_of]
                cutter_height_adj.append(text)  
            else:
                cutter_height_adj.append('')   

            print('reel_text_list-', reel_text_list)    

            if 'Type' in reel_text_list or 'TYPE' in reel_text_list:
                if 'Type' in reel_text_list:
                    index_of = reel_text_list.index('Type')
                if 'TYPE' in reel_text_list:
                    index_of = reel_text_list.index('TYPE')    
                text=reel_ans_list[index_of]
                reel_type.append(text)  
            else:
                reel_type.append('') 

            if 'Dia of Reel (mm)' in reel_text_list or 'DIA (mm)' in reel_text_list:
                if 'Dia of Reel (mm)' in reel_text_list:
                    index_of = reel_text_list.index('Dia of Reel (mm)')
                if 'DIA (mm)' in reel_text_list:
                    index_of = reel_text_list.index('DIA (mm)')    
                text=reel_ans_list[index_of]
                reel_dia.append(text)  
            else:
                reel_dia.append('')

            if 'Speed Adjustment' in reel_text_list or 'Speed Adjustments' in reel_text_list:
                if 'Speed Adjustment' in reel_text_list:
                    index_of = reel_text_list.index('Speed Adjustment')
                if 'Speed Adjustments' in reel_text_list:
                    index_of = reel_text_list.index('Speed Adjustments')    
                text=reel_ans_list[index_of]
                speed_adjustment.append(text)  
            else:
                speed_adjustment.append('')

            if 'Max Revolution' in reel_text_list:
                index_of = reel_text_list.index('Max Revolution')
                text=reel_ans_list[index_of]
                max_revolution.append(text)  
            else:
                max_revolution.append('') 

            if 'Min Revolution' in reel_text_list:
                index_of = reel_text_list.index('Min Revolution')
                text=reel_ans_list[index_of]
                min_revolution.append(text)  
            else:
                min_revolution.append('')

            if 'Height Adjustment' in reel_text_list or 'Height Adjustments' in reel_text_list:
                if 'Height Adjustment' in reel_text_list:   
                    index_of = reel_text_list.index('Height Adjustment')
                if  'Height Adjustments' in reel_text_list:
                    index_of = reel_text_list.index('Height Adjustments')
                text=reel_ans_list[index_of]
                reel_height_adj.append(text)  
            else:
                reel_height_adj.append('')                     

            if 'Cooling System' in engine_text_list:
                index_of = engine_text_list.index('Cooling System')
                text=engine_ans_list[index_of]
                cooling_sys.append(text)  
            else: 
                cooling_sys.append('') 
            
            if 'Coolent Capcity' in engine_text_list:
                index_of = engine_text_list.index('Coolent Capcity')
                text=engine_ans_list[index_of]
                cooling_cap.append(text)  
            else:
                cooling_cap.append('')

            print('threshing_text_list-', threshing_text_list)        

            if 'Width (mm)' in threshing_text_list or 'Width' in threshing_text_list or 'Threshing Section Width' in threshing_text_list or 'Drum Width' in threshing_text_list:
                if 'Width (mm)' in threshing_text_list:
                    index_of = threshing_text_list.index('Width (mm)')
                if 'Width' in threshing_text_list:  
                    index_of = threshing_text_list.index('Width')
                if 'Threshing Section Width'  in threshing_text_list:
                    index_of = threshing_text_list.index('Threshing Section Width')
                if 'Drum Width' in threshing_text_list:
                    index_of = threshing_text_list.index('Drum Width')   
                text=threshing_ans_list[index_of]
                threshing_width.append(text)  
            else:
                threshing_width.append('')

            if 'Length of Drum' in threshing_text_list or 'Length' in threshing_text_list :
                if 'Length of Drum' in threshing_text_list:
                    index_of = threshing_text_list.index('Length of Drum')
                if 'Length' in threshing_text_list:
                    index_of = threshing_text_list.index('Length')    
                text=threshing_ans_list[index_of]
                threshing_length.append(text)  
            else:
                threshing_length.append('') 

            if 'Outside dia (mm)' in threshing_text_list  or 'Dia of Drum' in threshing_text_list   or 'Diameter' in threshing_text_list or 'Drum Diameter' in threshing_text_list:
                if 'Outside dia (mm)' in threshing_text_list:
                    index_of = threshing_text_list.index('Outside dia (mm)')
                if 'Diameter' in threshing_text_list:
                    index_of = threshing_text_list.index('Diameter')
                if 'Drum Diameter' in threshing_text_list:
                    index_of = threshing_text_list.index('Drum Diameter')
                if 'Dia of Drum' in threshing_text_list:
                    index_of = threshing_text_list.index('Dia of Drum')    
                text=threshing_ans_list[index_of]
                threshing_diameter.append(text)  
            else:
                threshing_diameter.append('') 

            if 'Adjustment' in threshing_text_list or  'Speed Adjustment' in threshing_text_list:
                if 'Adjustment' in threshing_text_list:
                    index_of = threshing_text_list.index('Adjustment')
                if 'Speed Adjustment' in threshing_text_list:
                    index_of = threshing_text_list.index('Speed Adjustment')
                text=threshing_ans_list[index_of]
                threshing_adjusment.append(text)  
            else:
                threshing_adjusment.append('') 

            if 'Clearance' in threshing_text_list or 'Clearance Between' in cancave_text_list:
                if 'Clearance' in threshing_text_list:
                    index_of = threshing_text_list.index('Clearance')
                    text=threshing_ans_list[index_of]
                if 'Clearance Between' in cancave_text_list:
                    index_of = cancave_text_list.index('Clearance Between')    
                    text=cancave_ans_list[index_of]
                concave_clearance.append(text)  
            else:
                concave_clearance.append('')

            print('graintank_text_list-', graintank_text_list)     

            if 'Capacity: Volume Basis (m3)' in graintank_text_list  or 'Capacity' in graintank_text_list or 'Capacity (L)' in graintank_text_list:
                if 'Capacity: Volume Basis (m3)' in graintank_text_list:
                    index_of = graintank_text_list.index('Capacity: Volume Basis (m3)')
                if 'Capacity' in graintank_text_list:
                    index_of = graintank_text_list.index('Capacity')  
                if 'Capacity (L)' in graintank_text_list:
                    index_of = graintank_text_list.index('Capacity (L)')      
                text=graintank_ans_list[index_of]
                grain_tank_capacity.append(text)  
            else:
                print('ele- cap')
                if 'Grain Tank' in capacity_text_list or 'Grain Tank Capacity' in capacity_text_list:
                    if 'Grain Tank' in capacity_text_list:
                        index_of = capacity_text_list.index('Grain Tank')
                    if 'Grain Tank Capacity' in capacity_text_list:
                        index_of = capacity_text_list.index('Grain Tank Capacity')    
                    text=capacity_ans_list[index_of]
                    grain_tank_capacity.append(text) 
                else:    
                    grain_tank_capacity.append('')                   

            transmission_gear.append('')

            print('clutch_text_list-', clutch_text_list) 

            if 'Type' in clutch_text_list:
                index_of = clutch_text_list.index('Type')
                text=clutch_ans_list[index_of]
                transmission_clutch_type.append(text)  
            else:
                transmission_clutch_type.append('') 

            print('tyre_text_list-', tyre_text_list)     

            if 'Front' in tyre_text_list:
                index_of = tyre_text_list.index('Front')
                text=tyre_ans_list[index_of]
                tyre_size_front.append(text)  
            else:
                if 'Front Tyre Sizes' in dimension_text_list:
                    index_of = dimension_text_list.index('Front Tyre Sizes')
                    text=dimension_ans_list[index_of]
                    tyre_size_front.append(text)
                else: 
                    tyre_size_front.append('')

            if 'Rear' in tyre_text_list  or 'Rear/Trolley' in tyre_text_list :
                if 'Rear' in tyre_text_list:
                    index_of = tyre_text_list.index('Rear')
                if 'Rear/Trolley' in tyre_text_list:
                    index_of = tyre_text_list.index('Rear/Trolley')   
                text=tyre_ans_list[index_of]
                tyre_size_rear.append(text)  
            else:
                if 'Rear Tyre Sizes'  in dimension_text_list:
                    index_of = dimension_text_list.index('Rear Tyre Sizes')
                    text=dimension_ans_list[index_of]
                    tyre_size_rear.append(text)
                else:     
                    tyre_size_rear.append('') 

            print('capacity_text_list-', capacity_text_list)           

            if 'Fuel Tank' in capacity_text_list or 'Fuel tank capacity Ltr.' in capacity_text_list or 'Fuel Tank Capacity' in capacity_text_list:
                    if 'Fuel Tank' in capacity_text_list:
                        index_of = capacity_text_list.index('Fuel Tank')
                    if 'Fuel tank capacity Ltr.' in capacity_text_list:
                        index_of = capacity_text_list.index('Fuel tank capacity Ltr.') 
                    if 'Fuel Tank Capacity' in capacity_text_list:
                        index_of = capacity_text_list.index('Fuel Tank Capacity') 
                    text=capacity_ans_list[index_of]
                    fuel_tank_capacity.append(text) 
            else:    
                fuel_tank_capacity.append('')
            
            print('dimension_text_list-', dimension_text_list)

            if 'Weight' in dimension_text_list or 'Machine Weight' in dimension_text_list:
                if 'Weight' in dimension_text_list:
                    index_of = dimension_text_list.index('Weight')
                if 'Machine Weight' in dimension_text_list: 
                    index_of = dimension_text_list.index('Machine Weight')   
                text=dimension_ans_list[index_of]
                total_weight.append(text)  
            else:
                total_weight.append('')

            if 'Length (mm)' in dimension_text_list or 'Length' in dimension_text_list or 'Length (including cutterbar )' in dimension_text_list or 'Length (with front attachment )' in dimension_text_list:
                if 'Length (mm)' in dimension_text_list:
                    index_of = dimension_text_list.index('Length (mm)')
                if 'Length' in dimension_text_list:
                    index_of = dimension_text_list.index('Length') 
                if 'Length (including cutterbar )' in dimension_text_list:
                    index_of = dimension_text_list.index('Length (including cutterbar )')
                if 'Length (with front attachment )' in dimension_text_list:
                    index_of = dimension_text_list.index('Length (with front attachment )')
                text=dimension_ans_list[index_of]
                dimensions_length.append(text)  
            else:
                dimensions_length.append('')

            if 'Height' in dimension_text_list or 'Height (Working Position)' in dimension_text_list:
                if 'Height' in dimension_text_list:
                    index_of = dimension_text_list.index('Height')
                if 'Height (Working Position)' in dimension_text_list:
                    index_of = dimension_text_list.index('Height (Working Position)')    
                text=dimension_ans_list[index_of]
                dimensions_height.append(text)  
            else:
                dimensions_height.append('')

            if 'Width (mm)' in dimension_text_list or 'Width' in dimension_text_list:
                if 'Width (mm)' in dimension_text_list:
                    index_of = dimension_text_list.index('Width (mm)')
                if  'Width' in dimension_text_list:
                    index_of = dimension_text_list.index('Width')   
                text=dimension_ans_list[index_of]
                dimensions_width.append(text)  
            else:
                dimensions_width.append('')

            if 'Ground Clearance' in tyre_text_list or 'Ground Clearance' in dimension_text_list or 'Min. Ground Clearance' in dimension_text_list:
                print('ground here--')
                if 'Ground Clearance' in tyre_text_list: 
                    index_of = tyre_text_list.index('Ground Clearance')
                    text=tyre_ans_list[index_of]
                if 'Ground Clearance' in dimension_text_list:
                    index_of = dimension_text_list.index('Ground Clearance')    
                    text=dimension_ans_list[index_of]
                if 'Min. Ground Clearance' in dimension_text_list:
                    index_of = dimension_text_list.index('Min. Ground Clearance')  
                    text=dimension_ans_list[index_of]  
                
                if 'Min Ground Clearance' in dimension_text_list:
                    index_of = dimension_text_list.index('Min Ground Clearance')  
                    text=dimension_ans_list[index_of]      
                ground_clearance.append(text)  
            else:
                print('else---ground here--')
                if 'Ground clearance' in dimension_text_list:
                    index_of = dimension_text_list.index('Ground clearance')
                    text=dimension_ans_list[index_of]      
                    ground_clearance.append(text)
                else:
                    ground_clearance.append('')                 
            
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
                # close_modal= WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
                # close_modal.click()
                # time.sleep(2)

                load_more = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
                
                buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
                while buttonText == 'Load More Implements':
                    buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')    
                    if buttonText != 'Load More Implements':
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
            driver.execute_script("arguments[0].click();", new_harvester)
        except TimeoutException as e:
            print('TimeoutException for loop-///+++')

else:
    print('else..no more btn.. ')
    for i in range(1,2):
    print('looping start...i-', i)

    try:
        try:
            print('click on image..///')
            new_harvester = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div#implementMoreData div:nth-child("+str(i)+")>div.implement-main>div.implement-img>a>img")))
            new_harvester.click()
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
            m= model.split('/')
            model = m[0]+"_"+m[1]

        dirname = "Fram_Images/"
        imagename_list=[]
        for i in range((len(src))):
            if(src[i] != ''):
                path = urlparse(src[i]).path
                extension = os.path.splitext(path)[1]
                name = os.path.splitext(path)[0]
                img_name = ''.join(model.split())+"img"+str(i)+"-"+name[name.rfind("/") + 1:]
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
        # Add Watermark
        print('dirname/', dirname)
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
                
                if((width > 450 and width != 1400 and width != 600  and width != 500 )  and (height>180 and height!=933 and height!=350 and height!=500)):
                    print('if...')
                    d.text(((width/2+157),(height-h-12)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                if(width==500 and height==500):
                    print('if 500..')
                    d.text(((width/2+157),(height-h-12)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                if(width == 1400 and height==933):
                    print('if.1400..')
                    d.text(((width/2+320),(height-h-64)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                elif(width==320 and height==180):
                    print('elif...')
                    d.text(((width/2+(w*1.20)),(height/2+(height/3)+h*1.3)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                else:
                    print('else//..')
                    d.text(((width/2+70),(height-h-5)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    # d.text(((width/2+112),(height-h-10)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
                    
                out = Image.alpha_composite(img.convert("RGBA"), txt)
                output_path = dirname+file
                out.save(output_path)

        #Moving images
        subfolder_names=[]
        source_folders =[dirname]
        for source_folder in source_folders:
            print('sorce folder-- //')
            items = os.listdir(source_folder)
            subfolders = [item for item in items if os.path.isdir(os.path.join(source_folder, item))]
            subfolder_names.extend(subfolders)
        
        destination_folder = 'Moved_Imgaes'
        for source_folder in source_folders:
            image_files = glob(os.path.join(source_folder, '*.jpg')) + glob(os.path.join(source_folder, '*.png')) + glob(os.path.join(source_folder, '*.jpeg'))
            for image_file in image_files:
                filename = os.path.basename(image_file)
                destination_path = os.path.join(destination_folder, filename)
                # Move the image
                print('moving images...')
                shutil.move(image_file, destination_path)
    
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
            if 'Implement Type'  in  feature_list:
                index=feature_list.index('Implement Type')
                implement_type.append(feature_ans_list[index]) 
            else:
                implement_type.append('')

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

        # for tr in tr_list:
        #     tr_text = tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
        #     text = (tr_text.text).lstrip()
        #     tr_text_list_withcolon.append(text)
        #     if ':' in text:
        #         tr_text_list.append(text[:-1])
        #     else:    
        #         tr_text_list.append(text)
        
        engine_text_list=[]
        engine_ans_list=[]

        cutting_text_list =[]
        cutting_ans_list =[]

        reel_text_list =[]
        reel_ans_list =[]

        threshing_text_list=[]
        threshing_ans_list=[]

        graintank_text_list=[]
        graintank_ans_list=[]

        clutch_text_list =[]
        clutch_ans_list=[]

        tyre_text_list =[]
        tyre_ans_list=[]

        dimension_text_list=[]
        dimension_ans_list=[]

        capacity_text_list=[]
        capacity_ans_list=[]

        cancave_text_list=[]
        cancave_ans_list=[]

        for tr in tr_list:
            try:
                tr_text = tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
                text = (tr_text.text).lstrip()
                print('text is - ', text)
                if (text.capitalize()).strip() == 'Standard Fitments Features' or (text.capitalize()).strip() == 'Engine':
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+5):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('rangei-', i, new_tr_text) 
                            if ':' in new_tr_text:
                                (engine_text_list.append((new_tr_text[:-1]).strip()))
                            else:
                                engine_text_list.append((new_tr_text).strip())  
                            engine_ans_list.append(new_tr_ans_text)
                        except IndexError as e:
                            print('Index error...')
                        except NoSuchElementException as e:
                            print('No such element')   

                if  (text).strip() == 'CUTTER BAR' or (text).strip() == 'Cutter Bar' or (text).strip() == 'CUTTER BAR MECHANISM' or (text).strip() == 'Cutter-bar': 
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+6):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('cutter rangei-', i, new_tr_text, new_tr_ans_text) 
                            if ':' in new_tr_text:
                                cutting_text_list.append((new_tr_text[:-1]).strip())
                            else:
                                cutting_text_list.append((new_tr_text).strip())    
                            cutting_ans_list.append(new_tr_ans_text)
                        except IndexError as e:
                            print('Index error...')
                        except NoSuchElementException as e:
                            print('No such element') 
                
                if  (text).strip() == 'Reel Assembly' or (text).strip() == 'REEL' or (text).strip() == 'REAL'  or (text).strip() == 'Reel': 
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+4):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('rangei-', i, new_tr_text)
                            if ':' in new_tr_text:
                                reel_text_list.append((new_tr_text[:-1]).strip())
                            else:
                                reel_text_list.append((new_tr_text).strip())        
                            reel_ans_list.append(new_tr_ans_text)
                        except IndexError as e:
                            print('Index error...')
                        except NoSuchElementException as e:
                            print('No such element')     

                if  (text).strip() == 'THRESHING EQUIPMENT' or  (text).strip() == 'THRESHING DRUM' or (text).strip() == 'Threshing System' or (text).strip() == 'Thresher Drum': 
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+7):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('rangei-', i, new_tr_text)
                            if new_tr_text !='':
                                if ':' in new_tr_text:
                                    threshing_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    threshing_text_list.append((new_tr_text).strip())    
                            else:
                                threshing_text_list.append('')

                            if new_tr_ans_text !='':
                                threshing_ans_list.append(new_tr_ans_text[:-1])
                            else:
                                threshing_ans_list.append('') 
                        except IndexError as e:
                            print('Index error...')
                        except NoSuchElementException as e:
                            print('No such element')
                
                if  (text).strip() == 'Concave':
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+4):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('rangei-', i, new_tr_text)
                            if new_tr_text !='':
                                if ':' in new_tr_text:
                                    cancave_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    cancave_text_list.append((new_tr_text).strip())    
                            else:
                                cancave_text_list.append('')

                            if new_tr_ans_text !='':
                                cancave_ans_list.append(new_tr_ans_text[:-1])
                            else:
                                cancave_ans_list.append('') 
                        except IndexError as e:
                            print('Index error...')
                        except NoSuchElementException as e:
                            print('No such element')

                if  (text).strip() == 'Grain Tank': 
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+4):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('rangei-', i, new_tr_text)
                            if new_tr_text !='':
                                if ':' in new_tr_text:   
                                    graintank_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    graintank_text_list.append((new_tr_text).strip())
                            else:
                                graintank_text_list.append('')

                            if new_tr_ans_text !='':   
                                graintank_ans_list.append(new_tr_ans_text)
                            else:
                                graintank_ans_list.append('') 
                        except IndexError as e:
                            print('Index error...') 
                        except NoSuchElementException as e:
                            print('No such element')                                   
            
                if  (text).strip() == 'CAPACITY' or (text).strip() == 'Capacity (Ltr)' or (text).strip() == 'Capacity': 
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+3):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('rangei-', i, new_tr_text)
                            if new_tr_text !='':
                                if ':' in new_tr_text:  
                                    capacity_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    capacity_text_list.append((new_tr_text).strip())    
                            else:
                                capacity_text_list.append('')

                            if new_tr_ans_text !='':   
                                capacity_ans_list.append(new_tr_ans_text)
                            else:
                                capacity_ans_list.append('') 
                        except IndexError as e:
                            print('Index error...') 
                        except NoSuchElementException as e:
                            print('No such element')                                   
                
                if  (text.capitalize()).strip() == 'Clutch': 
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+2):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('rangei-', i, new_tr_text)
                            if new_tr_text !='':
                                if ':' in new_tr_text:  
                                    clutch_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    clutch_text_list.append((new_tr_text).strip())    
                            else:
                                clutch_text_list.append('')

                            if new_tr_ans_text !='':   
                                clutch_ans_list.append(new_tr_ans_text)
                            else:
                                clutch_ans_list.append('')
                        except IndexError as e:
                            print('Index error...')    
                        except NoSuchElementException as e:
                            print('No such element')          

                if  (text.capitalize()).strip() == 'Tyres' or (text).strip() =='Tyre Sizes' or  (text).strip() =='Tyre Size' or (text).strip() =='TYRE SIZE': 
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+3):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('rangei-', i, new_tr_text)
                            if new_tr_text !='':
                                if ':' in new_tr_text:  
                                    tyre_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    tyre_text_list.append((new_tr_text).strip())    
                            else:
                                tyre_text_list.append('')

                            if new_tr_ans_text !='':   
                                tyre_ans_list.append(new_tr_ans_text)
                            else:
                                tyre_ans_list.append('')
                        except IndexError as e:
                            print('Index error...')            
                        except NoSuchElementException as e:
                            print('No such element')         

                if  (text).strip() == 'Overall Dimension' or (text).strip() =='Overall dimensions' or (text).strip() == 'Dimensions' or (text).strip() == 'DIMENSIONS' or (text).strip() == 'Overall Dimension (mm)': 
                    index = tr_list.index(tr)
                    print('index-',index,  tr.find_element(By.CSS_SELECTOR,  "td:nth-child(1)").text)
                    for i in range(index+1, index+7):
                        try:
                            new_tr_text = (tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text).strip()
                            new_tr_ans_text = tr_list[i].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                            print('dimen rangei-', i,new_tr_text, new_tr_ans_text)
                            if new_tr_text !='':
                                if ':' in new_tr_text: 
                                    dimension_text_list.append((new_tr_text[:-1]).strip())
                                else:
                                    dimension_text_list.append((new_tr_text).strip())    
                            else:
                                dimension_text_list.append('')

                            if new_tr_ans_text !='':   
                                dimension_ans_list.append(new_tr_ans_text)
                            else:
                                dimension_ans_list.append('')
                        except IndexError as e:
                            print('Index error...')        
                        except NoSuchElementException as e:
                            print('No such element')         
            
            except NoSuchElementException as e:
                print('NoSuchElementException---')

        print('engine_text_list-', engine_text_list)

        cylinder=[]
        if 'No.of Cylinder' in engine_text_list or 'No.of Cylinders' in engine_text_list or  'No. Of Cylinders' in engine_text_list or 'Cylinders/Displacements' in engine_text_list or 'Cylinders' in engine_text_list:
            print('')
            if 'No.of Cylinder' in engine_text_list:
                index_of = engine_text_list.index('No.of Cylinder')
            if 'No.of Cylinders' in engine_text_list:
                index_of = engine_text_list.index('No.of Cylinders')
            if 'No. Of Cylinders' in engine_text_list:
                index_of = engine_text_list.index('No. Of Cylinders')        
            if 'Cylinders/Displacements' in engine_text_list:
                index_of = engine_text_list.index('Cylinders/Displacements')   
            if 'Cylinders' in engine_text_list:
                index_of = engine_text_list.index('Cylinders')       
            text=engine_ans_list[index_of]
            cylinder.append(text)  
        else:
            cylinder.append('')
        if 'Rated Speed' in engine_text_list or 'Rated Engine Speed' in engine_text_list:
            if 'Rated Speed' in engine_text_list:
                index_of = engine_text_list.index('Rated Speed')
            if 'Rated Engine Speed' in engine_text_list:
                index_of = engine_text_list.index('Rated Engine Speed')
            text=engine_ans_list[index_of]
            engine_rpm.append(text)  
        else:
            engine_rpm.append('') 

        if 'Air Cleaner' in engine_text_list:
            index_of = engine_text_list.index('Air Cleaner')
            text=engine_ans_list[index_of]
            engine_airfilter.append(text)  
        else:
            engine_airfilter.append('') 

        # engine_airfilter.append('')
        print('cutting_text_list-', cutting_text_list, cutting_ans_list)
        
        if 'Cutting Height Max.' in cutting_text_list or 'Cutting Height Max' in cutting_text_list:
            if 'Cutting Height Max.' in cutting_text_list:
                index_of = cutting_text_list.index('Cutting Height Max.')
            if 'Cutting Height Max' in cutting_text_list:
                index_of = cutting_text_list.index('Cutting Height Max')    
            text=cutting_ans_list[index_of]
            cutter_max_height.append(text)  
        else:
            cutter_max_height.append('') 

        if 'Cutting Height Min.' in cutting_text_list or 'Cutting Height Min' in cutting_text_list:
            if 'Cutting Height Min.' in cutting_text_list:
                index_of = cutting_text_list.index('Cutting Height Min.')
            if 'Cutting Height Min' in cutting_text_list:
                index_of = cutting_text_list.index('Cutting Height Min')    
            text=cutting_ans_list[index_of]
            cutter_min_height.append(text)  
        else:
            cutter_min_height.append('') 

        if 'Height Adjustment' in cutting_text_list or 'Height Adjustments' in cutting_text_list:
            if 'Height Adjustment' in cutting_text_list:
                index_of = cutting_text_list.index('Height Adjustment')
            if 'Height Adjustments' in cutting_text_list:
                index_of = cutting_text_list.index('Height Adjustments')    
            text=cutting_ans_list[index_of]
            cutter_height_adj.append(text)  
        else:
            cutter_height_adj.append('')   

        print('reel_text_list-', reel_text_list)    

        if 'Type' in reel_text_list or 'TYPE' in reel_text_list:
            if 'Type' in reel_text_list:
                index_of = reel_text_list.index('Type')
            if 'TYPE' in reel_text_list:
                index_of = reel_text_list.index('TYPE')    
            text=reel_ans_list[index_of]
            reel_type.append(text)  
        else:
            reel_type.append('') 

        if 'Dia of Reel (mm)' in reel_text_list or 'DIA (mm)' in reel_text_list:
            if 'Dia of Reel (mm)' in reel_text_list:
                index_of = reel_text_list.index('Dia of Reel (mm)')
            if 'DIA (mm)' in reel_text_list:
                index_of = reel_text_list.index('DIA (mm)')    
            text=reel_ans_list[index_of]
            reel_dia.append(text)  
        else:
            reel_dia.append('')

        if 'Speed Adjustment' in reel_text_list or 'Speed Adjustments' in reel_text_list:
            if 'Speed Adjustment' in reel_text_list:
                index_of = reel_text_list.index('Speed Adjustment')
            if 'Speed Adjustments' in reel_text_list:
                index_of = reel_text_list.index('Speed Adjustments')    
            text=reel_ans_list[index_of]
            speed_adjustment.append(text)  
        else:
            speed_adjustment.append('')

        if 'Max Revolution' in reel_text_list:
            index_of = reel_text_list.index('Max Revolution')
            text=reel_ans_list[index_of]
            max_revolution.append(text)  
        else:
            max_revolution.append('') 

        if 'Min Revolution' in reel_text_list:
            index_of = reel_text_list.index('Min Revolution')
            text=reel_ans_list[index_of]
            min_revolution.append(text)  
        else:
            min_revolution.append('')

        if 'Height Adjustment' in reel_text_list or 'Height Adjustments' in reel_text_list:
            if 'Height Adjustment' in reel_text_list:   
                index_of = reel_text_list.index('Height Adjustment')
            if  'Height Adjustments' in reel_text_list:
                index_of = reel_text_list.index('Height Adjustments')
            text=reel_ans_list[index_of]
            reel_height_adj.append(text)  
        else:
            reel_height_adj.append('')                     

        if 'Cooling System' in engine_text_list:
            index_of = engine_text_list.index('Cooling System')
            text=engine_ans_list[index_of]
            cooling_sys.append(text)  
        else: 
            cooling_sys.append('') 
        
        if 'Coolent Capcity' in engine_text_list:
            index_of = engine_text_list.index('Coolent Capcity')
            text=engine_ans_list[index_of]
            cooling_cap.append(text)  
        else:
            cooling_cap.append('')

        print('threshing_text_list-', threshing_text_list)        

        if 'Width (mm)' in threshing_text_list or 'Width' in threshing_text_list or 'Threshing Section Width' in threshing_text_list or 'Drum Width' in threshing_text_list:
            if 'Width (mm)' in threshing_text_list:
                index_of = threshing_text_list.index('Width (mm)')
            if 'Width' in threshing_text_list:  
                index_of = threshing_text_list.index('Width')
            if 'Threshing Section Width'  in threshing_text_list:
                index_of = threshing_text_list.index('Threshing Section Width')
            if 'Drum Width' in threshing_text_list:
                index_of = threshing_text_list.index('Drum Width')   
            text=threshing_ans_list[index_of]
            threshing_width.append(text)  
        else:
            threshing_width.append('')

        if 'Length of Drum' in threshing_text_list or 'Length' in threshing_text_list :
            if 'Length of Drum' in threshing_text_list:
                index_of = threshing_text_list.index('Length of Drum')
            if 'Length' in threshing_text_list:
                index_of = threshing_text_list.index('Length')    
            text=threshing_ans_list[index_of]
            threshing_length.append(text)  
        else:
            threshing_length.append('') 

        if 'Outside dia (mm)' in threshing_text_list  or 'Dia of Drum' in threshing_text_list   or 'Diameter' in threshing_text_list or 'Drum Diameter' in threshing_text_list:
            if 'Outside dia (mm)' in threshing_text_list:
                index_of = threshing_text_list.index('Outside dia (mm)')
            if 'Diameter' in threshing_text_list:
                index_of = threshing_text_list.index('Diameter')
            if 'Drum Diameter' in threshing_text_list:
                index_of = threshing_text_list.index('Drum Diameter')
            if 'Dia of Drum' in threshing_text_list:
                index_of = threshing_text_list.index('Dia of Drum')    
            text=threshing_ans_list[index_of]
            threshing_diameter.append(text)  
        else:
            threshing_diameter.append('') 

        if 'Adjustment' in threshing_text_list or  'Speed Adjustment' in threshing_text_list:
            if 'Adjustment' in threshing_text_list:
                index_of = threshing_text_list.index('Adjustment')
            if 'Speed Adjustment' in threshing_text_list:
                index_of = threshing_text_list.index('Speed Adjustment')
            text=threshing_ans_list[index_of]
            threshing_adjusment.append(text)  
        else:
            threshing_adjusment.append('') 

        if 'Clearance' in threshing_text_list or 'Clearance Between' in cancave_text_list:
            if 'Clearance' in threshing_text_list:
                index_of = threshing_text_list.index('Clearance')
                text=threshing_ans_list[index_of]
            if 'Clearance Between' in cancave_text_list:
                index_of = cancave_text_list.index('Clearance Between')    
                text=cancave_ans_list[index_of]
            concave_clearance.append(text)  
        else:
            concave_clearance.append('')

        print('graintank_text_list-', graintank_text_list)     

        if 'Capacity: Volume Basis (m3)' in graintank_text_list  or 'Capacity' in graintank_text_list or 'Capacity (L)' in graintank_text_list:
            if 'Capacity: Volume Basis (m3)' in graintank_text_list:
                index_of = graintank_text_list.index('Capacity: Volume Basis (m3)')
            if 'Capacity' in graintank_text_list:
                index_of = graintank_text_list.index('Capacity')  
            if 'Capacity (L)' in graintank_text_list:
                index_of = graintank_text_list.index('Capacity (L)')      
            text=graintank_ans_list[index_of]
            grain_tank_capacity.append(text)  
        else:
            print('ele- cap')
            if 'Grain Tank' in capacity_text_list or 'Grain Tank Capacity' in capacity_text_list:
                if 'Grain Tank' in capacity_text_list:
                    index_of = capacity_text_list.index('Grain Tank')
                if 'Grain Tank Capacity' in capacity_text_list:
                    index_of = capacity_text_list.index('Grain Tank Capacity')    
                text=capacity_ans_list[index_of]
                grain_tank_capacity.append(text) 
            else:    
                grain_tank_capacity.append('')                   

        transmission_gear.append('')

        print('clutch_text_list-', clutch_text_list) 

        if 'Type' in clutch_text_list:
            index_of = clutch_text_list.index('Type')
            text=clutch_ans_list[index_of]
            transmission_clutch_type.append(text)  
        else:
            transmission_clutch_type.append('') 

        print('tyre_text_list-', tyre_text_list)     

        if 'Front' in tyre_text_list:
            index_of = tyre_text_list.index('Front')
            text=tyre_ans_list[index_of]
            tyre_size_front.append(text)  
        else:
            if 'Front Tyre Sizes' in dimension_text_list:
                index_of = dimension_text_list.index('Front Tyre Sizes')
                text=dimension_ans_list[index_of]
                tyre_size_front.append(text)
            else: 
                tyre_size_front.append('')

        if 'Rear' in tyre_text_list  or 'Rear/Trolley' in tyre_text_list :
            if 'Rear' in tyre_text_list:
                index_of = tyre_text_list.index('Rear')
            if 'Rear/Trolley' in tyre_text_list:
                index_of = tyre_text_list.index('Rear/Trolley')   
            text=tyre_ans_list[index_of]
            tyre_size_rear.append(text)  
        else:
            if 'Rear Tyre Sizes'  in dimension_text_list:
                index_of = dimension_text_list.index('Rear Tyre Sizes')
                text=dimension_ans_list[index_of]
                tyre_size_rear.append(text)
            else:     
                tyre_size_rear.append('') 

        print('capacity_text_list-', capacity_text_list)           

        if 'Fuel Tank' in capacity_text_list or 'Fuel tank capacity Ltr.' in capacity_text_list or 'Fuel Tank Capacity' in capacity_text_list:
                if 'Fuel Tank' in capacity_text_list:
                    index_of = capacity_text_list.index('Fuel Tank')
                if 'Fuel tank capacity Ltr.' in capacity_text_list:
                    index_of = capacity_text_list.index('Fuel tank capacity Ltr.') 
                if 'Fuel Tank Capacity' in capacity_text_list:
                    index_of = capacity_text_list.index('Fuel Tank Capacity') 
                text=capacity_ans_list[index_of]
                fuel_tank_capacity.append(text) 
        else:    
            fuel_tank_capacity.append('')
        
        print('dimension_text_list-', dimension_text_list)

        if 'Weight' in dimension_text_list or 'Machine Weight' in dimension_text_list:
            if 'Weight' in dimension_text_list:
                index_of = dimension_text_list.index('Weight')
            if 'Machine Weight' in dimension_text_list: 
                index_of = dimension_text_list.index('Machine Weight')   
            text=dimension_ans_list[index_of]
            total_weight.append(text)  
        else:
            total_weight.append('')

        if 'Length (mm)' in dimension_text_list or 'Length' in dimension_text_list or 'Length (including cutterbar )' in dimension_text_list or 'Length (with front attachment )' in dimension_text_list:
            if 'Length (mm)' in dimension_text_list:
                index_of = dimension_text_list.index('Length (mm)')
            if 'Length' in dimension_text_list:
                index_of = dimension_text_list.index('Length') 
            if 'Length (including cutterbar )' in dimension_text_list:
                index_of = dimension_text_list.index('Length (including cutterbar )')
            if 'Length (with front attachment )' in dimension_text_list:
                index_of = dimension_text_list.index('Length (with front attachment )')
            text=dimension_ans_list[index_of]
            dimensions_length.append(text)  
        else:
            dimensions_length.append('')

        if 'Height' in dimension_text_list or 'Height (Working Position)' in dimension_text_list:
            if 'Height' in dimension_text_list:
                index_of = dimension_text_list.index('Height')
            if 'Height (Working Position)' in dimension_text_list:
                index_of = dimension_text_list.index('Height (Working Position)')    
            text=dimension_ans_list[index_of]
            dimensions_height.append(text)  
        else:
            dimensions_height.append('')

        if 'Width (mm)' in dimension_text_list or 'Width' in dimension_text_list:
            if 'Width (mm)' in dimension_text_list:
                index_of = dimension_text_list.index('Width (mm)')
            if  'Width' in dimension_text_list:
                index_of = dimension_text_list.index('Width')   
            text=dimension_ans_list[index_of]
            dimensions_width.append(text)  
        else:
            dimensions_width.append('')

        if 'Ground Clearance' in tyre_text_list or 'Ground Clearance' in dimension_text_list or 'Min. Ground Clearance' in dimension_text_list:
            print('ground here--')
            if 'Ground Clearance' in tyre_text_list: 
                index_of = tyre_text_list.index('Ground Clearance')
                text=tyre_ans_list[index_of]
            if 'Ground Clearance' in dimension_text_list:
                index_of = dimension_text_list.index('Ground Clearance')    
                text=dimension_ans_list[index_of]
            if 'Min. Ground Clearance' in dimension_text_list:
                index_of = dimension_text_list.index('Min. Ground Clearance')  
                text=dimension_ans_list[index_of]  
               
            if 'Min Ground Clearance' in dimension_text_list:
                index_of = dimension_text_list.index('Min Ground Clearance')  
                text=dimension_ans_list[index_of]      
            ground_clearance.append(text)  
        else:
            print('else---ground here--')
            if 'Ground clearance' in dimension_text_list:
                index_of = dimension_text_list.index('Ground clearance')
                text=dimension_ans_list[index_of]      
                ground_clearance.append(text)
            else:
                ground_clearance.append('')                 
        
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
            # close_modal= WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.tj-product-list-popup span.list_close")))
            # close_modal.click()
            # time.sleep(2)

            load_more = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "loadmorebtn")))
            
            buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')
            while buttonText == 'Load More Implements':
                buttonText = driver.find_element(By.ID, 'loadmorebtn').get_attribute('innerHTML')    
                if buttonText != 'Load More Implements':
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
        driver.execute_script("arguments[0].click();", new_harvester)
    except TimeoutException as e:
        print('TimeoutException for loop-///+++')

time.sleep(1) 
print('\n\ground_clearance.......-', ground_clearance)

data_dict = {
    'Brand':brand_list,
    'Model':model_list,
    'images_name':images_name,
    'implement_type':implement_type,
    'category_list':category_list,
    'implement_power':implement_power,
    'Crop':crop,
    'About':about_list,
    'Image_Type_Nmae':['product']
}
df=pd.DataFrame.from_dict(data_dict, orient="index")
df= df.transpose()

writer = pd.ExcelWriter('Kartar.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False,startrow=1, header=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({'bold':True, 'bottom':2, 'bg_color':'#F9DA04'})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()    
driver.close()
