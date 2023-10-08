from PIL import Image
from rembg import remove 

stencilIntensity = 4.5
menuon = True
def removeBackground(image_path):
    output_path = "output.png"
    with open(image_path, "rb") as input_file, open(output_path, "wb") as output_file:
        input_image = input_file.read()
        output_image = remove(input_image)
        output_file.write(output_image)
    input_path = user_dir

def redWhiteThreshold(image, threshold=128):
    width, height = image.size
    stencil_img = Image.new('RGB', (width, height), (255, 255, 255))
    
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            gray_value = sum(pixel) // stencilIntensity  
            if gray_value >= threshold:
                stencil_img.putpixel((x, y), (255, 0, 0)) 
    
    stencil_img.show()
def blackWhiteThreshold(image, threshold=128):
    width, height = image.size
    stencil_img = Image.new('RGB', (width, height), (255, 255, 255))
    
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            gray_value = sum(pixel) // stencilIntensity  # Calculate average grayscale value
            if gray_value >= threshold:
                stencil_img.putpixel((x, y), (0, 0, 0))  # Set pixel to black if above threshold
    
    stencil_img.show()

def homescreen():
    openaski =open("aski","r")
    file_contents =openaski.read()
    print(file_contents)
    user_inpustenintt = input("Adjust Stencil Intensity? y/n (default 4.5):")
    if user_inpustenintt == 'y':
        sentintinput = input("Enter new Stencil intensity:")
        stencilIntensity = float(sentintinput)
    else: stencilIntensity =4.5
    while menuon:
       
        user_dir = input("Put directory here: ")
        try:
            image = Image.open(user_dir)
        except IOError:
            print("Error opening the image. Make sure the directory is correct.")
            continue
        
        print("Choose Options:")
        print("1. Black and White threshold stencil")
        print("2. Red and Black threshold stencil")
        print("3. Remove background")
        user_input = input()
        if user_input == "1":
            blackWhiteThreshold(image)
        elif user_input =="2":
            redWhiteThreshold(image) 
        elif user_input =="3":
            removeBackground(image)
        else:
            print("Invalid choice!")
        menuon = True
        
homescreen()