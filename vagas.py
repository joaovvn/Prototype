from abc import ABCMeta
import copy

class Estacionamento(metaclass = ABCMeta):

  def __init__(self):
    self.valorHora = None
    self.qtdVagas = None
    self.id = None
  
  def getValor(self):
    return self.valor

  def getQtd(self):
    return self.qtdVagas

  def getID(self):
    return self.id

  def setID(self, id):
    self.id = id
  
  def clone(self):
    return copy.copy(self)

class EdificioGaragem(Estacionamento):
  def __init__(self):
    super().__init__()
    self.valor = 1.5
    self.qtdVagas = 300

class EstacionamentoExterno(Estacionamento):
  def __init__(self):
    super().__init__()
    self.valor = 1
    self.qtdVagas = 175

class Cache:

  cache = {}

  @staticmethod
  def getEstacionamento(id):
    estacionamento = Cache.cache.get(id, None)
    return estacionamento.clone()

  @staticmethod
  def load():
    eg = EdificioGaragem()
    eg.setID(1)
    Cache.cache[eg.getID()] = eg
  
    ext = EstacionamentoExterno()
    ext.setID(2)
    Cache.cache[ext.getID()] = ext