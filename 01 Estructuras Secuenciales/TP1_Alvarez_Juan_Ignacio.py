# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.#

print ("Hola Mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.#

nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}, un gusto!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.#

nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
residencia = input("Ingrese su lugar de residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.#

radio = input("Ingrese el radio del circulo:")
radio = float(radio)
area = 3.14 * radio**2
perimetro = 3.14*2*radio

print (f"El area del circulo es {area} y el perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.#

segundos = input("Ingrese la cantidad de segundos:")
segundos = int(segundos)
horas =  segundos/60
horas = float(horas)

print(f"Esto equivale a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.#

numero = input("Ingrese un numero ")
numero = int(numero)

print( numero, "por 1 es" ,numero*1)
print( numero, "por 2 es" ,numero*2)
print( numero, "por 3 es" ,numero*3)
print( numero, "por 4 es" ,numero*4)
print( numero, "por 5 es" ,numero*5)
print( numero, "por 6 es" ,numero*6)
print( numero, "por 7 es" ,numero*7)
print( numero, "por 8 es" ,numero*8)
print( numero, "por 9 es" ,numero*9)
print( numero, "por 10 es" ,numero*10)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.#

numero1 = int(input("Ingrese un numero entero mayor que 0: "))
numero2 = int(input("Ingrese otro numero entero mayor que 0: "))

if numero1 > 0 and numero2 > 0:
    print(numero1, "+" ,numero2, "es" , (numero1+numero2 ))
    print(numero1, "-" ,numero2, "es" , (numero1 - numero2))
    print(numero1, "x" ,numero2, "es" , (numero1 * numero2))
    print(numero1, "/" ,numero2, "es" , (numero1 / numero2))
else: 
    print( numero1, "y/o" ,numero2, "no son numeros enteros mayores que 0")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.#

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))
imc = float(peso/(altura**2))

print("Su IMC es: " , imc)

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.#

celsius = float(input("Ingrese la temperatura en grados Celcius: "))
farenheit = float((celsius*9/5)+32)

print("El equivalente en grados Frenheit es: " , farenheit)

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.#

numero1 = int(input("Ingrese un primer numero: "))
numero2 = int(input("Ingrese un segundo numero: "))
numero3 = int(input("Ingrese un tercer numero: "))
promedio = float((numero1+numero2+numero3)/3)

print("El promedio entre los tres numeros es: " ,promedio)