from tkinter import *

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
        aken = Canvas(raam, width=170, height=600, background="white")
        Estonia(aken)
        Noname(aken)
        aken.pack(side=LEFT, padx=10, pady=10)


def Estonia(aken):
    aken.create_line(0, 0, 70, 0, 170, 40, 0, 40, 0, 0)
    aken.create_rectangle(0, 0, 170, 40, fill="#0072c6")
    aken.create_line(0, 40, 170, 40, 170, 80, 0, 80, 0, 40)
    aken.create_rectangle(0, 40, 170, 80, fill="#000000")
    aken.create_line(0, 80, 170, 80, 170, 120, 0, 120, 0, 80)

def Noname(aken):
    aken.create_rectangle(0, 100, 500, 140, fill="#2ca3c7")
    aken.create_rectangle(0, 140, 500, 180, fill="Yellow")
    aken.create_rectangle(0, 180, 500, 220, fill="#2ca3c7")
    aken.create_polygon([0,70],[0,190],[70,130],fill="black")

    #tahvel.create_polygon([300,60],[300,180],[370,120],fill="black")


aken = Tk()
aken.title("Erinevad nupud")
aken.geometry("200x200")

var = IntVar()

r1 = Radiobutton(aken, text="Esimene (Flags)", variable=var, value=1, command=valik)
r2 = Radiobutton(aken, text="Teine", variable=var, value=2)
r3 = Radiobutton(aken, text="Kolmas", variable=var, value=3)

lbox = Listbox(aken, height=3, width=33)

lbox.grid(row=0, column=0, columnspan=2)
r1.grid(row=1, column=0)
r2.grid(row=2, column=0)
r3.grid(row=3, column=0)

aken.mainloop()
