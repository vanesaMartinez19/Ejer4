class Ventana:
    __Titulo = str
    __XsupIzq = 0
    __YsupIzq = 0
    __XinfDer = 500
    __YinfDer = 500
    def __init__(self, Titulo, XsupIzq=100, YsupIzq=100, XinfDer=500, YinfDer=500):

        self.__Titulo=Titulo
        self.__XsupIzq=int(XsupIzq)
        self.__YsupIzq=int(YsupIzq)
        self.__XinfDer=int(XinfDer)
        self.__YinfDer=int(YinfDer)
    def setXS(self, v):
        self.__XsupIzq = v
    def getXS(self):
        return self.__XsupIzq
    def setYS(self, v):
        self.__YsupIzq = v
    def getYS(self):
        return self.__YsupIzq
    def setXI(self, v):
        self.__XinfDer = v
    def getXI(self):
        return self.__XinfDer
    def setYI(self, v):
        self.__YinfDer = v
    def getYI(self):
        return self.__YinfDer
    def __str__(self):
        return +self.__Titulo

    def mostrar(self):
        #print("Titulo: {} ".format(self.__Titulo))
        print("Coordenada Vertice Superior Izquierdo (x,y) = (",self.__XsupIzq,',', self.__YsupIzq,")")
        print("Coordenada Vertice Inferior Derecho (x,y) = (",self.__XinfDer,',', self.__YinfDer,")")

    def getTitulo(self):
        return self.__Titulo
    def alto(self):
        return (self.__YinfDer-self.__YsupIzq)
    def ancho(self):
        return (self.__XinfDer-self.__XsupIzq)

    def moverDerecha(self,x=1):
        x = x + self.__XinfDer
        self.setXI(x)

    def moverIzquierda(self,x=1):
        x = self.__XinfDer - x
        self.setXI(x)

    def bajar(self,x=1):
        x = self.__YsupIzq - x
        self.setYS(x)
    def subir(self,x=1):
        x = self.__YsupIzq + x
        self.setYS(x)





