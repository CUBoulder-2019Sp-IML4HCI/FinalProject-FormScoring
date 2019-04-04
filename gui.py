import argparse
from pythonosc import dispatcher
from pythonosc import osc_server
import threading
from tkinter import *
import _pickle as p



class GuiLogic:
    def __init__(self):
        self.master = Tk()
        exercises = ["Bicep Curl","Bench Press"]
        self.selected_exercise = StringVar(self.master)
        self.selected_exercise.set(exercises[1])
        exercise_select = OptionMenu(self.master, self.selected_exercise,*exercises)
        record_button = Button(self.master, text="Start/Stop Recording",command=self.record)
        self.file_name = StringVar(self.master)
        self.file_name.set("FormScoringData")
        file_name_entry = Entry(self.master, textvariable=self.file_name)
        save_button = Button(self.master, text="Save Data",command=self.save)
        exercise_select.pack()
        record_button.pack()
        file_name_entry.pack()
        save_button.pack()
        self.recording = BooleanVar()
        self.recording.set(False)
        self.loop = True
        self.e = threading.Event()
        self.data = []
    def save(self):
        file_name = self.file_name.get() + ".pickle"
        with open(file_name, 'wb') as data_handle:
            p.dump(self.data,data_handle)
        print("Data saved as ", file_name)
    def record(self):
        #print(self.selected_exercise.get())
        if self.recording.get():
            self.stop_record()
        else:
            self.start_record()

    def start_record(self):
        print("started recording")
        self.recording.set(True)
        self.single_movement = []

    def stop_record(self):
        print("stopped recording")
        self.recording.set(False)
        self.data.append(self.single_movement)

    def receiveData(self,one=None,two=None,three=None,four=None,five=None,six=None,seven=None,eight=None,nine=None,ten=None):
        if self.recording.get():
            if self.e.is_set():
                print("data lost")
            else:
                self.e.set()
                self.single_movement.append([one,two,three,four,five,six,seven,eight,nine,ten])
                self.e.clear()
                print(self.single_movement)

    def gui_mainloop(self):
        while self.loop:
            self.master.update_idletasks()
            self.master.update()


class Server:
    def __init__(self, GL, ip="localhost", port=8999):
        self.GL = GL
        self.ip = ip
        self.port = port

    def run_server(self):
        d = dispatcher.Dispatcher()
        d.map("/final", self.GL.receiveData)
        server = osc_server.ThreadingOSCUDPServer(
          (self.ip, self.port), d)
        print("Serving on {}".format(server.server_address))
        server.serve_forever()


GL = GuiLogic()
S = Server(GL)
Server_Thread = threading.Thread(target = S.run_server , args=())
Server_Thread.daemon = True
Server_Thread.start()
GL.master.mainloop()


'''
class ButtonHandler:
    def __init__(self,master):
        frame = Frame(master)
        menu = Menu(master)
        master.config(menu=menu)
        subMenu = Menu(menu)
        editMenu = Menu(menu)
        menu.add_cascade(label = "File", menu=subMenu)
        subMenu.add_command(label = "New Project", command = self.printMessage)
        subMenu.add_separator()
        subMenu.add_command(label="Exit",command=frame.quit)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="hello",command = self.printMessage)


        frame.pack()

        self.printButton = Button(frame, text="Print Message", command = self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)
    def printMessage(self):
        print("hello")





root = Tk()
BH = ButtonHandler(root)
root.mainloop()
'''

'''
def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")

root= Tk()
frame = Frame(root, width=300,height=250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()
'''
'''
root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
l = Label(topFrame,text="Hello Tkinter")
l2 = Label(bottomFrame,text="Bye Tkinter")
l.pack()
l2.pack()
button1 = Button(topFrame, text="Button 1", fg="red",bg="black")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")
e1 = Entry(root)
button1.pack(fill=X)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()
root.mainloop()
'''
'''
root = Tk()
label_1 = Label(root,text="Name")
label_2 = Label(root,text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan = 2)

root.mainloop()
'''