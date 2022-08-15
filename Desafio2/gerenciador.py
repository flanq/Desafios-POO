class GerenciadorDeElevadores:
  def __init__(self, elevador1, elevador2):
    self.__elevadores = [elevador1, elevador2]

  def locomover(self, andar, id):
    if (andar < 1 or andar > 15): return self.__mensagem_de_erro()
    else: return self.__seleciona_elevador_e_altera_andar(andar, id)

  def __seleciona_elevador_e_altera_andar(self, andar, id):
    for elevador in self.__elevadores:
      if elevador.check_id(id):
        return self.__alteracao_de_andar(andar, elevador)
      else: return 'ID de elevador incorreto. Escolha 1 ou 2.'

  def __alteracao_de_andar(self, andar, elevador):
    elevador.set_andar(andar)
    if (andar == 1): return 'O elevador {} está indo pra o terreo' .format(elevador.get_id())
    else: return 'Elevador {}, indo para o {}º andar'.format(elevador.get_id(), elevador.get_andar())

  def __mensagem_de_erro(self):
    return 'Andar incorreto!'

  









