class No():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo
        
class Ldse():
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0

    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1

    def inserirFim(self,valor):
        aux=No(valor,None)
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None)
        self.quant+=1

    def show(self):
        aux=self.prim
        while aux!=None:
            print(aux.info)
            aux=aux.prox

    def removerInicio(self):
        if self.quant==0:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1

    def removerFim(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            aux=self.prim
            while aux.prox != self.ult:
                aux=aux.prox
            self.ult=self.aux
            self.ult.prox=None
        self.quant-=1

    def getPrim(self):
        return self.prim.info

    def getUlt(self):
        aux=self.ult
        return self.ult.info

    def getQuant(self):
        return self.quant

    def estahVazia(self):
        return self.quant==0

    def inserirApos(self,valor1,valor2):
        aux1=aux2=self.prim
        if self.prim.info == valor1:
            aux2=No(valor2,self.prim.prox)
            self.prim.prox=aux2
            self.quant+=1
        else:
            while aux1.info != valor1:
                aux1=aux1.prox
            if aux1.info == valor1 and aux1.prox != None:
                aux2=No(valor2,aux1.prox)
                aux1.prox=aux2
            else:
                aux2=No(valor2,None)
                self.ult.prox=aux2
                self.ult=aux2
            self.quant+=1
