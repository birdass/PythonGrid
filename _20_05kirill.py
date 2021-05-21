from tkinter import *
from tkinter.ttk import Radiobutton


def clicked():
    global photo
    if selected.get()==1:
        k = open('krasnqi.txt', encoding='utf-8-sig')
        lbl.configure(text=k.read())
        photo = PhotoImage(file="krasnqi.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==2:
        o = open('oranzheviq.txt', encoding='utf-8-sig')
        lbl.configure(text=o.read())
        photo = PhotoImage(file="orange.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==3:
        zelt = open('zheltqi.txt', encoding='utf-8-sig')
        lbl.configure(text=zelt.read())
        photo = PhotoImage(file="zelt.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==4:
        zel = open('zelenqi.txt', encoding='utf-8-sig')
        lbl.configure(text=zel.read())
        photo = PhotoImage(file="zelen.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==5:
        g = open('goluboi.txt', encoding='utf-8-sig')
        lbl.configure(text=g.read())
        photo = PhotoImage(file="golub.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==6:
        s = open('sinii.txt', encoding='utf-8-sig')
        lbl.configure(text=s.read())
        photo = PhotoImage(file="sin.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==7:
        f = open('fioletovqi.txt', encoding='utf-8-sig')
        lbl.configure(text=f.read())
        photo = PhotoImage(file="fio.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    else:
        lbl.configure(text="Выбери цвет")



window = Tk()
window.title("Значение Цветов")
#window.geometry('720x360')
window.resizable(height = False, width = False)
selected = IntVar()
rad1 = Radiobutton(window, text='Красный', value=1, variable=selected)
rad2 = Radiobutton(window, text='Оранжевый', value=2,variable=selected)
rad3 = Radiobutton(window, text='Желтый', value=3, variable=selected)
rad4 = Radiobutton(window, text='Зеленый', value=4, variable=selected)
rad5 = Radiobutton(window, text='Голубой', value=5, variable=selected)
rad6 = Radiobutton(window, text='Синий', value=6, variable=selected)
rad7 = Radiobutton(window, text='Фиолетовый', value=7, variable=selected)
btn = Button(window, text="Узнать значение", command=clicked,font=("Arial Bold", 9))
lbl = Label(window,font=("Arial Bold", 10))

window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=0)
window.rowconfigure(3, weight=0)
window.rowconfigure(4, weight=0)
window.rowconfigure(5, weight=0)
window.rowconfigure(6, weight=0)
window.columnconfigure(4, weight=1)

rad1.grid(column=0, row=2,sticky='w')
rad2.grid(column=0, row=3,sticky='w')
rad3.grid(column=0, row=4,sticky='w')
rad4.grid(column=0, row=5,sticky='w')
rad5.grid(column=0, row=6,sticky='w')
rad6.grid(column=0, row=7,sticky='w')
rad7.grid(column=0, row = 8,sticky='w')
btn.grid(column = 0, row = 1)
lbl.grid(column = 2, row = 9, rowspan=6)

canvas = Canvas(window, height=200, width=500)
canvas.grid(row=2, column=2, rowspan=7)



window.mainloop()