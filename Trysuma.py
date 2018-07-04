"""def suma(num1,num2):
        return num1+num2 


try:
    op1 = int(input("Introduce el primer numero: "))
    op2 = int(input("Introduce el segundo numero: "))


    print(suma(op1,op2))

except:
    print("No se puede leer texto")
        

print("Operacion ejecutada. Continua la ejecucion del programa")"""




#raiz cuadra de un numero 


import math 

def calculaRaiz(num1):

    if num1<0:
        raise ValueError ("El numero no puede ser negativo")

    else:
        return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))

try:
    print(calculaRaiz(op1))

except ValueError as ErrorNumeronegativo:
        print(ErrorNumeronegativo)

print("Programa terminado")
