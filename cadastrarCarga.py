from contato import *
from endereco import *
from cliente import *
from carga import *
from gerenciador_BD import *


class CadastrarCarga:
    #Cadastrar uma nova carga
    def cadastrarCarga(self, idCarga, material, peso, periculosidade, tamanhoConteiner, origem, destino, kmPercorrido, datas, cliente):

        #Criar o objeto
        c = Carga(idCarga, material, peso, origem, destino, periculosidade, tamanhoConteiner, kmPercorrido, datas, cliente)
        #Gravar no BD os atributos do obj
        bd = Gerenciador_BD()
        bd.inserirCarga(c.id, c.peso, c.origem, c.destino, c.periculosidade, c.material, c.tamanhoConteiner, c.kmPercorrido, c.custoDeTrasporte, c.pontosDeParada, c.datas, c.cliente)

        return c
