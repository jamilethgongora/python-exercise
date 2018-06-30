"""i=1

while i<=10:
    print("Ejecucioón" + str(i))
    i=i+1

print("Termino la ejecución")"""



"""edad=int(input("Introduce tu edad, por favor: "))

while edad<5 or edad>100:
    print("Has introducido una edad incorrecta, vuelve a intentarlo")
    edad=input(input("Introduce tu edad por favor: "))                      #el programa se ejecutara infinitas veces hasta que la edad se FALSE 

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))"""



"""import math


print ("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número por favor: "))

intentos=0

while numero<0:
    print("No se puede hallar la raíz cuadrada de un número negativo")

    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break
    
    numero=int(input("Introduce el número por favor: "))
    if numero<0:
            intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print ("La raíz cuadrada de " + str(numero) + " es " + str(solucion))"""



            
                                     #Instrucccion Continue



"""for letra in "Python":              #lee todas nuestras letras y se salta la H
    if letra=="h":
        continue
    
    print("Viendo la letra: " + letra)"""



"""nombre="Pildoras Informaticas"                  #Cuenta el numeros de caracteres sin contar el espacio(20)

contador=0

for i in nombre:
    if i==" ":
        continue
    contador+=1

print(contador)"""



                           # Instrucccion Pass(pasar)
class Miclase:
    pass #Para terminar mas tarde, es como que fuera nula


                            # Instrucccion ELSE


email=input("Introduce tu email, por favor: ")

for i in email:
    if i=="@":
        arroba=True
        break

else:
    arroba=False         #cuando ya ha analizado todo el codigo y no encuentra el @ efecuta False

print(arroba)