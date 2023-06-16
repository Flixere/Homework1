# 第三题：图像平移、镜像和旋转，以及三种几何变换的复合

import cv2
import numpy as np

# 1. 平移
 
# 读取图片
img = cv2.imread("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/Lena.bmp", cv2.IMREAD_UNCHANGED)
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

 
# 图像平移 下、上、右、左平移
image1 = image.copy()

M = np.float32([[1, 0, 0], [0, 1, 100]])
img1 = cv2.warpAffine(image1, M, (image.shape[1], image.shape[0]))
 
M = np.float32([[1, 0, 0], [0, 1, -100]])
img2 = cv2.warpAffine(image1, M, (image.shape[1], image.shape[0]))
 
M = np.float32([[1, 0, 100], [0, 1, 0]])
img3 = cv2.warpAffine(image1, M, (image.shape[1], image.shape[0]))
 
M = np.float32([[1, 0, -100], [0, 1, 0]])
img4 = cv2.warpAffine(image1, M, (image.shape[1], image.shape[0]))
 
# 显示结果
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/orginal.jpg',image)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/down.jpg',img1)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/up.jpg',img2)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/right.jpg',img3)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/left.jpg',img4)

# 2. 镜像
image2 = image.copy()
img5 = cv2.flip(image2,0) #以X轴为对称轴翻转 垂直翻转
img6 = cv2.flip(image2,1)  #以Y轴为对称轴翻转 水平翻转
img7 = cv2.flip(image2,-1) #在X轴、Y轴方向同时翻转 水平垂直翻转

cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/x.jpg',img5)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/y.jpg',img6)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/x&y.jpg',img7)

# 3.旋转
# M = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1)
# 其中，参数分别为：旋转中心、旋转度数、scale
image3 = image.copy()
rows, cols, channel = image.shape

# 绕图像的中心旋转
# 参数：旋转中心 旋转度数 scale
# 以长宽中心点，逆时针旋转30度
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 1)
# 参数：原始图像 旋转参数 元素图像宽高
rotated1 = cv2.warpAffine(image3, M, (cols, rows))

# 逆时针旋转60度
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 60, 1)
rotated2 = cv2.warpAffine(image3, M, (cols, rows))

# 逆时针旋转90度
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
rotated3 = cv2.warpAffine(image3, M, (cols, rows))

cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/30.jpg',rotated1)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/60.jpg',rotated2)
cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework3/result/90.jpg',rotated3)


# 4.三种几何变换的组合
