class No:
  def __init__(self, dado, prox = None):
    self.__dado = dado
    self.__prox = prox

  @property
  def dado(self):
    return self.__dado

  @dado.setter
  def dado(self, dado):
    self.__dado = dado

  @property
  def prox(self):
    return self.__prox

  @prox.setter
  def prox(self, prox):
    self.__prox = prox

  def __str__ (self) :
    return "{}".format(self.__dado)