import cv2
import numpy as np


color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 40, 35]), 'Upper': np.array([90, 255, 255])},
              }
#Target_color: 目标颜色 ('red'/'blue'/'green')
#freame 图片

def Object_Recongnition(frame , Target_color):
    gs_frame = cv2.GaussianBlur(frame, (5, 5), 0)                     # 高斯模糊
    hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
    erode_hsv = cv2.erode(hsv, None, iterations=2)                   # 腐蚀 粗的变细
    inRange_hsv = cv2.inRange(erode_hsv, color_dist[Target_color]['Lower'], color_dist[Target_color]['Upper'])#除去所选颜色的其它颜色,二值化图像
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] #轮廓检测
    c=None
    if(len(cnts)==0):
        return 0,0,frame,inRange_hsv
    elif(len(cnts)>1):
        c = max(cnts, key=cv2.contourArea)
    else:
        c = max(cnts)
    
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)

    #图片宽高
    sp = frame.shape
    H=sp[0]
    W=sp[1]
    
    #相对面积
    box_size=( (box[0][0]-box[2][0])*(box[0][1]-box[2][1]))/ (H*W)
    box_size=abs(box_size)
    if(box_size<0.001):
        return 0,0,frame,inRange_hsv
    #相对中心点
    Center_x=(box[0][0]+box[2][0])/2 
    Center_y=(box[0][1]+box[2][1])/2

    Center_x=(box[0][0]+box[1][0])/2 
    Center_y=(box[0][1]+box[1][1])/2
    Center_y=box[0][1]


    air=(np.int0(Center_x),np.int0(Center_y))
   
    
    # print(air)
    
    cv2.drawContours(frame, [np.int0(box)], -1, (0, 255, 255), 2)#画框
    # cv2.circle(frame, air, 2, (0, 0, 255), 0)#画中点

    X=air[0]
    Y=air[1]
	
    air=((Center_x/W),(Center_y/H))

    #返回目标坐标
    return air,box_size,frame,inRange_hsv



#坐标系,图片中间的点作为坐标原点
def TF(Target):

    X=Target[0]
    Y=Target[1]
    if Y>0.5:
        Y=Y-0.5
        Y=-2*Y
    else :
        Y=0.5-Y
        Y=Y*2
    
    if X>0.5:
        X=X-0.5
        X=2*X
    else :
        X=0.5-X
        X=-2*X
    # print(X,Y)
    return (X,Y)