from tkinter import *

from Ass_Student import Student

window = Tk()
window.geometry("500x600")
window.title("Zodiac Sign Calculator")


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

subm1 = Menu(menu1)
menu1.add_cascade(label="Options", menu=subm1)
subm1.add_command(label="Insert Person")
subm1.add_command(label="Clear", font=("arial", 12, "bold"), command=clearData)
subm1.add_command(label="Exit", command=ext)

# GRID
frame = Frame(window, width=400, height=500)
frame.place(x=110, y=200)
frame.pack(pady=20)

# Title
label1 = Label(window, text="Zodiac Sign Calculator", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=30, y=10)
label1.pack(pady=60)

# Name LABEL
label2 = Label(frame, text="Name", fg="blue", width=15, font=("arial", 10, "bold"))
label2.grid(row=0, column=0, sticky=W + E, padx=30)

# Name ENTRY
entry1 = Entry(frame)
entry1.grid(row=0, column=1, sticky=W + E)
entry1.focus_set()

# Day born LABEL
label3 = Label(frame, text="Day Born", fg="blue", width=15, font=("arial", 10, "bold"))
label3.grid(row=1, column=0, sticky=W + E)

# Day born COMBOBOX
list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
         "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
days = StringVar()
combo2 = OptionMenu(frame, days, *list1)
days.set("1")
combo2.grid(row=1, column=1, sticky=W + E)

# Month born LABEL
label4 = Label(frame, text="Month Born", fg="blue", width=15, font=("arial", 10, "bold"))
label4.grid(row=2, column=0, sticky=W + E)

# Month born COMBOBOX
list2 = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
months = StringVar()
combo1 = OptionMenu(frame, months, *list2)
months.set("January")
combo1.grid(row=2, column=1, sticky=W + E)

# Year born LABEL
label5 = Label(frame, text="Year Born", fg="blue", width=15, font=("arial", 10, "bold"))
label5.grid(row=3, column=0, sticky=W + E)

# Year born ENTRY
entry2 = Entry(frame, state="disabled", validate="key", validatecommand=(vcmd, '%P'))
years = StringVar()
entry2.grid(row=3, column=1, sticky=W + E)

# Chinese Zodiac Sign CHECKBUTTON
cbVar = IntVar()
cb = Checkbutton(frame, text="Chinese Zodiac Sign", variable=cbVar, command=checker)
cb.grid(row=4, column=0, columnspan=2)
cb.deselect()

# Calculate Zodiac Sign BUTTON
button1 = Button(frame, text="Calculate Zodiac Sign", fg="black", font=("arial", 10, "bold"), command=calculate)
button1.grid(row=5, column=0, columnspan=2)

# Astrological Sign LABEL
label6 = Label(frame, text="Astrological Sign", fg="blue", width=15, font=("arial", 10, "bold"))
label6.grid(row=6, column=0, sticky=W + E)

# Chinese Zodiac Sign LABEL
label7 = Label(frame, text="Chinese Zodiac Sign", fg="blue", width=15, font=("arial", 10, "bold"))
label7.grid(row=6, column=1, sticky=W + E)

# Astrological Sign Result ENTRY
entry3 = Entry(frame, state="disabled")
entry3.grid(row=7, column=0, sticky=W + E)

# Chinese Zodiac Sign Result ENTRY
entry4 = Entry(frame, state='disabled')
entry4.grid(row=7, column=1, sticky=W + E)


display(0)

mainloop()
