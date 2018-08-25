class No():
    def __init__(self,valor,prox):
        self.info=valor
        self.prox=prox
class LDSE():
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0
    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1
    def removerInicio(self):
        if self.quant == 1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1
    def show(self):
        aux=self.prim
        while aux!=None:
            print(aux.info)
            aux=aux.prox
    def inserirFim(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None)
        self.quant+=1
    def removerFim(self):
        if self.quant == 1:
            self.prim=self.ult=None
        else:
            aux=self.prim
            while aux.prox!=self.ult:
                aux=aux.prox
            self.ult=aux
            self.ult.prox=None
        self.quant-=1
    def inserirAntesDe(self,valor1,valor2):
        ant=aux=self.prim
        if self.prim.info==valor2:
            self.prim=No(valor1,self.prim)
            aux=aux.prox
            self.quant+=1
        while aux!=None:
            if aux.info==valor2:
                ant.prox=No(valor1,aux)
                self.quant+=1
            ant=aux
            aux=aux.prox
        
        
                
