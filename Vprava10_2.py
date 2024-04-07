from tkinter import *

def button_click():
    a = float(entry1.get())
    b = float(entry2.get())
    result = a*(4*b-a)
    label3['text'] = 'Результат' + str(result)

root = Tk()
label1 = Label(text='a = ')
label1.pack()
entry1 = Entry()
entry1.pack()
label2 = Label(text='b = ')
label2.pack()
entry2 = Entry()
entry2.pack()
label3 = Label()
label3.pack()
button = Button(text = 'обчислити',command=button_click)
button.pack()
mainloop()