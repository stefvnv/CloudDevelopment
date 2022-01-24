from tkinter import *
from ex3_5Class import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


# ============================================================
# Event Handling Methods

def display(index):
    global current
    global product
    product = productlist[index]
    current = index
    entry2.delete(0, END)
    entry2.insert(END, product.getMake())
    entry3.delete(0, END)
    entry3.insert(END, product.getModel())
    entry4.delete(0, END)
    entry4.insert(END, product.getPrice())
    entry5.delete(0, END)
    entry5.insert(END, product.readType())
    entry6.delete(0, END)
    entry6.insert(END, product.readDescription())


def nextCmd():
    global current
    if current < (len(productlist) - 1):
        current += 1
        display(current)


def prevCmd():
    global current
    if current > 0:
        current -= 1
        display(current)


def firstCmd():
    display(0)


def lastCmd():
    display(len(productlist) - 1)


def clearData():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


# End of Method Declarations
# ========================================================================


# Definitions
# =====================================================================
product1 = Car("VW", "Golf", 20000, 1400)
product2 = TV("SAMSUNG", "QE55QN95AATXXU", 1894, 55)
product3 = Laptop("HP", "Chromebook", 399, 14)
product4 = Laptop("Lenovo", "IdeaPad", 299, 11.5)
product5 = Car("VW", "Golf", 20000, 1400)
product6 = TV("JVC", "LT-55CF890", 699, 55)

productlist = [product1, product2, product3, product4, product5, product6]
global current  # current product
global product
product = productlist[0]  # initialize to first product

# ========= End of Definitions ============================

# =======================================================


# ======= End of Menu Definition ============================

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

label1 = Label(window, text="Product example", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)  # place on screen

label2 = Label(frame, text="Make", fg="blue", width=15, font=("arial", 10, "bold"))  #
label2.grid(row=0, column=0, sticky=W + E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W + E)

label3 = Label(frame, text="Model", fg="blue", width=15, font=("arial", 10, "bold"))  #
label3.grid(row=1, column=0, sticky=W + E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W + E)

label4 = Label(frame, text="Price", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4.grid(row=2, column=0, sticky=W + E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W + E)

label5 = Label(frame, text="Type", fg="blue", width=15, font=("arial", 10, "bold"))  #
label5.grid(row=3, column=0, sticky=W + E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=3, column=1, sticky=W + E)

label6 = Label(frame, text="Description", fg="blue", width=15, font=("arial", 10, "bold"))  #
label6.grid(row=4, column=0, sticky=W + E)

entry6 = Entry(frame)
entry6.insert(END, '0')
entry6.grid(row=4, column=1, sticky=W + E)

button5 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button5.grid(row=10, column=0, sticky=W + E)

button6 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button6.grid(row=10, column=1, sticky=W + E)

button7 = Button(frame, text="First", fg="black", font=("arial", 10, "bold"), command=firstCmd)
button7.grid(row=11, column=0, sticky=W + E)

button8 = Button(frame, text="Last", fg="black", font=("arial", 10, "bold"), command=lastCmd)
button8.grid(row=11, column=1, sticky=W + E)

display(0)

mainloop()
