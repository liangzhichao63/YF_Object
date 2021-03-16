import cv2
import numpy as np

ball_color = 'blue'

color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
              }

path=r'test1.png'
frame=cv2.imread(path)
#cv2.imshow('pirate',pirate)
# air=()

if frame is not None:
    gs_frame = cv2.GaussianBlur(frame, (5, 5), 0)                     # 高斯模糊
    hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
    erode_hsv = cv2.erode(hsv, None, iterations=2)                   # 腐蚀 粗的变细
    inRange_hsv = cv2.inRange(erode_hsv, color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])#除去所选颜色的其它颜色,二值化图像
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] #
    c = max(cnts, key=cv2.contourArea)
    print(type(c))
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)

    print(box)

    Center_x=(box[0][0]+box[2][0])/2
    Center_y=(box[0][1]+box[2][1])/2
    air=(np.int0(Center_x),np.int0(Center_y))
   
    
    print(air)
    
    # print(air)
    cv2.drawContours(frame, [np.int0(box)], -1, (0, 255, 255), 2)#画框

    cv2.circle(frame, air, 2, (0, 0, 255), 0)#画中点


# cv2.imshow('camera', frame)

cv2.imwrite("./gs_frame.jpg", gs_frame)
cv2.imwrite("./hsv.jpg", hsv)
cv2.imwrite("./erode_hsv.jpg", erode_hsv)
cv2.imwrite("./inRange_hsv.jpg", inRange_hsv)
cv2.imwrite("./out.jpg", frame)
