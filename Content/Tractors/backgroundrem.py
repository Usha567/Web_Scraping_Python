from rembg import remove 
from PIL import Image 
import os
  
files = os.listdir('D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Mahindra_27_ARJUN NOVO 605 DI–i-4WD/')
for file in files:
    print('file-',file)
    im = Image.open(os.path.join('D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors/Mahindra_27_ARJUN NOVO 605 DI–i-4WD/', file))
    output_path = 'D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors/Mahindra_usha2/'+file 

    # Removing the background from the given Image 
    output = remove(im,  bgcolor=(0, 0, 0, 3)) 
    
    #Saving the image in the given path 
    output.save(output_path, quality=95) 


# from rembg import remove
# from PIL import Image # pillow
# import easygui
# import cv2

# print("Please Wait...")
# input_path = easygui.fileopenbox("Select your Image")
# Output_path = easygui.filesavebox("Where you want to save your Image")


# # input_path = 'input.png'
# # output_path = 'output.png'

# input = cv2.imread(input_path)
# output = remove(input, only_mask=True)
# cv2.imwrite(Output_path, output)


# my_img = Image.open(input_path)
# print("Please Wait...")
# rem = remove(my_img)

# save = rem.save(Output_path)
# print("Successfully Done, check your Folder")
















