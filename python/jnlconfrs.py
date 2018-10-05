from Tkinter import *

class Janelinhapop:

    def __init__(self, master, strings):
        self.master = master

        self.frame = Frame(master, width=300, height=100)
        self.frame.pack()


        self.texto = Label(self.frame, text=strings)
        self.texto.pack(fill=BOTH, expand=True, pady=5)

        self.butaum = Button(self.frame, text="OK", width=3, height=1, command=self.fechar)
        self.butaum.pack(expand=True, pady=15)


    def fechar(self):
        self.master.destroy()


class ChamaPopopizinho:

    def __init__(self):
        self.texto = ""


    def definirPopopizinho(self, codigo):
        if(codigo == 0):
            self.texto = "Sucesso!"
        elif(codigo == 1):
            self.texto = "ID em uso"
        elif(codigo == 2):
            self.texto = "CPF em uso"
        elif(codigo == 3):
            self.texto = "Formato de idade incorreto"
        elif(codigo == 4):
            self.texto = "Formato de salario incorreto"
        elif(codigo == 5):
            self.texto = "Formato de periculozidade incorreto"
        elif(codigo == 6):
            self.texto = "Formato de tamanho incorreto"
        elif(codigo == 7):
            self.texto = "Formato de km incorreto"
        elif(codigo == 8):
            self.texto = "Formato de nota fiscal incorreto"
        elif(codigo == 9):
            self.texto = "Nota fiscal ja em uso"
        elif(codigo == 10):
            self.texto = "ID invalido"
        elif(codigo == 11):
            self.texto = "ID ou disponibilidade fornecidos incorretamente"
        elif(codigo == 12):
            self.texto = "Formato de posicao de carga incorreto"
        elif(codigo == 13):
            self.texto = "Sem motorista disponivel"
        elif(codigo == 14):
            self.texto = "Sem veiculo disponivel"
        elif(codigo == 15):
            self.texto = "Erro na mudanca de disponibilidade do veiculo"
        elif(codigo == 16):
            self.texto = "Erro na mudanca de disponibilidade do motorista"
        elif(codigo == 17):
            self.texto = "Formato de toneladas incorreto"
        elif(codigo == 18):
            self.texto = "ID invalido ou nao ha cargas registradas"
        else:
            self.texto = "Erro desconhecido"

        self.root = Tk()
        self.root.resizable(0,0)
        self.root.geometry("300x100")
        self.coisa = Janelinhapop(self.root, self.texto)
        self.root.mainloop()
