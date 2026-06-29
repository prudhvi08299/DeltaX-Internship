import cv2
import numpy as np
img=cv2.imread("image.jpg")
# --------------------
# Add Gaussian Noise
# --------------------
noise=np.random.normal(0,25,img.shape)
gaussian_noisy=img+noise
gaussian_noisy=np.clip(gaussian_noisy,0,255).astype(np.uint8)
# --------------------
# Add Salt & Pepper Noise
# --------------------
sp_noisy=np.copy(img)
prob=0.02
num_salt=np.ceil(prob*img.shape[0]*img.shape[1]*0.5)
coords=[np.random.randint(0,i-1,int(num_salt)) for i in img.shape[:2]]
sp_noisy[coords[0],coords[1]]=255
num_pepper=np.ceil(prob*img.shape[0]*img.shape[1]*0.5)
coords=[np.random.randint(0,i-1,int(num_pepper)) for i in img.shape[:2]]
sp_noisy[coords[0],coords[1]]=0
# --------------------
# Remove Gaussian Noise
# --------------------
mean_gaussian=cv2.blur(gaussian_noisy,(5,5))
gaussian_blur=cv2.GaussianBlur(gaussian_noisy,(5,5),0)
median_gaussian=cv2.medianBlur(gaussian_noisy,5)
# --------------------
# Remove Salt & Pepper Noise
# --------------------
mean_sp=cv2.blur(sp_noisy,(5,5))
gaussian_sp=cv2.GaussianBlur(sp_noisy,(5,5),0)
median_sp=cv2.medianBlur(sp_noisy,5)
# --------------------
# Display Results
# --------------------
cv2.imshow("Original Image",img)
cv2.imshow("Gaussian Noise",gaussian_noisy)
cv2.imshow("Mean Filter on Gaussian Noise",mean_gaussian)
cv2.imshow("Gaussian Filter on Gaussian Noise",gaussian_blur)
cv2.imshow("Median Filter on Gaussian Noise",median_gaussian)
cv2.imshow("Salt and Pepper Noise",sp_noisy)
cv2.imshow("Mean Filter on Salt & Pepper",mean_sp)
cv2.imshow("Gaussian Filter on Salt & Pepper",gaussian_sp)
cv2.imshow("Median Filter on Salt & Pepper",median_sp)
cv2.waitKey(0)
cv2.destroyAllWindows()