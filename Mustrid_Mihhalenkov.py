from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks

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


#Синий
tahvel.create_rectangle(800, 60, 600, 120, fill="Blue")
#Желтый
tahvel.create_rectangle(800, 120, 600, 180, fill="Yellow")






raam.mainloop()

