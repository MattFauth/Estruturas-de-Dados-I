class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)

    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()

    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()

    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()    

    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()

    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()

    def h(self,valor):
        if self.raiz != None:
            return self.raiz.h(valor)
        
    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()

    def maisesq(self):
        if self.raiz != None:
            return self.raiz.maisesq()

    def contaQtd(self, valor):
        if self.raiz != None:
            return self.raiz.contaQtd(valor)

    def maiorQue(self, valor):
        if self.raiz != None:
            return self.raiz.maiorQue(valor)

    def somaMaiores(self, valor):
        if self.raiz != None:
            return self.raiz.somaMaiores(valor)
        
class No:
    def __init__(self,valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor <= self.info:
            if self.esq == None:
                 self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def busca(self, valor):
        if valor == self.info:
            return True
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)
    
    def buscaseovalornexistir(self, valor):
        if valor == self.info:
            return True
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                aux= self.esq.busca(valor)
                if aux!= False:
                    return aux+1
                else:
                    return False
        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.busca(valor)
                if aux != False:
                    return aux+1
                else:
                    return False

    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info,end=" ")
        if self.dir != None:
            self.dir.inOrdem()

    def preOrdem(self):
        print(self.info,end=" ")
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:            
            self.dir.preOrdem()

    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:            
            self.dir.posOrdem()
        print(self.info,end=" ")
              
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        print(total)
        return total

    def somaFolhas(self):
        total = 0
        if self.esq==None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total

    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq==None and self.dir == None:
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.printFolhas()

    def max(self, a, b):
        if a>b:
            return a
        return b

    def altura(self):
        hesq=hdir=0
        if self.esq!=None:
            hesq=self.esq.altura()
        if self.dir!=None:
            hdir=self.dir.altura()
        return 1 + max(hesq,hdir)

    def h(self, valor):
        if valor == self.info:
             return self.altura()
        elif valor <= self.info:
            if self.esq == None:
                 return False
            else:
                 return self.esq.h(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)

    def maisdir(self):
        if self.dir!=None:
            return self.dir.maisdir()
        else:
            return self.info

    def maisesq(self):
        if self.esq!=None:
            return self.esq.maisesq()
        else:
            return self.info

    def contaQtd(self, valor):
        if valor == self.info:
            if self.esq!=None:
                return 1 + self.esq.contaQtd(valor)
            else:
                return 1
        elif valor < self.info:
            if self.esq!=None:
                return self.esq.contaQtd(valor)
            else:
                return 0
        else:
            if self.dir!=None:
                return self.dir.contaQtd(valor)
            else:
                return 0

    def maiorQue(self, valor):
        if valor == self.info:
            if self.dir != None:
                self.dir.inOrdem()
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.maiorQue(valor)
                print(self.info)
                if aux == True and self.dir!=None:
                    self.dir.inOrdem()
                return True
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.maiorQue(valor)

    def somaMaiores(self, valor):
        if valor == self.info:
            if self.dir != None:  
                return self.dir.soma()
            else:
                return 0
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.somaMaiores(valor)
                if aux and self.dir!=None:
                     return aux + self.dir.soma() + self.info
        else:
            if self.dir == None:
                return 0
            else:
                return self.dir.somaMaiores(valor)
