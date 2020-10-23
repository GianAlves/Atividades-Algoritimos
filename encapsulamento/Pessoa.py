class Pessoa:

    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = int(codigo)
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        print('Nome: ' + self.nome)

    def __imprimeTelefone(self):
        return print('Telefone: ' + self.__telefone)

    def getImprimirTelefone(self):
        return self.__imprimeTelefone()

    def getCodigo(self):
        return self.__codigo

    def getTelefone(self):
        return self.__telefone
