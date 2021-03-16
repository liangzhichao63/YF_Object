import cv2
import numpy as np


color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
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
        return 0,frame
    elif(len(cnts)>1):
        c = max(cnts, key=cv2.contourArea)
    else:
        c = max(cnts)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)

    # print(box)

    Center_x=(box[0][0]+box[2][0])/2
    Center_y=(box[0][1]+box[2][1])/2
    air=(np.int0(Center_x),np.int0(Center_y))
   
    
    print(air)
    
    cv2.drawContours(frame, [np.int0(box)], -1, (0, 255, 255), 2)#画框
    cv2.circle(frame, air, 2, (0, 0, 255), 0)#画中点
    #返回目标坐标
    return air,frame

