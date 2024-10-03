# Definición de una estructura de datos que contiene otras estructuras de datos
numeros = ((1, 2, (3, 5), 8, "hola"), (2, 5, 8))

# Imprime el cuarto elemento del primer grupo de datos (8)
print(numeros[0][3])

# Imprime el quinto elemento del primer grupo de datos ("hola")
print(numeros[0][4])

# Imprime el primer carácter de la palabra "hola" ('h')
print(numeros[0][4][0])

# Imprime el segundo carácter de la palabra "hola" ('o')
print(numeros[0][4][1])

# Imprime el tercer carácter de la palabra "hola" ('l')
print(numeros[0][4][2])

# Imprime el cuarto carácter de la palabra "hola" ('a')
print(numeros[0][4][3])
