# requires the following python libraries:
#  python-osc
#  pyserial

import os
import serial
from pythonosc import udp_client

class Sender:
    def __init__(self):
        self.output = [None]*8
        self.send = self.wait_for_fill
    def wait_for_fill(self):
        if None in self.output:
            print("Waiting on full output.")
        else:
            self.send = self.send_signal
    def send_signal(self):
        print(self.output)
        client.send_message("/final", self.output)


#if windows
if os.name == 'nt':
    serialport = "COM7"
#else linux
else:
    serialport = "/dev/cu.usbmodem14302"

 
ser = serial.Serial(serialport, 115200)
client = udp_client.SimpleUDPClient("localhost", 8999)
S = Sender()
while(True):
    line = ser.readline().decode('utf8').strip()

    message = list(map(str, line.split("^")))
    tag = message[0]
    if tag == "a":
        S.output[:4] = message[1:]
    elif tag == "b":
        S.output[4:] = message[1:]
    S.send()
    #print(S.output)


#import serial
#from pythonosc import udp_client

# change this string depending upon where your computer makes a device for the micro:bit
#serialport = "/dev/ttyACM0"

#ser = serial.Serial(serialport, 115200)
#client = udp_client.SimpleUDPClient("localhost", 8999)

#while(True):
#    try:
#        line = ser.readline().decode('utf8').strip()
#        data = list(map(float, line.split("^")))
#    except:
#        data = []
#        
#    if(len(data) == 6):        
#        print(f"({data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]})")