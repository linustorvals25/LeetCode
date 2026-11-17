# Tipos de datos
n = 42               # int
promedio = 8.5       # float
palabra = 'leetcode' # str
es_par = n % 2 == 0  # bool -> True
nulo = None          # ausencia de valor

# La funcion type regresa la clase de la variable
print(type(n))       # <class 'int'>

# Asignación múltiple 
a, b = 1, 2

# Intercambio sin variable temporal
a, b = b, a

# Infinito: valor inicial ideal para buscar un mínimo o un máximo
infinito_positivo = float('inf')
infinito_negativo = float('-inf')

# Operadores
print(7 / 2)            #  7 / 2  = 3.5
print(7 // 2)           #  7 // 2 = 3
print(-7 // 2)          # -7 // 2 = -4 -> trunca hacia -inf
print(int(-7 / 2))      #  int(-7 / 2) -> trunca hacia cero
print(7 % 3)            #  7 % 3  = 1
print(-7 % 3)           # -7 % 3  = 2
print(2 ** 10)          #  2 ^ 10 = 1024
print(divmod(17, 5))    # (a // b, a % b) -> div(17, 5) = (3, 2)

# Booleanos y truthiness
# False -> 0, 0.0, '', [], (), {}, set(), None, False, deque(), range(0), todo contenedor vacío
nums = []
if not nums: 
    print('lista vacía')
