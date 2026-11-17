# Conversión de tipos
int('42')       # 42
int(3.9)        # 3 (trunca, no redondea)
float('2.5')    # 2.5
str(123)        # '123'
list('abc')     # ['a', 'b', 'c']
list(range(3))  # [0, 1, 2]
bool(0)         # False
ord('A')        # 65 (código ASCII del carácter)
chr(97)         # 97 (ASCII -> char)

# Dígitos de un número
digitos = [int (d) for d in str(12345)]     # [1, 2, 3, 4, 5]

# Convertir letra minúscula en un índice de 0 a 25
mi_letra = 'c'
ord(mi_letra) - ord('a') 