from tkinter import *

from Ass_Student import Student

window = Tk()
window.geometry("300x400")
window.title("Welcome")

#============================================================
# Event Handling Methods


def display(index):
    global current
    global student
    student = studentlist[index]
    current=index
    entry2.delete(0, END)
    entry2.insert(END, student.getName())
    entry3.delete(0, END)
    entry3.insert(END, student.getID())
    entry4.delete(0, END)
    entry4.insert(END, student.getPresent())
    entry5.delete(0, END)
    entry5.insert(END, student.getAbsent())
    entry6.delete(0, END)
    entry6.insert(END, student.getExcused())

    international=student.getInternational()
    if (international==True):
        var_cb1.set(1)
    else:
        var_cb1.set(0)


def markPresent():
    student.markPresent()
    display(current)


def markAbsent():
    student.markAbsent()
    display(current)

def markExcused():
    days = int(excusedVar.get())
    student.markExcused(days)
    display(current)

def percentAttended():
    result = student.getPercentAttendance()
    entry7.delete(0, END)
    entry7.insert(END, (str(result) + " %"))

def nextCmd():
    global current
    if (current<(len(studentlist)-1) ):
        current += 1
        display(current)

def prevCmd():
    global current
    if (current>0):
        current -= 1
        display(current)

def firstCmd():
    display(0)

def lastCmd():
    display(len(studentlist)-1)


def clearData():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    var_cb1.set(0)

def insertNewStudent():
    name=entry2.get()
    ID=entry3.get()
    International=False
    if (var_cb1.get()==1):
        International=True
    newStudent=Student(name,ID,International)
    studentlist.append(newStudent)

# End of Method Declarations
#========================================================================



# Definitions
#=====================================================================
student1 = Student("J.Smith", "A003451245",False)
student2 = Student("L.Shine", "A003478344",True)
student3 = Student("M.Jones", "A003499123",False)
student4 = Student("T.Lennon", "A003468812",True)
student5 = Student("H.Green", "A003462194",False)

studentlist=[student1,student2,student3,student4,student5]
global current     # current student
global student
student = studentlist[0]  # initialize to first student

#========= End of Definitions ============================

#=======================================================
# Menu to Add New Student
menu1 = Menu(window) #MenuBar
window.config(menu=menu1)
subm1=Menu(menu1)  #Menu
menu1.add_cascade(label="Add_Student_Options", menu=subm1)
subm1.add_command(label="clearData",  font=("arial", 12, "bold"),command = clearData)   # menu item
subm1.add_command(label="Insert Student", font=("arial", 12, "bold"), command = insertNewStudent)

#======= End of Menu Definition ============================

frame = Frame(window, width=200, height=200)
frame.place(x=10,y=80)






label1 = Label(window, text="Student example", fg="blue",bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen


label2 = Label(frame, text="Name", fg="blue",width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="ID", fg="blue",width=15, font=("arial", 10, "bold"))   #
label3.grid(row=1, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W+E)

label4 = Label(frame, text="Present", fg="blue",width=15, font=("arial", 10, "bold"))   #
label4.grid(row=2, column=0, sticky=W+E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W+E)


label5 = Label(frame, text="Absent", fg="blue",width=15, font=("arial", 10, "bold"))   #
label5.grid(row=3, column=0, sticky=W+E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=3, column=1, sticky=W+E)

label6 = Label(frame, text="Excused", fg="blue",width=15, font=("arial", 10, "bold"))   #
label6.grid(row=4, column=0, sticky=W+E)

entry6 = Entry(frame)
entry6.insert(END, '0')
entry6.grid(row=4, column=1, sticky=W+E)

var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="International Student", variable=var_cb1)
cb1.grid(row=5,column=0,columnspan=2)

button1 = Button(frame, text="mark Present", fg="black", font=("arial", 10, "bold"), command=markPresent)
button1.grid(row=6, column=0, sticky=W+E)

button2 = Button(frame, text="mark Absent", fg="black", font=("arial", 10, "bold"), command=markAbsent)
button2.grid(row=6, column=1, sticky=W+E)

button3 = Button(frame, text="mark Excused", fg="black", font=("arial", 10, "bold"), command=markExcused)
button3.grid(row=7, column=0, sticky=W+E)

list1=['1','2','3','4','5']
excusedVar = StringVar()
combo1= OptionMenu(frame,excusedVar, *list1)
excusedVar.set("1")
combo1.grid(row=7,column=1, sticky=W+E)

button4 = Button(frame, text="% Attendance", fg="black", font=("arial", 10, "bold"), command=percentAttended)
button4.grid(row=8, column=0, sticky=W+E)

entry7 = Entry(frame)
entry7.insert(END, '')
entry7.grid(row=8, column=1, sticky=W+E)

labelBlank = Label(frame, text=" ", fg="blue",width=15, font=("arial", 10, "bold"))   #
labelBlank.grid(row=9, column=0, columnspan=2,sticky=W+E)

button5 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button5.grid(row=10, column=0, sticky=W+E)

button6 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button6.grid(row=10, column=1, sticky=W+E)

button7 = Button(frame, text="First", fg="black", font=("arial", 10, "bold"), command=firstCmd)
button7.grid(row=11, column=0, sticky=W+E)

button8 = Button(frame, text="Last", fg="black", font=("arial", 10, "bold"), command=lastCmd)
button8.grid(row=11, column=1, sticky=W+E)

display(0)

mainloop()
