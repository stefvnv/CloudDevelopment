from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def incr():
    value = int(entry2.get())
    value = value + 1
    entry2.delete(0, END)
    entry2.insert(END, value)
    checkbox1.deselect()


def decr():
    value = int(entry2.get())
    value = value - 1
    entry2.delete(0, END)
    entry2.insert(END, value)


def reset():
    value = int(entry3.get())
    entry2.delete(0, END)
    entry2.insert(END, value)
    checkbox1.deselect()


def add():
    value1 = int(entry2.get())
    value2 = int(entry4.get())
    result = value1+value2
    entry2.delete(0, END)
    entry2.insert(END, result)
    checkbox1.deselect()


def subtract():
    value1 = int(entry2.get())
    value2 = int(stepDownVar.get())
    result = value1-value2

    if value1 > value2:
        checkbox1.select()
    else:
        result = value1 - value2
        entry2.delete(0, END)
        entry2.insert(END, result)
        checkbox1.deselect()


button1 = Button(window, text="Increment", fg="black", font=("arial", 12, "bold"), command=incr)
button1.place(x=40, y=80)

button2 = Button(window, text="Decrement", fg="black", font=("arial", 12, "bold"), command=decr)
button2.place(x=140, y=80)

button3 = Button(window, text="Reset", fg="black", font=("arial", 12, "bold"), command=reset)
button3.place(x=40, y=120)

button4 = Button(window, text="Add", fg="black", font=("arial", 12, "bold"), command=add)
button4.place(x=40, y=160)

button5 = Button(window, text="Subtract", fg="black", font=("arial", 12, "bold"), command=subtract)
button5.place(x=40, y=200)


entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=130, y=50)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=130, y=125)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=130, y=165)


label1 = Label(window, text="Welcome", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=10)                            # place on screen

label2 = Label(window, text="Value", fg="blue", font=("arial", 12, "bold"))
label2.place(x=30, y=50)


list1 = ['1', '2', '3', '4']
stepDownVar = StringVar()
combo1 = OptionMenu(window, stepDownVar, *list1)
stepDownVar.set("1")
combo1.place(x=130, y=200)


checkbox1 = IntVar()
checkbox1 = Checkbutton(window, text="Not allowed", variable=checkbox1)
checkbox1.place(x=90, y=250)
checkbox1.deselect()


mainloop()
