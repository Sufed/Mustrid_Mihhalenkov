from tkinter import *
from math import *
from random import *
from tkinter import font
#def valik_2():
#    val1=var1.get()
#    val2=var2.get()
#    val3=var3.get()
#    if val1=="-": lbox.insert(END,val1)
#    if val2=="-": lbox.insert(END,val2)
#    if val3=="-": lbox.insert(END,val3)

def valik():
    num = var.get()
    if num == 1:
        raam = Tk()
        raam.title("Flags")
        aken = Canvas(raam, width=170, height=450, background="white")
        Estonia(aken)
        Noname(aken)
        Ukraina(aken)
        aken.pack()
    elif num ==2:
        raam1 = Tk()
        raam1.title("Harjutus 2.")
        aken = Canvas(raam1, width=300, height=300, background="white")
        Kvadrat(aken)
        aken.pack()
    elif num == 3:
        raam2 = Tk()
        raam2.title("Harjutus 2.")
        aken = Canvas(raam2, width=300, height=300, background="white")
        sahmati(aken)
        aken.pack()
    elif num==4:
        raam2 = Tk()
        raam2.title("Harjutus 2.")
        aken = Canvas(raam2, width=600, height=600, background="white")
        krug(aken)
        aken.pack()
    elif num==5:
        raam2 = Tk()
        raam2.title("Harjutus 2.")
        aken = Canvas(raam2, width=500, height=500, background="white")
        Svetofor(aken)
        knopka1.grid(row=6, column=0)
        aken.pack()
    elif num==6:
        raam2 = Tk()
        raam2.title("Harjutus 2.")
        aken = Canvas(raam2, width=500, height=500, background="white")
        Svetofor1(aken)
        aken.pack()
        


def Estonia(aken):
    aken.create_line(0, 0, 70, 0, 170, 40, 0, 40, 0, 0)
    aken.create_rectangle(0, 0, 170, 40, fill="#0072c6")
    aken.create_line(0, 40, 170, 40, 170, 80, 0, 80, 0, 40)
    aken.create_rectangle(0, 40, 170, 80, fill="#000000")
    aken.create_line(0, 80, 170, 80, 170, 120, 0, 120, 0, 80)

def Noname(aken):
    aken.create_rectangle(0, 120, 500, 160, fill="#2ca3c7")
    aken.create_rectangle(0, 160, 500, 200, fill="Yellow")
    aken.create_rectangle(0, 200, 500, 240, fill="#2ca3c7")
    aken.create_polygon([0,120],[0,240],[100,180],fill="black")

def Ukraina(aken):
    aken.create_rectangle(0, 280, 500, 320, fill="Blue")
    aken.create_rectangle(0, 320, 500, 360, fill="Yellow")

def Kvadrat(aken):
    k = 10
    x0 = 0
    y0 = 0
    x1 = 300
    y1 = 300
    a = 150
    r = (a ** 2 + a ** 2) ** (1/2)
    p = (a - r)
    for i in range(k):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        aken.create_rectangle(x0, y0, x1, y1, width=1, outline="blue", fill="red")
        aken.create_oval(x0, y0, x1, y1, width=1, outline="blue", fill="yellow")  
        p = r - a
        r = r - p
        a = ((r) * sqrt(2)) / 2


def sahmati(aken):
    square_size = 35
    board_size = square_size * 8
    for i in range(8):
        for j in range(8):
            x1 = i * square_size
            y1 = j * square_size
            if (i + j) % 2 == 0:
                color = "white"
            else:
                color = "black"
                square = aken.create_rectangle(x1, y1, x1 + square_size, y1 + square_size, fill=color)


def krug(aken):
    colors=["black",
            "cyan",
            "red",
            "blue",
            "gray",
            "yellow",
            "green",
            "lightblue",
            "pink",
            "gold"]
    x0=0
    y0=0
    x1=600
    y1=600
    p=5
    for i in range(55):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
        aken.create_oval(x0,y0,x1,y1, fill=choice(colors))


def Svetofor(aken):
    aken.create_line(0,0,  0,400,  width=330 , fill="#a3a7ad")
    suur_font = font.Font(family='Algerian', size=20, weight='bold')
    aken.create_text(40, 0, text="Valgusfoor", font=suur_font, anchor=NW)
    aken.create_line(60,50,  100,50,  width=40 , fill="red")
    aken.create_line(60,100,  100,100,  width=40 , fill="yellow")
    aken.create_line(60,150,  100,150,  width=40 , fill="green")
    aken.create_line(80 ,180,  80,300,  width=8 , fill="black")
    aken.create_line(30,310,  140,310,  width=4 , fill="black")

def Svetofor1(aken):
    aken.create_line(0,0,  0,400,  width=330 , fill="#a3a7ad")
    suur_font = font.Font(family='Algerian', size=20, weight='bold')
    aken.create_text(40, 0, text="Valgusfoor", font=suur_font, anchor=NW)
    aken.create_line(60,50,  100,50,  width=40 , fill="yellow")
    aken.create_line(60,100,  100,100,  width=40 , fill="yellow")
    aken.create_line(60,150,  100,150,  width=40 , fill="yellow")
    aken.create_line(80 ,180,  80,300,  width=8 , fill="black")
    aken.create_line(30,310,  140,310,  width=4 , fill="black")


aken = Tk()
aken.title("Erinevad nupud")
aken.geometry("200x200")

var = IntVar()

r1 = Radiobutton(aken, text="Flags", variable=var, value=1, command=valik)
r2 = Radiobutton(aken, text="Ruut", variable=var, value=2, command=valik)
r3 = Radiobutton(aken, text="Шахматы", variable=var, value=3, command=valik)
r4 = Radiobutton(aken, text="Разноцветный круг", variable=var, value=4, command=valik)
r5 = Radiobutton(aken, text="Valgusfoor", variable=var, value=5, command=valik)
knopka1=Radiobutton(aken, text="Väljalülitatud valgusfoorid", variable=var, value=6, command=valik)

lbox = Listbox(aken, height=3, width=33)

lbox.grid(row=0, column=0, columnspan=2)
r1.grid(row=1, column=0)
r2.grid(row=2, column=0)
r3.grid(row=3, column=0)
r4.grid(row=4, column=0)
r5.grid(row=5, column=0)

aken.mainloop()

