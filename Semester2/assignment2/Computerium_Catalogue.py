from tkinter import *
from Computerium_Classes import *


def display(window, part_list):
    window_catalogue = Toplevel(window)
    window_catalogue.geometry("1200x600")
    window_catalogue.title("Computerium Catalogue")
    parts = part_list

    # Event Handling Methods
    def displayParts():
        for product in parts:
            line = product.readType()

            # text.insert(END, line)

    def readType(self):
        return 'idk'

    def exitEvent():
        window_catalogue.destroy()

    # Close button
    button_close = Button(window_catalogue, text="Exit", fg="black", font=("arial", 12, "bold"), command=exitEvent)
    button_close.place()

    # Text content
    text = Text(window_catalogue, undo=True, height=36, width=150)
    text.place(x=20, y=60)

    displayParts()
