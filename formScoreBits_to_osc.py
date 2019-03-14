# requires the following python libraries:
#  python-osc
#  pyserial
 
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


# change this string depending upon where your computer makes a device for the micro:bit
serialport = "/dev/cu.usbmodem14302"
 
ser = serial.Serial(serialport, 115200)
client = udp_client.SimpleUDPClient("localhost", 8999)
S = Sender()
while(True):
    line = ser.readline().decode('utf8').strip()

    message = list(map(float, line.split("^")))
    tag = message[0]
    if tag == "a":
        S.output[0:3] = message[0:3]
    elif tag == "b":
        S.output[4:7] = message[0:3]

 
    S.send()


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
#        client.send_message("/wand_accel", data )
