from pythonosc import dispatcher
from pythonosc import osc_server
import threading
from tkinter import *
import serial
from pythonosc import udp_client
import os


class GuiLogic:
    def __init__(self):
        self.master = Tk()
        self.exercises = ["Still","Bicep Curl-Good","Bicep Curl-Bad(pronation)","Bicep Curl-Bad(half)"]
        self.exercise_gifs = ["placeholder","still.gif","BicepCurl_GoodForm_1Arm.gif","BicepCurl_PronationFailure_crop.gif","BicepCurl_HalfRep_1Arm.gif"]
        self.exercise_gifs_length = [0,1,41,3,17]
        self.exercise_speed = [0,100,100,300,100]
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
        self.gifs_dict = {i+1:self.load_gif_by_value(i+1) for i,e in enumerate(self.exercises)}
        self.frames = self.gifs_dict[self.getExerciseValue()]
        self.label = Label(self.master)
        self.label.pack()
        #self.rep_text = Label(self.master, text = "Number of Reps" )
        #self.rep_text.pack()
        #self.reps_entry = Entry(self.master)
        #self.reps_entry.insert(END, '5')
        #self.reps_entry.pack()
        self.history = []

        self.good_counts = IntVar(self.master,0)
        self.half_counts = IntVar(self.master,0)
        self.pronation_counts = IntVar(self.master,0)

        self.good_rep_mesg = StringVar(self.master, value= "Good Reps Counted: %i" % self.good_counts.get())
        self.half_rep_mesg = StringVar(self.master, value="Half Reps Counted: %i" % self.half_counts.get())
        self.pronation_rep_mesg = StringVar(self.master, value="Failures to Pronate Counted: %i" % self.pronation_counts.get())

        self.good_rep_disp = Label(self.master,textvariable = self.good_rep_mesg)
        self.half_rep_disp = Label(self.master, textvariable= self.half_rep_mesg)
        self.pronation_rep_disp = Label(self.master, textvariable=self.pronation_rep_mesg)

        self.good_rep_disp.pack()
        self.half_rep_disp.pack()
        self.pronation_rep_disp.pack()
    def load_gif_by_value(self,value):
        file_name = self.exercise_gifs[value]
        return [PhotoImage(master=self.master, file=file_name, format='gif -index %i' % i) for i in range(self.exercise_gifs_length[value])]

    def run(self):
        if self.isRunning.get():
            self.isRunning.set(False)
            self.analyze_set()
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
            ind = 0
            self.frames = self.gifs_dict[self.getExerciseValue()]
        frame = self.frames[ind]
        ind = (ind + 1)%self.exercise_gifs_length[prev_image]
        self.label.configure(image=frame)
        self.master.after(self.exercise_speed[prev_image], self.update_gif, ind, prev_image)

    def receive_data(self,head,one,two,three,four):
        print("received this data: ", head,one,two,three,four)

    def receive_class(self,head):
        if head == "/output_1":
            self.history.append(1)
        elif head == "/output_2":
            self.history.append(2)
        elif head == "/output_3":
            self.history.append(3)
        else:
            self.history.append(4)
        print(self.history)

    def analyze_set(self):
        self.good_counts.set(0)
        self.half_counts.set(0)
        self.pronation_counts.set(0)
        good_reps_counted = 0
        half_reps_counted = 0
        pronation_reps_counted = 0
        for input in self.history:
            if input == 2:
                good_reps_counted += 1
            elif input == 3:
                pronation_reps_counted += 1
            elif input == 4:
                half_reps_counted += 1

        half_reps_counted = abs(half_reps_counted-good_reps_counted)
        self.good_counts.set(good_reps_counted)
        self.half_counts.set(half_reps_counted)
        self.pronation_counts.set(pronation_reps_counted)

        self.good_rep_mesg.set("Good Reps Counted: %i" % self.good_counts.get())
        self.half_rep_mesg.set("Half Reps Counted: %i" % self.half_counts.get())
        self.pronation_rep_mesg.set("Failures to Pronate Counted: %i" % self.pronation_counts.get())

        print("good_reps", good_reps_counted)
        print("half_reps", half_reps_counted)
        print("pronation_reps", pronation_reps_counted)
        self.history = []






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
        #print(o)
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


class Listener:
    def __init__(self,GL):
        self.GL = GL
    def run_listener(self):
        d = dispatcher.Dispatcher()
        #d.map("/wek/outputs", self.GL.receive_data)
        d.map("/output_1", self.GL.receive_class)
        d.map("/output_2", self.GL.receive_class)
        d.map("/output_3", self.GL.receive_class)
        d.map("/output_4", self.GL.receive_class)
        port = 12000
        ip = "127.0.0.1"
        server = osc_server.ThreadingOSCUDPServer((ip, port), d)
        print("Serving on {}".format(server.server_address))
        server.serve_forever()


GL = GuiLogic()
S = Server(GL)
L = Listener(GL)
Server_Thread_L = threading.Thread(target = L.run_listener , args=())
Server_Thread_L.daemon = True
Server_Thread_L.start()
Server_Thread_S = threading.Thread(target = S.run_server , args=())
Server_Thread_S.daemon = True
Server_Thread_S.start()
GL.master.after(0, GL.update_gif, 0, GL.getExerciseValue())
GL.master.mainloop()