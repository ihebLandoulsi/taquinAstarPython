from abc import abstractmethod
class transition:
    def __init__(self,etat,value):
        self.etatSuivant=None
        self.value=None
class Etat:
    def __init__(self):
        self.transitions = []
    @abstractmethod
    def generateSucc(self):
        pass
    def getSucc(self):
        if(self.transitions==[]):
            self.generateSucc()
        return self.transitions
    @abstractmethod
    def getHeur(self, Etatfinal):
        pass
    @abstractmethod
    def Equals(self,other):
        pass
class Noeud:
    def __init__(self,etat,estimation,coutTotal,parent):
        self.etat=etat
        self.estimation=estimation
        self.coutTotal=coutTotal
        self.parent=parent
    def getSucc(self,etatfinal):
        transitions=self.etat.getSucc()
        result=[]
        for t in transitions:
            etatSuivant=t.etatsuivant
            coutTotal=self.coutTotal+t.value
            estimation=coutTotal+etatSuivant.getHeur(etatfinal)
            result.push(Noeud(etatSuivant,estimation,coutTotal,self))
        return result

def AStar(etatInit,etatFinal):
    n0=Noeud(etatInit, etatInit.getHeur(), 0, None)
    trouve=False;
    ouverts=[n0]
    fermes=[]
    while(len(ouverts)!=0)and not (trouve):
        leMeilleur=ouverts[0]
        for noeud in ouverts:
            if(leMeilleur.estimation>noeud.estimation):
                leMeilleur=noeud
        courant=leMeilleur
        ouverts=ouverts.remove(courant)
        fermes=fermes.push(courant)
        if etatFinal.equals(courant.etat):
            trouve=True
        else:
            succs=courant.getSucc(etatFinal)
            for succ in succs:
                aux= findEtat(fermes, succ.etat)
                if aux is None:
                    ouverts.push(succ)
                else:
                    if(aux.estimation>succ.estimation):
                        fermes.remove(aux)
                        ouverts.push(succ)
        list=[]
        if trouve:
            i=courant
        while not (i.parent is None):
            list.push(i)
            i=i.parent
            return list

def findEtat(list,etat):
    for noeud in list:
        if noeud.etat.equals(etat):
            return noeud
    return None

