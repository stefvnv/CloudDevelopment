from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Stepper:
    def __init__(self):
        self.__value = 0

    def getValue(self):
        return self.__value

    def stepUp(self, amt):
        self.__value += amt

    def stepDown(self, amt):
        self.__value -= amt

    def reset(self, amt):
        self.__value = amt


def display():
    value1 = a1.getValue()
    value2 = 0
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)


def depositEvent():
    amt = int(entry4.get())
    a1.stepUp(amt)
    display()


def resetEvent():
    amt = int(entry3.get())
    a1.reset(amt)
    display()


def withdrawEvent():
    amt = int(entry5.get())
    a1.stepDown(amt)
    display()


a1 = Stepper()


label1 = Label(window, text="Stepper Details", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen


button4 = Button(window, text="Reset", fg="black", font=("arial", 10, "bold"), command=resetEvent)
button4.place(x=40, y=110)


entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Value", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=80)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)


button4 = Button(window, text="stepUp", fg="black", font=("arial", 10, "bold"), command=depositEvent)
button4.place(x=40, y=140)

entry4 = Entry(window)
entry4.insert(END, '30')
entry4.place(x=120, y=140)

button5 = Button(window, text="stepDown", fg="black", font=("arial", 10, "bold"), command=withdrawEvent)
button5.place(x=40, y=180)

entry5 = Entry(window)
entry5.insert(END, '20')
entry5.place(x=120, y=180)


display()


mainloop()
