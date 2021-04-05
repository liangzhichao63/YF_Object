import CSI_Video as video
import Object_Recongnition as OD
import Serial
if __name__ == "__main__":
    if(video.Init()==False):
        exit(0)
    # video.Show_Init()
    # video.Show()
    Serial.Set_Speed(10)

    while True:
        frame=video.Read()
        # print(frame.shape)
        target,target_size,frame,inRange_hsv=OD.Object_Recongnition(frame,'green')
        if(target_size!=0):
            target=OD.TF(target)

  

            Left_Right_Out =  target[0] * 50

            if Left_Right_Out>30:
                Left_Right_Out = 30
            if Left_Right_Out<-30:
                Left_Right_Out = -30
            
       

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
            else :
                print("up down")
                speed = abs(target[1]+0.4)*50
                if speed > 30 :
                    speed = 30
              
                Serial.Set_Speed(speed)

                if( target[1] > -0.41 ):
                    Serial.Run()
                elif ( target[1] < -0.39 ):
                    Serial.Back()
            
        
        # video.Show_img(inRange_hsv)
        # video.Show_img(frame)
