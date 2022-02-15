"""LINEAR/SEQUENTIAL SEARCH"""

from tkinter import *

window = Tk()
window.geometry("950x300")
window.title("Welcome")

from ex8_1Class import *


# ------------end of class definition------------------

def display():
    value1 = a1.readList()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)


def searchEvent():
    amt = int(entry2b.get())
    res = a1.linearSearch(amt)
    display()
    if res:
        entry5.delete(0, END)  # delete old value
        entry5.insert(END, "Found")
    else:
        entry5.delete(0, END)  # delete old value
        entry5.insert(END, "Not Found")


list = [2, 59, 7, 88, 9, 11, 102, 22, 27, 28, 29, 34, 55, 60, 61, 65, 68, 71, 73, 75, 77, 8, 89, 9, 96]
a1 = MyList(list)

label1 = Label(window, text="Search Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

entry2 = Entry(window, width=100, font=("arial", 16, "bold"))
entry2.insert(END, '1')
entry2.place(x=20, y=80)

entry2b = Entry(window, width=18, font=("arial", 12, "bold"))
entry2b.insert(END, '40')
entry2b.place(x=230, y=120)

label3b = Label(window, text="Enter Search Item", fg="blue", width=18, font=("arial", 12, "bold"))  #
label3b.place(x=10, y=120)

button5 = Button(window, text="Perform LinearSearch", fg="black", font=("arial", 12, "bold"), command=searchEvent)
button5.place(x=20, y=160)

entry5 = Entry(window, width=18, font=("arial", 12, "bold"))
entry5.insert(END, '')
entry5.place(x=230, y=160)

display()

mainloop()
