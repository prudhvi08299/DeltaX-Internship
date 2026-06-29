import numpy as np
from PIL import Image
# Create a grayscale image (200x200)
gray=np.zeros((200,200),dtype=np.uint8)
gray[50:150,50:150]=180
gray[75:125,75:125]=255
gray_img=Image.fromarray(gray)
gray_img.save("grayscale_image.png")
# Create an RGB image (200x200)
rgb=np.zeros((200,200,3),dtype=np.uint8)
rgb[:100,:100]=[255,0,0]
rgb[:100,100:]=[0,255,0]
rgb[100:,:100]=[0,0,255]
rgb[100:,100:]=[255,255,0]
rgb_img=Image.fromarray(rgb)
rgb_img.save("rgb_image.png")
# Indexing
print("Grayscale pixel at (75,75):",gray[75,75])
print("RGB pixel at (50,50):",rgb[50,50])
center_gray=gray[50:150,50:150]
top_half_rgb=rgb[:100,:,:]
print("Center grayscale shape:",center_gray.shape)
print("Top half RGB shape:",top_half_rgb.shape)
bright_gray=np.clip(gray+50,0,255).astype(np.uint8)
bright_img=Image.fromarray(bright_gray)
bright_img.save("bright_grayscale.png")
dark_rgb=(rgb*0.5).astype(np.uint8)
dark_img=Image.fromarray(dark_rgb)
dark_img.save("dark_rgb.png")
print("Images saved successfully.")