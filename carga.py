from cliente import *
from contato import *

class Carga:
    def __init__(self, idCarga, material, peso, origem, destino, periculosidade, tamanhoConteiner, kmPercorrido, datas, cliente):
        self.material = material                                         #str
        self.peso = float(peso)                                                #flt
        self.origem = origem                                             #str
        self.destino = destino                                           #str
        self.periculosidade = int(periculosidade)                             #int
        if(self.periculosidade == 1):
            self.taxa = 1
        elif(self.periculosidade == 2):
            self.taxa = 1.1
        elif(self.periculosidade == 3):
            self.taxa = 1.18
        elif(self.periculosidade == 4):
            self.taxa = 1.25
        elif(self.periculosidade == 5):
            self.taxa = 1.3
        elif(self.periculosidade == 6):
            self.taxa = 1.4
        else:
            self.taxa = 1
            print "\nPericulosidade incorreta, atribuido 0%\n"
        self.tamanhoConteiner = float(tamanhoConteiner)                         #flt
        self.kmPercorrido = float(kmPercorrido)                                 #flt
        self.custoDeTrasporte = (1000 + 3*self.kmPercorrido) * self.taxa      #flt
        self.pontosDeParada = []                                         #lista str
        self.datas = datas                                               #str
        self.id = idCarga                   					         #int
        self.cliente = cliente                                           #cliente


    #Modificar a quilometragem percorrida no transporte
    def modKmPercorrido(self, novoKmPercorrido):
        self.kmPercorrido = novoKmPercorrido

    #Adicionar um novo ponto de parada
    def addPontoDeParada(self, novoPontoDeParada):
        self.pontosDeParada.append(str(novoPontoDeParada))

    def calcularCustoTransporte(self, valorCustoTransporte):
        self.custoTransporte = valorCustoTransporte

    def __str__(self):
        return "Info: \n\tMaterial: " + str(self.material) + "\n\tPeso: " + str(self.peso) + "\n\tOrigem: " + str(self.origem) + "\n\tDestino: " + str(self.destino) + "\n\tPericulosidade: " + str(self.periculosidade) + "\n\tTamanho do container: " + str(self.tamanhoConteiner) + "\n\tDistancia percorrida: " + str(self.kmPercorrido) + "Km\n\tCliente: " + str(self.cliente.infoCompleta()) + "\n"

    def infoCompleta(self):
        return "Info Completa: \n\n" + "\tMaterial: " + str(self.material) + "\n\tPeso: " + str(self.peso) + "\n" + "\tOrigem: " + str(self.origem) + "\n" + "\tDestino: " + str(self.destino) + "\n" + "\tpericulosidade: " + str(self.periculosidade) + "\n\tTamanho do container: " + str(self.tamanhoConteiner) + "\n\tDistancia percorrida: " + str(self.kmPercorrido) + "Km\n\tCliente: " + str(self.cliente.infoCompleta()) + "\n\tCusto de Tranporte: " + str(self.custoDeTrasporte) + "\n\tPontos de parada: " + str(self.pontosDeParada) + "\n\tDatas: " + str(self.datas) + "\n"
