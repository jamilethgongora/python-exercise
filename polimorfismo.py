class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo en dos ruedas")


class Camion():

    def desplazamiento(self):
        print("Me desplazo en seis ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto()

desplazamientoVehiculo(miVehiculo)




#un objeto puede cambiar de formas dependiendo del contexto en que se utilice.