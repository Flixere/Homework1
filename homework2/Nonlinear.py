# 对数变换

import cv2
import imutils
import numpy as np
import math

image = cv2.imread('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/girl.bmp')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

log_img = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        log_img[i][j] = math.log(1 + image[i][j])
cv2.normalize(log_img, log_img, 0, 255, cv2.NORM_MINMAX)
log_img = cv2.convertScaleAbs(log_img)

cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Nonlinear/orginal.bmp",image)
cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Nonlinear/log_img.bmp",log_img)


# 幂变换
#幂律变换 φ>1
gamma_img1 = np.zeros((image.shape[0], image.shape[1]), dtype=np.float32)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        gamma_img1[i][j] = math.pow(image[i][j], 5)
 
cv2.normalize(gamma_img1, gamma_img1, 0, 255, cv2.NORM_MINMAX)
gamma_img1 = cv2.convertScaleAbs(gamma_img1)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Nonlinear/gamma_img1.bmp',gamma_img1)

#幂律变换，φ<1
gamma_img2 = np.zeros((image.shape[0], image.shape[1]), dtype=np.float32)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        gamma_img2[i][j] = math.pow(image[i][j], 0.4)

cv2.normalize(gamma_img2, gamma_img2, 0, 255, cv2.NORM_MINMAX)
gamma_img2 = cv2.convertScaleAbs(gamma_img2)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Nonlinear/gamma_img2.bmp',gamma_img2)



