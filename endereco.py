class Endereco:
    def __init__ (self, estado, cidade, bairro, rua, numeroCasa, complemento):
        self.estado = estado                #str
        self.cidade = cidade                #str
        self.bairro = bairro                #str
        self.rua = rua                      #str
        self.numeroCasa = numeroCasa        #str
        self.complemento = complemento      #str

    #Modificar Informacoes do endereco
    def modEndereco(self, estado, cidade, bairro, rua, numeroCasa, complemento):
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numeroCasa = numeroCasa
        self.complemento = complemento

    def infoParciais (self):
        return 'Estado: ' + str(self.estado) + '\nCidade: ' + str(self.cidade)

    def infoCompleta (self):
        return 'Estado: ' + str(self.estado) + '\nCidade: ' + str(self.cidade) + '\nBairro: ' + str(self.bairro) + '\nRua: ' + str(self.rua) + '\nNumero da Casa: ' + str(self.numeroCasa) + '\nComplemento: ' + str(self.complemento)
