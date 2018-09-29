from motorista import *
from contato import *
from endereco import *
from gerenciador_BD import *

class CadastrarMotorista:

        def cadastrarMotorista(self, telefone, email, site, estado, cidade, bairro, rua, numeroCasa, complemento, idMoto, cpf, nome, idade, anosTrabalhando, salario):

            #Cria endereco e contato
            contato = Contato(telefone, email, site)
            endereco = Endereco(estado, cidade, bairro, rua, numeroCasa, complemento)

            #Criar o objeto
            motorista = Motorista(idMoto, cpf, nome, idade, anosTrabalhando, contato, endereco, salario)
            #Gravar no BD os atributos do obj
            bd = Gerenciador_BD()
            bd.colocarMotorista(motorista.idMoto, motorista.cpf,  motorista.nome, motorista.idade, motorista.anosTrabalho, motorista.contato.telefone, motorista.contato.email, motorista.contato.site, motorista.endereco.estado, motorista.endereco.cidade, motorista.endereco.bairro, motorista.endereco.rua, motorista.endereco.numeroCasa, motorista.endereco.complemento, motorista.salario, motorista.disponibilidade)

            return motorista
