from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

Lucas = Pessoa(100, 'Lucas', 'rua lucas 230', '(51) 98989898')

Jonathas = Fisica('84584584500', 25, 60, 1.8)
Alice = Juridica('845845845845', 'ok', 15)

Lucas.imprimeNome()
Lucas.getImprimirTelefone()
print('----------')
Jonathas.imprimeCPf()
Jonathas.getCalculaIMC()
print('----------')
Alice.imprimeCNPJ()
Alice.getNotaFiscal()