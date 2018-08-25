class Frac():
    def __init__(self,num,den):
        self.__num=num
        self.__den=den
    def getnum(self):
        return self.__num
    def getden(self):
        return self.__den
    def setnum(self,num):
        self.__num=num
    def setden(self,den):
        self.__den=den
    def show(self):
        print(self.__num,'/',self.__den)
    def mult(self,num,den):
        self.__num=self.__num*num
        self.__den=self.__den*den
    def div(self,num,den):
        self.__num=self.__num*den
        self.__den=self.__den*num
