from tkinter import*
from tkinter.messagebox import*

def click(event):
    root.geometry('400x300')
    root.title('Я змінюю значення вдастивостей форми')
    root['bg']='yellow'
    h = root.winfo_height() + 150
    root.geometry('400x{}'.format(h))
    showinfo ('Події','Україна - єдина країна')
    

root = Tk()

root.bind ('<1>', click)
root.mainloop()