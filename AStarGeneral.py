from abc import abstractmethod
class Transition:
    def __init__(self,etat,value):
        self.etatSuivant=etat
        self.value=value
    @property
    def etatSuivant(self):
        return self._etatSuivant
    @etatSuivant.setter
    def etatSuivant(self,etat):
        self._etatSuivant=etat
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,val):
        self._value=val
class Etat:
    def __init__(self):
        self.transitions = []
    @abstractmethod
    def generateSucc(self):
        pass
    def getSucc(self):
        self.transitions=self.generateSucc()
        return self.transitions
    @abstractmethod
    def getHeur(self, Etatfinal) -> float:
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
            etatSuivant=t.etatSuivant
            coutTotal=self.coutTotal+t.value
            estimation=coutTotal+etatSuivant.getHeur(etatfinal)
            result.append(Noeud(etatSuivant,estimation,coutTotal,self))
        return result

def AStar(etatInit,etatFinal):
    n0=Noeud(etatInit, etatInit.getHeur(etatFinal), 0, None)
    trouve=False
    ouverts= [n0]
    fermes=[]
    while(len(ouverts)!=0)and not (trouve):
        leMeilleur=ouverts[0]
        for noeud in ouverts:
            if(leMeilleur.estimation>noeud.estimation):
                leMeilleur=noeud
        courant=leMeilleur
        ouverts.remove(courant)
        fermes.append(courant)
        if etatFinal.Equals(courant.etat):
            trouve= True
        else :
            succs=courant.getSucc(etatFinal)

            for succ in succs:
                aux= findEtat(fermes, succ.etat)
                if aux is None:
                    ouverts.append(succ)
                else:
                    if(aux.estimation>succ.estimation):
                        fermes.remove(aux)
                        ouverts.append(succ)
        # print(courant.etat.matrix)
        # print("ouverts")
        # for i in ouverts:
        #     print(i.etat.matrix)
        # print ("-------------------------------------------")
        list=[]
        if trouve:
            i=courant
            while not (i is None):
                list.append(i)
                i=i.parent
            return list
    return list

def findEtat(list,etat):
    for noeud in list:
        if noeud.etat.Equals(etat):
            return noeud
    return None

