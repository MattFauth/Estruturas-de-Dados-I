class No():
    def __init__(self,ant,valor,prox):
        self.ant = ant
        self.info = valor
        self.prox = prox
        
class Ldde():
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(None,valor,None)
        else:
            self.prim.ant = self.prim = No(None,valor,self.prim)
        self.quant += 1

    def inserirFim(self,valor):
        if self.quant == 0:
            self.ult = self.prim = No(None,valor,None)
        else:
            self.ult.prox = self.ult = No(self.ult,valor,None)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = None
        self.quant -= 1

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info)
            aux = aux.prox

    def showReverso(self):
        aux = self.ult
        while aux != None:
            print(aux.info)
            aux = aux.ant

    def getPrim(self):
        return self.prim

    def getUlt(self):
        return self.ult          
            
    def inserirApos(self,valor1,valor2):
        aux1=aux2=self.prim
        if self.prim.info == valor1:
            aux2=No(self.prim,valor2,self.prim.prox)
            self.prim.prox.ant=self.prim.prox=aux2
            self.quant+=1
        else:
            while aux1.info != valor1:
                aux1=aux1.prox
            if aux1.info == valor1 and aux1.prox != None:
                aux2=No(aux1,valor2,aux1.prox)
                aux1.prox.ant=aux1.prox=aux2
            else:
                aux2=No(aux1,valor2,None)
                self.ult.prox=aux2
                self.ult=aux2
            self.quant+=1
                
