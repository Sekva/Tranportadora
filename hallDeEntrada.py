from cliente import *
from veiculo import *
from endereco import *
from contato import *
from gerenciador_BD import *
from cadastrarCarga import *
from cadastrarVeiculo import *
from cadastrarMotorista import *
from jnlconfrs import *

class HallDeEntrada:

    def criarVeiculo(self, ID, PLACA, COR, CAPACIDADE, ID_MOTORISTA):
        try:
            print "[Cadastro Veiculo]"

            self.ID = str(ID.get())
            self.PLACA = str(PLACA.get())
            self.COR = str(COR.get())
            try:
                self.CAPACIDADE = float(CAPACIDADE.get())
            except:
                print "Formato de toneladas incorreto\n17"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(17)
                return 17

            self.ID_MOTORISTA = str(ID_MOTORISTA.get())

            self.bd = Gerenciador_BD()
            self.checkid = self.bd.retornarInfoVeiculo(self.ID)

            if (self.checkid == None):
                self.checkid = []

            if (len(self.checkid) > 2):
                print "ID em uso"
                print 1
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(1)
                return 1

            else:
                self.cadastraVeic = CadastrarVeiculo()
                self.v = self.cadastraVeic.cadastrarVeiculo(self.ID, self.PLACA, self.COR, self.CAPACIDADE, self.ID_MOTORISTA)
                print 0
                print "OK"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(0)
                return 0

        except:
            print "ERRO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88

    def criarMotorista(self, idMoto, cpf, nome, idade, salario, telefone, email, estado, cidade, bairro, rua, numeroCasa, complemento):
        try:
            print "Cadastro Motorista"
            self.idMoto = int(idMoto.get())
            self.cpf = str(cpf.get())

            self.bd = Gerenciador_BD()
            self.checkidcpf = self.bd.retornarInfoMotorista(self.idMoto)

            if (self.checkidcpf == None):
                self.checkidcpf = []

            print 'asd50'
            if(len(self.checkidcpf) > 2):
                print 1
                print "ID em uso"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(1)
                return 1
                if(self.cpf == self.checkidcpf[1]):
                    print "CPF ja usado, pessoas duplicadas nao existem, xeroqui rolmis."
                    print 2
                    self.c = ChamaPopopizinho()
                    self.c.definirPopopizinho(2)
                    return 2
            else:

                self.nome = str(nome.get())
                try:
                    self.idade = int(idade.get())
                except:
                    print "Formato de idade errado\n3"
                    self.c = ChamaPopopizinho()
                    self.c.definirPopopizinho(3)
                    return 3
                self.anosTrabalhando = '0'
                try:
                    self.salario = float(salario.get())
                except:
                    print "Formato de salario incorreto\n4"
                    self.c = ChamaPopopizinho()
                    self.c.definirPopopizinho(4)
                    return 4
                self.telefone = str(telefone.get())
                self.email = str(email.get())
                self.site = 'Nulo'
                self.estado = str(estado.get())
                self.cidade = str(cidade.get())
                self.bairro = str(bairro.get())
                self.rua = str(rua.get())
                self.numeroCasa = str(numeroCasa.get())
                self.complemento = str(complemento.get())
                print 'asd82'
                self.cadastrarMoto = CadastrarMotorista()
                self.m = self.cadastrarMoto.cadastrarMotorista(self.telefone, self.email, self.site, self.estado, self.cidade, self.bairro, self.rua, self.numeroCasa, self.complemento, self.idMoto, self.cpf, self.nome, self.idade, self.anosTrabalhando, self.salario)
                print 0
                print "OK"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(0)
                return 0

        except:
            print "ERRO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88

    def criarCarga(self, idCarga, material, peso, periculosidade, tamanhoConteiner, origem, destino, kmPercorrido, datas, nome, cpf, numNotaFiscal, telefone, email, site, estado, cidade, bairro, rua, numeroCasa, complemento):

        print "[Nova carga]"

        self.idCarga  = int(idCarga.get())

        #Confere se os dados sao validos
        self.bd = Gerenciador_BD()
        self.checkcarga = self.bd.retornarInfoCarga(self.idCarga)
        if (self.checkcarga == None):
            self.checkcarga = []

        if(len(self.checkcarga) !=0):
            print "ID de carga ja usado"
            print 1
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(1)
            return 1
        else:
            self.material = str(material.get())
            self.peso = str(peso.get())
            try:
                self.periculosidade = int(periculosidade.get())
            except:
                print "Formato de periculosidade incorreto\n5"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(5)
                return 5
            try:
                self.tamanhoConteiner = float(tamanhoConteiner.get())
            except:
                print "Formato de tamanh  incorreto\n6"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(6)
                return 6
            self.origem = str(origem.get())
            self.destino = str(destino.get())
            try:
                self.kmPercorrido = float(kmPercorrido.get())
            except:
                print "Formato de km incorreto\n7"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(7)
                return 7
            self.datas = str(datas.get())
            print '\n=-=Informacoes do Cliente=-='
            self.nome = str(nome.get())
            self.cpf = str(cpf.get())
            try:
                self.numNotaFiscal = int(numNotaFiscal.get())
            except:
                print "Formato de nota fiscal incorreto\n8"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(8)
                return 8

            if(self.bd.retornarNotasFiscais(self.numNotaFiscal)):
                print "Numero de nota fiscal ja usada"
                print 9
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(9)
                return 9

            else:

                self.telefone = str(telefone.get())
                self.email = str(email.get())
                self.site = str(site.get())
                self.estado = str(estado.get())
                self.cidade = str(cidade.get())
                self.bairro = str(bairro.get())
                self.rua = str(rua.get())
                self.numeroCasa = str(numeroCasa.get())
                self.complemento = str(complemento.get())

                #Escrever o custo de uma carga
                self.contato = Contato(self.telefone, self.email, self.site)
                self.endereco = Endereco(self.estado, self.cidade, self.bairro, self.rua, self.numeroCasa, self.complemento)
                self.cliente = Cliente(self.nome, self.cpf, self.contato, self.endereco, self.numNotaFiscal)

                #Pegar Motorista Disponivel
                self.listaMotorista = self.bd.retornarInfoMotoristaDisponivel()
                if (self.listaMotorista == None):
                    self.listaMotorista = []
                if(len(self.listaMotorista) == 0):
                    print "Sem motoristas disponiveis\n13"
                    self.c = ChamaPopopizinho()
                    self.c.definirPopopizinho(13)
                    return 13
                self.idMoto = self.listaMotorista[0]



                #Alterar status de disponibilidade do motorista
                self.contatoMotorista = Contato(self.listaMotorista[5], self.listaMotorista[6], "Nulo")
                self.enderecoMotorista = Endereco(self.listaMotorista[8], self.listaMotorista[9], self.listaMotorista[10], self.listaMotorista[11], self.listaMotorista[12], self.listaMotorista[13])
                self.motoristaObj = Motorista(self.idMoto, self.listaMotorista[1], self.listaMotorista[2], self.listaMotorista[3], self.listaMotorista[4], self.contatoMotorista, self.enderecoMotorista, self.listaMotorista[14])
                self.motoristaObj.modDisponibilidade(False)

                #Pegar Veiculo Disponivel
                self.listaVeiculo = self.bd.retornarInfoVeiculoDisponivel()
                print self.listaVeiculo
                print len(self.listaVeiculo)
                if(len(self.listaVeiculo) == 0):
                    print "Sem veiculos disponiveis\n14"
                    self.c = ChamaPopopizinho()
                    self.c.definirPopopizinho(14)
                    return 14

                #Salva a carga se tudo ok
                self.carga1 = CadastrarCarga()
                self.carga = self.carga1.cadastrarCarga(self.idCarga, self.material, self.peso, self.periculosidade, self.tamanhoConteiner, self.origem, self.destino, self.kmPercorrido, self.datas, self.cliente)
                self.bd.BDGastosGanhos(str(self.carga.custoDeTrasporte), self.cliente.numNotaFiscal, self.carga.id)

                #Atualizar status de disponibilidade do veiculo
                self.veiculoObj = Veiculo(self.listaVeiculo[0], self.listaVeiculo[1], self.listaVeiculo[2], self.listaVeiculo[3], self.idMoto)
                self.veiculoObj.modDisponibilidade(False)
                self.veiculoObj.addCarga(int(self.carga.id))

                self.bd.tirar("veiculos.txt", self.veiculoObj.idVeic)
                self.bd.colocarVeiculo(self.veiculoObj.idVeic, self.veiculoObj.placa, self.veiculoObj.cor, self.veiculoObj.capacidade, self.veiculoObj.carga, self.veiculoObj.disponibilidade,  self.veiculoObj.idMotorista)
                self.bd.tirar("motorista.txt", self.idMoto)
                self.bd.colocarMotorista(self.motoristaObj.idMoto, self.motoristaObj.cpf, self.motoristaObj.nome, self.motoristaObj.idade, self.motoristaObj.anosTrabalho, self.motoristaObj.contato.telefone, self.motoristaObj.contato.email, self.motoristaObj.contato.site, self.motoristaObj.endereco.estado, self.motoristaObj.endereco.cidade, self.motoristaObj.endereco.bairro, self.motoristaObj.endereco.rua, self.motoristaObj.endereco.numeroCasa, self.motoristaObj.endereco.complemento, self.motoristaObj.salario, self.motoristaObj.disponibilidade)
                self.bd.definirHistorico(self.veiculoObj.idVeic, self.veiculoObj.placa, self.motoristaObj.idMoto, self.motoristaObj.nome, self.motoristaObj.cpf, self.carga.id, self.carga.material, self.carga.peso, self.carga.origem, self.carga.destino, self.carga.periculosidade, self.carga.tamanhoConteiner, self.carga.kmPercorrido, self.carga.pontosDeParada, self.carga.datas, self.cliente)
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(0)
                return 0

    def mudarDisponibilidadeVeic(self, ID, condicao):
        try:
            self.ID = str(ID.get())
            self.condicao = int(condicao.get())

        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(11)

        #Recria o objeto mudando a disponibilidade de acordo com a condicao
        self.bd = Gerenciador_BD()
        self.listaVeiculo = self.bd.retornarInfoVeiculo(self.ID)
        try:
            if self.condicao == 0:
                self.condicao = False
            elif self.condicao == 1:
                self.condicao = True
            else:
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(15)
                return 15

            self.veiculoObj = Veiculo(self.listaVeiculo[0], self.listaVeiculo[1], self.listaVeiculo[2], self.listaVeiculo[3], self.listaVeiculo[6])
            self.veiculoObj.carga = self.listaVeiculo[4]
            self.veiculoObj.modDisponibilidade(bool(self.condicao))


            #Modifica na "garagem"
            self.bd.tirar("veiculos.txt", self.ID)
            self.bd.colocarVeiculo(self.veiculoObj.idVeic, self.veiculoObj.placa, self.veiculoObj.cor, self.veiculoObj.capacidade, self.veiculoObj.carga, self.veiculoObj.disponibilidade,  self.veiculoObj.idMotorista)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0

        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def mudarDisponibilidadeMoto(self, ID, condicao):
        try:
            self.ID = str(ID.get())
            self.condicao = int(condicao.get())
            print 1
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(11)
        #Recria o objeto mudando a disponibilidade de acordo com a condicao
        self.bd = Gerenciador_BD()
        self.listaMotorista = self.bd.retornarInfoMotorista(self.ID)

        try:
            if self.condicao == 0:
                self.condicao = False
            elif self.condicao == 1:
                self.condicao = True
            else:
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(16)
                return 16

            self.contatoMotorista = Contato(self.listaMotorista[5], self.listaMotorista[6], "Nulo")
            self.enderecoMotorista = Endereco(self.listaMotorista[8], self.listaMotorista[9], self.listaMotorista[10], self.listaMotorista[11], self.listaMotorista[12], self.listaMotorista[13])
            self.motoristaObj = Motorista(self.ID, self.listaMotorista[1], self.listaMotorista[2], self.listaMotorista[3], self.listaMotorista[4], self.contatoMotorista, self.enderecoMotorista, self.listaMotorista[14])
            self.motoristaObj.modDisponibilidade(bool(self.condicao))

            #Modifica na "garagem"
            self.bd.tirar("motorista.txt", self.ID)
            self.bd.colocarMotorista(self.motoristaObj.idMoto, self.motoristaObj.cpf, self.motoristaObj.nome, self.motoristaObj.idade, self.motoristaObj.anosTrabalho, self.motoristaObj.contato.telefone, self.motoristaObj.contato.email, self.motoristaObj.contato.site, self.motoristaObj.endereco.estado, self.motoristaObj.endereco.cidade, self.motoristaObj.endereco.bairro, self.motoristaObj.endereco.rua, self.motoristaObj.endereco.numeroCasa, self.motoristaObj.endereco.complemento, self.motoristaObj.salario, self.motoristaObj.disponibilidade)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0

        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def addCargaVeic(self, idCarga, idVeic, disponibilidade):
        try:
            self.idCarga = int(idCarga.get())
            self.idVeic = str(idVeic.get())
            self.disponibilidade = str(disponibilidade.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(11)

        #Recria os objetos carga e veiculo mudando o atributo carga em veiculo
        self.bd = Gerenciador_BD()
        self.listaCarga = self.bd.retornarInfoCarga(self.idCarga)
        try:
            self.listaVeiculo = self.bd.retornarInfoVeiculo(self.idVeic)
            self.veiculoObj = Veiculo(self.listaVeiculo[0], self.listaVeiculo[1], self.listaVeiculo[2], self.listaVeiculo[3], self.listaVeiculo[6])
            self.veiculoObj.carga = self.listaVeiculo[4]
            self.lista11 = []
            for i in range(len(self.veiculoObj.carga)):
                self.str1 = ""
                if self.veiculoObj.carga[i] == " ":
                    self.str1 += " "
                if (self.veiculoObj.carga[i] != "'" and self.veiculoObj.carga[i] != "," and self.veiculoObj.carga[i] != "[" and self.veiculoObj.carga[i] != "]" and self.veiculoObj.carga[i] != " "):
                    if (self.veiculoObj.carga[i+1] != "'" and self.veiculoObj.carga[i+1] != "," and self.veiculoObj.carga[i+1] != "[" and self.veiculoObj.carga[i+1] != "]" and self.veiculoObj.carga[i+1] != " "):
                        self.str1 = self.veiculoObj.carga[i] + self.veiculoObj.carga[i+1]
                if (self.str1 != "" and self.str1 != " "):
                    self.str1 = int(self.str1)
                    self.lista11.append(self.str1)

            self.veiculoObj.carga = self.lista11
            self.veiculoObj.addCarga(self.idCarga)

            self.veiculoObj.modDisponibilidade(self.disponibilidade)

            self.bd.tirar("veiculos.txt", self.idVeic)
            self.bd.colocarVeiculo(self.veiculoObj.idVeic, self.veiculoObj.placa, self.veiculoObj.cor, self.veiculoObj.capacidade, self.veiculoObj.carga, self.veiculoObj.disponibilidade,  self.veiculoObj.idMotorista)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0

        except:
            print "ID Invalido ou disponibilidade Invalido\n11"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(11)
            return 11

    def removerCargaVeic(self, idVeic, posicaoCarga, disponibilidade):

        self.idVeic = str(idVeic.get())
        try:
            self.posicaoCarga = int(posicaoCarga.get())
        except:
            print "Formato de posi incorreto\n12"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(12)
            return 12
        self.disponibilidade = str(disponibilidade.get())
        self.bd = Gerenciador_BD()
        self.listaVeiculo = self.bd.retornarInfoVeiculo(self.idVeic)
        try:
            self.veiculoObj = Veiculo(self.listaVeiculo[0], self.listaVeiculo[1], self.listaVeiculo[2], self.listaVeiculo[3], self.listaVeiculo[6])

            self.listaFinal = []

            for j in self.listaVeiculo[4]:
                if(j != "[" and j != "]" and j != "," and j != " "):
                    self.listaFinal.append(int(j))
            print self.listaFinal

            for i in self.listaFinal:
                self.veiculoObj.addCarga(int(i))
            self.veiculoObj.removerCarga(self.posicaoCarga)
            self.veiculoObj.modDisponibilidade(self.disponibilidade)
            self.bd.tirar("veiculos.txt", self.idVeic)
            self.bd.colocarVeiculo(self.veiculoObj.idVeic, self.veiculoObj.placa, self.veiculoObj.cor, self.veiculoObj.capacidade, self.veiculoObj.carga, self.veiculoObj.disponibilidade,  self.veiculoObj.idMotorista)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0
        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def modIdadeMotorista(self, idMoto, novaIdade):
        try:
            self.idMoto = str(idMoto.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
        try:
            self.novaIdade = int(novaIdade.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(3)

        #Recria o motorista a partir do ID
        self.bd = Gerenciador_BD()
        self.listaMotorista = self.bd.retornarInfoMotorista(self.idMoto)

        try:
            self.contatoMotorista = Contato(self.listaMotorista[5], self.listaMotorista[6], "Nulo")
            self.enderecoMotorista = Endereco(self.listaMotorista[8], self.listaMotorista[9], self.listaMotorista[10], self.listaMotorista[11], self.listaMotorista[12], self.listaMotorista[13])
            self.motoristaObj = Motorista(self.idMoto, self.listaMotorista[1], self.listaMotorista[2], self.listaMotorista[3], self.listaMotorista[4], self.contatoMotorista, self.enderecoMotorista, self.listaMotorista[14])
            self.motoristaObj.modDisponibilidade(self.listaMotorista[15])

            #Altera a idade do motorista
            try:
                self.motoristaObj.modIdade(int(self.novaIdade))
            except:
                print "Formato de idade incorreto\n3"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(3)
                return 3

            #Salva a alteracao na "garagem"
            self.bd.tirar("motorista.txt", self.idMoto)
            self.bd.colocarMotorista(self.motoristaObj.idMoto, self.motoristaObj.cpf, self.motoristaObj.nome, self.motoristaObj.idade, self.motoristaObj.anosTrabalho, self.motoristaObj.contato.telefone, self.motoristaObj.contato.email, self.motoristaObj.contato.site, self.motoristaObj.endereco.estado, self.motoristaObj.endereco.cidade, self.motoristaObj.endereco.bairro, self.motoristaObj.endereco.rua, self.motoristaObj.endereco.numeroCasa, self.motoristaObj.endereco.complemento, self.motoristaObj.salario, self.motoristaObj.disponibilidade)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0
        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def modSalarioMotorista(self, idMoto, novoSalario):
        try:
            self.idMoto = str(idMoto.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
        try:
            self.novoSalario = float(novoSalario.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(4)

        #Recria o motorista a partir do ID
        self.bd = Gerenciador_BD()
        self.listaMotorista = self.bd.retornarInfoMotorista(self.idMoto)
        try:
            self.contatoMotorista = Contato(self.listaMotorista[5], self.listaMotorista[6], "Nulo")
            self.enderecoMotorista = Endereco(self.listaMotorista[8], self.listaMotorista[9], self.listaMotorista[10], self.listaMotorista[11], self.listaMotorista[12], self.listaMotorista[13])
            self.motoristaObj = Motorista(self.idMoto, self.listaMotorista[1], self.listaMotorista[2], self.listaMotorista[3], self.listaMotorista[4], self.contatoMotorista, self.enderecoMotorista, self.listaMotorista[14])
            self.motoristaObj.modDisponibilidade(self.listaMotorista[15])
            #Altera o salario do motorista
            try:
                self.motoristaObj.modSalario(self.novoSalario)
            except:
                print "Forato de salario incorreto\n4"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(4)
                return 4

            #Salva a alteracao na "garagem"
            self.bd.tirar("motorista.txt", self.idMoto)
            self.bd.colocarMotorista(self.motoristaObj.idMoto, self.motoristaObj.cpf, self.motoristaObj.nome, self.motoristaObj.idade, self.motoristaObj.anosTrabalho, self.motoristaObj.contato.telefone, self.motoristaObj.contato.email, self.motoristaObj.contato.site, self.motoristaObj.endereco.estado, self.motoristaObj.endereco.cidade, self.motoristaObj.endereco.bairro, self.motoristaObj.endereco.rua, self.motoristaObj.endereco.numeroCasa, self.motoristaObj.endereco.complemento, self.motoristaObj.salario, self.motoristaObj.disponibilidade)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0

        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def modAnosTrabalhoMotorista(self, idMoto, novoAnosTrabalho):
        try:
            self.idMoto = str(idMoto.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
        try:
            self.novoAnosTrabalho = int(novoAnosTrabalho.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(3)

        #Recria o motorista a partir do ID
        self.bd = Gerenciador_BD()
        self.listaMotorista = self.bd.retornarInfoMotorista(self.idMoto)
        try:
            self.contatoMotorista = Contato(self.listaMotorista[5], self.listaMotorista[6], "Nulo")
            self.enderecoMotorista = Endereco(self.listaMotorista[8], self.listaMotorista[9], self.listaMotorista[10], self.listaMotorista[11], self.listaMotorista[12], self.listaMotorista[13])
            self.motoristaObj = Motorista(self.idMoto, self.listaMotorista[1], self.listaMotorista[2], self.listaMotorista[3], self.listaMotorista[4], self.contatoMotorista, self.enderecoMotorista, self.listaMotorista[14])
            self.motoristaObj.modDisponibilidade(self.listaMotorista[15])

            #Altera o tempo trabalhado do motorista
            try:
                self.motoristaObj.modAnosTrabalho(int(self.novoAnosTrabalho))

            except:
                print "Formato de idade incorreto\n3"
                self.c = ChamaPopopizinho()
                self.c.definirPopopizinho(3)
                return 3

            #Salva a alteracao na "garagem"
            self.bd.tirar("motorista.txt", self.idMoto)
            self.bd.colocarMotorista(self.motoristaObj.idMoto, self.motoristaObj.cpf, self.motoristaObj.nome, self.motoristaObj.idade, self.motoristaObj.anosTrabalho, self.motoristaObj.contato.telefone, self.motoristaObj.contato.email, self.motoristaObj.contato.site, self.motoristaObj.endereco.estado, self.motoristaObj.endereco.cidade, self.motoristaObj.endereco.bairro, self.motoristaObj.endereco.rua, self.motoristaObj.endereco.numeroCasa, self.motoristaObj.endereco.complemento, self.motoristaObj.salario, self.motoristaObj.disponibilidade)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0

        except:
            print "Id invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def modEnderecoMotorista(self, idMoto, estado, cidade, bairro, rua, numeroCasa, complemento):
        try:
            self.idMoto = str(idMoto.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        self.estado = str(estado.get())
        self.cidade = str(cidade.get())
        self.bairro = str(bairro.get())
        self.rua = str(rua.get())
        self.numeroCasa = str(numeroCasa.get())
        self.complemento = str(complemento.get())

        #Recria o motorista a partir do ID
        try:
            self.bd = Gerenciador_BD()
            self.listaMotorista = self.bd.retornarInfoMotorista(self.idMoto)
            self.contatoMotorista = Contato(self.listaMotorista[5], self.listaMotorista[6], "Nulo")
            self.enderecoMotorista = Endereco(self.listaMotorista[8], self.listaMotorista[9], self.listaMotorista[10], self.listaMotorista[11], self.listaMotorista[12], self.listaMotorista[13])
            self.motoristaObj = Motorista(self.idMoto, self.listaMotorista[1], self.listaMotorista[2], self.listaMotorista[3], self.listaMotorista[4], self.contatoMotorista, self.enderecoMotorista, self.listaMotorista[14])
            self.motoristaObj.modDisponibilidade(self.listaMotorista[15])

            #Cria uma nova instancia de um endereco
            self.novoEndereco = Endereco(self.estado, self.cidade, self.bairro, self.rua, self.numeroCasa, self.complemento)

            #Redefine o endereco do motorista
            self.motoristaObj.endereco = self.novoEndereco

            #Salva a alteracao na "garagem"
            self.bd.tirar("motorista.txt", self.idMoto)
            self.bd.colocarMotorista(self.motoristaObj.idMoto, self.motoristaObj.cpf, self.motoristaObj.nome, self.motoristaObj.idade, self.motoristaObj.anosTrabalho, self.motoristaObj.contato.telefone, self.motoristaObj.contato.email, self.motoristaObj.contato.site, self.motoristaObj.endereco.estado, self.motoristaObj.endereco.cidade, self.motoristaObj.endereco.bairro, self.motoristaObj.endereco.rua, self.motoristaObj.endereco.numeroCasa, self.motoristaObj.endereco.complemento, self.motoristaObj.salario, self.motoristaObj.disponibilidade)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0
        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def modContatoMotorista(self, idMoto, telefone, email):
        try:
            self.idMoto = str(idMoto.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        self.telefone = str(telefone.get())
        self.email = str(email.get())

        #Recria o motorista a partir do ID
        self.bd = Gerenciador_BD()
        self.listaMotorista = self.bd.retornarInfoMotorista(self.idMoto)
        print self.listaMotorista
        try:
            self.contatoMotorista = Contato(self.listaMotorista[5], self.listaMotorista[6], "Nulo")
            print 1
            self.enderecoMotorista = Endereco(self.listaMotorista[8], self.listaMotorista[9], self.listaMotorista[10], self.listaMotorista[11], self.listaMotorista[12], self.listaMotorista[13])
            self.motoristaObj = Motorista(self.idMoto, self.listaMotorista[1], self.listaMotorista[2], self.listaMotorista[3], self.listaMotorista[4], self.contatoMotorista, self.enderecoMotorista, self.listaMotorista[14])
            self.motoristaObj.modDisponibilidade(self.listaMotorista[15])

            #Cria uma nova instancia de um contato
            self.novoContato = Contato(self.telefone, self.email, "Nulo")

            #Redefine o contato do motorista
            self.motoristaObj.contato = self.novoContato

            #Salva a alteracao na "garagem"
            self.bd.tirar("motorista.txt", self.idMoto)
            self.bd.colocarMotorista(self.motoristaObj.idMoto, self.motoristaObj.cpf, self.motoristaObj.nome, self.motoristaObj.idade, self.motoristaObj.anosTrabalho, self.motoristaObj.contato.telefone, self.motoristaObj.contato.email, self.motoristaObj.contato.site, self.motoristaObj.endereco.estado, self.motoristaObj.endereco.cidade, self.motoristaObj.endereco.bairro, self.motoristaObj.endereco.rua, self.motoristaObj.endereco.numeroCasa, self.motoristaObj.endereco.complemento, self.motoristaObj.salario, self.motoristaObj.disponibilidade)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0

        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def modMotoristaDeVeiculo(self, idVeic, idMoto):
        try:
            self.idMoto = str(idMoto.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        try:
            self.idVeic = str(idVeic.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        #Recria o veiculo a partir do ID
        self.bd = Gerenciador_BD()
        self.listaVeiculo = self.bd.retornarInfoVeiculo(self.idVeic)
        try:
            self.veiculoObj = Veiculo(self.listaVeiculo[0], self.listaVeiculo[1], self.listaVeiculo[2], self.listaVeiculo[3], self.listaVeiculo[6])
            self.veiculoObj.modDisponibilidade(self.listaVeiculo[5])

            #Altera o motorista do veiculo
            self.veiculoObj.modMotorista(self.idMoto)

            #Salva a alteracao na "garagem"
            self.bd.tirar("veiculos.txt", self.idVeic)
            self.bd.colocarVeiculo(self.veiculoObj.idVeic, self.veiculoObj.placa, self.veiculoObj.cor, self.veiculoObj.capacidade, self.veiculoObj.carga, self.veiculoObj.disponibilidade,  self.veiculoObj.idMotorista)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0

        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def addPontoParada(self, pontoDeParada, idCarga):
        try:
            self.idCarga = str(idCarga.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        self.pontoDeParada = str(pontoDeParada.get())

        #Recria os objetos carga e veiculo mudando o atributo carga em veiculo
        self.bd = Gerenciador_BD()
        self.listaCarga = self.bd.retornarInfoCarga(self.idCarga)
        print self.listaCarga

        try:
            self.contatoCliente = Contato(self.listaCarga[13], self.listaCarga[14], self.listaCarga[15])
            self.enderecocliente = Endereco(self.listaCarga[16], self.listaCarga[17], self.listaCarga[18], self.listaCarga[19], self.listaCarga[20], self.listaCarga[21])
            self.clienteObj = Cliente(self.listaCarga[11], self.listaCarga[12], self.contatoCliente, self.enderecocliente, self.listaCarga[22])
            self.cargaObj = Carga(self.listaCarga[0], self.listaCarga[1], self.listaCarga[2], self.listaCarga[3], self.listaCarga[4], self.listaCarga[5], self.listaCarga[6], self.listaCarga[7], self.listaCarga[10], self.clienteObj)
            #Insere o ponto de parada na cargaObj
            self.cargaObj.addPontoDeParada(self.pontoDeParada)
            #Salva a alteracao na relacao de estado das cargas
            self.bd.tirar("cargas.txt", self.idCarga)
            self.bd.inserirCarga(self.cargaObj.id, self.cargaObj.peso, self.cargaObj.origem, self.cargaObj.destino, self.cargaObj.periculosidade, self.cargaObj.material, self.cargaObj.tamanhoConteiner, self.cargaObj.kmPercorrido, self.cargaObj.custoDeTrasporte, self.cargaObj.pontosDeParada, self.cargaObj.datas, self.cargaObj.cliente)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
            return 0
        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def removerVeiculoDaGaragem(self, idVeic):
        try:
            self.idVeic = str(idVeic.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        #Remove da garagem
        try:
            self.bd = Gerenciador_BD()
            self.bd.tirar("veiculos.txt", self.idVeic)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def removerMotoristaDaGaragem(self, idMoto):
        try:
            self.idMoto = str(idMoto.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        #Retirar motorista da "garagem"
        try:
            self.bd = Gerenciador_BD()
            self.bd.tirar("motorista.txt", self.idMoto)
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(0)
        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def infoDeVeiculo(self, idVeic):
        try:
            self.idVeic = str(idVeic.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        #Recria o veiculo a partir do ID
        self.bd = Gerenciador_BD()
        self.listaVeiculo = self.bd.retornarInfoVeiculo(self.idVeic)
        try:
            self.veiculoObj = Veiculo(self.listaVeiculo[0], self.listaVeiculo[1], self.listaVeiculo[2], self.listaVeiculo[3], self.listaVeiculo[6])
            self.veiculoObj.modDisponibilidade(bool(self.listaVeiculo[5]))
            print self.veiculoObj.infoParciais()
            return self.listaVeiculo

        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def infoDeMoto(self, idMoto):
        try:
            self.idMoto = str(idMoto.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        #Recria o motorista a partir do ID
        self.bd = Gerenciador_BD()
        self.listaMotorista = self.bd.retornarInfoMotorista(self.idMoto)
        try:
            self.contatoMotorista = Contato(self.listaMotorista[5], self.listaMotorista[6], "Nulo")
            self.enderecoMotorista = Endereco(self.listaMotorista[8], self.listaMotorista[9], self.listaMotorista[10], self.listaMotorista[11], self.listaMotorista[12], self.listaMotorista[13])
            self.motoristaObj = Motorista(self.idMoto, self.listaMotorista[1], self.listaMotorista[2], self.listaMotorista[3], self.listaMotorista[4], self.contatoMotorista, self.enderecoMotorista, self.listaMotorista[14])
            self.motoristaObj.modDisponibilidade(bool(self.listaMotorista[15]))

            print self.motoristaObj.infoParciais()
            return self.listaMotorista

        except:
            print "ID invalido\n10"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 10

    def infoCarga(self, idCarga):
        try:
            self.idCarga = str(idCarga.get())
        except:
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)

        #Recria a carga a partir do ID
        self.bd = Gerenciador_BD()
        self.listaCarga = self.bd.retornarInfoCarga(self.idCarga)
        try:
            self.contatoCliente = Contato(self.listaCarga[13], self.listaCarga[14], self.listaCarga[15])
            self.enderecocliente = Endereco(self.listaCarga[16], self.listaCarga[17], self.listaCarga[18], self.listaCarga[19], self.listaCarga[20], self.listaCarga[21])
            self.clienteObj = Cliente(self.listaCarga[11], self.listaCarga[12], self.contatoCliente, self.enderecocliente, self.listaCarga[22])
            self.cargaObj = Carga(self.listaCarga[0], self.listaCarga[1], self.listaCarga[2], self.listaCarga[3], self.listaCarga[4], self.listaCarga[5], self.listaCarga[6], self.listaCarga[7], self.listaCarga[10], self.clienteObj)

            print self.cargaObj
            return self.listaCarga

        except:
            print "ID invalido\n18"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(18)
            return 10

    def mostrarHistorico(self):
        try:
            self.bd = Gerenciador_BD()
            self.l = self.bd.entregarHistorico()
            print self.l
            return self.l

        except:
            print "ERRO DESCONHECIDO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(10)
            return 88

    def todosVeiculos(self):

        try:
            self.bd = Gerenciador_BD()
            self.l = self.bd.entregarVeiculos()
            print self.l
            return self.l

        except:
            print "ERRO DESCONHECIDO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88

    def todosMotoristas(self):
        try:
            self.bd = Gerenciador_BD()
            self.l = self.bd.entregarMotoristas()
            print self.l
            return self.l

        except:
            print "ERRO DESCONHECIDO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88

    def todosMotoristasDisponiveis(self):
        try:
            self.bd = Gerenciador_BD()
            self.l = self.bd.entregarMotoristasDisponiveis()
            print self.l
            return self.l

        except:
            print "ERRO DESCONHECIDO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88

    def todosVeiculosDisponiveis(self):
        try:
            self.bd = Gerenciador_BD()
            self.l = self.bd.entregarVeiculosDisponiveis()
            print self.l
            return self.l

        except:
            print "ERRO DESCONHECIDO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88

    def todosMotoristasOcupados(self):
        try:
            self.bd = Gerenciador_BD()
            self.l = self.bd.entregarMotoristasOcupados()
            print self.l
            return self.l

        except:
            print "ERRO DESCONHECIDO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88

    def todosVeiculosOcupados(self):
        try:
            self.bd = Gerenciador_BD()
            self.l = self.bd.entregarVeiculosOcupados()
            print self.l
            return self.l

        except:
            print "ERRO DESCONHECIDO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88

    def parteFiscal(self):
        try:
            self.bd = Gerenciador_BD()
            self.l = self.bd.entregarDinheiros()
            return self.l
        except:
            print "ERRO DESCONHECIDO"
            self.c = ChamaPopopizinho()
            self.c.definirPopopizinho(88)
            return 88
