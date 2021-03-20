import serial 
import os
import time
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

data=bytearray(5)
data[0]=0xff
data[1]=0xfe

def Protocol():
    global data 
    data[4]=(data[2]+data[3])%256
    ser.write(data)


# while True:
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
    data[3]=0x01
    Protocol()

def Across_Right():
    global data
    data[2]=0x00
    data[3]=0x08
    Protocol()

# def Right():
#     global data
#     data[2]=0x00
#     data[3]=0x20
#     Protocol()

# def Right():
#     global data
#     data[2]=0x00
#     data[3]=0x20
#     Protocol()