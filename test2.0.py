import cv2
import numpy
import os
def find(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图
    blur = cv2.GaussianBlur(gray, (3, 3),0)  # 用高斯滤波处理原图像降噪
    canny = cv2.Canny(blur, 20, 30)  # 20是最小阈值,50是最大阈值 边缘检测
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    dilation = cv2.dilate(canny,kernel,iterations = 1)#膨胀一下，来连接边缘
    contours, hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#找边框
#cv2.drawContours(img,contours,-1,(0,255,0),10)  
    p1=()
    p2=()
    p3=()
    p4=()
    pp=[p1,p2,p3,p4]
#筛选边框

    for t in range(len(contours)):
        hull = cv2.convexHull(contours[t])
        epsilon = 0.1*cv2.arcLength(hull, True)#0.36081735求边框周长，epsilon 是精度
  
        point=cv2.approxPolyDP(hull, epsilon, True) 
        if (len(point) == 4 and epsilon>100 and epsilon<600 ):#and (int(point[0][0][0:1])>700) and (int(point[0][0][1:2])>1000)这里找身份证特征，因为背景简单直接判断边框周长就行
	        for i in range(len(point)-1):
		    #cv2.line(img, tuple(point[i][0]), tuple(point[i+1][0]), (0,255,0), 8)
		        pp[i]=tuple(point[i][0])
		        if(i==(len(point)-2)):
			        pp[i+1]=tuple(point[i+1][0])
		    
            
			
#扩展边界
    extends=150
    ppx1=pp[0][0]+extends
    ppy1=pp[0][1]+extends
    temp=(ppx1,ppy1)
    pp[0]=temp

    ppx2=pp[1][0]-extends
    ppy2=pp[1][1]+extends
    temp=(ppx2,ppy2)
    pp[1]=temp

    ppx3=pp[2][0]-extends
    ppy3=pp[2][1]-extends
    temp=(ppx3,ppy3)
    pp[2]=temp

    ppx4=pp[3][0]+extends
    ppy4=pp[3][1]-extends
    temp=(ppx4,ppy4)
    pp[3]=temp
    #cv2.rectangle(img, pp[0], pp[2], (0,255,0),10)#框出身份证
    imga=img[ppy4:ppy1,ppx3:ppx4]
    return imga
#读取当前文件下的两张图片
path='./'
def get_img_file(file_name):
    imagelist = []
    for parent, dirnames, filenames in os.walk(trainpath):
        for filename in filenames:
            if filename.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                imagelist.append(os.path.join(parent, filename))
        return imagelist
   
arr=get_img_file(path)
#创建图像
I=numpy.zeros((3501,2500),dtype=numpy.uint8)
I[:]=255
I=cv2.cvtColor(I,cv2.COLOR_GRAY2BGR)
for z in range(len(arr)):
    img = cv2.imread(arr[z])
    y, x = img.shape[0:2]
    imga=find(img)
    ya, xa = imga.shape[0:2]
#粘贴
    if (z==0):
        I[225:(225+ya),665:(665+xa)]=imga
    else:
	    I[(675+ya):(675+ya*2),665:(665+xa)]=imga
    #IX, IY = I.shape[0:2]
#保存图像
cv2.imwrite("./ok.jpg", I)

#print(point)打印图像
#cv2.rectangle(canvas, (10, 10), (60, 60), green) #12
#img_test1 = cv2.resize(I, (int(x / 5), int(y / 5)))
#cv2.imshow('dilation', img_test1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
