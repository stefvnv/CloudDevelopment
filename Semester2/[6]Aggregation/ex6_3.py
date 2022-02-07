from tkinter import *

window = Tk()
window.geometry("300x340")
window.title("Welcome")

from ex6_3Class import *


# ------------end of class definition------------------

def display():
    value1 = t1.readTitle()
    value2 = t1.readAuthor()
    value3 = t1.readPrice()
    value4 = t1.readDelivery()
    value5 = t1.totalCost()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, value4)
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, value5)


def incrYearEvent():
    t1.incrementYear()
    display()


def setPriceEvent():
    newPrice = entry4b.get()
    list = newPrice.split(".")
    euro = list[0]
    euro = euro.lstrip('€')
    cent = list[1]
    t1.updatePrice(int(euro), int(cent))
    display()


def setDeliveryEvent():
    newDelivery = entry5b.get()
    list = newDelivery.split(".")
    euro = list[0]
    euro = euro.lstrip('€')
    cent = list[1]
    t1.updateDelivery(int(euro), int(cent))
    display()


def exitEvent():
    quit()


def setTitleEvent():
    newTitle = entry3b.get()
    t1.updateTitle(newTitle)
    display()


t1 = Book("Database Intro", "T.Jones", 21, 26, 2, 30)

label1 = Label(window, text="Book Details", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=40, y=30)  # place on screen

label2 = Label(window, text="Author", fg="blue", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Price", fg="blue", width=12, font=("arial", 10, "bold"))  #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Price", fg="blue", width=8, font=("arial", 10, "bold"))  #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

label5 = Label(window, text="Delivery", fg="blue", width=12, font=("arial", 10, "bold"))  #
label5.place(x=10, y=170)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=170)

label6 = Label(window, text="TotalCost", fg="blue", width=12, font=("arial", 10, "bold"))  #
label6.place(x=10, y=200)

entry6 = Entry(window)
entry6.insert(END, '1')
entry6.place(x=120, y=200)

# -------------------------------


button3 = Button(window, text="updateTitle", fg="black", font=("arial", 10, "bold"), command=setTitleEvent)
button3.place(x=40, y=240)

entry3b = Entry(window)
entry3b.insert(END, 'Basic Python')
entry3b.place(x=150, y=240)

button4 = Button(window, text="updatePrice", fg="black", font=("arial", 10, "bold"), command=setPriceEvent)
button4.place(x=40, y=270)

entry4b = Entry(window)
entry4b.insert(END, '€22.48')
entry4b.place(x=150, y=270)

button5 = Button(window, text="updateDelivery", fg="black", font=("arial", 10, "bold"), command=setDeliveryEvent)
button5.place(x=40, y=300)

entry5b = Entry(window)
entry5b.insert(END, '€3.67')
entry5b.place(x=150, y=300)

display()

mainloop()
