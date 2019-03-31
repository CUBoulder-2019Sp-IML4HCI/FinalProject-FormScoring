from tkinter import *



class GuiLogic:
    def __init__(self,master):
        exercises = ["Bicep Curl","Bench Press"]
        self.selected_exercise = StringVar(master)
        self.selected_exercise.set(exercises[0])
        exercise_select = OptionMenu(master, self.selected_exercise,*exercises)
        record_button = Button(master, text="Start/Stop Recording",command=self.record)
        exercise_select.pack()
        record_button.pack()
    def record(self):
        #implement logic to record data
        print("record")

root = Tk()
GL = GuiLogic(root)
root.mainloop()


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