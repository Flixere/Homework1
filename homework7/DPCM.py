import cv2
import numpy as np
import math
from skimage import metrics

# 对随机一张灰度图片进行编码和解码，比较不同量化器(1-bit,2-bit,4-bit,8-bit)
# 的重建图像区别，并计算重建图像的PSNR和SSIM值

def dpcm(radio,h,w,y):
    img_re = np.zeros(w*h, np.uint16)  # 用来存储重建图像,因为中间计算可能超过255，先用16，后面转回8
    yprebuff = np.zeros(w*h, np.uint16)  # 预测
    for i in range(h):
        for j in range(w):
            if j == 0:
                ypre = y[j + i * w]-128  # 计算预测误差
                yprebuff[j + i * w] = (ypre+255)/radio  # 量化预测误差
                img_re[j + i * w] = (yprebuff[j + i * w]-255/radio)*radio+128  # 重建像素,j解码
                if img_re[j + i * w].all()>255:
                    img_re[j + i * w] = 255# 防止重建像素超过255
                yprebuff[j + i * w] = yprebuff[j + i * w]*radio/2
            else:
                ypre = y[j + i * w] - img_re[j + i * w - 1]  # 计算预测误差
                yprebuff[j + i * w] = (ypre+255) /radio  # 量化  # 量化器
                img_re[j + i * w] = (yprebuff[j + i * w]-255/radio)*radio+img_re[j + i * w - 1]  # 反量化
                yprebuff[j + i * w] = yprebuff[j + i * w] * radio / 2  # 预测器
                if img_re[j + i * w].all()>255:
                    img_re[j + i * w] = 255# 防止重建电平超过255
    img_re = img_re.astype(np.uint8) # 用来存储重建图像,后面转回uint8
    yprebuff = yprebuff.astype(np.uint8)  # 预测误差

    y = y.reshape((h,w))  # 转换向量形状回原来的y分量
    yprebuff = yprebuff.reshape((h,w))  # 预测的y分量
    img_re = img_re.reshape((h,w))  # 重建的y分量
    yvu_pre = cv2.merge((yprebuff, v, u))
    bgr_pre = cv2.cvtColor(yvu_pre, cv2.COLOR_YCrCb2BGR)  # 将y的预测误差转换为图片
    yvu_re = cv2.merge((img_re, v, u))
    bgr_re = cv2.cvtColor(yvu_re, cv2.COLOR_YCrCb2BGR)  # 将解码后的的y,u,v分量转换回原图

    return bgr_pre,bgr_re

# PSNR  PSNR越大，代表着图像质量越好
def psnr(img1, img2):
    img1 = np.float64(img1)
    img2 = np.float64(img2)
    mse = np.mean( (img1/255.0 - img2/255.0) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 1
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

# SSIM 



if __name__=='__main__':
    img = cv2.imread('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/cameraman.tif')
    h, w = img.shape[:2]  # 高，宽
    print(w,h)
    yvu = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, v, u = cv2.split(yvu)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/y.jpg',y)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/v.jpg',v)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/u.jpg',u)

    y=y.reshape(w*h)
    img_re = np.zeros(w*h, np.uint16)  # 用来存储重建图像,因为中间计算可能超过255，先用16，后面转回8
    yprebuff = np.zeros(w*h, np.uint16)  # 预测

# ---------------------------------------------------------8bit--------------------------------------------------
    radio=512/(1<<8)  
    print(radio)
    bgr_pre,bgr_re=dpcm(radio,h,w,y)

    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/bgr_pre_8bit.jpg',bgr_pre)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/bgr_re_8bit.jpg',bgr_re)

    # print('量化为8Bit时的PSNR值：',psnr(img,bgr_re))
    # print('量化为8Bit时的SSMI值：',ssmi(img,bgr_re))
    psnr = metrics.peak_signal_noise_ratio(img,bgr_re)
    print('量化为8Bit时的PSNR值：{}'.format(psnr))
    # 计算结构相似度SSIM
    ssim = metrics.structural_similarity(img,bgr_re, multichannel=True)
    print('量化为8Bit时的SSMI值：{}'.format(ssim))   



# ---------------------------------------------------------4bit--------------------------------------------------
    radio=512/(1<<4)  
    print(radio)
    bgr_pre,bgr_re=dpcm(radio,h,w,y)

    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/bgr_pre_4bit.jpg',bgr_pre)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/bgr_re_4bit.jpg',bgr_re)
    psnr = metrics.peak_signal_noise_ratio(img,bgr_re)
    print('量化为4Bit时的PSNR值：{}'.format(psnr))
    # 计算结构相似度SSIM
    ssim = metrics.structural_similarity(img,bgr_re, multichannel=True)
    print('量化为4Bit时的SSMI值：{}'.format(ssim))   


# ---------------------------------------------------------2bit--------------------------------------------------
    radio=512/(1<<2) 
    print(radio) 
    bgr_pre,bgr_re=dpcm(radio,h,w,y)

    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/bgr_pre_2bit.jpg',bgr_pre)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/bgr_re_2bit.jpg',bgr_re)
    psnr = metrics.peak_signal_noise_ratio(img,bgr_re)
    print('量化为2Bit时的PSNR值：{}'.format(psnr))
    # 计算结构相似度SSIM
    ssim = metrics.structural_similarity(img,bgr_re, multichannel=True)
    print('量化为2Bit时的SSMI值：{}'.format(ssim))   



# # ---------------------------------------------------------1bit--------------------------------------------------
    radio=512/(1<<1) 
    print(radio)  
    bgr_pre,bgr_re=dpcm(radio,h,w,y)

    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/bgr_pre_1bit.jpg',bgr_pre)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework7/result/bgr_re_1bit.jpg',bgr_re)
    psnr = metrics.peak_signal_noise_ratio(img,bgr_re)
    print('量化为1Bit时的PSNR值：{}'.format(psnr))
    # 计算结构相似度SSIM
    ssim = metrics.structural_similarity(img,bgr_re, multichannel=True)
    print('量化为1Bit时的SSMI值：{}'.format(ssim))   

