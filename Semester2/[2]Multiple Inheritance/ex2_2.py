

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

from ex2_2Class import *


#------------end of class definition------------------

def display():
    value1 = t1.getLanguage()
    value2 = t1.getLevel()
    value3 = t1.getTitle()
    value4 = t1.getEmployees()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, value4)


def stepEvent():
    t1.stepProgammingLevel()
    display()


def incrEvent():
    t1.incrementEmployees()
    display()

def decrEvent():
    t1.decrementEmployees()
    display()

def exitEvent():
    quit()

def changeEvent():
    newTitle = entry6.get()
    t1.changeTitle(newTitle)
    display()

t1=ProgrammingManager("Python",1, "Project Manager",30)


label1 = Label(window, text="Manager Details", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Language", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Prog Level", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Title", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

label5 = Label(window, text="Employees", fg="blue", width=8, font=("arial", 10, "bold"))   #
label5.place(x=10, y=170)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=170)


#-------------------------------
button1= Button(window, text="stepLevel", fg="black", font=("arial", 10, "bold"), command=stepEvent)
button1.place(x=40, y=200)

button2= Button(window, text="incrEmployees", fg="black", font=("arial", 10, "bold"), command=incrEvent)
button2.place(x=120, y=200)

button3= Button(window, text="decrEmployees", fg="black", font=("arial", 10, "bold"), command=decrEvent)
button3.place(x=120, y=230)

button4= Button(window, text="Exit", fg="black", font=("arial", 10, "bold"), command=exitEvent)
button4.place(x=40, y=230)


button5= Button(window, text="changeTitle", fg="black", font=("arial", 10, "bold"), command=changeEvent)
button5.place(x=10, y=260)

entry6 = Entry(window)
entry6.insert(END, 'Dept Manager')
entry6.place(x=120, y=260)


display()

mainloop()
