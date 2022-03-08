from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")
from ex9_4Sub import *

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Dialog example", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)

label2 = Label(frame, text="Options", fg="blue", width=15, font=("arial", 10, "bold"))
label2.grid(row=0, column=0, sticky=W + E)

button5 = Button(frame, text="AddDialog", fg="black", font=("arial", 10, "bold"), command=lambda: addDialog(window))
button5.grid(row=1, column=0, sticky=W + E)

button6 = Button(frame, text="SubDialog", fg="black", font=("arial", 10, "bold"), command=lambda: subDialog(window))
button6.grid(row=2, column=0, sticky=W + E)

mainloop()
