import CSI_Video as video
import Object_Recongnition as OD
import Serial
import time

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


if __name__ == "__main__":
    if(video.Init()==False):
        exit(0)
    # video.Show_Init()
    # video.Show()

   
    Serial.Set_Speed(0)
    Robot_arm_Rest()

    while True:
        frame=video.Read()
        Serial.Link()
        # print(frame.shape)
        target,target_size,frame,inRange_hsv=OD.Object_Recongnition(frame,'green')
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
            elif (Left_Right_Out<-5) :
                if(abs(Left_Right_Out)<15):
                    Left_Right_Out = 15
                Serial.Set_Speed(abs(Left_Right_Out))
                Serial.Across_Left()
            else :#前后对准
                print("up down")
                speed = abs(target[1]+0.4)*50
                if speed > 30 :
                    speed = 30

                Serial.Set_Speed(speed)
                if( target[1] > -0.41 ):
                    Serial.Run()
                elif ( target[1] < -0.39 ):
                    Serial.Back()
                else :
                    while True:
                        Serial.Set_Speed(0)
                        Serial.Run()
                        Robot_arm_GO()
                        time.sleep(0.1)
            
        
        video.Show_img(inRange_hsv)
        video.Show_img(frame)
