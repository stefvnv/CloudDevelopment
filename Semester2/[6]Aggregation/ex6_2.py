from tkinter import *

window = Tk()
window.geometry("300x400")
window.title("Welcome")

from ex6_2Class import *


# ------------end of class definition------------------

def display():
    value1 = t1.readStudentNo()
    value2 = t1.readStudentName()
    value3 = t1.readAddress()
    value4 = t1.readCourseTitle()
    value5 = t1.readCourseQualification()
    value6 = t1.readCourseLevel()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, value4)
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, value5)
    entry7.delete(0, END)  # delete old value
    entry7.insert(END, value6)


def incrYearEvent():
    t1.incrementYear()
    display()


def setQualEvent():
    newQual = entry4b.get()
    t1.updateCourseQualification(newQual)
    display()


def setCourseEvent():
    newTitle = entry5b.get()
    t1.updateCourseTitle(newTitle)
    display()


def stepLevelEvent():
    t1.stepCourseLevel()
    display()


def exitEvent():
    quit()


def setAddressEvent():
    newAddress = entry3b.get()
    t1.updateAddress(newAddress)
    display()


t1 = Student("A00234123", "T.Jones", "Moate", "Computer Science", "BEng", 7)

label1 = Label(window, text="Student Details", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=40, y=30)  # place on screen

label2 = Label(window, text="Student No", fg="blue", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Name", fg="blue", width=12, font=("arial", 10, "bold"))  #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Address", fg="blue", width=8, font=("arial", 10, "bold"))  #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

label5 = Label(window, text="Course", fg="blue", width=12, font=("arial", 10, "bold"))  #
label5.place(x=10, y=170)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=170)

label6 = Label(window, text="Qualification", fg="blue", width=12, font=("arial", 10, "bold"))  #
label6.place(x=10, y=200)

entry6 = Entry(window)
entry6.insert(END, '1')
entry6.place(x=120, y=200)

label7 = Label(window, text="Level", fg="blue", width=12, font=("arial", 10, "bold"))  #
label7.place(x=10, y=230)

entry7 = Entry(window)
entry7.insert(END, '1')
entry7.place(x=120, y=230)

# -------------------------------


button3 = Button(window, text="updateAddress", fg="black", font=("arial", 10, "bold"), command=setAddressEvent)
button3.place(x=40, y=270)

entry3b = Entry(window)
entry3b.insert(END, 'Athlone')
entry3b.place(x=150, y=270)

button4 = Button(window, text="updateQual", fg="black", font=("arial", 10, "bold"), command=setQualEvent)
button4.place(x=40, y=300)

entry4b = Entry(window)
entry4b.insert(END, 'BSc')
entry4b.place(x=150, y=300)

button5 = Button(window, text="updateCourse", fg="black", font=("arial", 10, "bold"), command=setCourseEvent)
button5.place(x=40, y=330)

entry5b = Entry(window)
entry5b.insert(END, 'Software Design')
entry5b.place(x=150, y=330)

button6 = Button(window, text="stepLevel", fg="black", font=("arial", 10, "bold"), command=stepLevelEvent)
button6.place(x=40, y=360)

button7 = Button(window, text="Exit", fg="black", font=("arial", 10, "bold"), command=exitEvent)
button7.place(x=150, y=360)

display()

mainloop()
