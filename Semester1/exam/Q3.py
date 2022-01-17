"""Q3 by Stefana Chiritescu
    A00282343"""

from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Treble:

    # new code
    def __init__(self, val1, val2, val3):
        self.__value1 = val1
        self.__value2 = val2
        self.__value3 = val3

    def resetValue2(self, val):
        self.__value2 = val

    def getValue1(self):
        return self.__value1

    def getValue2(self):
        return self.__value2

    def getValue3(self):
        return self.__value3

    def add(self):
        return self.__value1 + self.__value2 + self.__value3

    def largest(self):
        return max(self.__value1, self.__value2, self.__value3)


# ------------end of class definition------------------


def display():
    value1 = c1.getValue1()
    value2 = c1.getValue2()
    value3 = c1.getValue3()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)


def maxEvent():
    result = c1.largest()
    display()
    entry7.delete(0, END)  # delete old value
    entry7.insert(END, result)


def addEvent():
    result = c1.add()
    display()
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, result)


def resetEvent():
    value = int(entry5.get())
    c1.resetValue2(value)
    display()


c1 = Treble(3, 5, 4)

label1 = Label(window, text="Welcome", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)

label2 = Label(window, text="Value1", fg="blue", width=8, font=("arial", 10, "bold"))
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Value2", fg="blue", width=8, font=("arial", 10, "bold"))
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

# changed 'Value2' to be 'Value3'
label4 = Label(window, text="Value3", fg="blue", width=8, font=("arial", 10, "bold"))
label4.place(x=10, y=150)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=150)

button0 = Button(window, text="resetV2", fg="black", font=("arial", 10,), command=resetEvent)
button0.place(x=10, y=190)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=190)

button6 = Button(window, text="add", fg="black", font=("arial", 10), command=addEvent)
button6.place(x=10, y=230)

entry6 = Entry(window)
entry6.insert(END, '1')
entry6.place(x=120, y=230)

button7 = Button(window, text="Largest", fg="black", font=("arial", 10), command=maxEvent)
button7.place(x=10, y=270)

entry7 = Entry(window)
entry7.insert(END, '1')
entry7.place(x=120, y=270)
display()

mainloop()
