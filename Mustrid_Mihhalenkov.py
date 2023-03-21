from re import A
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
import random
from math import *
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=1000, height=1000, background="white")
tahvel.grid()


#Canvas.create_line(x1, y1, x2, y2, ...., options = ...)


#Синий
tahvel.create_line(30,60,  100,60,  200,100,  30,100,  30,60)
tahvel.create_rectangle(30, 60, 200, 100, fill="#0072c6")
#Черный
tahvel.create_line(30,100, 200,100, 200,140, 30,140, 30,100)
tahvel.create_rectangle(30, 100, 200, 140, fill="#000000")
#Белый
tahvel.create_line(30,140, 200,140, 200,180, 30,180, 30,140)


#Бирюзовый
tahvel.create_rectangle(300, 60, 500, 100, fill="#2ca3c7")
#Желтый
tahvel.create_rectangle(300, 100, 500, 140, fill="Yellow")
#Бирюзовый
tahvel.create_rectangle(300, 140, 500, 180, fill="#2ca3c7")
#Треугольник
#tahvel.create_rectangle(300,60, 300,100, 300,60)( fill="Black")
tahvel.create_polygon([300,60],[300,180],[370,120],fill="black")


#Флаг Синий, Желтый
tahvel.create_rectangle(800, 60, 600, 120, fill="Blue")

tahvel.create_rectangle(800, 120, 600, 180, fill="Yellow")


#Светофор
tahvel.create_line(420,550,  770,550,  width=500 , fill="#a3a7ad")
suur_font = font.Font(family='Helvetica', size=20, weight='bold')
tahvel.create_text(490, 310, text="Valgusfoor", font=suur_font, anchor=NW)
tahvel.create_line(520,400,  570,400,  width=45 , fill="red")
tahvel.create_line(520,450,  570,450,  width=45 , fill="yellow")
tahvel.create_line(520,500,  570,500,  width=45 , fill="green")

tahvel.create_line(545 ,530,  545,750,  width=8 , fill="black")
tahvel.create_line(450,760,  630,760,  width=4 , fill="black")

square_size = 50
board_size = square_size * 8
y_offset = 200

#for i in range(8):
#    for j in range(8):
#        x1 = i * square_size
#        y1 = j * square_size + y_offset  # добавляем y_offset к координате y
#        if (i + j) % 2 == 0:
#            color = "white"
#        else:
#            color = "black"
#        square = tahvel.create_rectangle(x1, y1, x1 + square_size, y1 + square_size, fill=color)


#tahvel.pack()


k = 10
x0 = 0
y0 = 0
x1 = 300
y1 = 300
a = 150
r = (a ** 2 + a ** 2) ** (1/2)
p = (a - r)

# создаем фигуры
for i in range(k):
    x0 += p
    y0 += p
    x1 -= p
    y1 -= p
    tahvel.create_rectangle(x0, y0, x1, y1, width=1, outline="blue", fill="red")
    tahvel.create_oval(x0, y0, x1, y1, width=1, outline="blue", fill="yellow")  
    p = r - a
    r = r - p
    a = ((r) * sqrt(2)) / 2

raam.mainloop()

