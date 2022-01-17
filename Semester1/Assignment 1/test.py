from tkinter import *
from UsersTEST import User

window = Tk()
window.geometry("1000x600")
window.title("Zodiac Sign Calculator")
window.resizable(False, False)
global current
current = 0


def display(index):
    global current
    user = userlist[index]
    print("Index: " + str(index))
    print("Person name at index: " + user.getName())
    entry1.delete(0, END)
    entry1.insert(END, user.getName())


def addUser():
    global current
    name = entry1.get()

    newUser = User(name)
    if userlist[0].getName() == "Default":
        userlist[0] = newUser

    elif userlist[current].getName() == "":
        userlist[current] = newUser

    else:
        userlist.append(newUser)

    current = (len(userlist) - 1)
    display(current)


def nextCmd():
    clearData()
    global current
    display(current)
    if userlist[current].getName() == userlist[current].getName() and userlist[current].getName() != "" and userlist[
        current].getName() != "Default":
        userlist.append(emptyUser)

        print("Did a blank")
    if current < (len(userlist) - 1):
        current += 1
        display(current)


def prevCmd():
    clearData()
    global current
    display(current)
    if current > 0:
        current -= 1
        display(current)


def clearData():
    entry1.delete(0, END)
    entry1.focus_set()


user1 = User("")
userlist = [user1]
emptyUser = User("")

# MENU
menu1 = Menu(window)
window.config(menu=menu1)

sub1 = Menu(menu1)
menu1.add_cascade(label="Manage Users", menu=sub1)
sub1.add_command(label="Add current user", command=addUser)

# ENTRY
entry1 = Entry(window, width=10, fg="navy", bg="lightblue", font=("Cambria", 12))
entry1.place(x=100, y=200)

# BUTTONS

# Previous BUTTON
button2 = Button(window, text="Previous User", width=16, height=1, fg="lightblue", bg="navy", activebackground="blue",
                 activeforeground="lightblue", font=("Haettenschweiler", 12), command=prevCmd)
button2.place(x=170, y=510)

# Next BUTTON
button3 = Button(window, text="Next User", width=16, height=1, fg="lightblue", bg="navy", activebackground="blue",
                 activeforeground="lightblue", font=("Haettenschweiler", 12), command=nextCmd)
button3.place(x=330, y=510)

display(0)

mainloop()
