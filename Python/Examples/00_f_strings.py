"""Guía práctica de f-strings en Python.

Este archivo reúne los ejemplos explicados de f-strings (formatted string
literals). Puedes ejecutarlo directamente con Python 3.8 o una versión
posterior. La sintaxis básica de f-strings existe desde Python 3.6; el uso
para depuración con {expresion=} requiere Python 3.8 o posterior.
"""


# ============================================================================
# 1. SINTAXIS BÁSICA
# ============================================================================
# Una f-string se crea colocando la letra f antes de las comillas.
# Las expresiones o variables que deben sustituirse se escriben entre llaves.
# Python evalúa esas expresiones y coloca sus resultados dentro del texto.

nombre = "Carlos"
edad = 25

mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print("1. SINTAXIS BÁSICA")
print(mensaje)
print()


# ============================================================================
# 2. INSERTAR EXPRESIONES, FUNCIONES Y MÉTODOS
# ============================================================================
# Las llaves no sirven solamente para insertar variables: también permiten
# evaluar operaciones matemáticas, llamar funciones y utilizar métodos.

a = 10
b = 5

print("2. INSERTAR EXPRESIONES")
print(f"La suma es: {a + b}")
print(f"La resta es: {a - b}")
print(f"La multiplicación es: {a * b}")
print(f"La división es: {a / b}")

# También puedes llamar métodos y funciones dentro de una f-string.
nombre_lenguaje = "python"
print(f"Lenguaje: {nombre_lenguaje.upper()}")
print(f"Número de caracteres: {len(nombre_lenguaje)}")
print()


# ============================================================================
# 3. FORMATEAR NÚMEROS
# ============================================================================
# La sintaxis general de un especificador de formato es:
#
#     f"{expresion:formato}"
#
# Los dos puntos (:) separan la expresión del formato que se desea aplicar.

# 3.1. Controlar la cantidad de decimales.
# .2f muestra dos decimales; .4f muestra cuatro y .6f muestra seis.
# La letra f indica que se utilizará el formato de punto flotante.

pi = 3.14159265359

print("3. FORMATEAR NÚMEROS")
print("3.1. Cantidad de decimales")
print(f"Dos decimales: {pi:.2f}")
print(f"Cuatro decimales: {pi:.4f}")
print(f"Seis decimales: {pi:.6f}")

# 3.2. Separadores de miles.
# La coma (,) agrega separadores de miles para facilitar la lectura.

poblacion = 123456789
print("3.2. Separadores de miles")
print(f"Población: {poblacion:,}")

# 3.3. Porcentajes.
# El especificador % multiplica el valor por 100 y agrega el símbolo %.
# .2% muestra dos decimales; .0% muestra el porcentaje sin decimales.

resultado = 0.8567
print("3.3. Porcentajes")
print(f"Resultado: {resultado:.2%}")
print()


# ============================================================================
# 4. ALINEAR TEXTO
# ============================================================================
# Puedes reservar un ancho determinado para un valor y elegir su alineación.
# El número indica el ancho total del campo, incluidos los caracteres del
# texto. Los símbolos de alineación son:
#
#     <  Alinea a la izquierda.
#     >  Alinea a la derecha.
#     ^  Centra el texto.
#
# En este ejemplo, cada campo tiene un ancho de 15 caracteres. Los caracteres
# | se incluyen para que puedas distinguir visualmente los espacios.

nombre = "Python"

print("4. ALINEAR TEXTO")
print(f"Izquierda: |{nombre:<15}|")
print(f"Derecha:   |{nombre:>15}|")
print(f"Centro:    |{nombre:^15}|")
print()


# ============================================================================
# 5. MOSTRAR LLAVES LITERALMENTE
# ============================================================================
# En una f-string, las llaves simples se utilizan para delimitar expresiones.
# Si necesitas imprimir llaves como caracteres normales, debes duplicarlas:
# {{ produce { y }} produce }.

nombre = "Carlos"

print("5. MOSTRAR LLAVES LITERALMENTE")
print(f"Mi nombre es {nombre}")
print(f"En Python se utilizan llaves así: {{variable}}")
print()


# ============================================================================
# 6. DEPURACIÓN CON F-STRINGS
# ============================================================================
# Desde Python 3.8 puedes escribir {expresion=} para mostrar tanto la
# expresión como su resultado. Es una forma práctica de inspeccionar valores
# durante la depuración sin tener que escribir etiquetas manualmente.

numero = 10
resultado = numero * 2

print("6. DEPURACIÓN CON F-STRINGS")
print(f"{numero=}")
print(f"{resultado=}")
print(f"{numero * resultado=}")
print()


# ============================================================================
# 7. COMPARACIÓN CON OTROS MÉTODOS DE FORMATEO
# ============================================================================
# Python permite construir cadenas de varias maneras. Estos tres ejemplos
# generan el mismo mensaje, pero las f-strings suelen ser más directas.

nombre = "Carlos"
edad = 25

# 7.1. Concatenación.
# Para concatenar una cadena con un número es necesario convertir el número
# a texto mediante str().
mensaje_concatenado = (
    "Hola, me llamo " + nombre + " y tengo " + str(edad) + " años."
)

# 7.2. Método format().
# Los marcadores {} se sustituyen por los argumentos de format(), en orden.
mensaje_format = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)

# 7.3. f-string.
# Las variables aparecen directamente dentro de la cadena, lo que facilita
# relacionar cada valor con el lugar donde se utiliza.
mensaje_f_string = f"Hola, me llamo {nombre} y tengo {edad} años."

print("7. COMPARACIÓN DE MÉTODOS")
print("Concatenación:", mensaje_concatenado)
print("format():     ", mensaje_format)
print("f-string:     ", mensaje_f_string)
print()


# ============================================================================
# 8. EJEMPLO PRÁCTICO: CALCULAR UN DESCUENTO
# ============================================================================
# Este ejemplo reúne varios usos de las f-strings en un caso sencillo.
# Se calcula el ahorro y el precio final de un producto después de aplicar
# un descuento. Los formatos .2f y .0% controlan cómo se muestran los valores.

producto = "Teclado mecánico"
precio = 1200.00
descuento = 0.15

ahorro = precio * descuento
precio_final = precio - ahorro

print("8. EJEMPLO PRÁCTICO: DESCUENTO")
print(f"Producto: {producto}")
print(f"Precio original: ${precio:.2f}")
print(f"Descuento: {descuento:.0%}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Precio final: ${precio_final:.2f}")
