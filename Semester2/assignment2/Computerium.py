"""Computerium - PC Part Picker
    by Stefana Chiritescu"""

from tkinter import *

from Computerium_Classes import *
from Computerium_Catalogue import *

window = Tk()
window.geometry("500x700")
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

def nextCmd():
    global current
    if (current < (len(parts) - 1)):
        current += 1
        display(current)


def prevCmd():
    global current
    if (current > 0):
        current -= 1
        display(current)


def ext():
    """Exits the application"""
    exit()


'''Definitions'''

# CPUs
part_CPU1 = CPU("Intel Core i5-12600k", 340, "10 (6P + 4E) / 16", "3.7GHz", "4.9GHz")
part_CPU2 = CPU("AMD Ryzen 5 5600X", 350, "6/12", "4.1GHz", "4.8GHz")
#part_CPU3 = CPU("")
#part_CPU4 = CPU("")
#part_CPU5 = CPU("")

# CPU coolers
part_cooler1 = CPUCooler("EK-AIO Basic 240", 88, "240mm", "550-2200RPM", "Up to 33.5dB(A)")
part_cooler2 = CPUCooler("Deepcool Gammaxx L240 V2", 68, "240mm", "500–1800RPM", "Up to 30dB(A)")
#part_cooler3 = CPUCooler
#part_cooler4 = CPUCooler
#part_cooler5 = CPUCooler

parts = [part_CPU1, part_CPU2, part_cooler1, part_cooler2]
global current
global part

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
button_catalogue = Button(window, text="Browse Catalogue", width=22, height=1, fg="lightblue", bg="navy",
                     activebackground="gray", activeforeground="lightgrey", font=("Century Gothic", 12),
                     command=lambda: display(window, parts))
button_catalogue_window = canvas.create_window(250, 200, window=button_catalogue)

# Part Type text
canvas.create_text(230, 280, text="Part Type", anchor="e", font=("Century Gothic", 16), fill="#000000")


# Part Type combobox
list_type = ["CPU", "CPU Cooler"]
type = StringVar()
combo_type = OptionMenu(window, type, *list_type)
type.set("CPU")
combo_type.config(fg="white", bg="black", font=("Century Gothic", 12))
# combo_type["menu"].config(fg="navy", font=("Cambria", 10))
combo_type_window = canvas.create_window(250, 280, anchor="w", window=combo_type)

# Name label


# Name entry box










display(0)

mainloop()
