from tkinter import *

raiz=Tk()

raiz.title("Ventana de prueba")

raiz.config(bg="blue")

miFrame = Frame()

miFrame.pack()                                              #podemos direccionarlo donde queramos

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="groove")                         #border

miFrame.config(cursor="pirate")

raiz.mainloop()  