from Tkinter import *
from ttk import Notebook
from functools import partial
from hallDeEntrada import *

class Note_CM:
    def __init__(self, master, principal):
        self.objHall = HallDeEntrada()

        #Frame Criar Motorista
        self.frameCriarMotorista = Frame(principal, width=720, height=480)
        self.frameCriarMotorista.pack()

        self.lbNomeAba = Label(self.frameCriarMotorista, text='Criar Motorista', width=11, height=2, font='Arial, 14')
        self.lbNomeAba.grid(row=0, column=0)

        self.lbID_CM = Label(self.frameCriarMotorista, text='ID:', font='Arial, 11')
        self.lbID_CM.grid(row=1, column=0, sticky=E)
        self.edID_CM = Entry(self.frameCriarMotorista, width=85)
        self.edID_CM.grid(row=1, column=1, sticky=W)

        self.lbCPF_CM = Label(self.frameCriarMotorista, text='CPF:', font='Arial, 11')
        self.lbCPF_CM.grid(row=2, column=0, sticky=E)
        self.edCPF_CM = Entry(self.frameCriarMotorista, width=85)
        self.edCPF_CM.grid(row=2, column=1, sticky=W)

        self.lbNome_CM = Label(self.frameCriarMotorista, text='Nome:', font='Arial, 11')
        self.lbNome_CM.grid(row=3, column=0, sticky=E)
        self.edNome_CM = Entry(self.frameCriarMotorista, width=85)
        self.edNome_CM.grid(row=3, column=1, sticky=W)

        self.lbIdade_CM = Label(self.frameCriarMotorista, text='Idade:', font='Arial, 11')
        self.lbIdade_CM.grid(row=4, column=0, sticky=E)
        self.edIdade_CM = Entry(self.frameCriarMotorista, width=85)
        self.edIdade_CM.grid(row=4, column=1, sticky=W)

        self.lbSalario_CM = Label(self.frameCriarMotorista, text='Salario:', font='Arial, 11')
        self.lbSalario_CM.grid(row=6, column=0, sticky=E)
        self.edSalario_CM = Entry(self.frameCriarMotorista, width=85)
        self.edSalario_CM.grid(row=6, column=1, sticky=W)

        self.lbTelefone_CM = Label(self.frameCriarMotorista, text='Telefone:', font='Arial, 11')
        self.lbTelefone_CM.grid(row=7, column=0, sticky=E)
        self.edTelefone_CM = Entry(self.frameCriarMotorista, width=85)
        self.edTelefone_CM.grid(row=7, column=1, sticky=W)

        self.lbEmail_CM = Label(self.frameCriarMotorista, text='Email:', font='Arial, 11')
        self.lbEmail_CM.grid(row=8, column=0, sticky=E)
        self.edEmail_CM = Entry(self.frameCriarMotorista, width=85)
        self.edEmail_CM.grid(row=8, column=1, sticky=W)

        self.lbEstado_CM = Label(self.frameCriarMotorista, text='Estado:', font='Arial, 11')
        self.lbEstado_CM.grid(row=10, column=0, sticky=E)
        self.edEstado_CM = Entry(self.frameCriarMotorista, width=85)
        self.edEstado_CM.grid(row=10, column=1, sticky=W)

        self.lbCidade_CM = Label(self.frameCriarMotorista, text='Cidade:', font='Arial, 11')
        self.lbCidade_CM.grid(row=11, column=0, sticky=E)
        self.edCidade_CM = Entry(self.frameCriarMotorista, width=85)
        self.edCidade_CM.grid(row=11, column=1, sticky=W)

        self.lbBairro_CM = Label(self.frameCriarMotorista, text='Bairro:', font='Arial, 11')
        self.lbBairro_CM.grid(row=12, column=0, sticky=E)
        self.edBairro_CM = Entry(self.frameCriarMotorista, width=85)
        self.edBairro_CM.grid(row=12, column=1, sticky=W)

        self.lbRua_CM = Label(self.frameCriarMotorista, text='Rua:', font='Arial, 11')
        self.lbRua_CM.grid(row=13, column=0, sticky=E)
        self.edRua_CM = Entry(self.frameCriarMotorista, width=85)
        self.edRua_CM.grid(row=13, column=1, sticky=W)

        self.lbNumeroCasa_CM = Label(self.frameCriarMotorista, text='Numero da Casa:', font='Arial, 11')
        self.lbNumeroCasa_CM.grid(row=14, column=0, sticky=E)
        self.edNumeroCasa_CM = Entry(self.frameCriarMotorista, width=85)
        self.edNumeroCasa_CM.grid(row=14, column=1, sticky=W)

        self.lbComplemento_CM = Label(self.frameCriarMotorista, text='Complemento:', font='Arial, 11')
        self.lbComplemento_CM.grid(row=15, column=0, sticky=E)
        self.edComplemento_CM = Entry(self.frameCriarMotorista, width=85)
        self.edComplemento_CM.grid(row=15, column=1, sticky=W)

        self.btContinuarCM = Button(self.frameCriarMotorista, text='Continuar')
        self.btContinuarCM['command'] = partial(self.objHall.criarMotorista, self.edID_CM, self.edCPF_CM, self.edNome_CM, self.edIdade_CM, self.edSalario_CM, self.edTelefone_CM, self.edEmail_CM, self.edEstado_CM, self.edCidade_CM, self.edBairro_CM, self.edRua_CM, self.edNumeroCasa_CM, self.edComplemento_CM)
        self.btContinuarCM.grid(row=16, column=1, sticky=E)

        principal.add(self.frameCriarMotorista, text='Motorista')
        principal.pack(fill=BOTH, expand=Y)

class Note_CV:
    def __init__ (self, master, principal):
        #Frame Criar Veiculo
        self.frameCriarVeiculo = Frame(principal, width=720, height=480)
        self.frameCriarVeiculo.pack()

        self.lbNomeAbaCriarVeiculo = Label(self.frameCriarVeiculo, text='Criar Veiculo', width=11, height=2, font='Arial, 14')
        self.lbNomeAbaCriarVeiculo.grid(row=0, column=0)

        self.lbID_CV = Label(self.frameCriarVeiculo, text='ID:', font='Arial, 11')
        self.lbID_CV.grid(row=1, column=0, sticky=E)
        self.edID_CV = Entry(self.frameCriarVeiculo, width=85)
        self.edID_CV.grid(row=1, column=1, sticky=W)

        self.lbPlaca_CV = Label(self.frameCriarVeiculo, text='Placa:', font='Arial, 11')
        self.lbPlaca_CV.grid(row=2, column=0, sticky=E)
        self.edPlaca_CV = Entry(self.frameCriarVeiculo, width=85)
        self.edPlaca_CV.grid(row=2, column=1, sticky=W)

        self.lbCor_CV = Label(self.frameCriarVeiculo, text='Cor:', font='Arial, 11')
        self.lbCor_CV.grid(row=3, column=0, sticky=E)
        self.edCor_CV = Entry(self.frameCriarVeiculo, width=85)
        self.edCor_CV.grid(row=3, column=1, sticky=W)

        self.lbCapacidade_CV = Label(self.frameCriarVeiculo, text='Capacidade:', font='Arial, 11')
        self.lbCapacidade_CV.grid(row=4, column=0, sticky=E)
        self.edCapacidade_CV = Entry(self.frameCriarVeiculo, width=85)
        self.edCapacidade_CV.grid(row=4, column=1, sticky=W)

        self.lbID_Motorista_CV = Label(self.frameCriarVeiculo, text='ID do Motorista:', font='Arial, 11')
        self.lbID_Motorista_CV.grid(row=5, column=0, sticky=E)
        self.edID_Motorista_CV = Entry(self.frameCriarVeiculo, width=85)
        self.edID_Motorista_CV.grid(row=5, column=1, sticky=W)

        self.btContinuarCV = Button(self.frameCriarVeiculo, text='Continuar')
        self.btContinuarCV['command'] = partial(self.objHall.criarVeiculo, self.edID_CV, self.edPlaca_CV, self.edCor_CV, self.edCapacidade_CV, self.edID_Motorista_CV)
        self.btContinuarCV.grid(row=6, column=1, sticky=E)

        principal.add(self.frameCriarVeiculo, text='Veiculo')
        principal.pack(fill=BOTH, expand=Y)

class Note_CC:
    def __init__(self, master, principal):
        #Frame Criar Carga
        self.frameCriarCarga = Frame(principal, width=720, height=480)
        self.frameCriarCarga.pack()

        self.lbNomeAbaCriarCarga = Label(self.frameCriarCarga, text='Criar Carga', width=11, height=2, font='Arial, 14')
        self.lbNomeAbaCriarCarga.grid(row=0, column=0)

        self.lbID_CC = Label(self.frameCriarCarga, text='ID:', font='Arial, 11')
        self.lbID_CC.grid(row=1, column=0, sticky=E)
        self.edID_CC = Entry(self.frameCriarCarga, width=10)
        self.edID_CC.grid(row=1, column=1, sticky=W)

        self.lbMaterial_CC = Label(self.frameCriarCarga, text='Material:', font='Arial, 11')
        self.lbMaterial_CC.place(x=260, y=50)
        self.edMaterial_CC = Entry(self.frameCriarCarga, width=35)
        self.edMaterial_CC.place(x=350, y=54)

        self.lbPeso_CC = Label(self.frameCriarCarga, text='Peso:', font='Arial, 11')
        self.lbPeso_CC.grid(row=3, column=0, sticky=E)
        self.edPeso_CC = Entry(self.frameCriarCarga, width=25)
        self.edPeso_CC.grid(row=3, column=1, sticky=W)

        self.lbPericulosidade_CC = Label(self.frameCriarCarga, text='Periculosidade:', font='Arial, 11')
        self.lbPericulosidade_CC.place(x=335, y=73)
        self.edPericulosidade_CC = Entry(self.frameCriarCarga, width=10)
        self.edPericulosidade_CC.place(x=472, y=77)

        self.lbTamanho_Conteiner_CC = Label(self.frameCriarCarga, text='Tamanho do Conteiner:', font='Arial, 11')
        self.lbTamanho_Conteiner_CC.grid(row=5, column=0, sticky=E)
        self.edTamanho_Conteiner_CC = Entry(self.frameCriarCarga, width=10)
        self.edTamanho_Conteiner_CC.grid(row=5, column=1, sticky=W)

        self.lbOrigem_CC = Label(self.frameCriarCarga, text='Origem:', font='Arial, 11')
        self.lbOrigem_CC.place(x=238, y=96)
        self.edOrigem_CC = Entry(self.frameCriarCarga, width=18)
        self.edOrigem_CC.place(x=327, y=99)

        self.lbDestino_CC = Label(self.frameCriarCarga, text='Destino:', font='Arial, 11')
        self.lbDestino_CC.place(x=444, y=96)
        self.edDestino_CC = Entry(self.frameCriarCarga, width=18)
        self.edDestino_CC.place(x=535, y=99)

        self.lbKm_Percorrido_CC = Label(self.frameCriarCarga, text='Km Percorrido:', font='Arial, 11')
        self.lbKm_Percorrido_CC.grid(row=8, column=0, sticky=E)
        self.edKm_Percorrido_CC = Entry(self.frameCriarCarga, width=85)
        self.edKm_Percorrido_CC.grid(row=8, column=1, sticky=W)

        self.lbDatas_CC = Label(self.frameCriarCarga, text='Datas:', font='Arial, 11')
        self.lbDatas_CC.grid(row=9, column=0, sticky=E)
        self.edDatas_CC = Entry(self.frameCriarCarga, width=85)
        self.edDatas_CC.grid(row=9, column=1, sticky=W)

        self.lbNome_Cliente_CC = Label(self.frameCriarCarga, text='Nome do Cliente:', font='Arial, 11')
        self.lbNome_Cliente_CC.grid(row=10, column=0, sticky=E)
        self.edNome_Cliente_CC = Entry(self.frameCriarCarga, width=85)
        self.edNome_Cliente_CC.grid(row=10, column=1, sticky=W)

        self.lbCPF_CC = Label(self.frameCriarCarga, text='CPF:', font='Arial, 11')
        self.lbCPF_CC.place(x=300, y=186)
        self.edCPF_CC = Entry(self.frameCriarCarga, width=25)
        self.edCPF_CC.place(x=370, y=190)

        self.lbNum_NotaFical_CC = Label(self.frameCriarCarga, text='Num_NotaFical:', font='Arial, 11')
        self.lbNum_NotaFical_CC.grid(row=12, column=0, sticky=E)
        self.edNum_NotaFical_CC = Entry(self.frameCriarCarga, width=18)
        self.edNum_NotaFical_CC.grid(row=12, column=1, sticky=W)

        self.lbTelefone_CC = Label(self.frameCriarCarga, text='Telefone:', font='Arial, 11')
        self.lbTelefone_CC.grid(row=13, column=0, sticky=E)
        self.edTelefone_CC = Entry(self.frameCriarCarga, width=85)
        self.edTelefone_CC.grid(row=13, column=1, sticky=W)

        self.lbEmail_CC = Label(self.frameCriarCarga, text='Email:', font='Arial, 11')
        self.lbEmail_CC.grid(row=14, column=0, sticky=E)
        self.edEmail_CC = Entry(self.frameCriarCarga, width=85)
        self.edEmail_CC.grid(row=14, column=1, sticky=W)

        self.lbSite_CC = Label(self.frameCriarCarga, text='Site:', font='Arial, 11')
        self.lbSite_CC.grid(row=15, column=0, sticky=E)
        self.edSite_CC = Entry(self.frameCriarCarga, width=85)
        self.edSite_CC.grid(row=15, column=1, sticky=W)

        self.lbEstado_CC = Label(self.frameCriarCarga, text='Estado:', font='Arial, 11')
        self.lbEstado_CC.grid(row=16, column=0, sticky=E)
        self.edEstado_CC = Entry(self.frameCriarCarga, width=8)
        self.edEstado_CC.grid(row=16, column=1, sticky=W)

        self.lbCidade_CC = Label(self.frameCriarCarga, text='Cidade:', font='Arial, 11')
        self.lbCidade_CC.place(x=238, y=278)
        self.edCidade_CC = Entry(self.frameCriarCarga, width=35)
        self.edCidade_CC.place(x=323, y=283)

        self.lbBairro_CC = Label(self.frameCriarCarga, text='Bairro:', font='Arial, 11')
        self.lbBairro_CC.grid(row=18, column=0, sticky=E)
        self.edBairro_CC = Entry(self.frameCriarCarga, width=85)
        self.edBairro_CC.grid(row=18, column=1, sticky=W)

        self.lbRua_CC = Label(self.frameCriarCarga, text='Rua:', font='Arial, 11')
        self.lbRua_CC.grid(row=19, column=0, sticky=E)
        self.edRua_CC = Entry(self.frameCriarCarga, width=85)
        self.edRua_CC.grid(row=19, column=1, sticky=W)

        self.lbNumero_Casa_CC = Label(self.frameCriarCarga, text='Numero da Casa:', font='Arial, 11')
        self.lbNumero_Casa_CC.grid(row=20, column=0, sticky=E)
        self.edNumero_Casa_CC = Entry(self.frameCriarCarga, width=85)
        self.edNumero_Casa_CC.grid(row=20, column=1, sticky=W)

        self.lbComplemento_CC = Label(self.frameCriarCarga, text='Complemento:', font='Arial, 11')
        self.lbComplemento_CC.grid(row=21, column=0, sticky=E)
        self.edComplemento_CC = Entry(self.frameCriarCarga, width=85)
        self.edComplemento_CC.grid(row=21, column=1, sticky=W)

        self.btContinuarCC = Button(self.frameCriarCarga, text='Continuar')
        self.btContinuarCC['command'] = partial(self.objHall.criarCarga, self.edID_CC, self.edMaterial_CC, self.edPeso_CC, self.edPericulosidade_CC, self.edTamanho_Conteiner_CC, self.edOrigem_CC, self.edDestino_CC, self.edKm_Percorrido_CC, self.edDatas_CC, self.edNome_Cliente_CC, self.edCPF_CC, self.edNum_NotaFical_CC, self.edTelefone_CC, self.edEmail_CC, self.edSite_CC, self.edEstado_CC, self.edCidade_CC, self.edBairro_CC, self.edRua_CC, self.edNumero_Casa_CC, self.edComplemento_CC)
        self.btContinuarCC.grid(row=22, column=1, sticky=E)

        principal.add(self.frameCriarCarga, text='Carga')
        principal.pack(fill=BOTH, expand=Y)


        #================================================================
