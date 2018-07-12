import sqlite3

miConexion=sqlite3.connect("BBDD/Primera base")

miCursor=miConexion.cursor()


#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")               #crear una table de productos

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

variosProductos=[ 

    ("BALON", 15, "DEPORTES"),
    ("Camisa", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),                                                         #insert muchos registros
    ("Camion", 20, "Jugueteria")

]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?,?)", variosProductos)
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)


# miCursor.execute("DELETE FROM PRODUCTOS")

miCursor.execute("SELECT *  FROM PRODUCTOS")

variosProductos1=miCursor.fetchall()                                         #fetchall devuelve una lista con los reg

for productos in variosProductos:

    print("Nombre Articulo:", productos[0], "Seccion:", productos[2])



# print(variosProductos1)


miConexion.commit()                                                 #CONFIRMAMOS EL REGISTRO DE LA TABLE

miConexion.close() 