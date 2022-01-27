from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("List Functions")


def search(list, target):
    result = False
    for el in list:
        if el == target:
            result = True
    return result


def myLargest(list):
    result = max(list1)
    return result

    # OR
    # result = 0
    # for el in list:
    #   if el > result:
    #       result = el
    # return result


def searchEvent():
    global list1
    target = int(entry3.get())
    result = search(list1, target)
    entry4.delete(0, END)
    if result == True:
        entry4.insert(END, 'True')
    else:
        entry4.insert(END, 'False')


def largestEvent():
    global list1
    result = myLargest(list1)
    entry5.delete(0, END)
    entry5.insert(END, result)


list1 = [2, 6, 2, 7, 8, 4, 2, 6]
label1 = Label(window, text="List Functions", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

label2 = Label(window, text="Value1", fg="blue", width=10, font=("arial", 12, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '[2, 6, 2, 7, 8, 4, 2, 6]')
entry2.place(x=100, y=80)

label3 = Label(window, text="Value2", fg="blue", width=10, font=("arial", 12, "bold"))  #
label3.place(x=10, y=120)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=100, y=120)

button1 = Button(window, text="search", width=8, fg="black", font=("arial", 10, "bold"), command=searchEvent)
button1.place(x=40, y=160)

entry4 = Entry(window, width=13)
entry4.insert(END, '')
entry4.place(x=140, y=160)

button2 = Button(window, text="my Largest", width=8, fg="black", font=("arial", 10, "bold"), command=largestEvent)
button2.place(x=40, y=190)

entry5 = Entry(window, width=13)
entry5.insert(END, '1')
entry5.place(x=140, y=190)

mainloop()
