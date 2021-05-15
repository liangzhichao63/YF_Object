import serial 
import os
import time
import numpy as np
portx="/dev/ttyUSB0" 
bps= 115200
timex=5 
ser = serial.Serial(portx, int(bps), timeout=1, parity=serial.PARITY_NONE,stopbits=1) 
if (ser.isOpen()): 
    print("串口打开成功") 
else :
    print("请检查串口是否链接或用sudo运行")


def Read_Data():
    line = ser.readline()
    print(line)

def Send_Data(data):
    global ser
    ser.write(data)
#协议头
data=bytearray(5)
data[0]=0xff
data[1]=0xfe

def Protocol():
    global data 
    data[4]=(data[2]+data[3])%256
    # print(data)
    ser.write(data)


#     data[2]=0xA1
#     data[3]=0xEA

#     Protocol()
#     time.sleep(1)
#     Read_Data()
#define _PS2_Key_Dir_U  0x0010
#define _PS2_Key_Dir_D  0x0040
#define _PS2_Key_Dir_L  0x0080
#define _PS2_Key_Dir_R  0x0020

#define _PS2_Key_Butt_U  0x1000
#define _PS2_Key_Butt_D  0x4000
#define _PS2_Key_Butt_L  0x8000
#define _PS2_Key_Butt_R  0x2000

#define _PS2_Key_SideL_1 0x0400
#define _PS2_Key_SideL_2 0x0100

#define _PS2_Key_SideR_1 0x0800
#define _PS2_Key_SideR_2 0x0200

#define _PS2_Key_SELECT  0x0001
#define _PS2_Key_MODE    0x0008

def Link():
    global data
    data[2]=0x00
    data[3]=0x01
    Protocol()

def Run():
    global data
    data[2]=0x00
    data[3]=0x10
    Protocol()

def Back():
    global data
    data[2]=0x00
    data[3]=0x40
    Protocol()

def Left():
    global data
    data[2]=0x00
    data[3]=0x80
    Protocol()

def Right():
    global data
    data[2]=0x00
    data[3]=0x20
    Protocol()

def Across_Left():
    global data
    data[2]=0x00
    data[3]=0x04
    Protocol()

def Across_Right():
    global data
    data[2]=0x00
    data[3]=0x08
    Protocol()
#speed:0-200
def Set_Speed(speed):
    global data
    if(speed>200):
        speed=200
    if(speed<0):
        speed=0
    data[2]=0xff
    data[3]=np.int0(speed)
    Protocol()

#舵机输入范围50-250
#爪子舵机 150 闭合 150-50打开
def Set_Servo_A(Servo):
    global data
    if(Servo>255):
        Servo=255
    if(Servo<0):
        Servo=0
    data[2]=0xfa
    data[3]=Servo
    Protocol()
#右舵机 
def Set_Servo_B(Servo):
    global data
    if(Servo>255):
        Servo=255
    if(Servo<0):
        Servo=0
    data[2]=0xfb
    data[3]=Servo
    Protocol()
#左舵机
def Set_Servo_C(Servo):
    global data
    if(Servo>255):
        Servo=255
    if(Servo<0):
        Servo=0
    data[2]=0xfc
    data[3]=Servo
    Protocol()
#底盘旋转舵机
def Set_Servo_D(Servo):
    global data
    if(Servo>255):
        Servo=255
    if(Servo<0):
        Servo=0
    data[2]=0xfd
    data[3]=Servo
    Protocol()

# while True:
#     Link()
#     Set_Servo_A(150)
#     Set_Servo_B(130)
#     Set_Servo_C(150)
#     Set_Servo_D(150)

#     time.sleep(0.1)