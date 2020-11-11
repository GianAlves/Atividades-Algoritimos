from Automovel import Automovel

class Carro(Automovel):

    def __init__(self,  marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.__qtdPortas = qtdPortas

    def imprimirInformacoesCarro(self):
        Automovel.imprimirInformacoesAuto(self)
        print(f'Quantidade de portas: {self.getQtdPortas()}')
        print('----------------------')

    def getQtdPortas(self):
        return self.__qtdPortas