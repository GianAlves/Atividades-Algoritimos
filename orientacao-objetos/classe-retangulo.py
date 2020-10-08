class Retangulo:

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calculaArea(self):
        self.area = self.altura * self.largura
        return print(f'A área do retângulo é {self.area}m².')

    def imprimeValores(self):
        print(f'A altura é {self.altura}m e a largura é {self.largura}m.')

ret1 = Retangulo(30, 40)

ret1.imprimeValores()
ret1.calculaArea()