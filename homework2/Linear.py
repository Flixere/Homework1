import cv2
import random
import numpy as np

# 1.线性运算
#彩色图像每个像素值是[x,y,z], 灰度图像每个像素值便是一个np.uint8
image = cv2.imread('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/girl.bmp')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# y=a*x+b
# a<0 and b=0: 图像的亮区域变暗，暗区域变亮
a, b = -0.5, 0
new_img1 = np.ones((gray_img.shape[0],gray_img.shape[1]), dtype=np.uint8)
for i in range(new_img1.shape[0]):
    for j in range(new_img1.shape[1]):
        new_img1[i][j] = gray_img[i][j]*a + b

cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Linear_arithmeticimg/new_img1.bmp",new_img1)


# a>1: 增强图像的对比度,图像看起来更加清晰
a, b = 1.5, 20
new_img2 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
for i in range(new_img2.shape[0]):
    for j in range(new_img2.shape[1]):
        if gray_img[i][j]*a + b > 255:
            new_img2[i][j] = 255
        else:
            new_img2[i][j] = gray_img[i][j]*a + b

cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Linear_arithmeticimg/new_img2.bmp",new_img2)

# #0<a<1: 减小了图像的对比度, 图像看起来变暗
a, b = 0.5, 0
new_img3 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
for i in range(new_img3.shape[0]):
    for j in range(new_img3.shape[1]):
        new_img3[i][j] = gray_img[i][j]*a + b

cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Linear_arithmeticimg/new_img3.bmp",new_img3)

# #a=1且b≠0, 图像整体的灰度值上移或者下移, 也就是图像整体变亮或者变暗, 不会改变图像的对比度
a, b = 1, -50
new_img4 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
for i in range(new_img4.shape[0]):
    for j in range(new_img4.shape[1]):
        pix = gray_img[i][j]*a + b
        if pix > 255:
            new_img4[i][j] = 255
        elif pix < 0:
            new_img4[i][j] = 0
        else:
            new_img4[i][j] = pix

cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Linear_arithmeticimg/new_img4.bmp",new_img4)

# #a=-1, b=255, 图像翻转
new_img5 = 255 - gray_img
cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework2/result/Linear_arithmeticimg/new_img5.bmp",new_img5)

