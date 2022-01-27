from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Calculator")


def add():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    resultAdd = value1 + value2
    entry4.delete(0, END)
    entry4.insert(END, resultAdd)


def subtract():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    resultSubtract = value1 - value2
    entry5.delete(0, END)
    entry5.insert(END, resultSubtract)


label1 = Label(window, text="Calculator", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)

label2 = Label(window, text="Value1", fg="blue", width=10, font=("arial", 12, "bold"))  #
label2.place(x=10, y=80)

label3 = Label(window, text="Value2", fg="blue", width=10, font=("arial", 12, "bold"))  #
label3.place(x=10, y=120)

button1 = Button(window, text="Add", fg="black", width=7, font=("arial", 12, "bold"), command=add)
button1.place(x=30, y=160)

button2 = Button(window, text="Subtract", fg="black", width=7, font=("arial", 12, "bold"), command=subtract)
button2.place(x=30, y=200)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=100, y=80)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=100, y=120)

entry4 = Entry(window, width=12)
entry4.insert(END, '1')
entry4.place(x=150, y=165)

entry5 = Entry(window, width=12)
entry5.insert(END, '1')
entry5.place(x=150, y=205)


mainloop()
