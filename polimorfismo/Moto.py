from Automovel import Automovel

class Moto(Automovel):

    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.__partidaEletrica = partidaEletrica

    def imprimirInformacoesMoto(self):
        Automovel.imprimirInformacoesAuto(self)
        print(f'Partida eletrica: {self.getPartida()}')
        print('----------------------')

    def getPartida(self):
        return self.__partidaEletrica