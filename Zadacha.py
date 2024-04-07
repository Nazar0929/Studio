from tkinter import *
root = Tk()
root.geometry('400x300')
entry = Entry(width = 25, bg = 'yellow', fg = 'blue', font = 'Arial 14', bd = 3)
entry.pack()
entry.insert(0, 'Вивчаємо властивості поля')
mainloop()