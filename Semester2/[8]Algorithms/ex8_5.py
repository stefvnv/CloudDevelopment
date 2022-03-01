"""LINKED LIST"""

from tkinter import *

window = Tk()
window.geometry("1350x450")
window.title("Welcome")

from ex8_5Class import *


# ------------end of class definition------------------

def display():
    value1 = a1.printList()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)


def initList():
    a1.insert('A', 33)
    a1.insert('B', 21)
    a1.insert('B', 43)
    a1.insert('C', 12)
    a1.insert('G', 39)
    a1.insert('B', 29)
    a1.insert('E', 23)


def insertEvent():
    name = entry5.get()
    age = int(entry6.get())
    a1.insert(name, age)
    display()


def countEvent():
    name = entry51.get()
    res = a1.countOccurs(name)
    entry61.delete(0, END)  # delete old value
    entry61.insert(END, res)


def searchEvent():
    age = int(entry52.get())
    res = a1.findName(age)
    entry62.delete(0, END)  # delete old value
    entry62.insert(END, str(res))


def sumEvent():
    res = a1.sumOfAllAges()
    entry53.delete(0, END)  # delete old value
    entry53.insert(END, res)


def maxEvent():
    res = a1.oldest()
    entry54.delete(0, END)  # delete old value
    entry54.insert(END, res)


list = [2, 59, 7, 88, 9, 11, 102, 22, 27, 28, 29, 34, 55, 60, 61, 65, 68, 71, 73, 75, 77, 8, 89, 9, 96]
a1 = MyList(list)

label1 = Label(window, text="Linked List Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

entry2 = Entry(window, width=120, font=("arial", 14, "bold"))
entry2.insert(END, '1')
entry2.place(x=20, y=80)

# entry2b = Entry(window,width=18, font=("arial", 12, "bold"))
# entry2b.insert(END, '40')
# entry2b.place(x=230, y=120)

# label3b = Label(window, text="Enter Search Item", fg="blue", width=18, font=("arial", 12, "bold"))   #
# label3b.place(x=10, y=120)


button5 = Button(window, text="Insert Item", fg="black", font=("arial", 12, "bold"), command=insertEvent)
button5.place(x=20, y=160)

entry5 = Entry(window, width=14, font=("arial", 12, "bold"))
entry5.insert(END, 'W')
entry5.place(x=170, y=160)

entry6 = Entry(window, width=14, font=("arial", 12, "bold"))
entry6.insert(END, '8')
entry6.place(x=320, y=160)

button5 = Button(window, text="Count Occurs", fg="black", font=("arial", 12, "bold"), command=countEvent)
button5.place(x=20, y=210)

entry51 = Entry(window, width=14, font=("arial", 12, "bold"))
entry51.insert(END, 'B')
entry51.place(x=170, y=210)

entry61 = Entry(window, width=14, font=("arial", 12, "bold"))
entry61.insert(END, '')
entry61.place(x=320, y=210)

# Search

button52 = Button(window, text="findName", fg="black", font=("arial", 12, "bold"), command=searchEvent)
button52.place(x=20, y=260)

entry52 = Entry(window, width=14, font=("arial", 12, "bold"))
entry52.insert(END, '21')
entry52.place(x=170, y=260)

entry62 = Entry(window, width=14, font=("arial", 12, "bold"))
entry62.insert(END, '')
entry62.place(x=320, y=260)

# Sum of all Ages

button53 = Button(window, text="sumOfAllAges", fg="black", font=("arial", 12, "bold"), command=sumEvent)
button53.place(x=20, y=310)

entry53 = Entry(window, width=14, font=("arial", 12, "bold"))
entry53.insert(END, '')
entry53.place(x=170, y=310)

# Max Age

button54 = Button(window, text="Oldest", fg="black", font=("arial", 12, "bold"), command=maxEvent)
button54.place(x=20, y=360)

entry54 = Entry(window, width=14, font=("arial", 12, "bold"))
entry54.insert(END, '')
entry54.place(x=170, y=360)

initList()

display()

mainloop()
