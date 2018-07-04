class Vehiculos():

    def __init__(self,marca, modelo):         #constructor

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    
    def arrancar(self):                     #metodos
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:",self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,             #\n salto de linea 
            "\nAcelerando:",self.acelera, "\nFrenando:", self.frena)




class furgoneta(Vehiculos):
     def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furganeta no esta cargada"




class Moto(Vehiculos):
    hacecaballito=""
    def caballito(self):
        self.hacecaballito="Voy haciendo caballito"

    def estado(self):
        print("Marca:",self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,             #\n salto de linea 
            "\nAcelerando:",self.acelera, "\nFrenando:", self.frena,"\n",self.hacecaballito)




class VElectricos():
    def __init__(self):

        self.autonomia=100

    def cargarEnergia(self):

        self.cargando=True



miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta=furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))
    
class BiciElectrica(VElectricos,Vehiculos):                         #hereda el constructor de ambos, pero solo lee 1 izqd
    pass
 
miBici=BiciElectrica() 