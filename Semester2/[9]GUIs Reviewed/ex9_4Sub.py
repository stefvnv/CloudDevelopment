from tkinter import *


def addDialog(window):
    window2 = Toplevel(window)
    window2.geometry("300x400")
    window2.title("Add Dialog")

    def add():
        value1 = int(list2Var.get())
        value2 = int(list3Var.get())
        result = value1 + value2
        entry5.delete(0, END)
        entry5.insert(END, result)

    def clear():
        entry5.delete(0, END)
        entry5.insert(END, ' ')
        list2Var.set("1")

    def myExit():
        window2.destroy()

    frame = Frame(window2, width=300, height=200)
    frame.place(x=10, y=80)
    label1 = Label(window2, text="Add Dialog", fg="blue", bg="yellow", font=("arial", 16, "bold"))
    label1.place(x=90, y=30)  # place on screen

    label2 = Label(frame, text="Value1", fg="blue", width=10, font=("arial", 10, "bold"))  #
    label2.grid(row=0, column=0, sticky=W + E)

    list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    list2Var = StringVar()
    combo2 = OptionMenu(frame, list2Var, *list2)
    list2Var.set("1")
    combo2.grid(row=0, column=1, sticky=W + E)

    label3 = Label(frame, text="Value2", fg="blue", width=10, font=("arial", 10, "bold"))  #
    label3.grid(row=1, column=0, sticky=W + E)

    list3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    list3Var = StringVar()
    combo3 = OptionMenu(frame, list3Var, *list3)
    list3Var.set("1")
    combo3.grid(row=1, column=1, sticky=W + E)

    button5 = Button(frame, text="Add", fg="black", font=("arial", 10, "bold"), command=add)
    button5.grid(row=2, column=0, sticky=W + E)

    entry5 = Entry(frame)
    entry5.insert(END, '')
    entry5.grid(row=2, column=1, sticky=W + E)

    button61 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clear)
    button61.grid(row=3, column=0, sticky=W + E)

    button62 = Button(frame, text="Exit", fg="black", font=("arial", 10, "bold"), command=myExit)
    button62.grid(row=3, column=1, sticky=W + E)


def subDialog(window):
    window2 = Toplevel(window)
    window2.geometry("300x400")
    window2.title("Add Dialog")

    def sub():
        value1 = int(list2Var.get())
        value2 = int(list3Var.get())
        result = value1 - value2
        entry5.delete(0, END)
        entry5.insert(END, result)

    def clear():
        entry5.delete(0, END)
        entry5.insert(END, ' ')
        list2Var.set("1")

    def myExit():
        window2.destroy()

    frame = Frame(window2, width=300, height=200)
    frame.place(x=10, y=80)
    label1 = Label(window2, text="Subtract Dialog", fg="blue", bg="yellow", font=("arial", 16, "bold"))
    label1.place(x=90, y=30)
    label2 = Label(frame, text="Value1", fg="blue", width=10, font=("arial", 10, "bold"))
    label2.grid(row=0, column=0, sticky=W + E)

    list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    list2Var = StringVar()
    combo2 = OptionMenu(frame, list2Var, *list2)
    list2Var.set("1")
    combo2.grid(row=0, column=1, sticky=W + E)

    label3 = Label(frame, text="Value2", fg="blue", width=10, font=("arial", 10, "bold"))
    label3.grid(row=1, column=0, sticky=W + E)

    list3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    list3Var = StringVar()
    combo3 = OptionMenu(frame, list3Var, *list3)
    list3Var.set("1")
    combo3.grid(row=1, column=1, sticky=W + E)

    button5 = Button(frame, text="Subtract", fg="black", font=("arial", 10, "bold"), command=sub)
    button5.grid(row=2, column=0, sticky=W + E)

    entry5 = Entry(frame)
    entry5.insert(END, '')
    entry5.grid(row=2, column=1, sticky=W + E)

    button61 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clear)
    button61.grid(row=3, column=0, sticky=W + E)

    button62 = Button(frame, text="Exit", fg="black", font=("arial", 10, "bold"), command=myExit)
    button62.grid(row=3, column=1, sticky=W + E)
