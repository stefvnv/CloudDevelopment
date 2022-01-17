

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

from Ex214MyClasses import *


#------------end of class definition------------------

def display():
    value1 = a1.getValue()
    value2 = a1.getLimit()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry2b.delete(0, END)  # delete old value
    entry2b.insert(END, value2)




def depositEvent():
    amt=int(entry4.get())
    res= a1.stepUp(amt)
    display()
    if (res==True):
        entry6.delete(0, END)  # delete old value
        entry6.insert(END, "Success")
    else:
        entry6.delete(0, END)  # delete old value
        entry6.insert(END, "Exceeds Limit")

def resetEvent():
    amt=int(entry3.get())
    a1.resetLimit(amt)
    display()


def withdrawEvent():
    amt = int(entry5.get())
    res=a1.stepDown(amt)
    display()
    if (res==True):
        entry6.delete(0, END)  # delete old value
        entry6.insert(END, "Success")
    else:
        entry6.delete(0, END)  # delete old value
        entry6.insert(END, "Not Allowed")

a1=MyStepper(8,100)


label1 = Label(window, text="Stepper Details", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen


button4= Button(window, text="ResetLimit", fg="black", font=("arial", 10, "bold"), command=resetEvent)
button4.place(x=40, y=140)


entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Value", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=80)

entry2b = Entry(window)
entry2b.insert(END, '10')
entry2b.place(x=120, y=110)

label3b = Label(window, text="UpperLimit", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3b.place(x=10, y=110)



entry3 = Entry(window)
entry3.insert(END, '140')
entry3.place(x=120, y=140)



button4= Button(window, text="stepUp", fg="black", font=("arial", 10, "bold"), command=depositEvent)
button4.place(x=40, y=170)

entry4 = Entry(window)
entry4.insert(END, '30')
entry4.place(x=120, y=170)

button5= Button(window, text="stepDown", fg="black", font=("arial", 10, "bold"), command=withdrawEvent)
button5.place(x=40, y=210)

entry5 = Entry(window)
entry5.insert(END, '20')
entry5.place(x=120, y=210)


label6 = Label(window, text="Message", fg="blue", width=8, font=("arial", 10, "bold"))   #
label6.place(x=10, y=240)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=120, y=240)

display()

mainloop()
