from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, cpf, idade, peso, altura):
        self.__cpf = cpf 
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimeCPf(self):
        return print('CPF: ' + self.__cpf)

    def __calculaIMC(self):
        resultado = int(self.peso / (self.altura * self.altura))
        return print(f'Seu IMC é: {resultado}')

    def getCalculaIMC(self):
        return self.__calculaIMC()