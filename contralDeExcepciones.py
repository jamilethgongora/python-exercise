def suma(num1,num2):
    return num1+num2


def resta(num1, num2):
    return num1-num2


def multiplica(num1,num2):
    return num1*num2 


def divide(num1,num2):                                  
    try:                                                         #try es una excepcion (errores) 
        return num1/num2
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0 ")
        return"Operacion erronea"

while True:

    try:
        op1=(int(input("Introduce el primer numero: ")))

        op2=(int(input("Introduce el segundo numero: ")))

        break

    except:
        print("Los valores introducidos no son correctos, Intentalo de nuevo: ")

operacion=input("Introduce la operacion a realizar(suma,resta,multiplica,divide)")


if operacion =="suma":
    print(suma(op1,op2))

elif operacion =="resta":
    print(resta(op1,op2))

elif operacion =="multiplica":
    print(multiplica(op1,op2))

elif operacion =="divide":
    print(divide(op1,op2))


else:
    print("Operacion no contenplada")


print("Operacion ejecutada. Continua la ejecucion del programa")




"""def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No se permiten edades negativas")

    if edad<20:
        return "Eres muy joven"
    
    elif edad<40:
        return "Eres joven"
    
    elif edad<65:
        return "Eres maduro"

    elif edad<100:
        return "CUidate..."
    
print(evaluaEdad(16))"""