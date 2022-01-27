from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Hotel Application")


def getprice():
    nights = int(entry2.get())
    guests = int(guestsVar.get())
    price = 50 * nights

    if var_checkbox1.get() > 0:
        price = price + (guests * 10 * nights)

    entry3.delete(0, END)
    entry3.insert(END, '€')
    entry3.insert(END, price)


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

#Title
label1 = Label(window, text="Hotel Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)

#Nights
label2 = Label(window, text="Nights", fg="blue", font=("arial", 12, "bold"))
label2.grid(row=0, column=0, sticky=W+E)

#Guests
label3 = Label(window, text="Guests", fg="blue", font=("arial", 12, "bold"))
label3.grid(row=1, column=0, sticky=W+E)

#Nights Textbox
entry2 = Entry(window)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W+E)

#Price Result
entry3 = Entry(window)
entry3.insert(END, '1')
entry3.grid(row=3, column=1, sticky=W+E)


#Get Price Button
button1 = Button(window, text="Get Price", fg="black", font=("arial", 12, "bold"), command=getprice)
button1.grid(row=3, column=0, sticky=W+E)


list1 = ['1', '2', '3', '4']
guestsVar = StringVar()
combo1 = OptionMenu(frame, guestsVar, *list1)
guestsVar.set("1")
combo1.grid(row=1, column=1, sticky=W+E)


#Breakfast Checkbox
var_checkbox1 = IntVar()
checkbox1 = Checkbutton(frame, text="Breakfast", variable=var_checkbox1)
checkbox1.grid(row=2, column=0, columnspan=2, sticky=W+E)
checkbox1.deselect()


mainloop()
