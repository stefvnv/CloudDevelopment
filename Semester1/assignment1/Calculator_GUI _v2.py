from tkinter import *

from Ass_Student import Student

window = Tk()
window.geometry("500x600")
window.title("Zodiac Sign Calculator")
window.resizable(False, False)
background = PhotoImage(file="background.png")


# Event Handling Methods
def display(index):
    global current
    global student
    student = studentlist[index]
    current = index
    # entry1.delete(0, END)
    # entry1.insert(END, student.getName())


def nextCmd():
    global current
    if current < (len(studentlist) - 1):
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
    display(len(studentlist) - 1)


def clearData():
    entry1.delete(0, END)
    entry1.focus_set()
    entry2.delete(0, END)

    days.set("1")
    months.set("January")

    cb.deselect()

    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.config(state="disabled")

    entry4.config(state="normal")
    entry4.delete(0, END)
    entry4.config(state="disabled")


def ext():
    exit()


def checker():
    if cbVar.get() > 0:
        entry2.config(state="normal")
    else:
        entry2.config(state="disabled")


def validateE(P):
    if len(P) <= 4:
        return True
    else:
        return False

    
vcmd = window.register(validateE)


# Calculate Method
def calculate():
    # Astrological Zodiac Sign
    day = int(days.get())
    month = months.get()

    entry3.config(state="normal")

    if month == "December":
        sign = "Sagittarius" if (day < 22) else "Capricorn"

    elif month == "January":
        sign = "Capricorn" if (day < 20) else "Aquarius"

    elif month == "February":
        sign = "Aquarius" if (day < 19) else "Pisces"

    elif month == "March":
        sign = "Pisces" if (day < 21) else "Aries"

    elif month == "April":
        sign = "Aries" if (day < 20) else "Taurus"

    elif month == "May":
        sign = "Taurus" if (day < 21) else "Gemini"

    elif month == "June":
        sign = "Gemini" if (day < 21) else "Cancer"

    elif month == "July":
        sign = "Cancer" if (day < 23) else "Leo"

    elif month == "August":
        sign = "Leo" if (day < 23) else "Virgo"

    elif month == "September":
        sign = "Virgo" if (day < 23) else "Libra"

    elif month == "October":
        sign = "Libra" if (day < 23) else "Scorpio"

    elif month == "November":
        sign = "Scorpio" if (day < 22) else "Sagittarius"

    entry3.delete(0, END)
    entry3.insert(END, sign)
    entry3.config(state="disabled")

    # Chinese Zodiac Sign
    sign2 = ""

    if cbVar.get() > 0:
        year = int(entry2.get())

        entry4.config(state="normal")

        if (year - 2000) % 12 == 0:
            sign2 = "Dragon"

        elif (year - 2000) % 12 == 1:
            sign2 = "Snake"

        elif (year - 2000) % 12 == 2:
            sign2 = "Horse"

        elif (year - 2000) % 12 == 3:
            sign2 = "Sheep"

        elif (year - 2000) % 12 == 4:
            sign2 = "Monkey"

        elif (year - 2000) % 12 == 5:
            sign2 = "Rooster"

        elif (year - 2000) % 12 == 6:
            sign2 = "Dog"

        elif (year - 2000) % 12 == 7:
            sign2 = "Pig"

        elif (year - 2000) % 12 == 8:
            sign2 = "Rat"

        elif (year - 2000) % 12 == 9:
            sign2 = "Ox"

        elif (year - 2000) % 12 == 10:
            sign2 = "Tiger"

        else:
            sign2 = "Hare"

    else:
        entry4.config(state="disabled")

    entry4.delete(0, END)
    entry4.insert(END, sign2)
    entry4.config(state="disabled")


# Definitions
student1 = Student("J.Smith", "A003451245", False)
student2 = Student("L.Shine", "A003478344", True)
student3 = Student("M.Jones", "A003499123", False)
student4 = Student("T.Lennon", "A003468812", True)
student5 = Student("H.Green", "A003462194", False)

studentlist = [student1, student2, student3, student4, student5]
global current  # current student
global student
student = studentlist[0]  # initialize to first student

# MENU
menu1 = Menu(window)
window.config(menu=menu1)

sub1 = Menu(menu1)
menu1.add_cascade(label="Manage Users", menu=sub1)
sub1.add_command(label="Add current user")
sub1.add_command(label="Delete current user")

sub2 = Menu(menu1)
menu1.add_cascade(label="Options", menu=sub2)
sub2.add_command(label="Clear fields", command=clearData)
sub2.add_command(label="Exit", command=ext)


# CANVAS
canvas = Canvas(window, width=500, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)


# Set Image in Canvas
canvas.create_image(0, 0, image=background, anchor="nw")


# Title
canvas.create_text(250, 50, text="Zodiac Sign Calculator", font=("Papyrus", 20, "bold"), fill="gold")


# Name Text
canvas.create_text(220, 100, text="Name", anchor="e", font=("Haettenschweiler", 16), fill="lightblue")


# Name ENTRY
entry1 = Entry(window, width=14, fg="navy", bg="lightblue", font=("Cambria", 12))
entry1.focus_set()
entry1_window = canvas.create_window(260, 100, anchor="w", window=entry1)


# Day born TEXT
canvas.create_text(220, 140, text="Day Born", anchor="e", font=("Haettenschweiler", 16), fill="lightblue")


# Day born COMBOBOX
list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
         "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
days = StringVar()
combo1 = OptionMenu(window, days, *list1)
days.set("1")
combo1.config(fg="navy", bg="lightblue", font=("Cambria", 10))
combo1["menu"].config(fg="navy", font=("Cambria", 10))
combo1_window = canvas.create_window(260, 140,  anchor="w", window=combo1)


# Month born TEXT
canvas.create_text(220, 180, text="Month Born", anchor="e", font=("Haettenschweiler", 16), fill="lightblue")


# Month born COMBOBOX
list2 = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
months = StringVar()
combo2 = OptionMenu(window, months, *list2)
combo2["menu"].config(fg="navy", font=("Cambria", 10))
months.set("January")
combo2.config(fg="navy", bg="lightblue", font=("Cambria", 10))
combo2_window = canvas.create_window(260, 180, anchor="w", window=combo2)


# Year born TEXT
canvas.create_text(220, 220, text="Year Born", anchor="e", font=("Haettenschweiler", 16), fill="lightblue")
years = StringVar()


# Year born ENTRY
entry2 = Entry(window, width=14, fg="navy", bg="lightblue", font=("Cambria", 12), state="disabled",
               validate="key", validatecommand=(vcmd, '%P'))
entry2_window = canvas.create_window(260, 220, anchor="w", window=entry2)


# ---------------------------------------------------------------------------

# Chinese Zodiac Sign CHECKBUTTON
cbVar = IntVar()
cb = Checkbutton(window, text="Chinese Zodiac Sign", width=18, height=1, fg="navy", bg="lightblue",
                 activebackground="cyan", activeforeground="navy", font=("Papyrus", 10, "bold"),
                 variable=cbVar, command=checker)
cb.deselect()
cb_window = canvas.create_window(250, 270, window=cb)


# ---------------------------------------------------------------------------


# Calculate Zodiac Sign BUTTON
button1 = Button(window, text="Calculate Zodiac Sign", width=30, height=1, fg="darkblue", bg="gold",
                 activebackground="yellow", activeforeground="darkblue", font=("Haettenschweiler", 20),
                 command=calculate)
button1_window = canvas.create_window(250, 330, window=button1)


# ---------------------------------------------------------------------------

# Astrological Sign TEXT
canvas.create_text(170, 410, text="Astrological\n Sign", font=("Papyrus", 16, "bold"), fill="lightblue")


# Chinese Zodiac Sign TEXT
canvas.create_text(330, 410, text="Chinese Zodiac\n Sign", font=("Papyrus", 16, "bold"), fill="lightblue")


# Astrological Sign Result ENTRY
entry3 = Entry(window, state="disabled", width=14, font=("Cambria", 12))
entry3_window = canvas.create_window(170, 460, window=entry3)

# Chinese Zodiac Sign Result ENTRY
entry4 = Entry(window, state='disabled', width=14, font=("Cambria", 12))
entry4_window = canvas.create_window(330, 460, window=entry4)


# ---------------------------------------------------------------------------


# Previous BUTTON
button2 = Button(window, text="Previous User", width=16, height=1, fg="lightblue", bg="navy", activebackground="blue",
                 activeforeground="lightblue", font=("Haettenschweiler", 12), command=calculate)
button2_window = canvas.create_window(170, 520, window=button2)

# Next BUTTON
button3 = Button(window, text="Next User", width=16, height=1, fg="lightblue", bg="navy", activebackground="blue",
                 activeforeground="lightblue", font=("Haettenschweiler", 12), command=calculate)
button3_window = canvas.create_window(330, 520, window=button3)

display(0)

mainloop()
