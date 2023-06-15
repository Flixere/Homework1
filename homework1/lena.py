import cv2
import numpy as np

 
def ResizeImage(Img , scale):
    
    
    width,height=Img.shape[:2]
    width = int(width* scale)
    height = int(height*scale)
    out = cv2.resize(Img,(width,height)) #默认采取双线性插值

    return out

def change_gry(Img,level):
    width,height=Img.shape[:2]
    out=np.zeros((width,height))
    for i in range(width):
        for j in range(height):
            out[i][j]=np.uint8(Img[i][j]/level)
            # print(Img[i][j])
        
    return out

 
 
if __name__ == "__main__":
    img = cv2.imread('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework1/Lena.jpg', 1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    change_gry(img,2)
# 1.生成Lena图片不同空间分辨率
    cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework1/result/original.jpg",img)
    out1=ResizeImage(img,2)
    cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework1/result/scale_2.jpg",out1)
    out2=ResizeImage(img,0.5)
    cv2.imwrite("C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework1/result/scale_0.5.jpg",out2)

# 2.不同灰度分辨率
# 改变灰度值以实现灰度级的不同
    out3=change_gry(img,2)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework1/result/level_128.jpg',out3)
    out4=change_gry(img,4)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework1/result/level_64.jpg',out4)
    out5=change_gry(img,8)
    cv2.imwrite('C:/Users/BLACKSPACE/Desktop/Image_processing-main/homework1/result/level_32.jpg',out4)

# 3.总结
# 3.1 通过cv中resize函数调整图像宽高像素点个数，改变图像空间分辨率，观察结果可知，空间分辨率越高，放大图像细越清晰。
# 3.2 利用线性运算改变灰度级，观察3种不同灰度级，发现灰度级越大，图像越亮。
