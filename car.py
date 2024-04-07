from tkinter import*
def button_click():
    button['bg']='yellow'
    button['font']='Arial 14'
    button['text']='Змінюємо значення властивостей'
    cl = entry.get()
    root['bg'] = cl
root=Tk()
root.geometry('600x400+350+200')
root.title('Створюємо проект з вікном')
root['bg'] = 'lightblue'
label = Label (text="Уведіть у поле назву кольору англійською")
label['font']='Arial 14'
label.pack(pady=30)
entry = Entry()
entry.pack (pady=30)
button = Button(text='Вибери мене', command=button_click)
button.pack (pady=30)

root.mainloop()

