import CSI_Video as video
import Object_Recongnition as OD
import Serial
if __name__ == "__main__":
    if(video.Init()==False):
        exit(0)
    # video.Show_Init()
    # video.Show()
    while True:
        frame=video.Read()
        # print(frame.shape)
        target,target_size,frame=OD.Object_Recongnition(frame,'blue')
        if(target_size!=0):
            target=OD.TF(target)
            print(target[0])

            Serial.Set_Speed(abs(target[0])*50)
            if(target[0]<0):
                Serial.Across_Right()
            else if(target[0]>0):
                Serial.Across_Left()
            


        video.Show_img(frame)
    