import CSI_Video as video
import Object_Recongnition as OD
import Serial
import time
import numpy as np

def Robot_arm_Rest():
    Serial.Set_Servo_A(80)
    Serial.Set_Servo_B(150)
    Serial.Set_Servo_C(150)
    Serial.Set_Servo_D(150)

def Robot_arm_GO():
    Serial.Set_Servo_A(80)
    Serial.Set_Servo_B(220)
    Serial.Set_Servo_C(100)
    Serial.Set_Servo_D(150)
def Robot_arm_catch():
    Serial.Set_Servo_A(150)
    Serial.Set_Servo_B(220)
    Serial.Set_Servo_C(100)
    Serial.Set_Servo_D(150)
def Robot_arm_UP():
    Serial.Set_Servo_A(150)
    Serial.Set_Servo_B(150)
    Serial.Set_Servo_C(150)
    Serial.Set_Servo_D(150)

if __name__ == "__main__":
    if(video.Init()==False):
        exit(0)
    # video.Show_Init()
    # video.Show()
   
    Serial.Set_Speed(0)
    Robot_arm_Rest()
    Serial.Link()
    Ready = 0
    last_speed = 0
    while True:
        frame=video.Read()
        frame=video.rotate_bound(frame,180)
        Serial.Link()
        # print(frame.shape)
        target,target_size,frame,inRange_hsv=OD.Object_Recongnition(frame,'green')
        # video.Show_img(frame)        #显示RGB图像
        # continue
        if(target_size!=0):
            target=OD.TF(target)
            Left_Right_Out =  target[0] * 50

            if Left_Right_Out>30:
                Left_Right_Out = 30
            if Left_Right_Out<-30:
                Left_Right_Out = -30
            
            #左右对准
            if(Left_Right_Out>5):
                if(abs(Left_Right_Out)<15):
                    Left_Right_Out = 15
                Serial.Set_Speed(abs(Left_Right_Out))
                Serial.Across_Right()
                print("R")
            elif (Left_Right_Out<-5) :
                if(abs(Left_Right_Out)<15):
                    Left_Right_Out = 15
                Serial.Set_Speed(abs(Left_Right_Out))
                Serial.Across_Left()
                print("L")
            else :#前后对准
                speed = abs(target[1]+0.45)*50

                print("speed",speed)
                if speed > 11 :
                    speed = 11
                # elif speed >0 :
                #     if speed<6:
                #         speed = 6
                    
                print(target[1])
              
                speed = last_speed * 0.8 + speed * 0.2
                Serial.Set_Speed(np.int0(speed))
                last_speed = speed

                if( target[1] > -0.38 ):#0.41
                    Serial.Run()
                    Ready = 0
                    print("UP")
                elif ( target[1] < -0.45 ):#0.39
                    Serial.Back()
                    Ready = 0
                    print("BACK")
                else :
                    Ready = Ready + 1
                    Serial.Set_Speed(0)
                    Serial.Run()
                    if(Ready>2):
                        # for num in range(0,30):
                        #     Serial.Set_Speed(8)
                        #     Serial.Run()
                        #     time.sleep(0.01)
                        time.sleep(1)
                        while True:
                            print("OK\r\n")
                            Serial.Set_Speed(0)
                            Robot_arm_GO()
                            Serial.Link()
                            time.sleep(1)
                            Robot_arm_catch()
                            Serial.Link()
                            time.sleep(1)
                            Robot_arm_UP()
                            Serial.Link()
                            exit(0)
            
        
        # video.Show_img(inRange_hsv) #显示二值化图像
        # video.Show_img(frame)        #显示RGB图像
