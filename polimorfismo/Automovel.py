from Veiculo import Veiculo

class Automovel(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade )
        self.__potenciaDoMotor = float(potenciaDoMotor)

    def imprimirInformacoesAuto(self):
        Veiculo.imprimirInformacoes(self)
        print(f'Potência do moto: {self.getPotencia()}')
        print('----------------------')

    def getPotencia(self):
        return self.__potenciaDoMotor