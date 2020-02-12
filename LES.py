class Les():
    def __init__(self):
        self.vet=[None,None,None,None,None]
        self.quant=0
        
    def estahvazia(self):
        return self.quant==0
    
    def estahcheia(self):
        return self.quant==5
    
    def pegaQuant(self):
        return self.quant
    
    def inserirFim(self,valor):
        self.vet[self.quant]=valor
        self.quant+=1
        
    def show(self):
        i=0
        while i<self.quant:
            print(self.vet[i])
            i+=1
            
    def removerFim(self):
        self.quant-=1

    def getPrim(self):
        return self.vet[0]

    def getUlt(self):
        return self.vet[self.quant-1]

    def inserirInicio(self,valor):
        i=self.quant
        while i >0:
            self.vet[i]=self.vet[i-1]
            i-=1
        self.vet[0]=valor
        self.quant+=1

    def removerInicio(self):
        i=0
        while i<self.quant-1:
            self.vet[i]=self.vet[i+1]
            i+=1
        self.quant-=1

    def inserirApos(self,valor1,valor2):
        i=0
        while i < self.quant:
            if self.vet[i]==valor1:
                aux = 0
                aux=self.vet[i]
                self.vet[i+1]=valor2
                self.quant+=1
            i+=1

    def inserirAposDet(self,valor1,valor2):
        i=0
        while i < self.quant:
            if self.vet[i]==valor1:
                j=self.quant
                while j>i+1:
                    self.vet[j]=self.vet[j-1]
                    j-=1
                self.vet[j]=valor2
                self.quant+=1
            i+=1

    def limparLista(self):
        self.quant=0
        
        
