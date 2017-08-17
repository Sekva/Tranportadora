class Contato:
    def __init__(self, telefone, email, site):
        self.telefone = telefone    #str
        self.email = email          #str
        self.site = site            #str

    #Modificar as informacoes de contato.
    def modContato(self, telefone, email, site):
        self.telefone = telefone
        self.email = email
        self.site = site

    def infoCompleta(self):
        return "\nTelefone: " + str(self.telefone) + "\nEmail: " + str(self.email) + "\nSite: " + str(self.site)
