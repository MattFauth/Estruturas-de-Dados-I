class No():
    def __init__(self,ant,valor,prox):
        self.ant=ant
        self.info=valor
        self.prox=prox
class Ldde():
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0
    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(None,valor,None)
            self.quant+=1
        else:
            self.prim.ant=self.prim=No(None,valor,self.prim)
            self.quant+=1
    def inserirFim(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(None,valor,None)
            self.quant+=1
        else:
            self.ult.prox=self.ult=No(self.ult,valor,None)
            self.quant+=1
    def show(self):
        aux=self.prim
        while aux!=None:
            print(aux.info)
            aux=aux.prox
    def showReverso(self):
        aux=self.ult
        while aux!=None:
            print(aux.info)
            aux=aux.ant
    def RemoverFim(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            aux=self.prim
            while aux.prox!=self.ult:
                aux=aux.prox
            self.ult=aux
            self.ult.prox=None
        self.quant-=1
    def RemoverInicio(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            aux=self.ult
            while aux.ant!=self.prim:
                aux=aux.ant
            self.prim=aux
            self.prim.ant=None
        self.quant-=1
    def AlterarValor(self,valor1,valor2):
        aux1=aux2=self.prim
        if self.quant==1:
            self.prim=self.ult=No(None,valor1,None)
        else:
            while aux.prox!=None:
                if aux.self==valor2:
                    aux.self==valor1
                
