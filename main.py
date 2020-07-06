from PIL import Image

image = Image.open(r"C:\Users\Dinesh I\Desktop\img to pdf\img.JPG") # Copy img path and paste
 
img = image.convert("RGB")

img.save(r"C:\Users\Dinesh I\Desktop\img to pdf\output.pdf") # Copy output pdf path and paste 
