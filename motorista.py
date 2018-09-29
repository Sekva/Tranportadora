from contato import *
from endereco import *

class Motorista:
    def __init__ (self, idMoto, cpf, nome, idade, anosTrabalho, contato, endereco, salario):
        self.idMoto = idMoto                    #int
        self.cpf = cpf                          #str
        self.nome = nome                        #str
        self.idade = idade                      #int
        self.anosTrabalho = anosTrabalho        #int
        self.salario = salario                  #float
        self.disponibilidade = True             #boolean
        self.contato = contato                  #Contato
        self.endereco = endereco                #Endereco

    #Modificar a idade
    def modIdade(self, novaIdade):
        self.idade = novaIdade

    #Modificar os anos de trabalho
    def modAnosTrabalho(self, novoAnosTrabalho):
        self.anosTrabalho = novoAnosTrabalho

    #Modificar o salario
    def modSalario(self, novoSalario):
        self.salario = novoSalario

    #Modificar disponibilidade em booleano (True/False)
    def modDisponibilidade(self, novaDisponibilidade):
        self.disponibilidade = novaDisponibilidade

    def infoParciais (self):
        return 'ID: ' + str(self.idMoto) + '\nNome: ' + str(self.nome) + '\nIdade: ' + str(self.idade) + '\nAnos de Trabaho: ' + str(self.anosTrabalho) + '\nTelefone para contato: ' + str(self.contato) + '\n'

    def infoCompleta (self):
        return 'ID: ' + str(self.idMoto) + '\nCPF: ' + str(self.cpf) + '\nNome: ' + str(self.nome) + '\nIdade: ' + str(self.idade) + '\nAnos de Trabaho: ' + str(self.anosTrabalho) + '\nContato: ' + str(self.contato) + '\nEndereco: ' + str(self.endereco) + '\nSalario: ' + str(self.salario)
