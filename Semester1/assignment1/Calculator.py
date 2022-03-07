"""Zodiac Sign Calculator
    by Stefana Chiritescu"""

# Import tkinter and User class
from tkinter import *
from Users import User

# Creates GUI, sets the size and title, makes window non-resizable and stores an image in a variable
window = Tk()
window.geometry("500x600")
window.title("Zodiac Sign Calculator")
window.resizable(False, False)
background = PhotoImage(file="background.png")


'''Definitions'''
emptyUser = User("", "1", "January", False, "", "", "")
userlist = [emptyUser]
user = userlist[0]

global current
current = 0

'''Event Handling Methods'''


def display(index):
    """Refreshes entries and re-displays the current user's details from the 'Users' object"""

    global current
    user = userlist[index]

    entry_name.delete(0, END)
    entry_name.insert(END, user.getName())

    days.set(user.getDay())
    months.set(user.getMonth())

    chinese = user.getChinese()
    if chinese:
        cbVar.set(1)
    else:
        cbVar.set(0)

    entry_year.config(state="normal")
    entry_year.delete(0, END)
    entry_year.insert(END, user.getYear())
    entry_year.config(state="disabled")

    entry_astro.config(state="normal")
    entry_astro.delete(0, END)
    entry_astro.insert(END, user.getAstrologySign())
    entry_astro.config(state="disabled")

    entry_chinese.config(state="normal")
    entry_chinese.delete(0, END)
    entry_chinese.insert(END, user.getChineseSign())
    entry_chinese.config(state="disabled")

    entry_user.config(state="normal")
    entry_user.delete(0, END)
    entry_user.insert(END, index + 1)
    entry_user.config(state="disabled")


def clearData():
    """Clears data from all entry fields, unchecks checkbox and sets combo boxes to first (default) values"""

    entry_name.delete(0, END)
    entry_name.focus_set()

    days.set("1")
    months.set("January")

    cb.deselect()

    entry_year.config(state="normal")
    entry_year.delete(0, END)

    entry_year.config(state="disabled")

    entry_astro.config(state="normal")
    entry_astro.delete(0, END)

    entry_astro.config(state="disabled")

    entry_chinese.config(state="normal")
    entry_chinese.delete(0, END)
    entry_chinese.config(state="disabled")


def addUser():
    """Gets current user data and adds it to the 'newUser' variable;
        Adds an empty new user to the 'userlist' list if the first user name is empty,
    adds the current user as a new empty user to the 'userlist' list if current name is empty,
    otherwise, adds the current user to the 'userlist' list;
        Prints success"""

    global current
    name = entry_name.get()
    day = days.get()
    month = months.get()
    chinese = user.getChinese()
    if cbVar.get() == 1:
        chinese = True
    year = entry_year.get()
    sign1 = entry_astro.get()
    sign2 = entry_chinese.get()

    newUser = User(name, day, month, chinese, year, sign1, sign2)

    if userlist[0].getName() == "":
        userlist[0] = newUser

    elif userlist[current].getName() == "":
        userlist[current] = newUser

    else:
        userlist.append(newUser)

    current = (len(userlist) - 1)
    display(current)

    print("Current user added successfully.")


def deleteUser():
    """Deletes current user if 'userlist' list is greater than 1,
    creates an empty user and deletes current user if 'userlist' list is 0;
        Calls 'clearData' and 'display' methods;
        Prints success or failure"""

    global current
    global emptyUser

    if len(userlist) > 1:
        userlist.pop(current)
        current -= 1
        print("Current user deleted successfully.")
    elif len(userlist) == 0:
        userlist.append(emptyUser)
        userlist.pop(current)
        print("Current user deleted successfully.")
    else:
        print("There are not enough users to delete.")

    clearData()
    display(current)


def nextCmd():
    """Calls the 'clearData' and 'display' methods;
        Creates an empty user if there is no user in the list;
        Displays the next user
        """
    global current

    clearData()
    display(current)

    if userlist[current].getName() == userlist[current].getName() and userlist[len(userlist) - 1].getName() != "":
        userlist.append(emptyUser)

    if current < (len(userlist) - 1):
        current += 1
        display(current)


def prevCmd():
    """Calls the 'clearData' and 'display' methods
        If the current user is not first in 'userlist' list, goes to and displays previous user in 'userlist' list"""
    global current

    clearData()
    display(current)

    if current > 0:
        current -= 1
        display(current)


def validateE(P):
    """Returns true if P is greater or equal to 4, otherwise, returns false to stop user from entering
     more than 4 characters"""
    if len(P) <= 4:
        return True
    else:
        return False


# Assigns the validator to be used on click
vcmd = window.register(validateE)


def checker():
    """If Chinese checkbox is checked, enable 'entry_year' entry box
    otherwise, deletes its data and disables it"""
    if cbVar.get() > 0:
        entry_year.config(state="normal")
    else:
        entry_year.delete(0, END)
        entry_year.config(state="disabled")


def calculate():
    """Checks day and month selected by user, calculates Astrological sign and outputs into 'entry_astro'
        If user checks 'chinese' checkbox, calculates Chinese sign and outputs into 'entry_chinese' """

    # Astrological Zodiac Sign
    day = int(days.get())
    month = months.get()

    entry_astro.config(state="normal")

    match month:
        case "December":
            sign = "Sagittarius" if (day < 22) else "Capricorn"
        case "January":
            sign = "Capricorn" if (day < 20) else "Aquarius"
        case "February":
            sign = "Aquarius" if (day < 19) else "Pisces"
        case "March":
            sign = "Pisces" if (day < 21) else "Aries"
        case "April":
            sign = "Aries" if (day < 20) else "Taurus"
        case "May":
            sign = "Taurus" if (day < 21) else "Gemini"
        case "June":
            sign = "Gemini" if (day < 21) else "Cancer"
        case "July":
            sign = "Cancer" if (day < 23) else "Leo"
        case "August":
            sign = "Leo" if (day < 23) else "Virgo"
        case "September":
            sign = "Virgo" if (day < 23) else "Libra"
        case "October":
            sign = "Libra" if (day < 23) else "Scorpio"
        case "November":
            sign = "Scorpio" if (day < 22) else "Sagittarius"
        case _:
            sign = "Capricorn"

    entry_astro.delete(0, END)
    entry_astro.insert(END, sign)
    entry_astro.config(state="disabled")

    # Chinese Zodiac Sign
    sign2 = ""

    if cbVar.get() > 0:
        try:
            year = int(entry_year.get())

            entry_chinese.config(state="normal")

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

        except ValueError:
            entry_year.delete(0, END)

    else:
        entry_chinese.config(state="disabled")

    entry_chinese.delete(0, END)
    entry_chinese.insert(END, sign2)
    entry_chinese.config(state="disabled")


def ext():
    """Exits the application"""
    exit()


'''GUI'''
# MENU
menu = Menu(window)
window.config(menu=menu)

sub_manage = Menu(menu)
menu.add_cascade(label="Manage Users", menu=sub_manage)
sub_manage.add_command(label="Add current user", command=addUser)
sub_manage.add_command(label="Delete current user", command=deleteUser)

sub_options = Menu(menu)
menu.add_cascade(label="Options", menu=sub_options)
sub_options.add_command(label="Clear fields", command=clearData)
sub_options.add_command(label="Exit", command=ext)

# CANVAS
canvas = Canvas(window, width=500, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Set Image in Canvas
canvas.create_image(0, 0, image=background, anchor="nw")

# Title
canvas.create_text(250, 60, text="Zodiac Sign Calculator", font=("Papyrus", 21, "bold"), fill="gold")

# User TEXT
canvas.create_text(230, 110, text="User", anchor="e", font=("Haettenschweiler", 16), fill="#ffdd99")

# User ENTRY
entry_user = Entry(window, width=2, fg="navy", bg="lightblue", font=("Cambria", 12), state="disabled")
entry_user_window = canvas.create_window(250, 110, anchor="w", window=entry_user)

# Name TEXT
canvas.create_text(230, 155, text="Name", anchor="e", font=("Haettenschweiler", 16), fill="lightblue")

# Name ENTRY
entry_name = Entry(window, width=10, fg="navy", bg="lightblue", font=("Cambria", 12))
entry_name.focus_set()
entry_name_window = canvas.create_window(250, 155, anchor="w", window=entry_name)

# Day born TEXT
canvas.create_text(230, 190, text="Day Born", anchor="e", font=("Haettenschweiler", 16), fill="lightblue")

# Day born COMBOBOX
list_days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
             "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
days = StringVar()
combo1 = OptionMenu(window, days, *list_days)
days.set("1")
combo1.config(fg="navy", bg="lightblue", font=("Cambria", 10))
combo1["menu"].config(fg="navy", font=("Cambria", 10))
combo1_window = canvas.create_window(250, 190, anchor="w", window=combo1)

# Month born TEXT
canvas.create_text(230, 230, text="Month Born", anchor="e", font=("Haettenschweiler", 16), fill="lightblue")

# Month born COMBOBOX
list_months = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
months = StringVar()
combo2 = OptionMenu(window, months, *list_months)
combo2["menu"].config(fg="navy", font=("Cambria", 10))
months.set("January")
combo2.config(fg="navy", bg="lightblue", font=("Cambria", 10))
combo2_window = canvas.create_window(250, 230, anchor="w", window=combo2)

# Chinese Sign CHECKBUTTON
cbVar = IntVar()
cb = Checkbutton(window, text="Chinese Sign", width=12, height=1, fg="navy", bg="#99ebff",
                 activebackground="cyan", activeforeground="navy", font=("Papyrus", 11, "bold"),
                 variable=cbVar, command=checker)
cb.deselect()
cb_window = canvas.create_window(250, 278, window=cb)

# Year born TEXT
canvas.create_text(230, 320, text="Year Born", anchor="e", font=("Haettenschweiler", 16), fill="lightblue")

# Year born ENTRY
entry_year = Entry(window, width=8, fg="navy", bg="lightblue", font=("Cambria", 12), state="disabled",
                   validate="key", validatecommand=(vcmd, '%P'))
entry_year_window = canvas.create_window(250, 320, anchor="w", window=entry_year)
years = StringVar()

# Calculate Zodiac Sign BUTTON
button_calc = Button(window, text="Calculate Zodiac Sign(s)", width=28, height=1, fg="#1e3d7b", bg="#ffc266",
                     activebackground="yellow", activeforeground="darkblue", font=("Haettenschweiler", 20),
                     command=calculate)
button_calc_window = canvas.create_window(250, 380, window=button_calc)

# Astrological Sign TEXT
canvas.create_text(170, 440, text="Astrological Sign", font=("Papyrus", 14, "bold"), fill="gold")

# Chinese Zodiac Sign TEXT
canvas.create_text(330, 440, text="Chinese Sign", font=("Papyrus", 14, "bold"), fill="gold")

# Astrological Sign Result ENTRY
entry_astro = Entry(window, state="disabled", width=10, font=("Cambria", 12))
entry_astro_window = canvas.create_window(170, 470, window=entry_astro)

# Chinese Zodiac Sign Result ENTRY
entry_chinese = Entry(window, state='disabled', width=10, font=("Cambria", 12))
entry_chinese_window = canvas.create_window(330, 470, window=entry_chinese)

# Previous BUTTON
button_prev = Button(window, text="Previous User", width=12, height=1, fg="lightblue", bg="navy",
                     activebackground="blue", activeforeground="lightblue", font=("Haettenschweiler", 12),
                     command=prevCmd)
button_prev_window = canvas.create_window(170, 520, window=button_prev)

# Next BUTTON
button_next = Button(window, text="Next User", width=12, height=1, fg="lightblue", bg="navy",
                     activebackground="blue", activeforeground="lightblue", font=("Haettenschweiler", 12),
                     command=nextCmd)
button_next_window = canvas.create_window(330, 520, window=button_next)

display(0)

mainloop()
