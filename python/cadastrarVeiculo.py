from veiculo import *
from carga import *
from contato import *
from cliente import *
from gerenciador_BD import *

class CadastrarVeiculo:

    def cadastrarVeiculo(self, ID, PLACA, COR, CAPACIDADE, ID_MOTORISTA):

        #Criar o objeto
        v = Veiculo(ID, PLACA, COR, CAPACIDADE, ID_MOTORISTA)
        #Gravar no BD os atributos do obj
        bd = Gerenciador_BD()
        bd.colocarVeiculo(v.idVeic, v.placa, v.cor, v.capacidade, [],  v.disponibilidade, v.idMotorista)

        return v
