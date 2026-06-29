import cv2
import numpy as np
img=cv2.imread("image.jpg")
noise=np.random.randn(*img.shape)
speckle_noisy=img+img*0.2*noise
speckle_noisy=np.clip(speckle_noisy,0,255).astype(np.uint8)
mean_blur=cv2.blur(speckle_noisy,(5,5))
gaussian_blur=cv2.GaussianBlur(speckle_noisy,(5,5),0)
median_blur=cv2.medianBlur(speckle_noisy,5)
cv2.imshow("Original",img)
cv2.imshow("Speckle Noise",speckle_noisy)
cv2.imshow("Mean Blur",mean_blur)
cv2.imshow("Gaussian Blur",gaussian_blur)
cv2.imshow("Median Blur",median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()