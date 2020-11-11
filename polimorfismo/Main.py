from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Carro import Carro
from Moto import Moto

# meuVeiculo = Veiculo('Fiat', 4, 'Uno', 0)
# meuVeiculo.imprimirInformacoes()
# meuVeiculo.acelerar(10)
# meuVeiculo.imprimirInformacoes()
# meuVeiculo.frear(5)
# meuVeiculo.imprimirInformacoes()

minhaBike = Bicicleta('Ok', 2, 'Super 3000', 0, 3, False)
minhaBike.imprimirinformacoesBike()
minhaBike.acelerar(40)
minhaBike.imprimirinformacoesBike()

print('\n \n')

minhaMoto = Moto('Toyota', 2, 'XML900', 90, 200, True)
minhaMoto.imprimirInformacoesMoto()

print('\n \n')

meuCarro = Carro('Fiat', 4, 'Uno', 65, 220, 2)
meuCarro.imprimirInformacoesCarro()