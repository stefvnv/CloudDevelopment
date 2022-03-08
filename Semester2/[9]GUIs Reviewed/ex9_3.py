from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.title("Welcome")


def getQuote():
    days = int(daysVar.get())
    quote = 50 * days

    seats = int(seatsVar.get())

    if seats == 7:
        quote = 70 * days
    elif seats == 9:
        quote = 80 * days

    if var_cb1.get() > 0:
        quote = quote + (10 * days)

    if var_cb2.get() > 0:
        quote = quote + (15 * days)

    entry3.delete(0, END)
    entry3.insert(END, '€')
    entry3.insert(END, quote)


# Menu methods
def clear():
    daysVar.set("1")
    seatsVar.set("5")

    cb1.deselect()
    cb2.deselect()

    entry3.delete(0, END)
    entry3.insert(END, '')


def help():
    messagebox.showinfo("Car Hire", "From €50 per day for 5 seater\n\nSat Nav Optional -€10 per day\n\nInsurance "
                                    "Option -€15 per day")


# Menu
menu1 = Menu(window)
window.config(menu=menu1)

subm1 = Menu(menu1)
menu1.add_cascade(label="Options", menu=subm1)
subm1.add_command(label="Clear", command=clear)
subm1.add_command(label="Help", command=help)

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Car Hire Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)

label2 = Label(frame, text="No of Days", fg="blue", width=15, font=("arial", 10, "bold"))
label2.grid(row=0, column=0, sticky=W + E)

label3 = Label(frame, text="Seats", fg="blue", width=15, font=("arial", 10, "bold"))
label3.grid(row=1, column=0, sticky=W + E)

list0 = ['1', '2', '3', '4', '5', '6', '7']
daysVar = StringVar()
combo0 = OptionMenu(frame, daysVar, *list0)
daysVar.set("1")
combo0.grid(row=0, column=1, sticky=W + E)

list1 = ['5', '7', '9']
seatsVar = StringVar()
combo1 = OptionMenu(frame, seatsVar, *list1)
seatsVar.set("5")
combo1.grid(row=1, column=1, sticky=W + E)

var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Sat Nav", variable=var_cb1)
cb1.grid(row=2, column=0, columnspan=2)
cb1.deselect()

var_cb2 = IntVar()  # 0 unchecked, 1 checked
cb2 = Checkbutton(frame, text="Insurance", variable=var_cb2)
cb2.grid(row=3, column=0, columnspan=2)
cb2.deselect()

button1 = Button(frame, text="GetQuote", fg="black", font=("arial", 8, "bold"), command=getQuote)
button1.grid(row=4, column=0, sticky=W + E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=4, column=1, sticky=W + E)

mainloop()
