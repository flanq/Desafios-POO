class Elevador:
  def __init__(self):
    self._andar = 1

  def locomover(self, andar):
    if (andar < 1 or andar > 15): return self.__mensagem_de_erro()
    else:
      self._andar = andar
      if (andar == 1): return self.__mensagem_de_alteracao_para_terreo()
      return self.__mensagem_de_alteracao_de_andar()

  def __mensagem_de_erro(self):
    return 'Andar incorreto! Elevador no {}º andar'.format(self._andar)

  def __mensagem_de_alteracao_de_andar(self):
    return 'Elevador indo para o {}º andar.'.format(self._andar) 

  def __mensagem_de_alteracao_para_terreo(self):
    return 'O elevador está indo pra o terreo' 
      
elevador = Elevador()

while(True):
  andar = int(input('Informe o andar: '))
  resposta = elevador.locomover(andar)
  print(resposta)
  print()
  









