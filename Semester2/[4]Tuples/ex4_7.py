from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("List Functions")


def findNumber(dict, key):
    return dict.get(key)


def add(dict, key, value):
    dict.update({key: value})


def searchEvent():
    global studentList
    target = entry2.get()
    result = findNumber(studentList, target)
    entry3.delete(0, END)
    entry3.insert(END, result)


def addEvent():
    global studentList
    key = entry2.get()
    value = entry3.get()
    add(studentList, key, value)


def update():
    global studentList
    key = entry2.get()
    value = entry3.get()
    studentList.update({key: value})

    # OR

    # update(studentList, key,value)


studentList = {'Smith': '0874231234', 'Jones': '0861234123', 'peters': '0857878781', 'Adams': '0441234561',
               'Cross': '0874234566'}

label1 = Label(window, text="List Functions", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)  # place on screen

label2 = Label(window, text="Enter Name", fg="blue", width=10, font=("arial", 10, "bold"))
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '')
entry2.place(x=100, y=80)

label3 = Label(window, text="Phone No", fg="blue", width=10, font=("arial", 10, "bold"))  #
label3.place(x=10, y=120)

entry3 = Entry(window)
entry3.insert(END, '')
entry3.place(x=100, y=120)

button1 = Button(window, text="search", width=8, fg="black", font=("arial", 10, "bold"), command=searchEvent)
button1.place(x=40, y=160)

button2 = Button(window, text="add", width=8, fg="black", font=("arial", 10, "bold"), command=addEvent)
button2.place(x=140, y=160)

button3 = Button(window, text="update", width=8, fg="black", font=("arial", 10, "bold"), command=update)
button3.place(x=40, y=200)

mainloop()
