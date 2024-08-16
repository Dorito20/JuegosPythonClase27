#Declaramos un diccinario

opciones = {
    "izquierda":"Te encontraste con un dragon",
    "derecha":"Encontrotraste un tesora" ,
    "adelante":"caíste en un pozo"
}

#Solicitamos la opción al usuario
eleccion = input("Estás en un cruze. ¿Quiero ir a la derecha, izquierda o adelante?: ")

if eleccion in opciones:
    print("Respuesta: ",opciones[eleccion])
else:
    print("opció equivacocada")

#Carpeta con nombre que diga Clase27
#tarea: considera que el jugador pueda escribir
# las opciones tambien Mayúsculas,
# Capital Case (cuendo solo la primera letra es mayusculas)