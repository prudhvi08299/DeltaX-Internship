import cv2
import numpy as np
img=cv2.imread("image.jpg")
noise=np.random.randn(*img.shape)
speckle_noisy=img+img*0.2*noise
speckle_noisy=np.clip(speckle_noisy,0,255).astype(np.uint8)
cv2.imshow("Original Image",img)
cv2.imshow("Speckle Noise",speckle_noisy)
cv2.waitKey(0)
cv2.destroyAllWindows()