import numpy as np
from abc import abstractmethod

from AStarGeneral import *


class HeurAlgo:
    @abstractmethod
    def execute(self,etatFinal):
        pass

class ManhattanAlgo(HeurAlgo):
    def execute(self,etatFinal):
        pass
class MalPlaceAlgo(HeurAlgo):
    def execute(self,etatFinal):
        pass


class EtatTaquin(Etat):
    herrAlgo=None
    def __init__(self,matrix):
        self.matrix=matrix
    def getHeur(self, Etatfinal):
        pass

    def Equals(self, other):
        pass

    def generateSucc(self):
        pass