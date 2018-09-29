from Tkinter import *
from ttk import Notebook
from functools import partial
from hallDeEntrada import *
from gerenciador_BD import *

class Menus:
    def __init__(self):
        self.objHall = HallDeEntrada()

        self.root = Tk()

        self.lbID = Label(self.root, text='ID:', font='Arial, 11')
        self.lb = Label(self.root, font='Arial, 11')
        self.lbEstado = Label(self.root, text='Estado:', font='Arial, 11')
        self.lbCidade = Label(self.root, text='Cidade:', font='Arial, 11')
        self.lbBairro = Label(self.root, text='Bairro:', font='Arial, 11')
        self.lbRua = Label(self.root, text='Rua:', font='Arial, 11')
        self.lbNumCasa = Label(self.root, text='Num Casa:', font='Arial, 11')
        self.lbComplemento = Label(self.root, text='Complemento:', font='Arial, 11')
        self.lbTelefone = Label(self.root, text='Telefone:', font='Arial, 11')
        self.lbEmail = Label(self.root, text='Email:', font='Arial, 11')
        self.lbDisponibilidade = Label(self.root, text='0=Ocupado  |  1=Livre', font='Arial, 8')

        self.edID = Entry(self.root, width=15)
        self.ed = Entry(self.root, width=15)
        self.edEstado = Entry(self.root, width=40)
        self.edCidade = Entry(self.root, width=40)
        self.edBairro = Entry(self.root, width=40)
        self.edRua = Entry(self.root, width=40)
        self.edNumCasa = Entry(self.root, width=15)
        self.edComplemento = Entry(self.root, width=40)
        self.edTelefone = Entry(self.root, width = 20)
        self.edEmail = Entry(self.root, width = 30)

        self.bt = Button(self.root, text='Continuar')

    #Janelas Motorista
    def GUI_alterarMotoristaIdade(self):
        self.root

        self.root.resizable(0, 0)
        self.root.geometry('170x80')
        self.root.title('Modificar Idade')

        self.lbID.grid(row=0, column=0, sticky=E)

        self.lb['text'] = 'Idade'
        self.lb.grid(row=1, column=0, sticky=E)

        self.edID.grid(row=0, column=1, sticky=W)

        self.ed.grid(row=1, column=1, sticky=W)

        self.bt['command'] = partial(self.IdadeMotorista)
        self.bt.grid(row=2, column=1, sticky=E)

        self.root.mainloop()

    def GUI_alterarMotoristaAnosTrabalho(self):

        self.root.resizable(0, 0)
        self.root.geometry('175x80')
        self.root.title('Anos de Trabalho')

        self.lbID.grid(row=0, column=0, sticky=E)

        self.lb['text'] = 'Anos'
        self.lb.grid(row=1, column=0, sticky=E)

        self.edID.grid(row=0, column=1, sticky=W)

        self.ed.grid(row=1, column=1, sticky=W)

        self.bt['command'] = partial(self.AnosTrabalhoMotorista)
        self.bt.grid(row=2, column=1, sticky=E)

        self.root.mainloop()

    def GUI_alterarMotoristaEndereco(self):

        self.root.resizable(0, 0)
        self.root.geometry('400x200')
        self.root.title('Modificar Endereco')
        self.lbID.grid(row=0, column=0, sticky=E)

        self.lbEstado.grid(row=1, column=0, sticky=E)
        self.lbCidade.grid(row=2, column=0, sticky=E)
        self.lbBairro.grid(row=3, column=0, sticky=E)
        self.lbRua.grid(row=4, column=0, sticky=E)
        self.lbNumCasa.grid(row=5, column=0, sticky=E)
        self.lbComplemento.grid(row=6, column=0, sticky=E)

        self.edID.grid(row=0, column=1, sticky=W)
        self.edEstado.grid(row=1, column=1, sticky=W)
        self.edCidade.grid(row=2, column=1, sticky=W)
        self.edBairro.grid(row=3, column=1, sticky=W)
        self.edRua.grid(row=4, column=1, sticky=W)
        self.edNumCasa.grid(row=5, column=1, sticky=W)
        self.edComplemento.grid(row=6, column=1, sticky=W)

        self.bt['command'] = partial(self.EnderecoMotorista)
        self.bt.grid(row=7, column=1, sticky=E)

        self.root.mainloop()

    def GUI_alterarMotoristaContato(self):

        self.root.resizable(0, 0)
        self.root.geometry('300x100')
        self.root.title('Modificar Contato')

        self.lbID.grid(row=0, column=0, sticky=E)
        self.lbTelefone.grid(row=1, column=0, sticky=E)
        self.lbEmail.grid(row=2, column=0, sticky=E)

        self.edID.grid(row=0, column=1, sticky=W)
        self.edTelefone.grid(row=1, column=1, sticky=W)
        self.edEmail.grid(row=2, column=1, sticky=W)

        self.bt['command'] = partial(self.ContatoMotorista)
        self.bt.grid(row=3, column=1, sticky=E)

        self.root.mainloop()

    def GUI_alterarMotoristaSalario(self):

        self.root.resizable(0, 0)
        self.root.geometry('180x85')
        self.root.title('Modificar Salario')

        self.lbID.grid(row=0, column=0, sticky=E)
        self.lb['text'] = 'Salario'
        self.lb.grid(row=1, column=0, sticky=E)

        self.edID.grid(row=0, column=1, sticky=W)
        self.ed.grid(row=1, column=1, sticky=W)

        self.bt['command'] = partial(self.SalarioMotorista)
        self.bt.grid(row=2, column=1, sticky=E)

        self.root.mainloop()

    def GUI_alterarMotoristaDisponibilidade(self):

        self.root.resizable(0, 0)
        self.root.geometry('210x110')
        self.root.title('Disponibilidade')

        self.lbID.grid(row=0, column=0, sticky=E)
        self.lb['text'] = 'Disponibilidade:'
        self.lb.grid(row=1, column=0)
        self.lbDisponibilidade.grid(row=2, columnspan=2)

        self.edID.grid(row=0, column=1, sticky=W)
        self.ed.grid(row=1, column=1)

        self.bt['command'] = partial(self.DisponibilidadeMotorista)
        self.bt.grid(row=3, column=1, sticky=E)

        self.root.mainloop()

    def GUI_alterarMotoristaRemover(self):

        self.root.resizable(0, 0)
        self.root.geometry('130x50')
        self.root.title('Remover')

        self.lbID.grid(row=0, column=0, sticky=E)

        self.edID.grid(row=0, column=1, sticky=W)

        self.bt['command'] = partial(self.RemoverMotorista)
        self.bt.grid(row=1, column=1, sticky=E)

        self.root.mainloop()

    #Janelas Veiculos
    def GUI_alterarVeiculoDisponibilidade(self):

        self.root.resizable(0, 0)
        self.root.geometry('210x110')
        self.root.title('Disponibilidade')

        self.lbID.grid(row=0, column=0, sticky=E)
        self.lb['text'] = 'Disponibilidade:'
        self.lb.grid(row=1, column=0)
        self.lbDisponibilidade.grid(row=2, columnspan=2)

        self.edID.grid(row=0, column=1, sticky=W)
        self.ed.grid(row=1, column=1)

        self.bt['command'] = partial(self.DisponibilidadeVeiculo)
        self.bt.grid(row=3, column=1, sticky=E)

        self.root.mainloop()

    def GUI_alterarVeiculoRemover(self):

        self.root.resizable(0, 0)
        self.root.geometry('130x50')
        self.root.title('Remover')

        self.lbID.grid(row=0, column=0, sticky=E)

        self.edID.grid(row=0, column=1, sticky=W)

        self.bt['command'] = partial(self.RemoverVeiculo)
        self.bt.grid(row=1, column=1, sticky=E)

        self.root.mainloop()

    def GUI_alterarVeiculoAddPonto(self):

        self.root.resizable(0, 0)
        self.root.geometry('190x90')
        self.root.title('Mudar Ponto_Carga')

        self.lbID.grid(row=0, column=0, sticky=E)

        self.edID.grid(row=0, column=1, sticky=W)

        self.lb['text'] = 'Ponto'
        self.lb.grid(row=2, column=0, sticky=E)

        self.ed.grid(row=2, column=1, sticky=W)

        self.bt['command'] = partial(self.AddPontoVeiculo)
        self.bt.grid(row=3, column=1, sticky=E)

        self.root.mainloop()

    def GUI_mostrarMotorista(self):
        self.root.resizable(0, 0)
        self.root.geometry('1000x600')
        self.root.title('Mostrar Motoristas')

        scrollBar = Scrollbar(self.root)
        T = Text(self.root)

        T.focus_set()
        scrollBar.pack(side=RIGHT, fill=Y)
        T.pack(fill=BOTH, expand=Y)
        scrollBar.config(command=T.yview)
        T.config(yscrollcommand=scrollBar.set)

        for i in self.objHall.todosMotoristas():
           T.insert(END, i)
           T.insert(END, "\n============================================================================================================================================")

        self.root.mainloop()

    def GUI_mostrarVeiculo(self):
        self.root.resizable(0, 0)
        self.root.geometry('1000x600')
        self.root.title('Mostrar Veiculos')

        scrollBar = Scrollbar(self.root)
        T = Text(self.root)

        T.focus_set()
        scrollBar.pack(side=RIGHT, fill=Y)
        T.pack(fill=BOTH, expand=Y)
        scrollBar.config(command=T.yview)
        T.config(yscrollcommand=scrollBar.set)

        for i in self.objHall.todosVeiculos():
           T.insert(END, i)
           T.insert(END, "\n============================================================================================================================================")

        self.root.mainloop()

    def GUI_MostrarHistoricoPrincipal(self):
        self.root.resizable(0, 0)
        self.root.geometry('1000x600')
        self.root.title('Mostrar Historico Geral')

        scrollBar = Scrollbar(self.root)
        T = Text(self.root)

        T.focus_set()
        scrollBar.pack(side=RIGHT, fill=Y)
        T.pack(fill=BOTH, expand=Y)
        scrollBar.config(command=T.yview)
        T.config(yscrollcommand=scrollBar.set)

        for i in self.objHall.mostrarHistorico():
           T.insert(END, i)
           T.insert(END, "\n============================================================================================================================================")

        self.root.mainloop()

    def GUI_MostrarHistoricoCarga(self):
        msg = Label(self.root, text='=-=Em construcao=-=', font='Arial, 18')
        msg.pack()
        '''
        self.root.resizable(0, 0)
        self.root.geometry('1000x600')
        self.root.title('Mostrar Historico Cargas')

        scrollBar = Scrollbar(self.root)
        T = Text(self.root)

        T.focus_set()
        scrollBar.pack(side=RIGHT, fill=Y)
        T.pack(fill=BOTH, expand=Y)
        scrollBar.config(command=T.yview)
        T.config(yscrollcommand=scrollBar.set)

        for i in self.objHall.mostrarHistorico():
           T.insert(END, i)
           T.insert(END, "\n============================================================================================================================================")

        self.root.mainloop()
        '''

    def GUI_MostrarHistoricoFinanceiro(self):
        self.root.resizable(0, 0)
        self.root.geometry('1000x600')
        self.root.title('Mostrar Historico Financeiro')

        scrollBar = Scrollbar(self.root)
        T = Text(self.root)

        T.focus_set()
        scrollBar.pack(side=RIGHT, fill=Y)
        T.pack(fill=BOTH, expand=Y)
        scrollBar.config(command=T.yview)
        T.config(yscrollcommand=scrollBar.set)

        for i in self.objHall.parteFiscal():
           T.insert(END, i)
           T.insert(END, "\n============================================================================================================================================")


        root2 = Tk()

        root2.resizable(0, 0)
        root2.geometry('200x90')
        root2.title('Previsao Financeira')

        L = self.objHall.parteFiscal()
        cont = 0
        for i in range(len(L)):
            cont += float(L[i][2])

        mensal = Label(root2, text='Previa Mensal: R$ '+ str(cont*30), font='Arial, 12', height=2)
        anual = Label(root2, text='Previa Anual: R$ '+ str(cont*365), font='Arial, 12')
        mensal.pack()
        anual.pack()

        root2.mainloop()

        self.root.mainloop()


    #Funcoes de chamada
    def IdadeMotorista(self):
        self.objHall.modIdadeMotorista(self.edID, self.ed)

    def AnosTrabalhoMotorista(self):
        self.objHall.modAnosTrabalhoMotorista(self.edID, self.ed)

    def EnderecoMotorista(self):
        self.objHall.modEnderecoMotorista(self.edID, self.edEstado, self.edCidade, self.edBairro, self.edRua, self.edNumCasa, self.edComplemento)

    def ContatoMotorista(self):
        self.objHall.modEnderecoMotorista(self.edID, self.edTelefone, self.edEmail)

    def SalarioMotorista(self):
        self.objHall.modSalarioMotorista(self.edID, self.ed)

    def DisponibilidadeMotorista(self):
        self.objHall.mudarDisponibilidadeMoto(self.edID, self.ed)

    def RemoverMotorista(self):
        self.objHall.removerMotoristaDaGaragem(self.edID)

    def DisponibilidadeVeiculo(self):
        self.objHall.mudarDisponibilidadeVeic(self.edID, self.ed)

    def RemoverVeiculo(self):
        self.objHall.removerVeiculoDaGaragem(self.edID)

    def AddPontoVeiculo(self):
        self.objHall.addPontoParada(self.ed, self.edID)
