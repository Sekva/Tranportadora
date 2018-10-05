from Tkinter import *
from ttk import Notebook
from functools import partial
from GUI_Notebooks import *
from GUI_JanelasMenu import *

class GUI_Tudo(Note_CM, Note_CV, Note_CC):
    def __init__(self, master):
        self.master = master
        self.principal = Notebook(master)

        Note_CM.__init__(self, self.master, self.principal)
        Note_CV.__init__(self, self.master, self.principal)
        Note_CC.__init__(self, self.master, self.principal)


        menu = Menu(self.master)
        self.master.config(menu=menu)

        mBarFile = Menu(menu)
        mBarFile.add_command(label='Sair', command=self.sair)
        menu.add_cascade(label='Coisa', menu=mBarFile)

        mBarModMotorista = Menu(menu)
        mBarModMotorista.add_command(label='Idade', command=self.ChamarJanelaIdadeMotorista)
        mBarModMotorista.add_command(label='Anos de Trabalho', command=self.ChamarJanelaAnosTrabalhoMotorista)
        mBarModMotorista.add_command(label='Endereco', command=self.ChamarJanelaEnderecoMotorista)
        mBarModMotorista.add_command(label='Contato', command=self.ChamarJanelaContatoMotorista)
        mBarModMotorista.add_command(label='Salario', command=self.ChamarJanelaSalarioMotorista)
        mBarModMotorista.add_command(label='Disponibilidade', command=self.ChamarJanelaDisponibilidadeMotorista)
        mBarModMotorista.add_command(label='Remover Motorista', command=self.ChamarJanelaRemoverMotorista)
        menu.add_cascade(label='Motoristas', menu=mBarModMotorista)

        mBarModVeiculo = Menu(menu)
        mBarModVeiculo.add_command(label='Disponibilidade', command=self.ChamarJanelaDisponibilidadeVeiculo)
        mBarModVeiculo.add_command(label='Remover Veiculo', command=self.ChamarJanelaRemoverVeiculo)
        mBarModVeiculo.add_separator()
        mBarModVeiculo.add_command(label='Mudar Ponto Parada - Carga', command=self.ChamarJanelaAddPontoVeiculo)
        menu.add_cascade(label='Veiculos', menu=mBarModVeiculo)

        mBarHistorico = Menu(menu)
        mBarHistorico.add_command(label='Lista Motorista', command=self.ChamarJanelaMostrarMotorista)
        mBarHistorico.add_command(label='Lista Veiculos', command=self.ChamarJanelaMostrarVeiculo)
        mBarHistorico.add_command(label='Historico Principal', command=self.ChamarJanelaMostrarHistoricoPrincipal)
        mBarHistorico.add_command(label='Historico Cargas', command=self.ChamarJanelaMostrarHistoricoCarga)
        mBarHistorico.add_command(label='Historico Financeiro', command=self.ChamarJanelaMostrarHistoricoFinanceiro)
        menu.add_cascade(label='Listas/Historicos', menu=mBarHistorico)

    #Funcoes de chamada
    def ChamarJanelaIdadeMotorista(self):
        idadeM = Menus()
        idadeM.GUI_alterarMotoristaIdade()

    def ChamarJanelaAnosTrabalhoMotorista(self):
         AnosTrabalhoM = Menus()
         AnosTrabalhoM.GUI_alterarMotoristaAnosTrabalho()

    def ChamarJanelaEnderecoMotorista(self):
         EnderecoM = Menus()
         EnderecoM.GUI_alterarMotoristaEndereco()

    def ChamarJanelaContatoMotorista(self):
         ContatoM = Menus()
         ContatoM.GUI_alterarMotoristaContato()

    def ChamarJanelaSalarioMotorista(self):
         SalarioM = Menus()
         SalarioM.GUI_alterarMotoristaSalario()

    def ChamarJanelaDisponibilidadeMotorista(self):
         DisponibilidadeM = Menus()
         DisponibilidadeM.GUI_alterarMotoristaDisponibilidade()

    def ChamarJanelaRemoverMotorista(self):
         RemoverM = Menus()
         RemoverM.GUI_alterarMotoristaRemover()

    def ChamarJanelaDisponibilidadeVeiculo(self):
         DisponibilidadeV = Menus()
         DisponibilidadeV.GUI_alterarVeiculoDisponibilidade()

    def ChamarJanelaRemoverVeiculo(self):
         RemoverV = Menus()
         RemoverV.GUI_alterarVeiculoRemover()

    def ChamarJanelaAddPontoVeiculo(self):
         AddPontoV = Menus()
         AddPontoV.GUI_alterarVeiculoAddPonto()

    def ChamarJanelaMostrarMotorista(self):
        MostrarMotoristas = Menus()
        MostrarMotoristas.GUI_mostrarMotorista()

    def ChamarJanelaMostrarVeiculo(self):
        MostrarVeiculos = Menus()
        MostrarVeiculos.GUI_mostrarVeiculo()

    def ChamarJanelaMostrarHistoricoPrincipal(self):
        MostrarHistoricoPrincipal = Menus()
        MostrarHistoricoPrincipal.GUI_MostrarHistoricoPrincipal()

    def ChamarJanelaMostrarHistoricoCarga(self):
        MostrarHistoricoCarga = Menus()
        MostrarHistoricoCarga.GUI_MostrarHistoricoCarga()

    def ChamarJanelaMostrarHistoricoFinanceiro(self):
        MostrarHistoricoFinanceiro = Menus()
        MostrarHistoricoFinanceiro.GUI_MostrarHistoricoFinanceiro()

    def sair(self):
        exit()



root = Tk()
root.geometry('720x480')
root.resizable(0, 0)

gui = GUI_Tudo(root)
gui

root.mainloop()
