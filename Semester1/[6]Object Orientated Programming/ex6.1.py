from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Counter:

    def __init__(self, val, limit):
        self.value = val
        self.limit = limit

    def setValue(self, val):
        self.value = val

    def getValue(self):
        return self.value

    def getLimit(self):
        return self.limit

    def increment(self):
        if self.value < self.limit:
            self.value += 1
            return True
        else:
            return False

    def decrement(self):
        if self.value > 0:
            self.value -= 1
            return True
        else:
            return False


# ------------end of class definition------------------


def display():
    value = c1.getValue()
    limit = c1.getLimit()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, limit)


def incrEvent():
    result = c1.increment()
    display()
    entry4.delete(0, END)  # delete old value

    if not result:
        entry4.insert(END, 'Limit reached')
    else:
        entry4.insert(END, 'Success')


def decrEvent():
    result = c1.decrement()
    display()
    entry4.delete(0, END)  # delete old value

    if not result:
        entry4.insert(END, 'Already 0')
    else:
        entry4.insert(END, 'Success')


c1 = Counter(8, 10)

label1 = Label(window, text="Welcome", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

label2 = Label(window, text="Value", fg="blue", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Limit", fg="blue", width=8, font=("arial", 10, "bold"))  #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

button1 = Button(window, text="Increment", fg="black", font=("arial", 12, "bold"), command=incrEvent)
button1.place(x=40, y=140)

button2 = Button(window, text="Decrement", fg="black", font=("arial", 12, "bold"), command=decrEvent)
button2.place(x=140, y=140)

label4 = Label(window, text="Message", fg="blue", width=8, font=("arial", 10, "bold"))  #
label4.place(x=10, y=180)

entry4 = Entry(window)
entry4.insert(END, '')
entry4.place(x=120, y=180)

display()

mainloop()
