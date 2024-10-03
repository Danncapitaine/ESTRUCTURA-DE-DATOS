def ordenamientpo de Burbuja(arr):
    n = len(arr)
    # Bucle exterior para recorrer toda la lista
    for i in range(n):
        # Bucle interior para comparar elementos adyacentes
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Lista de ejemplo
arr = [64, 34, 25, 12, 22, 11, 90]
print("Lista sin ordenar:", arr)

Ordenamiento de Burbujas(arr)
print("Lista ordenada:", arr)
