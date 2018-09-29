from contato import *
from endereco import *
from cliente import *
import datetime as datatempo

class Gerenciador_BD:

	def colocarMotorista(self, ID, CPF, NOME, IDADE, ANOS_TRABALHANDO, TELEFONE, EMAIL, SITE, ESTADO, CIDADE, BAIRRO, RUA, NUMERO_CASA, COMPLEMENTO, SALARIO, DISPONIBILIDADE):
		arq = open("motorista.txt", "a")
		arq.write(str(ID) + "; " +str(CPF) + "; " + str(NOME) + "; " + str(IDADE) + "; " +str(ANOS_TRABALHANDO) + "; " +str(TELEFONE) + "; " +str(EMAIL) + "; " +str(SITE) + "; " +str(ESTADO) + "; " +str(CIDADE) + "; " + str(BAIRRO) + "; " +str(RUA) + "; " +str(NUMERO_CASA) + "; " +str(COMPLEMENTO) + "; " +str(SALARIO) + "; " +str(DISPONIBILIDADE)+"\n")
		arq.close()

	def colocarVeiculo(self, ID, PLACA, COR, CAPACIDADE, CARGA, DISPONIBILIDADE, IDMOTORISTA):
		arq = open("veiculos.txt", "a")
		arq.write(str(ID) +  "; " + str(PLACA) +  "; " + str(COR) +  "; " + str(CAPACIDADE) +  "; " + str(CARGA) +  "; " +  str(DISPONIBILIDADE)+  "; " + str(IDMOTORISTA) + "\n")
		arq.close()

	def definirHistorico(self, ID_VEICULO, PLACA, ID_MOTORISTA, NOME, CPF, ID_CARGA, MATERIAL, PESO, ORIGEM, DESTINO, PERICULOZIDADE, TAMANHO_CONTAINER, KM_PERCORRIDO, PONTOS_DE_PARADA, DATAS, CLIENTE):
		arq = open("historico.txt", "a")
		arq.write(str(ID_VEICULO) + "; " + str(PLACA) + "; " + str() + "; " + str(ID_MOTORISTA) + "; " + str(NOME) + "; " + str(CPF) + "; " + str(ID_CARGA) + "; " + str(MATERIAL) + "; " + str(PESO) + "; " + str(ORIGEM) + "; " + str(DESTINO) + "; " + str(PERICULOZIDADE) + "; " + str(TAMANHO_CONTAINER) + "; " + str(KM_PERCORRIDO) + "; " + str(PONTOS_DE_PARADA) + "; " + str(DATAS) + "; " + str(CLIENTE.nome) + "; " + str(CLIENTE.cpf) + "; " + str(CLIENTE.contato.telefone) + "; " + str(CLIENTE.contato.email) + "; " + str(CLIENTE.contato.site) + "; " + str(CLIENTE.numNotaFiscal) + "\n")
		arq.close()

	def inserirCarga(self, ID, PESO, ORIGEM, DESTINO, PERICULOZIDADE, MATERIAL, TAMANHO_CONTAINER, KM_PERCORRIDO, CUSTO_DE_TRANSPORTE, PONTOS_DE_PARADA, DATAS, CLIENTE):
		arq = open("cargas.txt", "a")
		arq.write(str(ID) + "; " + str(MATERIAL) + "; " + str(PESO) + "; " + str(ORIGEM) + "; " + str(DESTINO) + "; " + str(PERICULOZIDADE) + "; " + str(TAMANHO_CONTAINER) + "; " + str(KM_PERCORRIDO) + "; " + str(CUSTO_DE_TRANSPORTE) + "; " + str(PONTOS_DE_PARADA) + "; " + str(DATAS) + "; " + str(CLIENTE.nome) + "; " + str(CLIENTE.cpf) + "; " + str(CLIENTE.contato.telefone) + "; " + str(CLIENTE.contato.email) + "; " + str(CLIENTE.contato.site) + "; " + str(CLIENTE.endereco.estado) + "; " + str(CLIENTE.endereco.cidade) + "; " + str(CLIENTE.endereco.bairro) + "; " + str(CLIENTE.endereco.rua) + "; " + str(CLIENTE.endereco.numeroCasa) + "; " + str(CLIENTE.endereco.complemento) + "; " + str(CLIENTE.numNotaFiscal) + "\n")
		arq.close()

	def BDGastosGanhos(self, valor, numNotaFiscal, idCarga):
		arq = open("dinheiros.txt", "a")
		arq.write(str(datatempo.date.today()) + "; " + str(idCarga) + "; " +str(valor) + "; " + str(numNotaFiscal))
		arq.write("\n")
		arq.close()

	def tirar(self, arquivo, numid):
		num = str(numid) + ";"
		arq = open(arquivo, "r")
		l = []
		for i in arq:
			l.append(i.split(" "))
		arq.close()
		for j in l:
			if(j[0] == num):
				l.remove(j)

		list2 = []
		for m in l:
			for n in m:
				if (n[len(n)-1] == ";"):
					n = n + " "
					list2.append(n)
				else:
					list2.append(n)
		limpa = open(arquivo, "w")
		limpa.write(" ")
		limpa.close()
		arq2 = open(arquivo, "w")
		for o in list2:
			arq2.write(o)
		arq2.close()

	def retornarInfoMotoristaDisponivel(self):
		arq = open('motorista.txt', 'a')
		arq = open("motorista.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			if(j[15] == "True\n"):
				j[15] = j[15].split(None, 1)
				j[15] = j[15][0]
				lr = j

		return lr

	def retornarInfoVeiculoDisponivel(self):
		arq1 = open('veiculos.txt', 'a')
		arq1.close()
		arq = open("veiculos.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			if(j[5] == "True"):
				j[6] = j[6].split(None, 1)
				j[6] = j[6][0]
				lr = j

		return lr

	def retornarInfoMotorista(self, ID):
		ID = str(ID)
		arq = open('motorista.txt', 'a')
		arq = open("motorista.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			if(j[0] == ID):
				j[15] = j[15].split(None, 1)
				j[15] = j[15][0]
				lr = j
		return lr

	def retornarInfoVeiculo(self, ID):
		arq = open('veiculos.txt', 'a')
		ID = str(ID)
		arq = open("veiculos.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			if(j[0] == ID):
				j[6] = j[6].split(None, 1)
				j[6] = j[6][0]
				lr = j

		return lr

	def retornarInfoCarga(self, ID):
		ID = str(ID)
		arq = open('cargas.txt', 'a')
		arq = open("cargas.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			print j
			if(j[0] == ID):
				j[22] = j[22].split(None, 1)
				j[22] = j[22][0]
				lr = j

		return lr

	def retornarNotasFiscais(self, numNotaFiscal):
		arq = open('dinheiros.txt', 'a')
		numNotaFiscal = str(numNotaFiscal) + "\n"
		arq = open("dinheiros.txt", "r")
		l = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		try:
			for j in l:
				if (j[3] == numNotaFiscal):
					return True
				else:
					return False
		except:
			return False

	def entregarHistorico(self):
		arq = open('historico.txt', 'a')
		arq = open("historico.txt", "r")
		l = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			j[21] = j[21].split(None, 1)
			j[21] = j[21][0]
		return l

	def entregarMotoristas(self):
		arq = open('motorista.txt', 'a')
		arq = open("motorista.txt", "r")
		l = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			j[15] = j[15].split(None, 1)
			j[15] = j[15][0]

		return l

	def entregarVeiculos(self):
		arq = open('veiculos.txt', 'a')
		arq = open("veiculos.txt", "r")
		l = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			j[6] = j[6].split(None, 1)
			j[6] = j[6][0]

		return l

	def entregarMotoristasDisponiveis(self):
		arq = open('motorista.txt', 'a')
		arq = open("motorista.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			if(j[15] == "True\n"):
				j[15] = j[15].split(None, 1)
				j[15] = j[15][0]
				lr.append(j)

		return lr

	def entregarVeiculosDisponiveis(self):
		arq = open('veiculos.txt', 'a')
		arq = open("veiculos.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			if(j[5] == "True"):
				j[6] = j[6].split(None, 1)
				j[6] = j[6][0]
				lr.append(j)

		return lr

	def entregarMotoristasOcupados(self):
		arq = open('motorista.txt', 'a')
		arq = open("motorista.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			if(j[15] == "False\n"):
				j[15] = j[15].split(None, 1)
				j[15] = j[15][0]
				lr.append(j)

		return lr

	def entregarVeiculosOcupados(self):
		arq = open('veiculos.txt', 'a')
		arq = open("veiculos.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			if(j[5] == "False\n"):
				j[6] = j[6].split(None, 1)
				j[6] = j[6][0]
				lr.append(j)

		return lr


	def entregarDinheiros(self):
		arq = open('dinheiros.txt', 'a')
		arq = open("dinheiros.txt", "r")
		l = []
		lr = []
		for i in arq:
			l.append(i.split("; "))
		arq.close()
		for j in l:
			j[3] = j[3].split(None, 1)
			j[3] = j[3][0]
			lr.append(j)
		return lr
