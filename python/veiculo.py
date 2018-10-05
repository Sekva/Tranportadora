from carga import *
from motorista import *

class Veiculo:
    def __init__ (self, idVeic, placa, cor, capacidade, idMotorista):
        self.idVeic = idVeic                        #str
        self.placa = placa                          #str
        self.cor = cor                              #str
        self.carga = []                             #lista
        self.capacidade = capacidade                #float
        self.disponibilidade = True                 #boolean
        self.idMotorista = idMotorista              #str

    #Adicionar carga po ID
    def addCarga(self, novaCarga):
        self.carga.append(novaCarga)

    #Remover Carga por indicie da lista Carga
    def removerCarga(self, indicieLista):
        self.carga.pop(indicieLista)

    #Modificar motorista do veiculo
    def modMotorista(self, novoIdMotorista):
        self.idMotorista = novoIdMotorista

    #Modificar disponibilidade
    def modDisponibilidade(self, novaDisponibilidade):
        self.disponibilidade = novaDisponibilidade

    #Funcao para auxilio no retorno
    def retornaCargaStr(self):
        lista = []
        for i in self.carga:
            lista.append(str(i.id))
        return str(lista)

    def infoParciais (self):
        return 'Placa: ' + str(self.placa) + '\nCor: ' + str(self.cor) + '\n\t' + str(self.idMotorista)

    def infoCompleta (self):
        return 'ID: ' + str(self.idVeic) + '\nPlaca: ' + str(self.placa) + '\nCor: ' + str(self.cor) + '\nCargas: \n\t' + str(self.retornaCargaStr()) + '\nCapacidade: ' + str(self.capacidade) + '\nDisponibilidade: ' + str(self.disponibilidade) + '\nMotorista: \n\t' + str(self.idMotorista)
