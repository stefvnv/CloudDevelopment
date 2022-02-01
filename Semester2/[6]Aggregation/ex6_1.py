from tkinter import *

window = Tk()
window.geometry("300x340")
window.title("Welcome")

from ex6_1Class import *


# ------------end of class definition------------------

def display():
    value1 = t1.readTitle()
    value2 = t1.readTopic()
    value3 = t1.readLecturerName()
    value4 = t1.readLecturerOffice()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, value4)


# entry6.delete(0, END)  # delete old value
# entry6.insert(END, value5)

def incrYearEvent():
    t1.incrementYear()
    display()


def setOfficeEvent():
    newOffice = entry4b.get()
    t1.updateLecturerOffice(newOffice)
    display()


def exitEvent():
    quit()


def setTitleEvent():
    newTitle = entry3b.get()
    t1.updateTitle(newTitle)
    display()


t1 = Module("Database2", "Relational Databases", "J.Smith", "M312")

label1 = Label(window, text="Module Details", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=40, y=30)  # place on screen

label2 = Label(window, text="Title", fg="blue", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Topic", fg="blue", width=12, font=("arial", 10, "bold"))  #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Lecturer", fg="blue", width=8, font=("arial", 10, "bold"))  #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

label5 = Label(window, text="Office", fg="blue", width=12, font=("arial", 10, "bold"))  #
label5.place(x=10, y=170)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=170)

# -------------------------------


button3 = Button(window, text="updateTitle", fg="black", font=("arial", 10, "bold"), command=setTitleEvent)
button3.place(x=40, y=220)

entry3b = Entry(window)
entry3b.insert(END, 'Databases 2.1')
entry3b.place(x=150, y=220)

button4 = Button(window, text="updateOffice", fg="black", font=("arial", 10, "bold"), command=setOfficeEvent)
button4.place(x=40, y=250)

entry4b = Entry(window)
entry4b.insert(END, 'E231')
entry4b.place(x=150, y=250)

display()

mainloop()

