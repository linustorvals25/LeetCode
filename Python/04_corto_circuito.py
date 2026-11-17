# Ejemplo operadores
i, n = 3, 10
print(0 <=  i < n)      # True: comparacion encadenada
print(not (i > 5) and n == 10) # True

# Cortocircuito: el orden de las condiciones evita un IndexError
arr = [1, 2, 3, 4]
j = 3
if j < len(arr) and arr[j] == 3:  # si j esta fuera de rango, no evalua arr[j]
    print('encontrado')
    
# Comparar con None
nodo = None
if nodo is None:
    print('sin nodo')