from tkinter import *
from Computerium_Classes import *

total_item_price = 0
total_shipping_price = 0
total_total_price = 0


def displayDialog(window, cart_list):
    window_cart = Toplevel(window)
    window_cart.geometry("1200x600")
    window_cart.title("Computerium - Cart")
    parts = cart_list

    # Event Handling Methods
    def displayHeadings():
        heading = "Name"
        heading += '\t\t\t\t' + "Company"
        heading += '\t\t' + "Item Price"
        heading += '\t\t' + "Shipping Price"
        heading += '\t\t' + "Total Price"
        heading += '\n\n'

        text.insert(END, heading)

    def displayParts():
        global total_item_price
        global total_shipping_price
        global total_total_price

        for part in parts:
            line = part.readName()
            line += '\t\t\t\t' + part.readCompanyExt()
            line += '\t\t' + str(part.readPrice())
            total_item_price += int(part.readPrice())
            line += '\t\t' + part.readPriceExt()
            total_shipping_price += int(part.readPriceExt())
            tot = int(part.readPrice() + int(part.readPriceExt()))
            total_total_price += tot
            line += '\t\t' + str(tot)
            line += '\n\n'

            text.insert(END, line)

    def displayTotals():
        global total_item_price
        global total_shipping_price
        global total_total_price
        tots = "Total:"
        tots += '\t\t\t\t' + "\t"
        tots += '\t' + str(total_item_price)
        tots += '\t\t' + str(total_shipping_price)
        tots += '\t\t' + str(total_total_price)
        tots += '\n\n'

        text.insert(END, tots)


    def emptyEvent():


    def exitEvent():
        window_cart.destroy()

    # Empty button
    button_empty = Button(window_cart, text="Empty Cart", fg="black", font=("Century Gothic", 12), command=emptyEvent)
    button_empty.place(x=1100, y=400)


    # Exit button
    button_exit = Button(window_cart, text="Exit", fg="black", font=("Century Gothic", 12), command=exitEvent)
    button_exit.place(x=1100, y=600)

    # Text content
    text = Text(window_cart, undo=True, height=32, width=145)
    text.place(x=20, y=20)

    displayHeadings()
    displayParts()
    displayTotals()
