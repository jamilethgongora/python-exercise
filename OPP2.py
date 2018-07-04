class Coche():

    def __init__(self):                          #constructor (self.)

        self.__largoChasis=250                   #encapsuladas (__)
        self.__anchoChasis=120
        self.__ruedas=4                         
        self.__enmarcha=False


    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo==False):
            return "Algo ha salido mal con el chequeo, no podemos arrancar"
        
        else:

            return "El coche esta parado"

    
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ", 
        self.__largoChasis)

    
    def __chequeo_interno(self):                                                  #metodo 
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True 

        else:
            return False



miCoche=Coche()
print(miCoche.arrancar(True))

(miCoche.estado())

 
print(".....................A continuacion creamos el segundo objeto...........")

miCoche2=Coche()    
print(miCoche2.arrancar(False))
(miCoche2.estado())
