"""Computerium - PC Part Picker
    by Stefana Chiritescu"""

from tkinter import *

from Computerium_Classes import *
from Computerium_Catalogue import *

window = Tk()
window.geometry("600x700")
window.title("Computerium")


# Event Handling Methods
def displayChange():
    global current
    display(current)


def display(index):
    global current
    global product
    part = parts[index]
    current = index


def start_over():
    """Clears data from all entry fields, unchecks checkbox and sets combo boxes to first (default) values"""


def ext():
    """Exits the application"""
    exit()


'''Definitions'''
part_CPU1 = CPU
part_CPU2 = CPU
part_CPU3 = CPU
part_CPU4 = CPU
part_CPU5 = CPU

part_cooler1 = cooler
part_cooler2 = cooler
part_cooler3 = cooler
part_cooler4 = cooler
part_cooler5 = cooler



part = parts[0]


'''GUI'''
# Menu
menu = Menu(window)
window.config(menu=menu)

sub_options = Menu(menu)
menu.add_cascade(label="Options", menu=sub_options)
sub_options.add_command(label="Start Over", command=start_over)
sub_options.add_command(label="Exit", command=ext)

# CANVAS
canvas = Canvas(window, width=600, height=700, highlightthickness=0)
canvas.pack(fill="both", expand=True)

#Set Image in Canvas
#canvas.create_image(0, 0, image=background, anchor="nw")

# Title
canvas.create_text(250, 60, text="COMPUTERIUM", font=("Century Gothic", 21, "bold"), fill="black")

# Description
canvas.create_text(250, 100, text="PC Part Picker", font=("Century Gothic", 21, "bold"), fill="black")

# Catalogue button
button_catalogue = Button(window, text="Previous User", width=12, height=1, fg="lightblue", bg="navy",
                     activebackground="blue", activeforeground="lightblue", font=("Haettenschweiler", 12),
                     command=lambda: display(window, parts))
button_catalogue_window = canvas.create_window(170, 520, window=button_catalogue)









display(0)

mainloop()
