from Veiculo import Veiculo

class Bicicleta(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade )
        self.__numMarchas = numMarchas
        self.__bagageiro = bagageiro

    def imprimirinformacoesBike(self):
        Veiculo.imprimirInformacoes(self)
        print(f'Numero de marchas: {self.getNumMarchas()}')
        print(f'Bagageiro: {self.getBagageiro()}')
        print('----------------------')

    def getNumMarchas(self):
        return self.__numMarchas

    def getBagageiro(self):
        return self.__bagageiro