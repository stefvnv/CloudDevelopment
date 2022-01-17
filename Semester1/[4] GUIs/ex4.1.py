from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def incr():
    value = int(entry2.get())
    value = value + 1
    entry2.delete(0, END)
    entry2.insert(END, value)


def decr():
    value = int(entry2.get())
    value = value - 1
    entry2.delete(0, END)
    entry2.insert(END, value)


button2 = Button(window, text="Decrement", fg="black", font=("arial", 12, "bold"), command=decr)
button2.place(x=150, y=110)

label1 = Label(window, text="Welcome", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Value", fg="blue", width=10, font=("arial", 12, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=100, y=80)

button1 = Button(window, text="Increment", fg="black", font=("arial", 12, "bold"), command=incr)
button1.place(x=40, y=110)


mainloop()
