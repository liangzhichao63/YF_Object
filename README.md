## 运行示例程序
    可以直接远程连接上jetson nano在命令行中运行启动示例程序
    sudo python3 main.py

## 小车控制接口函数说明
    Serial.py文件中提供了控制小车的接口函数    
    控制小车移动一般分两步来完成，先设定小车的速度，在设置小车移动的方向
    
    设置小车速度函数，输入参数范围（0-200）
    Set_Speed()
    
    设置小车方向函数：
    Run()           #前进
    Back()          #后退
    Left()          #左转
    Right()         #右转
    Across_Left()   #向左平移
    Across_Right()  #向右平移

    例：
    import Serial
    while True:
        Serial.Set_Speed(100) #设定速度100
        Serial.Run() #前进

## 小车舵机控制接口说明

    小车一共有4个舵机A,B,C,D
    分别用以下4个函数控制舵机角度
    
    #舵机输入范围50-250

    #爪子舵机 150 闭合 150-50打开
    def Set_Servo_A(Servo):
    #右舵机 
    def Set_Servo_B(Servo):
    #左舵机
    def Set_Servo_C(Servo):
    #底盘旋转舵机
    def Set_Servo_D(Servo):

    在控制舵机后需要使用Link()函数来进行通信
    Link()

    #示例
    import Serial
    Serial.Set_Servo_A(150)
    Serial.Set_Servo_B(150)
    Serial.Set_Servo_C(150)
    Serial.Set_Servo_D(150)
    Serial.Link()

## 查看摄像头的图像

    在main.py的倒数两行中有显示图像的函数，注意只能选择查看其中一个图像
    修改main.py在次运行后既可查看摄像头的实时画面
    注意：此时运行必须是在远程桌面或外接显示器中运行，使用远程ssh命令行运行无法显示会报错

