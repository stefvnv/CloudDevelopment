"""Computerium - PC Part Picker
    by Stefana Chiritescu"""

# from tkinter import *
import tkinter as tk
from Computerium_Classes import *
from Computerium_Catalogue import *

window = Tk()

window.geometry("500x700")
window.title("Computerium")

'''Definitions'''

# CPUs
part_CPU1 = CPU("Intel Core i5-12600k", 340, "10 (6P + 4E) / 16", "3.7GHz", "4.9GHz")
part_CPU2 = CPU("AMD Ryzen 5 5600X", 350, "6/12", "4.1GHz", "4.8GHz")
# part_CPU3 = CPU("")
# part_CPU4 = CPU("")
# part_CPU5 = CPU("")

# CPU coolers
part_cooler1 = CPUCooler("EK-AIO Basic 240", 88, "240mm", "550-2200RPM", "Up to 33.5dB(A)")
part_cooler2 = CPUCooler("Deepcool Gammaxx L240 V2", 68, "240mm", "500–1800RPM", "Up to 30dB(A)")
# part_cooler3 = CPUCooler
# part_cooler4 = CPUCooler
# part_cooler5 = CPUCooler

cpus = [part_CPU1, part_CPU2]
coolers = [part_cooler1, part_cooler2]

parts = cpus

# parts = [part_CPU1, part_CPU2, part_cooler1, part_cooler2]
global current
global part

part = parts[0]

'''Event Handling Methods'''


def displayChange():
    global current
    display(current)


def changeType(*args):
    global parts

    if type.get() == "CPU":
        parts = cpus
        print("hey")

    if type.get() == "CPU Cooler":
        print("omg")
        parts = coolers


def display(index):
    global current
    global part
    part = parts[index]
    current = index

    # Option Menu
    changeType()

    entry_name.delete(0, END)
    entry_name.insert(END, part.readName())

    entry_desc1.delete(0, END)
    entry_desc1.insert(END, part.readDesc1())

    entry_desc2.delete(0, END)
    entry_desc2.insert(END, part.readDesc2())

    entry_desc3.delete(0, END)
    entry_desc3.insert(END, part.readDesc3())


def start_over():
    """Clears data from all entry fields, unchecks checkbox and sets combo boxes to first (default) values"""


def nextCmd():
    global current

    if current < (len(parts) - 1):
        current += 1
        display(current)


def prevCmd():
    global current

    if current > 0:
        current -= 1
        display(current)


def ext():
    """Exits the application"""
    exit()


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

# Set Image in Canvas
# canvas.create_image(0, 0, image=background, anchor="nw")


# Title
canvas.create_text(250, 40, text="COMPUTERIUM", font=("Haettenschweiler", 32), fill="grey")

# Description
canvas.create_text(250, 70, text="PC Part Picker", font=("Century Gothic", 21, "bold"), fill="black")

# Catalogue button
button_catalogue = Button(window, text="Browse Catalogue", width=22, height=1, fg="lightblue", bg="navy",
                          activebackground="gray", activeforeground="lightgrey", font=("Century Gothic", 12),
                          command=lambda: display(window, parts))
button_catalogue_window = canvas.create_window(250, 140, window=button_catalogue)

# Part Type text
canvas.create_text(230, 220, text="Part Type", anchor="e", font=("Century Gothic", 16), fill="#000000")

# Part Type combobox
list_type = ["CPU", "CPU Cooler"]
type = StringVar()
combo_type = OptionMenu(window, type, *list_type, command=changeType)

type.set("CPU")
combo_type.config(fg="white", bg="black", font=("Century Gothic", 12))
combo_type_window = canvas.create_window(250, 220, anchor="w", window=combo_type)

# Name text
canvas.create_text(230, 260, text="Name", anchor="e", font=("Century Gothic", 16), fill="black")

# Name entry box
entry_name = Entry(window, width=16, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_name.focus_set()
entry_name_window = canvas.create_window(250, 260, anchor="w", window=entry_name)

# Descriptions text
canvas.create_text(230, 300, text="Product Details", anchor="e", font=("Century Gothic", 16), fill="black")

# Description1 entry box
entry_desc1 = Entry(window, width=34, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_desc1_window = canvas.create_window(400, 340, anchor="e", window=entry_desc1)

# Description2 entry box
entry_desc2 = Entry(window, width=34, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_desc2_window = canvas.create_window(400, 380, anchor="e", window=entry_desc2)

# Description3 entry box
entry_desc3 = Entry(window, width=34, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_desc3_window = canvas.create_window(400, 420, anchor="e", window=entry_desc3)

# Previous BUTTON
button_prev = Button(window, text="Previous", width=12, height=1, fg="lightblue", bg="navy",
                     activebackground="blue", activeforeground="lightblue", font=("Century Gothic", 12),
                     command=prevCmd)
button_prev_window = canvas.create_window(170, 520, window=button_prev)

# Next BUTTON
button_next = Button(window, text="Next", width=12, height=1, fg="lightblue", bg="navy",
                     activebackground="blue", activeforeground="lightblue", font=("Century Gothic", 12),
                     command=nextCmd)
button_next_window = canvas.create_window(330, 520, window=button_next)

display(0)

mainloop()
