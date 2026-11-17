# ============================================================
# OPERADORES ARITMÉTICOS
# ============================================================
# +   Suma
# -   Resta
# *   Multiplicación
# /   División (resultado decimal)
# //  División entera (redondea hacia abajo)
# %   Módulo (residuo de la división)
# **  Potencia
# +=  Suma y asignación
# -=  Resta y asignación
# *=  Multiplicación y asignación
#
# Python no tiene operadores ++ ni --.
# Para incrementar o decrementar se utiliza += 1 o -= 1.

a = 10
b = 5

print("\n--- Operadores aritméticos ---")

print(f"Suma: {a + b}")                       # 15
print(f"Resta: {a - b}")                      # 5
print(f"Multiplicación: {a * b}")             # 50
print(f"División: {a / b}")                   # 2.0
print(f"División entera: {a // b}")           # 2
print(f"Módulo (residuo): {a % b}")            # 0
print(f"Potencia: {a ** b}")                  # 100000

# Operadores de asignación compuesta

a += b
print(f"Después de a += b: {a}")              # 15

a -= 1
print(f"Después de a -= 1: {a}")              # 14

a *= 2
print(f"Después de a *= 2: {a}")              # 28


# ============================================================
# OPERADORES DE COMPARACIÓN
# ============================================================
# ==  Igual que
# !=  Diferente de
# <   Menor que
# >   Mayor que
# <=  Menor o igual que
# >=  Mayor o igual que
#
# Los operadores de comparación devuelven True o False.
# También se pueden encadenar varias comparaciones.

a = 10
b = 5

print("\n--- Operadores de comparación ---")

print(f"a == b: {a == b}")                   # False
print(f"a != b: {a != b}")                   # True
print(f"a < b: {a < b}")                     # False
print(f"a > b: {a > b}")                     # True
print(f"a <= b: {a <= b}")                   # False
print(f"a >= b: {a >= b}")                   # True

# Comparaciones encadenadas:
# Equivale a (1 < b) and (b < 10).

print(f"1 < b < 10: {1 < b < 10}")           # True
print(f"1 <= a <= 10: {1 <= a <= 10}")       # True


# ============================================================
# OPERADORES LÓGICOS
# ============================================================
# and  Devuelve True si ambas condiciones son verdaderas.
# or   Devuelve True si al menos una condición es verdadera.
# not  Invierte el valor lógico.
#
# and y or utilizan evaluación de cortocircuito (short-circuit).
# Esto significa que pueden evitar evaluar la segunda expresión
# cuando el resultado ya se puede determinar.

print("\n--- Operadores lógicos ---")

es_mayor = a > b
es_positivo = b > 0

print(f"es_mayor and es_positivo: {es_mayor and es_positivo}")  # True
print(f"es_mayor or es_positivo: {es_mayor or es_positivo}")    # True
print(f"not es_mayor: {not es_mayor}")                          # False

# Ejemplo de cortocircuito con and:
denominador = 0

# La segunda condición NO se evalúa porque la primera es False.
# Por eso no ocurre una división entre cero.
print(denominador != 0 and 10 / denominador > 1)  # False

# Ejemplo de cortocircuito con or:
# La segunda condición NO se evalúa porque la primera es True.
print(denominador == 0 or 10 / denominador > 1)   # True


# ============================================================
# OPERADORES DE PERTENENCIA
# ============================================================
# in      Comprueba si un elemento pertenece a una colección.
# not in  Comprueba si un elemento NO pertenece a una colección.
#
# Complejidad promedio:
# x in list -> O(n)
# x in set  -> O(1)

print("\n--- Operadores de pertenencia ---")

lenguajes = ["Python", "C++", "Java", "C"]
lenguajes_set = {"Python", "C++", "Java", "C"}

print(f"'Python' in lenguajes: {'Python' in lenguajes}")  # True
print(f"'Ruby' in lenguajes: {'Ruby' in lenguajes}")      # False

print(f"'Ruby' not in lenguajes: {'Ruby' not in lenguajes}")  # True

# También se pueden utilizar con conjuntos (set).
print(f"'Java' in lenguajes_set: {'Java' in lenguajes_set}")  # True


# ============================================================
# OPERADORES DE IDENTIDAD
# ============================================================
# is      Comprueba si dos referencias apuntan al mismo objeto.
# is not  Comprueba si dos referencias apuntan a objetos distintos.
#
# Utiliza is e is not principalmente para comprobar None.
# No utilices is para comparar valores numéricos o cadenas.

print("\n--- Operadores de identidad ---")

dato = None

print(f"dato is None: {dato is None}")          # True
print(f"dato is not None: {dato is not None}")  # False

# Diferencia entre igualdad (==) e identidad (is).

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

# == compara los valores de los objetos.
print(f"lista1 == lista2: {lista1 == lista2}")  # True

# is comprueba si son exactamente el mismo objeto.
print(f"lista1 is lista2: {lista1 is lista2}")  # False
print(f"lista1 is lista3: {lista1 is lista3}")  # True