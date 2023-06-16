import cv2
import numpy as np
import matplotlib.pyplot as plt

# 使用大津法进行图像分割
# 迭代阈值
# 比较两者的性能差别

# 大津法
def otsu(img,Sigma):
    for t in range(0, 256):
        bg  = img[img <= t]
        obj = img[img > t]
    
        p0 = bg.size / img.size
        p1 = obj.size / img.size
    
        m0 = 0 if bg.size == 0 else bg.mean()
        m1 = 0 if obj.size == 0 else obj.mean()
    
        sigma = p0 * p1 * (m0 - m1)**2
    
        if sigma > Sigma:
            Sigma = sigma
            T = t
    T = int(T)
    return T

# 自适应阈值法
def iterate(img,thre,T0):
    mask1  = img <= T0
    mask2 = img > T0
    T1 = np.sum(mask1 * img) / np.sum(mask1)
    T2 = np.sum(mask2 * img) / np.sum(mask2)
    T = (T1 + T2) / 2

    while(abs(T-T0)<thre):
        mask1  = img[img <= T]
        mask2 = img[img > T]
        T1 = np.sum(mask1 * img) / np.sum(mask1)
        T2 = np.sum(mask2 * img) / np.sum(mask2)
        T = int((T1 + T2) / 2)
        # 终止条件
        
    return T

# 获取阈值机进行图像分割
def segmenting(img,T):
    w,h=img.shape[:2]
    # print(w,h)
    for i in range(w):
        for j in range(h):
            if(img[i][j]<T):
                img[i][j]=0
            else:
                img[i][j]=255
    return img

if __name__=='__main__':
    img = cv2.imread('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/house.tif')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/original.jpg',img)
    T1=otsu(img,-1)
    print(f"ostu_Best threshold = {T1}")
    T2=iterate(img,1,20)
    print(f"iterate_Best threshold = {T2}")
    seg_img1=segmenting(img,T1)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/seg_otsu_house.jpg',seg_img1)
    seg_img2=segmenting(img,T2)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/seg_iter_house.jpg',seg_img2)

    img1 = cv2.imread('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/cameraman.tif')
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/original.jpg',img1)
    T1=otsu(img1,-1)
    print(f"ostu_Best threshold = {T1}")
    T2=iterate(img1,1,20)
    print(f"iterate_Best threshold = {T2}")
    seg_img1=segmenting(img1,T1)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/seg_otsu_cameraman.jpg',seg_img1)
    seg_img2=segmenting(img1,T2)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/seg_iter_cameraman.jpg',seg_img2)

# 多目标图片
    img2 = cv2.imread('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/peppers_gray.tif')
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/original.jpg',img2)
    T1=otsu(img2,-1)
    print(f"ostu_Best threshold = {T1}")
    T2=iterate(img2,1,20)
    print(f"iterate_Best threshold = {T2}")
    seg_img1=segmenting(img2,T1)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/seg_otsu_peppers.jpg',seg_img1)
    seg_img2=segmenting(img2,T2)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework8/result/seg_iter_peppers.jpg',seg_img2)

# 总结
# 1. 大津法和自适应阈值法适合单目标分类，在背景和前景区别较大时，分割结果较好
# 2. 对于前景背景区别较大时，大津法和自适应阈值法效果差不多
