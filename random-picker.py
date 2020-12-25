import random
from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title('抽号器')
w, h = root.maxsize()
root.geometry('{}x{}'.format(w, h))

number = 1
ft = tkFont.Font(size=20)
try:
    with open('名单.txt', 'r', encoding='utf-8') as file:
        namelist = file.read()
        population = len(namelist.replace('\n', ' ').split())
except:
    namelist = '[错误]未找到名为"名单.txt"的文件！'
    population = 1

hugeframe1 = Frame(root)
bigframe = Frame(hugeframe1)
frame1 = LabelFrame(bigframe, text='名单')
frame2 = Frame(bigframe)
frame3 = LabelFrame(hugeframe1, text='结果')

sb1 = Scrollbar(frame1)
sb1.pack(side=RIGHT, fill=Y)
t1 = Text(frame1, padx=10, pady=10, width=30, height=20, yscrollcommand=sb1.set, font=ft)
t1.pack(side=TOP)
t1.insert(END, namelist)
sb1.config(command=t1.yview)
v1 = StringVar(value='识别出列表中共{0}人'.format(population))
Label(frame1, textvariable=v1).pack()

def checker(event):
    population = len(t1.get(0.1, END).replace('\n', ' ').split())
    v1.set('识别出列表中共{0}人'.format(population))

t1.bind('<Enter>', checker)
t1.bind('<Leave>', checker)
t1.bind('<Button-1>', checker)
t1.bind('<KeyPress>', checker)

def picker():
    test()
    contents = t1.get(1.0, END).replace('\n', ' ').split()
    try:
        rList = random.sample(contents, k=int(e1.get()))
    except:
        rList = ['无']
    t2.insert(END, '======== 抽取结果 ========\n')
    for each in range(len(rList)):
        t2.insert(END, '{0}: {1}\n'.format(each+1, rList[each]))

L5 = Label(frame2, text='===>', font=ft)
L5.pack(padx=10, pady=10)

sb2 = Scrollbar(frame3)
sb2.pack(side=RIGHT, fill=Y)
t2 = Text(frame3, padx=10, pady= 10, width=30, height=20, yscrollcommand=sb2.set, font=ft)
t2.pack(side=TOP)
sb2.config(command=t2.yview)

def swiper():
    t2.delete(1.0, END)
    
Button(frame3, text=' 清空 ', command=swiper).pack()

frame1.pack(padx=10, pady=10, side=LEFT)
frame2.pack(padx=10, pady=10, side=RIGHT)
bigframe.pack(side=LEFT)
frame3.pack(padx=10, pady=10, side=RIGHT)
hugeframe1.pack()

def positive():
    population = len(t1.get(0.1, END).replace('\n', ' ').split())
    test()
    if int(e1.get()) >= population:
        number = population
    else:
        number = int(e1.get())+1
    e1.delete(0, END)
    e1.insert(0, number)

def negative():
    population = len(t1.get(0.1, END).replace('\n', ' ').split())
    test()
    if int(e1.get()) <= 1:
        number = 1
    else:
        number = int(e1.get())-1
    e1.delete(0, END)
    e1.insert(0, number)

def test(event=None):
    population = len(t1.get(0.1, END).replace('\n', ' ').split())
    try:
        number = round(float(e1.get()))
        e1.delete(0, END)
        if number > population:
            if population == 0:
                e1.insert(0, 1)
            else:
                e1.insert(0, population)
        elif number <= 0:
            e1.insert(0, 1)
        else:
            e1.insert(0, number)
    except:
        e1.delete(0, END)
        e1.insert(0, 1)

hugeframe2 = Frame(root)
Label(hugeframe2, text='抽取数量：').pack(side=LEFT)
bigframe2 = Frame(hugeframe2)
Button(bigframe2, text='<', height=1, command=negative).pack(side=LEFT)
Button(bigframe2, text='>', height=1, command=positive).pack(side=RIGHT)
e1 = Entry(bigframe2, width=5, font=ft, validate='focus', validatecommand=test)
e1.insert(0, 1)

e1.bind('<Enter>', test)
e1.bind('<Leave>', test)
e1.bind('<Button-1>', test)
e1.bind('<KeyPress>', test)

e1.pack()
bigframe2.pack()
hugeframe2.pack()

b1 = Button(root, text=' 点击抽取 ', command=picker, font=ft, bg='lightgray')
b1.pack(padx=10, pady=10)

mainloop()
