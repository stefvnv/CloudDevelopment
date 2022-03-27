from tkinter import *

total_item_price = 0
total_shipping_price = 0
total_total_price = 0


def displayDialog(window, cart_list):
    """Creates the cart GUI"""

    window_cart = Toplevel(window)
    window_cart.geometry("1200x600")
    window_cart.title("Computerium - Cart")
    window_cart.config(bg="#303030")
    window_cart.resizable(False, False)
    parts = cart_list

    def displayHeadings():
        """Displays the headings in the text box"""

        text.config(state="normal")

        heading = "Name"
        heading += '\t\t\t\t' + "Company"
        heading += '\t\t' + "Part Price"
        heading += '\t\t' + "Shipping Price"
        heading += '\t\t' + "Total Price"
        heading += '\n'
        heading += '----------------------------------------------------------------------------------------------------------------------------------------------------------------\n'

        text.insert(END, heading)

        text.config(state="disabled")

    def displayParts():
        """Displays parts"""

        global total_item_price
        global total_shipping_price
        global total_total_price

        total_item_price = 0
        total_shipping_price = 0
        total_total_price = 0

        for part in parts:
            text.config(state="normal")
            line = part.readName()
            line += '\t\t\t\t' + part.readCompanyExt()
            line += '\t\t' + str(part.readPrice())
            total_item_price += int(part.readPrice())
            line += '\t\t' + part.readPriceExt()
            total_shipping_price += int(part.readPriceExt())
            tot = int(part.readPrice() + int(part.readPriceExt()))
            total_total_price += tot
            line += '\t\t' + str(tot)
            line += '\n'

            text.insert(END, line)

            text.config(state="disabled")

    def displayTotals():
        """Displays the total price of parts, shipping and their addition"""

        text.config(state="normal")

        global total_item_price
        global total_shipping_price
        global total_total_price
        tots = '----------------------------------------------------------------------------------------------------------------------------------------------------------------\n'
        tots += "Total:"
        tots += '\t\t\t\t' + "\t"
        tots += '\t€' + str(total_item_price)
        tots += '\t\t€' + str(total_shipping_price)
        tots += '\t\t€' + str(total_total_price)
        tots += '\n\n'

        text.insert(END, tots)

        text.config(state="disabled")

    def closeEvent():
        """Exits the GUI"""

        window_cart.destroy()

    # Close button
    button_exit = Button(window_cart, text="Exit", fg="black", bg="white", font=("Century Gothic", 12),
                         command=closeEvent)
    button_exit.place(x=600, y=550)

    # Text content
    text = Text(window_cart, undo=True, height=24, width=128, font=("Century Gothic", 12), state="disabled")
    text.place(x=20, y=20)

    displayHeadings()
    displayParts()
    displayTotals()
