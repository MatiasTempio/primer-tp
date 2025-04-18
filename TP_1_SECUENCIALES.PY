#                                                                    TRABAJO PRACTICO NUMERO 1 EN PROGRAMACION.
#ALUMNO: MATIAS DAMIAN TEMPIO DIAZ
#COMISION: 22




#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
saludo = "hola mundo"
print(saludo)


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla.

#nombre = input("dime tu nombre, por favor: ")
#print(f"hola {nombre}! mucho gusto.")


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.

#nombre = input("dime tu nombre, por favor: ")
#apellido = input(f"muy bien {nombre} ahora,te pido tu apellido: ")
#edad = input("genial!, cuantos años tenes?  ")
#residencia = input(f"el ultimo dato {nombre}, donde vivis? ")
#print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {residencia}")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro. 

#radio = float(input ("dame un valor para radio:")) 
#P = float(3.14)
#area = P * radio**2
#perimetro = 2 * P * radio
#print(f"el area segun el radio que diste es {area} y su respectivo perimetro es {perimetro}")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale. 

#segundos =float(input ("escribe los segundos que quieras y te dire su equivalente en horas: "))
#horas = round((segundos/3600), 2)
#print(f"tus {segundos} segundos equivalen a {horas} horas")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número.

#numero = int(input("escribe un numero, por favor: "))
#tabla = (numero*1, numero*2,numero*3 ,numero*4 ,numero*5 ,numero*6 ,numero*7 ,numero*8 ,numero*9,numero*10) 
#print (f"la tabla del numero {numero} es: {tabla}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

#num1 = int(input("escribe el primero numero Entero:"))
#num2 = int(input("ahora escribe el segundo: "))
#suma = num1 + num2
#resta = num1 - num2
#div = num1 / num2
#mult = num1 * num2

#print (f"suma:{num1}+{num2}={suma}    resta:{num1}-{num2}={resta}   div:{num1}/{num2}={div}   multiplicacion:{num1}*{num2}={mult}")


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo:  
#            I𝑀𝐶 =  𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#                   (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

#altura = float(input("Ingrese su altura en metros: "))
#peso = float(input("Ingrese su peso en kg: "))

#masaCORP= peso / (altura**2)

#print(f"Tu IMC O INDICE DE MASA CORPORAL ES: {masaCORP}")


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# 
#T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖t = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢s + 32

#celcius = float(input("escribe la temperatura en celcius: "))
#fahrenheit = ((9/5) * celcius) + 32
#print(f"el equivalente en fahrenheit es: {fahrenheit}")


#10) Crear un programa que pida al usuario  3 números e imprima por 
# pantalla el promedio de dichos números. 

#num1 = float(input("dame el primer numero: "))
#num2 = float(input("dame el segundo numero: "))
#num3 = float(input("dame el tercer numero: "))

#prom = (num1 + num2 + num3) / 3

#print(f"el promedio de tus numeros es: {prom}")




