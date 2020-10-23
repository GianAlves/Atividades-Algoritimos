from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, cnpj, incricaoEstadual, quantidadeFuncionarios):
        self.__cnpj = cnpj
        self.__incricaoEstadual = incricaoEstadual
        self.quantidadeFuncionarios = int(quantidadeFuncionarios)

    def imprimeCNPJ(self):
        return print(f'CNPJ: {self.__cnpj}')

    def getNotaFiscal(self):
        return self.__emitirNotaFiscal()

    def __emitirNotaFiscal(self):
       print('Nota fiscal:')
       print('CNPJ: ' , self.getCNPJ(),
        'Número da inscrição estadual: ' , self.getInscricaoEstadual(),
        'Quantidade de funcionários: ' , self.quantidadeFuncionarios)

    def getCNPJ(self):
        return self.__cnpj

    def getInscricaoEstadual(self):
        return self.__incricaoEstadual
