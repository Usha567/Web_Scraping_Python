import rembg
from rembg import remove 
from rembg import bg 
from PIL import Image 
  
files = os.listdir('D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Ace534_DI-305 NG/')
for file in files:
    print('file-',file)
    im = Image.open(os.path.join('D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Ace534_DI-305 NG/', file))
    output_path = 'D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors\Ace_usha/'+file 

    # Removing the background from the given Image 
    output = bg.remove(im) 
    
    #Saving the image in the given path 
    output.save(output_path) 