from abc import abstractmethod
import numpy as np
from AStarGeneral import *


class HeurAlgo:
    @abstractmethod
    def execute(self,etatCurrent,etatFinal):
        pass

class EtatTaquin(Etat):
    heurAlgo=None
    @staticmethod
    def setAlgo(algo):
        EtatTaquin.heurAlgo=algo
    def __init__(self,matrix):
        self.matrix=matrix
    def getHeur(self, etatfinal):
        return EtatTaquin.heurAlgo.execute(self,etatfinal)

    def Equals(self, other):
        return np.array_equal(self.matrix,other.matrix)

    def generateSucc(self):
        # position de la case vide designer par la valeur 0
        x,y=findIndex(self.matrix,0)
        dimension=self.matrix.shape[0]
        list=[]
        if(x != dimension -1):
            #la case vide peut se deplacer en bas
            aux=np.array(self.matrix)
            aux[x][y]=aux[x+1][y]
            aux[x+1][y]=0
            etat=EtatTaquin(aux)
            list.append(Transition(etat,1))
        if (x != 0):
            # la case vide peut se deplacer en haut
            aux = np.array(self.matrix)
            aux[x][y] = aux[x - 1][y]
            aux[x - 1][y] = 0
            etat = EtatTaquin(aux)
            list.append(Transition(etat, 1))
        if (y != dimension - 1):
            # la case vide peut se deplacer a droite
            aux = np.array(self.matrix)
            aux[x][y] = aux[x][y + 1]
            aux[x][y + 1] = 0
            etat = EtatTaquin(aux)
            list.append(Transition(etat, 1))
        if (y != 0):
            # la case vide peut se deplacer a gauche
            aux = np.array(self.matrix)
            aux[x][y] = aux[x][y - 1]
            aux[x][y - 1] = 0
            etat = EtatTaquin(aux)
            list.append(Transition(etat, 1))
        return list


# implementation heuristique algorithme
class ManhattanAlgo(HeurAlgo):
    def execute(self,etatCurrent,etatFinal):
        matrixCurrent=etatCurrent.matrix
        dimension = matrixCurrent.shape[0]
        matrixFinal=etatFinal.matrix
        s=0
        for i in range(dimension):
            for j in range(dimension):
                x,y=findIndex(matrixFinal,matrixCurrent[i][j])
                s+= abs(x-i)+abs(y-j)
        return s
class MalPlaceAlgo(HeurAlgo):
    def execute(self,etatCurrent,etatFinal):
        matrixCurrent = etatCurrent.matrix
        dimension = matrixCurrent.shape[0]
        matrixFinal = etatFinal.matrix
        aux=matrixCurrent-matrixFinal
        return np.count_nonzero(aux)

def findIndex(array,val):
    dimension = array.shape[0]
    x = -1;
    y = -1
    for i in range(dimension):
        for j in range(dimension):
            if array[i][j] == val:
                x = i;
                y = j;
                break
        if x != -1: break
    return x,y