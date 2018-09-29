from Tkinter import *
from hallDeEntrada import *



class Janelinham:

    def __init__(self, master):

        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.q = StringVar()
        self.w = StringVar()
        self.e = StringVar()
        self.f = StringVar()
        self.g = StringVar()
        self.h = StringVar()
        self.j = StringVar()
        self.idt = Entry(self.frame, width=10,  textvariable=self.q)
        self.idt.grid(row=1, column=1)
        self.idadet = Entry(self.frame, width=10, textvariable=self.w)
        self.idadet.grid(row=2, column=1)
        self.asd = Entry(self.frame, width=10, textvariable=self.e)
        self.asd.grid(row=3, column=1)
        self.asdf = Entry(self.frame, width=10, textvariable=self.f)
        self.asdf.grid(row=4, column=1)
        self.asdq = Entry(self.frame, width=10, textvariable=self.g)
        self.asdq.grid(row=5, column=1)
        self.asdfag = Entry(self.frame, width=10, textvariable=self.h)
        self.asdfag.grid(row=6, column=1)
        self.hjff = Entry(self.frame, width=10, textvariable=self.j)
        self.hjff.grid(row=7, column=1)

        self.bu = Button(self.frame, text="123",  width=1, height=1, command=self.coisar)
        self.bu.grid(row=8, column=1)

        self.hall = HallDeEntrada()

    def coisar(self):
        print self.hall.mudarDisponibilidadeVeic(self.q, self.w)

root = Tk()
Janelinham(root)
root.mainloop()
