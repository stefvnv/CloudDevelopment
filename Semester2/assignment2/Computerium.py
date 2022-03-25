"""Computerium - PC Part Picker
    by Stefana Chiritescu"""

from tkinter import *
from tkinter import messagebox
from pygame import mixer

from Computerium_Classes import *
from Computerium_Cart import *

mixer.init()
window = Tk()
window.geometry("500x700")
window.title("Computerium")
window.resizable(False, False)

background = PhotoImage(file="background.png")

'''Definitions'''

# CPUs
part_CPU1 = CPU("Intel Core i5-12600k", 340, "Ireland", "", "10 (6P + 4E) / 16", "3.7GHz", "4.9GHz")
part_CPU2 = CPU("AMD Ryzen 5 5600X", 350, "Germany", "", "6/12", "4.1GHz", "4.8GHz")
part_CPU3 = CPU("Intel Core i9-12900k", 690, "United Kingdom", "", "16 (8P + 8E) / 24", "3.2GHz", "5.2GHz")
part_CPU4 = CPU("AMD Ryzen 9 5950X", 820, "Ireland", "", "16/32", "3.4GHz", "4.9GHz")
part_CPU5 = CPU("Intel Core i7-12700K", 450, "Poland", "", "12 (8P+4E) / 20", "3.6GHz", "4.9GHz")

# CPU coolers
part_cooler1 = CPUCooler("EK-AIO Basic 240", 88, "United Kingdom", "", "240mm", "550-2200RPM", "Up to 33.5dB(A)")
part_cooler2 = CPUCooler("Deepcool Gammaxx L240 V2", 68, "Ireland", "", "240mm", "500–1800RPM", "Up to 30dB(A)")
part_cooler3 = CPUCooler("Corsair Hydro Series H60 V2", 78, "Spain", "", "120mm", "Up to 1700RPM", "Up to 28.3dB(A)")
part_cooler4 = CPUCooler("Deepcool AS500 Plus", 70, "Poland", "", "2x 140mm", "500–1200RPM", "Up to 31.5dB(A)")
part_cooler5 = CPUCooler("Be Quiet! Pure Rock 2", 55, "Ireland", "", "1x Pure Wings 2 120mm", "Up to 1500RPM", "Up to "
                                                                                                               "26"
                                                                                                               ".8dB("
                                                                                                               "A)")

# Motherboards
part_motherboard1 = Motherboard("Gigabyte Z690 Aorus Pro", 360, "Spain", "", "LGA 1700", "Intel Z690", "ATX")
part_motherboard2 = Motherboard("MSI MEG Z690I Unify", 444, "Poland", "", "LGA 1700", "Intel Z690", "Mini-ITX")
part_motherboard3 = Motherboard("MSI MAG B660M Mortar WIFI DDR4", 220, "Ireland", "", "LGA 1700", "Intel B660", "mATX")
part_motherboard4 = Motherboard("Asus ROG Maximus XIII Hero", 570, "Portugal", "", "LGA 1200", "Intel Z590", "ATX")
part_motherboard5 = Motherboard("Gigabyte X299X Designare 10G", 680, "Poland", "", "LGA 2066", "Intel X299 PCH", "EATX")

# Memory
part_memory1 = Memory("Corsair Vengeance LED", 95, "Spain", "", "DDR4", "6GB Kit (2 x 8GB)", "3200MHz")
part_memory2 = Memory("G.Skill Trident Z RGB", 230, "Portugal", "", "DDR4", "16GB (2x8GB)", "3200MHz")
part_memory3 = Memory("Kingston HyperX Predator", 160, "Ireland", "", "DDR4", "8GB, 16GB", "up to 4600MHz")
part_memory4 = Memory("Kingston HyperX Fury", 115, "Spain", "", "DDR4", "4GB, 8GB, 16GB, 32GB", "up to 3733MHz")
part_memory5 = Memory("Corsair Dominator Platinum RGB", 125, "United Kingdom", "", "DDR4", "16GB (2 x 8GB)", "3000MHz")

# Storage
part_storage1 = Storage("Samsung 980 Pro", 230, "United Kingdom", "", "250GB, 500GB, 1TB, 2TB", "M.2 2280 Single-sided",
                        "7,000 MBps / 5,000 MBps")
part_storage2 = Storage("Kingston KC3000", 245, "Portugal", "", "512GB, 1TB, 2TB, 4TB", "M.2 2280 Double-sided",
                        "7,000 MBps / 7,000 MBps")
part_storage3 = Storage("WD Black SN850", 110, "United Kingdom", "", "250GB, 500GB, 1TB, 2TB", "M.2 2280 Single-sided",
                        "7,000 MBps / 5,300 MBps")
part_storage4 = Storage("Crucial P5 Plus", 125, "Ireland", "", "500GB, 1TB, and 2TB", "M.2 2280 Single-sided",
                        "Up to 6,600 MBps / 5,000 MBps")
part_storage5 = Storage("Sabrent Rocket 4 Plus", 135, "United Kingdom", "", "1TB, 2TB, 4TB", "M.2 2280 Double-sided",
                        "7,200 MBps / 6,900 MBps")

# Video cards
part_graphics1 = Graphics("Nvidia GeForce RTX 3080", 1150, "Germany", "", "1,440MHz", "1,710MHz", "10GB GDDR6X")
part_graphics2 = Graphics("AMD Radeon RX 6800 XT", 1440, "Ireland", "", "1,825MHz", "2,250MHz", "16GB GDDR6")
part_graphics3 = Graphics("Nvidia GeForce RTX 3060 Ti", 630, "United Kingdom", "", "1,410MHz", "1,665MHz", "8GB GDDR6")
part_graphics4 = Graphics("Nvidia GeForce RTX 3070", 705, "Germany", "", "1,500MHz", "1,725MHz", "8GB GDDR6")
part_graphics5 = Graphics("AMD Radeon RX 6900 XT", 1710, "Spain", "", "1,825MHz", "2,250MHz", "16GB GDDR6")

cpus = [part_CPU1, part_CPU2, part_CPU3, part_CPU4, part_CPU5]
coolers = [part_cooler1, part_cooler2, part_cooler3, part_cooler4, part_cooler5]
motherboards = [part_motherboard1, part_motherboard2, part_motherboard3, part_motherboard4, part_motherboard5]
memory = [part_memory1, part_memory2, part_memory3, part_memory4, part_memory5]
storage = [part_storage1, part_storage2, part_storage3, part_storage4, part_storage5]
graphics = [part_graphics1, part_graphics2, part_graphics3, part_graphics4, part_graphics5]

parts = cpus
cart_list = []

global current
global part

'''Event Handling Methods'''


def displayChange():
    global current
    display(current)


def changeType(*args):
    """Changes parts array to relevant part on option menu click"""

    global parts

    if type.get() == "CPU":
        parts = cpus

    if type.get() == "CPU Cooler":
        parts = coolers

    if type.get() == "CPU Cooler":
        parts = coolers

    if type.get() == "Motherboard":
        parts = motherboards

    if type.get() == "Memory":
        parts = memory

    if type.get() == "Storage":
        parts = storage

    if type.get() == "Graphics Card":
        parts = graphics

    radioChange()
    display(0)


def display(index):
    global current
    global part

    part = parts[index]
    current = index

    entry_name.delete(0, END)
    entry_name.insert(END, part.readName())

    entry_desc1.delete(0, END)
    entry_desc1.insert(END, part.readDesc1())

    entry_desc2.delete(0, END)
    entry_desc2.insert(END, part.readDesc2())

    entry_desc3.delete(0, END)
    entry_desc3.insert(END, part.readDesc3())

    entry_price.delete(0, END)
    entry_price.insert(END, part.readPrice())


def radioChange():
    global parts
    global part

    if rb.get() == 1:
        parts[current].setCompanyExt("DHL")
    elif rb.get() == 2:
        parts[current].setCompanyExt("UPS")
    elif rb.get() == 3:
        parts[current].setCompanyExt("FedEx")


def prevCmd():
    global current

    if current > 0:
        current -= 1
        display(current)

        # Play sound on click
        mixer.music.load("click.wav")
        mixer.music.play()


def nextCmd():
    global current

    if current < (len(parts) - 1):
        current += 1
        display(current)

        # Play sound on click
        mixer.music.load("click.wav")
        mixer.music.play()


# Menu methods
def addCmd():
    global current
    global parts
    global cart_list
    cart_list.append(parts[current])

    messagebox.showinfo("Notification", type.get() + " added to cart successfully.")


def clearCmd():
    global cart_list
    del cart_list[:]

    messagebox.showinfo("Notification", "Cart emptied successfully.")


def ext():
    """Exits the application"""
    exit()


'''GUI'''
# MENU
menu = Menu(window)
window.config(menu=menu)

sub_options = Menu(menu)
menu.add_cascade(label="Cart", menu=sub_options)
sub_options.add_command(label="View Cart", command=lambda: displayDialog(window, cart_list))
sub_options.add_command(label="Clear Cart", command=clearCmd)
sub_options.add_command(label="Exit", command=ext)

# CANVAS
canvas = Canvas(window, width=500, height=700, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Set Image in Canvas
canvas.create_image(0, 0, image=background, anchor="nw")

# Title
canvas.create_text(250, 40, text="COMPUTERIUM", font=("Haettenschweiler", 32), fill="grey")

# Description
canvas.create_text(250, 70, text="PC Part Picker", font=("Century Gothic", 21, "bold"), fill="black")

# Part Type text
canvas.create_text(200, 160, text="Part Type", anchor="e", font=("Century Gothic", 16), fill="#000000")

# Part Type combobox
list_type = ["CPU", "CPU Cooler", "Motherboard", "Memory", "Storage", "Graphics Card"]
type = StringVar()
combo_type = OptionMenu(window, type, *list_type, command=changeType)
type.set("CPU")
combo_type.config(fg="white", bg="black", font=("Century Gothic", 12))
combo_type["menu"].config(fg="navy", font=("Century Gothic", 12))
combo_type_window = canvas.create_window(220, 160, anchor="w", window=combo_type)

# Name text
canvas.create_text(200, 200, text="Name", anchor="e", font=("Century Gothic", 16), fill="black")

# Name entry box
entry_name = Entry(window, width=24, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_name.focus_set()
entry_name_window = canvas.create_window(220, 200, anchor="w", window=entry_name)

# Select shipping type text
canvas.create_text(100, 260, text="Select shipping method:", anchor="w", font=("Century Gothic", 16), fill="black")

# DHL, UPS, FedEx radiobutton
rb = IntVar()
rb.set(1)

rb_dhl = Radiobutton(window, text="DHL", font=("Century Gothic", 12), background="white", variable=rb, value=1, command=radioChange)
rb_dhl_window = canvas.create_window(200, 300, anchor="e", window=rb_dhl)

rb_ups = Radiobutton(window, text="UPS", font=("Century Gothic", 12), background="white", variable=rb, value=2, command=radioChange)
rb_ups_window = canvas.create_window(270, 300, anchor="e", window=rb_ups)

rb_fed = Radiobutton(window, text="FedEx", font=("Century Gothic", 12), background="white", variable=rb, value=3, command=radioChange)
rb_fed_window = canvas.create_window(350, 300, anchor="e", window=rb_fed)

# Descriptions text
canvas.create_text(230, 340, text="Product Details", anchor="e", font=("Century Gothic", 16), fill="black")

# Description1 entry box
entry_desc1 = Entry(window, width=36, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_desc1_window = canvas.create_window(400, 380, anchor="e", window=entry_desc1)

# Description2 entry box
entry_desc2 = Entry(window, width=36, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_desc2_window = canvas.create_window(400, 420, anchor="e", window=entry_desc2)

# Description3 entry box
entry_desc3 = Entry(window, width=36, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_desc3_window = canvas.create_window(400, 460, anchor="e", window=entry_desc3)

# Price text
canvas.create_text(100, 500, text="Price", anchor="e", font=("Century Gothic", 16), fill="black")

# Price entry box
entry_price = Entry(window, width=10, fg="navy", bg="lightblue", font=("Century Gothic", 12))
entry_price_window = canvas.create_window(200, 500, anchor="e", window=entry_price)

# Add BUTTON
button_add = Button(window, text="Add to cart", width=12, height=1, fg="lightblue", bg="navy",
                    activebackground="blue", activeforeground="lightblue", font=("Century Gothic", 12),
                    command=addCmd)
button_add_window = canvas.create_window(300, 500, window=button_add)

# Previous BUTTON
button_prev = Button(window, text="Previous", width=12, height=1, fg="lightblue", bg="navy",
                     activebackground="blue", activeforeground="lightblue", font=("Century Gothic", 12),
                     command=prevCmd)
button_prev_window = canvas.create_window(170, 620, window=button_prev)

# Next BUTTON
button_next = Button(window, text="Next", width=12, height=1, fg="lightblue", bg="navy",
                     activebackground="blue", activeforeground="lightblue", font=("Century Gothic", 12),
                     command=nextCmd)
button_next_window = canvas.create_window(330, 620, window=button_next)


display(0)
radioChange()
mainloop()
