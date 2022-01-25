

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

from Ex213MyClasses import *


#------------end of class definition------------------

def display():
    value1 = t1.getName()
    value2 = t1.getPlayed()
    value3 = t1.getPoints()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value


def winEvent():
    t1.win()
    display()


def drawEvent():
    t1.draw()
    display()

def lossEvent():
    t1.loss()
    display()

def exitEvent():
    quit()

def getWinsEvent():
    result=t1.getWins()
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, result)

t1=FootballTeam("Chelsea")


label1 = Label(window, text="Team Details", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Name", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Played", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Points", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

#-------------------------------
button1= Button(window, text="Win", fg="black", font=("arial", 10, "bold"), command=winEvent)
button1.place(x=40, y=180)

button2= Button(window, text="Draw", fg="black", font=("arial", 10, "bold"), command=drawEvent)
button2.place(x=120, y=180)

button3= Button(window, text="Loss", fg="black", font=("arial", 10, "bold"), command=lossEvent)
button3.place(x=40, y=220)

button4= Button(window, text="Exit", fg="black", font=("arial", 10, "bold"), command=exitEvent)
button4.place(x=120, y=220)



button5= Button(window, text="readWins", fg="black", font=("arial", 10, "bold"), command=getWinsEvent)
button5.place(x=10, y=260)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=260)


display()

mainloop()
