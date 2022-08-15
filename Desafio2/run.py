from elevador import Elevador
from gerenciador import GerenciadorDeElevadores

elevador1 = Elevador(1)
elevador2 = Elevador(2)
gerenciadorDeElavadores = GerenciadorDeElevadores(elevador1, elevador2)


while(True):
  elevadorid = int(input('Defina o elevador:'))
  andar = int(input('Defina um anadar:'))

  resposta = gerenciadorDeElavadores.locomover(andar, elevadorid)

  print(resposta)
  print()