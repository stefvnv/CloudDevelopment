from tkinter import *
window = Tk()
window.geometry("300x340")
window.title("Welcome")

from ex2_3Class import *


#------------end of class definition------------------

def display():
    value1 = t1.getCourse()
    value2 = t1.getYear()
    value3 = t1.getTopic()
    value4 = t1.getHours()
    value5 = t1.getOffice()
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

def incrYearEvent():
    t1.incrementYear()
    display()

def setTopicEvent():
    newTopic = entry4b.get()
    t1.setTopic(newTopic)
    display()

def exitEvent():
    quit()

def setHoursEvent():
    newHours = int(entry3b.get())
    t1.setHours(newHours)
    display()

t1=PostGraduate("MSc Computing",1, "Databases",4, "M312")


label1 = Label(window, text="PostGraduate Details", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=40, y=30)                            # place on screen

label2 = Label(window, text="Course", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="YearOfStudy", fg="blue", width=12, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Topic", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

label5 = Label(window, text="TeachingHours", fg="blue", width=12, font=("arial", 10, "bold"))   #
label5.place(x=10, y=170)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=170)

label6 = Label(window, text="Office", fg="blue", width=8, font=("arial", 10, "bold"))   #
label6.place(x=10, y=200)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=120, y=200)

#-------------------------------
button1= Button(window, text="incrYear", fg="black", font=("arial", 10, "bold"), command=incrYearEvent)
button1.place(x=40, y=230)

button2= Button(window, text="Exit", fg="black", font=("arial", 10, "bold"), command=exitEvent)
button2.place(x=120, y=230)

button3= Button(window, text="setHours", fg="black", font=("arial", 10, "bold"), command=setHoursEvent)
button3.place(x=40, y=260)

entry3b = Entry(window)
entry3b.insert(END, '7')
entry3b.place(x=120, y=260)

button4= Button(window, text="setTopic", fg="black", font=("arial", 10, "bold"), command=setTopicEvent)
button4.place(x=40, y=290)

entry4b = Entry(window)
entry4b.insert(END, 'Python')
entry4b.place(x=120, y=290)


display()

mainloop()
