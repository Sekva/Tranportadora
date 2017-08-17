from contato import *
from endereco import *

class Cliente:
    def __init__(self, nome, cpf, contato, endereco, numNotaFiscal):
        self.nome = nome                            #str
        self.cpf = cpf                              #str
        self.numNotaFiscal = numNotaFiscal          #int
        self.contato = contato                      #contato
        self.endereco = endereco                    #endereco

    def infoParciais(self):
        return "\n\t\tNome: " + str(self.nome) + "\n\t\tContato: " + str(self.contato.infoCompleta()) + "\n\t\tEndereco: " + str(self.endereco) + "\n\t\tNota Fiscal: " + str(self.numNotaFiscal)

    def infoCompleta(self):
        return "Info: \n\t\tNome: " + str(self.nome) + "\n\tContato: " + str(self.contato.infoCompleta()) + "\n\t\tEndereco: " + str(self.endereco.infoCompleta()) + "\n\tNota Fiscal: " + str(self.numNotaFiscal) + "\n\t\tCpf: " + str(self.cpf)
