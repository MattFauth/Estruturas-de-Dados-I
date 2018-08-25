class LES():
    def __init__(self):
        self.list=[None,None,None,None,None]
        self.quant=0
    def estaVazio(self):
        return self.quant==0
    def estaCheia(self):
        return self.quant==5
    def getQuant(self):
        return self.quant
    def insertEnd(self,value):
        self.list[self.quant]=value
        self.quant+=1
    def show(self):
        i=0
        while i<self.quant:
            print(self.list[i])
            i+=1
    def removeEnd(self):
        self.quant-=1
    def itsFull(self):
        return self.quant==5
    def itsEmpty(self):
        return self.quant==0
    def getFirst(self):
        return self.lista[0]
    def getLast(self):
        return self.lista[self.quant-1]
    def inserirInicio(self,valor):
        self.lista[0] == valor
    def removerInicio(self,valor):
        self.quant-=1
    def getPrim(self):
        return self.list[0]
    def getUlt(self):
        return self.lista[self.quant-1] 
    def InsertStart(self,value):
        i=self.quant
        while i >0:
            self.list[i]=self.list[i-1]
            i-=1
        self.list[0]=value
        self.quant+=1
    def RemoveStart(self):
        i=0
        while i<self.quant-1:
            self.list[i]=self.list[i+1]
            i+=1
        self.quant-=1
    def insertAfter(self,val1,val2):
        i=0
        while i < self.quant:
            if self.list[i]==val2:
                j=self.quant
                while j>i+1:
                    self.list[j]=self.list[j-1]
                    j-=1
                self.list[j]=val1
                self.quant+=1
            i+=1
    def inserirAntes(self,valor1, valor2):
        i=0
        j=self.quant
        while i < self.quant:
            if self.lista[i] == valor2:
                while j > i:
                    self.lista[j] = self.lista[j-1]
                    j-=1
                self.lista[j]=valor1
                self.quant+=1
            i+=1

    def substituir(self,val1,val2):
        i=0
        while i < self.quant:
            if self.list[i]==val1:
                self.list[i]=val2
            i+=1
    def substituirEcontar(self,val1,val2):
        i=0
        cont=0
        while i < self.quant:
            if self.list[i]==val1:
                self.list[i]=val2
                cont+=1
            i+=1
        return cont
