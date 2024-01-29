from PIL import Image , ImageFont, ImageDraw

# Opening the image
with Image.open("img0-5050-d-1632220934.png") as img:
    # Get the width and height of the image 
    width, height = img.size
    
    # Preparing the text watermark (Change the color in the last parameter below)
    txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
    
    # Adding custom font
    # fnt = ImageFont.truetype("nordic.ttf", 60)
    
    # Creating image text
    d = ImageDraw.Draw(txt)
    
    # Get the width and height of the text
    _, _, w, h = d.textbbox((0,0), "Bharatagrimart")

    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.20

    font = ImageFont.truetype("BerkshireSwash-Regular.ttf", fontsize)
    while d.textbbox((0, 0), "Bharatagrimart", font=font)[2] < img_fraction * width:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("BerkshireSwash-Regular.ttf", fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype("BerkshireSwash-Regular.ttf", fontsize)

   
    print('width-',width, height, w,h) 
    if(width > 450 and height>180):
        print('if...')
        d.text(((width/2+180),(height-h-12)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
    elif(width==320 and height==180):
        print('elif...')
        d.text(((width/2+(w*1.40)),(height/2+(height/3)+h*1.3)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
    else:
        print('else//..')
        d.text(((width/2+120),(height-h-10)), "Bharatagrimart",font=font, fill=(0, 0, 0, 150))
       
    
    # Combine the image with text watermark
    out = Image.alpha_composite(img.convert("RGBA"), txt)
    
    # Save the image as png
    out.save("smallwh.png")

    # Show the image
    out.show()
    
    ## To convert into jpg, it should discard the Alpha channel
    # rgb_img = out.convert("RGB")
    # rgb_img.save("wmark_arya.jpg")
    # rgb_img.show()