import serial 
import os
import time
portx="/dev/ttyUSB0" 
bps= 115200
timex=5 
ser = serial.Serial(portx, int(bps), timeout=1, parity=serial.PARITY_NONE,stopbits=1) 
if (ser.isOpen()): 
    print("open success") 
    # os.system('minicom &')


while True:
    line = ser.readline()
    print(line)
    time.sleep(0.01)


    
def posiion_get():
    ser = serial.Serial(portx, int(bps), timeout=1, parity=serial.PARITY_NONE,stopbits=1) 
    if (ser.isOpen()): 
        print("open success") 
        os.system('minicom &')
        #ser.write("hello".encode()) 
       
        line = ser.readline() 
        if(line): 
            #print(str(line) )
            temp = str(line)
            temp = temp.split('=')
            #print(temp)
            temp_x_y=[]
            for i in [1,2]:
                tempq=temp[i]
                tempq=tempq.split('C')
                tempq=int(tempq[0])
                temp_x_y.append(tempq)
                #print(temp_x_y)
            line=0 
        return temp_x_y
