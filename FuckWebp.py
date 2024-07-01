import os
from PIL import Image

#get current folder
script_dir = os.path.dirname(os.path.abspath(__file__))

# check all file
for filename in os.listdir(script_dir):
    if filename.endswith(".webp"):
        # open webp
        webp_image = Image.open(os.path.join(script_dir, filename))
        
        #convert
        png_image = webp_image.convert("RGBA")
        
        # save image with .png
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_image.save(os.path.join(script_dir, png_filename), "PNG")
        
        # fuck webp
        os.remove(os.path.join(script_dir, filename))
        
        print(f"Converted {filename} to {png_filename} and deleted the original file")

print("Conversion and deletion completed.")
