from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Dice:

    def __init__(self):
        self.__value = 0

    def getValue(self):
        return self.__value

    def setValue(self, val):
        self.__value = val

    def roll(self):
        import random
        self.__value = random.randint(1, 6)


# ------------end of class definition------------------

def display():
    value1 = d1.getValue()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)


def rollEvent():
    d1.roll()
    display()


def resetEvent():
    d1.setValue(1)
    display()


d1 = Dice()

label1 = Label(window, text="Dice ", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

label2 = Label(window, text="Value", fg="blue", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

# -------------------------------
button1 = Button(window, text="Roll Dice", fg="black", font=("arial", 10, "bold"), command=rollEvent)
button1.place(x=40, y=120)

button2 = Button(window, text="Reset", fg="black", font=("arial", 10, "bold"), command=resetEvent)
button2.place(x=120, y=120)

display()

mainloop()
