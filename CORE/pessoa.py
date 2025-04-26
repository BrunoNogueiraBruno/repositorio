class Pessoa:
    def __init__(self):
        self.nome="Brunos"
        self.idade=24

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self,nome):
        self.nome = nome

    