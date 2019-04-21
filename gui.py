import argparse
from pythonosc import dispatcher
from pythonosc import osc_server
import threading
from tkinter import *
#import tkinter
import _pickle as p
import os
import serial
from pythonosc import udp_client

import time
import os




class GuiLogic:
    def __init__(self):
        self.master = Tk()
        self.exercises = ["Still","Bicep Curl-Good","Bicep Curl-Bad(pronation)","Bicep Curl-Bad(range)"]
        self.exercise_gifs = ["placeholder","puppies.gif","dogs.gif","puppies.gif","dogs.gif"]
        self.exercise_values = {e:i+1 for i,e in enumerate(self.exercises)}
        self.selected_exercise = StringVar(self.master)
        self.selected_exercise.set(self.exercises[0])
        exercise_select = OptionMenu(self.master, self.selected_exercise,*self.exercises)
        record_button = Button(self.master, text="Start/Stop Recording",command=self.record)
        run_button = Button(self.master, text="Start/Stop Running",command = self.run)
        exercise_select.pack()
        record_button.pack()
        run_button.pack()
        self.isRunning = BooleanVar(self.master)
        self.isRunning.set(False)
        self.recording = BooleanVar(self.master)
        self.recording.set(False)
        self.loop = True
        self.e = threading.Event()
        self.data = []
        self.frames = self.load_gif()
        self.label = Label(self.master)
        self.label.pack()

    def load_gif(self):
        file_name = self.exercise_gifs[self.getExerciseValue()]
        return [PhotoImage(master=self.master, file=file_name, format='gif -index %i' % i) for i in range(10)]

    def run(self):
        if self.isRunning.get():
            self.isRunning.set(False)
        else:
            self.isRunning.set(True)

    def record(self):
        if self.recording.get():
            self.stop_record()
        else:
            self.start_record()

    def start_record(self):
        print("started recording")
        self.recording.set(True)

    def stop_record(self):
        print("stopped recording")
        self.recording.set(False)

    def getExerciseValue(self):
        v = self.exercise_values[self.selected_exercise.get()]
        return v

    def update_gif(self, ind, prev_image):
        if prev_image != self.getExerciseValue():
            prev_image = self.getExerciseValue()
            self.frames = self.load_gif()
            ind = 0
        frame = self.frames[ind]
        ind = (ind + 1)%10
        self.label.configure(image=frame)
        self.master.after(100, self.update_gif, ind, prev_image)


def str_float_map(x):
    try:
        y = float(x)
    except:
        y = str(x)
        
    return(y)
    
class Server:
    def __init__(self, GL, ip="localhost", port=6448):
        self.GL = GL
        self.ip = ip
        self.port = port
        self.client = udp_client.SimpleUDPClient(self.ip, self.port)
        self.output = [None] * 8
        self.send = self.wait_for_fill
        self.record_prev_state = False
        self.run_prev_state = False

    def wait_for_fill(self):
        if None in self.output:
            print("Waiting on full output.")
        else:
            self.send = self.send_signal

    def send_signal(self):
        s1 = self.output[0]
        s2 = self.output[4]
        if s1 == 0 or s2 == 0:
            strength = max(s1,s2)
        else:
            strength = (s1+s2)/2
        o = [strength] + self.output[1:4] + self.output[5:]
        print(o)
        self.client.send_message("/wek/inputs", o)

    def run_server(self):
        # if windows
        if os.name == 'nt':
            serialport = "COM7"
        # else linux
        else:
            #serialport = "/dev/cu.usbmodem14302"
            serialport = "/dev/ttyACM0"

        ser = serial.Serial(serialport, 115200)
        while (True):
            line = ser.readline().decode('utf8').strip()
            #message = list(map(str, line.split("^")))
            message = list(map(str_float_map, line.split("^")))
            
            tag = message[0]
            #print(message)
            if tag == "a":
                self.output[:4] = message[1:]
            elif tag == "b":
                self.output[4:] = message[1:]
            self.send()
            new_rec_state = GL.recording.get()
            new_run_state = GL.isRunning.get()

            if new_run_state != self.run_prev_state:
                self.run_prev_state = new_run_state
                if new_run_state:
                    self.client.send_message("/wekinator/control/startRunning", 1)
                else:
                    self.client.send_message("/wekinator/control/stopRunning", 1)

            if new_rec_state != self.record_prev_state:
                self.record_prev_state = new_rec_state
                if new_rec_state:
                    self.client.send_message("/wekinator/control/startDtwRecording", GL.getExerciseValue())
                else:
                    self.client.send_message("/wekinator/control/stopDtwRecording", 1)


GL = GuiLogic()
S = Server(GL)
Server_Thread = threading.Thread(target = S.run_server , args=())
Server_Thread.daemon = True
Server_Thread.start()
GL.master.after(0, GL.update_gif, 0, GL.getExerciseValue())
GL.master.mainloop()

