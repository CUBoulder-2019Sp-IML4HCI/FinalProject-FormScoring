# requires the following python libraries:
#  python-osc
#  pyserial
 
import serial
from pythonosc import udp_client
 
# change this string depending upon where your computer makes a device for the micro:bit
serialport = "/dev/cu.usbmodem14302"
 
ser = serial.Serial(serialport, 115200)
client = udp_client.SimpleUDPClient("localhost", 8999)
 
while(True):
    line = ser.readline().decode('utf8').strip()
 
    if line.count('^') != 2: continue
 
    x, y, z = map(float, line.split("^"))
 
    print(f"({x}, {y}, {z})")
 
    client.send_message("/wand_accel", [x, y, z] )

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
