class Veiculo:

    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.__marca = marca
        self.__qtdRodas = qtdRodas
        self.__modelo = modelo
        self.__velocidade = velocidade

    def imprimirInformacoes(self):
        print(f'Marca: {self.getMarca()}')
        print(f'Quantidade de rodas: {self.getQtdRodas()}')
        print(f'Modelo: {self.getModelo()}')
        print(f'Velocidade atual: {self.getVel()}')
        print('----------------------')

    def acelerar(self, valor: int):
        resultado = int(self.getVel()) + valor
        self.setVel(resultado)
        return print(f'Velocidade é de: {resultado}Km')

    def frear(self, valor: int):
        resultado = int(self.getVel()) - valor
        self.setVel(resultado)
        return print(f'Velocidade é de: {resultado}Km')

    def getVel(self):
        return self.__velocidade

    def setVel(self, res):
        self.__velocidade = res

    def getMarca(self):
        return self.__marca

    def getQtdRodas(self):
        return self.__qtdRodas

    def getModelo(self):
        return self.__modelo
