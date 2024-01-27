from PIL import Image , ImageFont, ImageDraw

# Opening the image
with Image.open("D:/PYTHON_WEB_SCRAPING/GithubCloned/Web_Scraping_Python/Content/Tractors/Tractors_Images\Mahindra__1_ARJUN NOVO 605 DI–i-4WD/img0-mahindra-arjun-novo-605-dii-4wd-1698917936.png") as img:
    # Get the width and height of the image 
    width, height = img.size
    
    # Preparing the text watermark (Change the color in the last parameter below)
    txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
    
    # Adding custom font
    # fnt = ImageFont.truetype("nordic.ttf", 60)
    
    # Creating image text
    d = ImageDraw.Draw(txt)
    
    # Get the width and height of the text
    _, _, w, h = d.textbbox((0, 0), "Bharat Agrimart")

    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.25

    font = ImageFont.truetype("arial.ttf", fontsize)
    while d.textbbox((0, 0), "Bharat Agrimart", font=font)[2] < img_fraction * width:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("arial.ttf", fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype("arialbi.ttf", fontsize)

   
    d.text(((width/2),(height-h-290)), "Bharat Agrimart",font=font, fill=(0, 0, 0, 255))
    
    # Combine the image with text watermark
    out = Image.alpha_composite(img.convert("RGBA"), txt)
    
    # Save the image as png
    out.save("ushaimg.png")

    # Show the image
    out.show()
    
    ## To convert into jpg, it should discard the Alpha channel
    # rgb_img = out.convert("RGB")
    # rgb_img.save("wmark_arya.jpg")
    # rgb_img.show()