from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title('Погода Населених пунктів')
root.wm_attributes('-alpha')
root.geometry('300x250')

root.resizable(width=False,height=False)
canvas = Canvas(root, height=300,width=250)
canvas.pack()
frame = Frame(root,bg='red')
frame.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=0.8)
title = Label(frame, text='Weather',bg='gray',font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow',)
btn.pack()




root.mainloop()