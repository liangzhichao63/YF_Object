import cv2
import numpy as np
import time
def gstreamer_pipeline(
    capture_width=320,
    capture_height=180,
    display_width=320,
    display_height=180,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
def Init():
    if not cap.isOpened():
        return False
    return True
    
def Read():
    flag, img = cap.read()
    return img

 
def Show():
    while True:
        img = Read()
        cv2.imshow("CSI Camera", img)
        kk = cv2.waitKey(1)
 
        # do other things
 
        if kk == ord('q'):  # 按下 q 键，退出
            break
 
    cap.release()
    cv2.destroyAllWindows()
# def Show_Init():
def Show_img(img):
    # cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
    cv2.imshow("img", img)
    kk = cv2.waitKey(1)