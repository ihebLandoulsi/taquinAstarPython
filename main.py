import numpy as np

from jeuDeTaquin import *
from AStarGeneral import  AStar


def saisieMatrix(d):
    initList = []
    for i in range(d):
        v = True
        print("ligne[", i, "]")
        while (v):
            x = list(map(int, input("Enter les valeurs séparés par un espace: ").split()))
            v = len(x) != d
        initList.append(x)
    return np.array(initList)

def main():
    print("Sil vous plait choisissez  l'algorithme heuristique :")
    print("1/manhattan")
    print("2/malplace")
    c=input("choix:")
    if c=="1":
        algo=ManhattanAlgo()
    elif c=="2":
        algo=MalPlaceAlgo()
    else:
        print("Erreur choix par défaut à été choisi (manhattan algo)")
        algo=ManhattanAlgo()
    EtatTaquin.setAlgo(algo)
    d=int(input("choisir une dimension:"))
    print("saisissez la matrice initiale:")
    init=saisieMatrix(d)
    print("------------------------------------------------")

    print("saisissez la matrice finale:")
    final=saisieMatrix(d)
    print("------------------------------------------------")
    print("solution en cours de résolution")
    print("------------------------------------------------")
    etatInit=EtatTaquin(init)
    etatFinal=EtatTaquin(final)
    l=AStar(etatInit,etatFinal)
    if len(l)==0:
        print("pas de solution")
    else:
        l.reverse()
        for i in l:
            print(i.etat.matrix)


class Main:
    if __name__ == '__main__':
        main()

