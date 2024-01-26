
# Importing Image class from PIL module
from PIL import Image
import os
 
# # Opens a image in RGB mode
# # im = Image.open(r"D:\PYTHON_WEB_SCRAPING\GithubCloned\Web_Scraping_Python\Content\Tractors\
# # Ace534_DI-305 NG\img0-di-305-ng-1632224204.png") 

# files = os.listdir('D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Ace534_DI-305 NG/')
# for file in files:
#     print('file-',file)
#     im = Image.open(os.path.join('D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Ace534_DI-305 NG/', file))
 
#     # Setting the points for cropped image
#     left = 55
#     top = 5
#     right = 550
#     bottom = 270
    
#     # Cropped image of above dimension
#     # (It will not change original image)
#     im1 = im.crop((left, top, right, bottom))
    
#     # Shows the image in image viewer
#     im1.show()


from rembg import remove 
# from PIL import Image 
  
# Store path of the image in the variable input_path 




# input_path =  'E:\C programs\ 
#                Remove BackGround\gfgimage.png' 
  

files = os.listdir('D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Ace534_DI-305 NG/')
for file in files:
    print('file-',file)
    im = Image.open(os.path.join('D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Ace534_DI-305 NG/', file))
    # Store path of the output image in the variable output_path 
    output_path = 'D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Ace_usha/'+file 

    
    # # Processing the image 
    # input = Image.open(input_path) 
    
    # Removing the background from the given Image 
    output = remove(im) 
    
    #Saving the image in the given path 
    output.save(output_path) 