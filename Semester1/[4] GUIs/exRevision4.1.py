from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


def getQuote():
    type = str(typeVar.get())
    days = int(daysVar.get())
    passengers = int(passVar.get())

    basePrice = 50
    if type == 'Medium':
        basePrice = 70
    if type == 'Large':
        basePrice = 90
    if passengers > 5:
        basePrice = 120

    quote = basePrice * days

    if var_cb1.get() > 0:
        quote = quote + (days * 10)

    if var_cb2.get() > 0:
        quote = quote + (days * 5)

    entry3.delete(0, END)
    entry3.insert(END, '€')
    entry3.insert(END, quote)


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Car Loan Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)  # place on screen

label2 = Label(frame, text="Car Type", fg="blue", width=15, font=("arial", 10, "bold"))  #
label2.grid(row=0, column=0, sticky=W + E)

list0 = ['Small', 'Medium', 'Large']
typeVar = StringVar()
combo0 = OptionMenu(frame, typeVar, *list0)
typeVar.set("Medium")
combo0.grid(row=0, column=1, sticky=W + E)

label3 = Label(frame, text="Days", fg="blue", width=15, font=("arial", 10, "bold"))  #
label3.grid(row=1, column=0, sticky=W + E)

label4 = Label(frame, text="Passengers", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4.grid(row=2, column=0, sticky=W + E)

list1 = ['1', '2', '3', '4', '5', '6']
daysVar = StringVar()
combo1 = OptionMenu(frame, daysVar, *list1)
daysVar.set("1")
combo1.grid(row=1, column=1, sticky=W + E)

# --------------------------------
# new Combo Goes Here   Passengers    if (passengers>5)    20 extra per day
# ------------------------------------
list2 = ['1', '2', '3', '4', '5', '6', '7']
passVar = StringVar()
combo2 = OptionMenu(frame, passVar, *list2)
passVar.set("1")
combo2.grid(row=2, column=1, sticky=W + E)

var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Insurance", variable=var_cb1)
cb1.grid(row=3, column=0, columnspan=2)
cb1.deselect()

# --------------------------------
# new CheckBox here SatNav                 5 extra per day
# ------------------------------------
var_cb2 = IntVar()
cb2 = Checkbutton(frame, text="SatNav", variable=var_cb2)
cb2.grid(row=4, column=0, columnspan=2)
cb2.deselect()

button1 = Button(frame, text="GetPrice", fg="black", font=("arial", 8, "bold"), command=getQuote)
button1.grid(row=5, column=0, sticky=W + E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=5, column=1, sticky=W + E)

mainloop()
