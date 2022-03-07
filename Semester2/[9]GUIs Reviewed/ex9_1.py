from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


def add():
    value1 = int(list2Var.get())
    value2 = int(list3Var.get())
    value3 = int(list4Var.get())
    result = value1 + value2 + value3
    entry5.delete(0, END)
    entry5.insert(END, result)


def max():
    value1 = int(list2Var.get())
    value2 = int(list3Var.get())
    value3 = int(list4Var.get())
    result = value1
    if value2 > result:
        result = value2
    if value3 > result:
        result = value3
    entry6.delete(0, END)
    entry6.insert(END, result)


def clear():
    entry5.delete(0, END)
    entry5.insert(END, ' ')
    entry6.delete(0, END)
    entry6.insert(END, ' ')
    list2Var.set("1")
    list3Var.set("1")
    list4Var.set("1")


def myExit():
    exit()


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Grid example", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)  # place on screen

label2 = Label(frame, text="Value1", fg="blue", width=15, font=("arial", 10, "bold"))  #
label2.grid(row=0, column=0, sticky=W + E)

list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list2Var = StringVar()
combo2 = OptionMenu(frame, list2Var, *list2)
list2Var.set("1")
combo2.grid(row=0, column=1, sticky=W + E)

label3 = Label(frame, text="Value2", fg="blue", width=15, font=("arial", 10, "bold"))  #
label3.grid(row=1, column=0, sticky=W + E)

list3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list3Var = StringVar()
combo3 = OptionMenu(frame, list3Var, *list3)
list3Var.set("1")
combo3.grid(row=1, column=1, sticky=W + E)

label4 = Label(frame, text="Value2", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4.grid(row=2, column=0, sticky=W + E)

list4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list4Var = StringVar()
combo4 = OptionMenu(frame, list4Var, *list4)
list4Var.set("1")
combo4.grid(row=2, column=1, sticky=W + E)

button5 = Button(frame, text="Add", fg="black", font=("arial", 10, "bold"), command=add)
button5.grid(row=3, column=0, sticky=W + E)

entry5 = Entry(frame)
entry5.insert(END, '')
entry5.grid(row=3, column=1, sticky=W + E)

button6 = Button(frame, text="Max", fg="black", font=("arial", 10, "bold"), command=max)
button6.grid(row=4, column=0, sticky=W + E)

entry6 = Entry(frame)
entry6.insert(END, '')
entry6.grid(row=4, column=1, sticky=W + E)

button61 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clear)
button61.grid(row=5, column=0, sticky=W + E)

button62 = Button(frame, text="Exit", fg="black", font=("arial", 10, "bold"), command=myExit)
button62.grid(row=5, column=1, sticky=W + E)

mainloop()
