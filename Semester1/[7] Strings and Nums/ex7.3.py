from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("List Functions")


def searchSubstr(text, tar):
    result = text.find(tar)
    if result == -1:
        result = False
    else:
        return True


def countSubstr(text, tar):
    result = text.count(tar)
    return result


def searchEvent():
    global list1
    target = str(entry3.get())
    result = searchSubstr(list1, target)
    entry4.delete(0, END)
    if result == True:
        entry4.insert(END, 'True')
    else:
        entry4.insert(END, 'False')



def countEvent():
    global list1
    target = str(entry3.get())
    result = countSubstr(list1, target)
    entry5.delete(0, END)
    entry5.insert(END, result)


list1 = 'abcdeabcdabcab'
label1 = Label(window, text="Text Functions", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Text", fg="blue", width=10, font=("arial", 12, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, 'abcdeabcdabcab')
entry2.place(x=100, y=80)

label3 = Label(window, text="Enter Target", fg="blue", width=10, font=("arial", 10, "bold"))   #
label3.place(x=10, y=120)

entry3 = Entry(window)
entry3.insert(END, 'abc')
entry3.place(x=100, y=120)

button1 = Button(window, text="searchTarget", width=10, fg="black", font=("arial", 8, "bold"), command=searchEvent)
button1.place(x=40, y=160)

entry4 = Entry(window, width=13)
entry4.insert(END, '')
entry4.place(x=140, y=160)

button2 = Button(window, text="countTarget", width=10, fg="black", font=("arial", 8, "bold"), command=countEvent)
button2.place(x=40, y=190)

entry5 = Entry(window, width=13)
entry5.insert(END, '1')
entry5.place(x=140, y=190)


mainloop()
