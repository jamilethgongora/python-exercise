"""from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

Label(miFrame, text="Hola a todos", fg= "blue",font=("Comic Sans MS",18)).place(x=200, y=200)

root.mainloop()"""



from tkinter import *

raiz= Tk()

miFrame=Frame(raiz,width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1, padx=10, pady=10)

cuadroDirreccion=Entry(miFrame)
cuadroDirreccion.grid(row=3,column=1, padx=10, pady=10)


nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame,text="Pasword: ")
passLabel.grid(row=1,column=0,sticky="e",padx=10, pady=10)

ApellidoLabel=Label(miFrame,text="Apellido: ")
ApellidoLabel.grid(row=2,column=0,sticky="e",padx=10, pady=10)

DireccionLabel=Label(miFrame,text="Direccion: ")
DireccionLabel.grid(row=3,column=0,sticky="e", padx=10, pady=10)


raiz.mainloop()


