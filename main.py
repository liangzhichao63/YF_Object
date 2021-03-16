import CSI_Video as video
import Object_Recongnition as OD
if __name__ == "__main__":
    if(video.Init()==False):
        exit(0)
    # video.Show_Init()
    # video.Show()
    while True:
        frame=video.Read()
        target,frame=OD.Object_Recongnition(frame,'blue')
        video.Show_img(frame)

    