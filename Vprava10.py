from tkinter import *

def buttom_click():
    entry['bg'] = 'red'
    entry['fg'] = 'white'
    entry['font'] = ('Arial', 14)
    entry['width'] = entry['width'] + 6
    entry.delete(0, END)
    entry.insert(0, 'Ми використовуємо властивості поля')

root = Tk()

entry = Entry(width=15, bd=5)
entry.pack(padx=30)
entry.insert(10, '8 Class')

button = Button(text = 'Виконати', command= buttom_click)
button.pack()
mainloop()