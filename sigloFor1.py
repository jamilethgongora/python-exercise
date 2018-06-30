for i in range(10):                                 #range en python 3 funciona como un array 
    print(i)



for i in range(10,50,3):                                #del 10 al 50 y un tercera para decirle de cuanto en cuanto quiere contar(3)
    print(f"valor de la variable {i}")               #f es una notacion especial/valor de la variable 0.....




valido=False

email=input("Introduce tu email: ")

for i in range(len(email)):

    if email[i]==  "@":
        valido=True

if valido:
    print("Email correcto")

else:
    print("Email incorrecto")
