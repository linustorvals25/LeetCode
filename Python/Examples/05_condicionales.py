# Condicionales
x = 7

if x < 0:
    signo = 'negativo'
elif x == 0:
    signo = 'cero'
else:
    signo = 'positivo'

print(f'La variable x =  {x} tiene signo {signo}')

# Expresion condicional (ternario)
paridad = 'par' if x % 2 == 0 else 'impar'

print(f'La varible x = {x} tiene paridad {paridad}')