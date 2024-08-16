#tarea: considera que el jugador pueda escribir
# las opciones tambien Mayúsculas,
# Capital Case (cuendo solo la primera letra es mayusculas)

# Declaramos un diccionario
opciones = {
    "izquierda": "Te encontraste con un dragón",
    "derecha": "Encontraste un tesoro",
    "adelante": "Caíste en un pozo"
}

# Convertimos las claves del diccionario a minúsculas para hacer la comparación insensible a mayúsculas
opciones_lower = {key.lower(): value for key, value in opciones.items()}

# Solicitamos la opción al usuario
eleccion = input("Estás en un cruce. ¿Quieres ir a la derecha, izquierda o adelante?: ").strip().lower()

if eleccion in opciones_lower:
    print("Respuesta: ", opciones_lower[eleccion])
else:
    print("Opción equivocada")
