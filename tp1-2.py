#Ejercicio 1
a=15
b=10
perim= 2*a+2*b
area=a*b

#Ejercicio 2
cat1=4
cat2=3
hip=(cat1**2 +cat2**2)**(1/2)

#Ejercicio 3
num1=6
num2=3
suma = num1+num2
resta = num1-num2
multp = num1*num2
div = num1/num2
print(f"numero A= {num1}, numero B= {num2}")
print(f"Suma= {suma}, resta= {resta}, multiplicacion={multp}, division={div}")

#Ejercicio 4
grados_f=int(input("Ingrese los grados Fahrenheit"))
grados_c= (grados_f*-32)*5/9
print(f"Es igual a {grados_c} Celsius.")

#Ejercicio 5
# a)Las comillas en Python son rectas y no curvadas como las que están escritas. Además nombre no es una variable, en este caso seria A donde se van a guardar los datos.
#Forma correcta:
A = input("¿Cuál es tu canción favorita?")
# b)El dato de precio no está tomado como dato numérico, solo como cadena. Hay que transformar ese input en un valor numérico, y en este caso seria un float. Forma correcta: 
precio = float(input("Precio: "))
# c)Para poner un mensaje junto con el valor de una variable hay que usar comillas. Forma correcta:  
edad = int(input("Edad: "))
print("Tu edad es: ",edad)
# d) #El operador de comparación es “==”. Forma correcta: 
print("Veamos si tu edad es 18…", edad == 18)

#Ejercicio 6
a = float(input("ingrese un valor A= "))
b = float(input("ingrese un valor B= "))
c = float(input("ingrese un valor C= "))
prom= (a+b+c)/3
print("La media de los 3 numeros es ", prom)
#Ejercicio 7
min = int(input("Ingrese los minutos: "))
horas = int(min/60)
min_rest = min- horas*60
print(f"{min} min son {horas} horas y {min_rest} min")

#Ejercicio 8
sueldo= float(input("Sueldo base es de : $"))
ventas1 = float(input("Monto de la primera venta: $"))
ventas2 = float(input("Monto de la segunda venta: $"))
ventas3 = float(input("Monto de la tercera venta: $"))
comision= (ventas1+ventas2+ventas3)*0.1
print("Obtendras por conceptos de comisiones: $", comision," En total a recibir: ", sueldo + comision)

#Ejercicio 9
recio=float(input("Ingrese el precio de lo que va a comprar: $"))
descuento= precio- precio*0.1
print("El precio de la compra con el 10% de descuento es de: $", descuento)

#Ejercicio 10
parciales = float(input("Ingrese el promedio de sus parciales: "))
final = float(input("Ingrese nota del examen final: "))
trabajo = float(input("Ingrese nota del trabajo final: "))
nota_final = parciales*0.55 + final*0.3 + trabajo*0.15
print("tu nota final es ",nota_final)

#Ejercicio 11
x1= float(input("Ingrese posicion a= "))
x2= float(input("Ingrese posicion b= "))
distancia= abs(x1-x2)
print("La distancia de la posicion a hasta b es: ",distancia)

#Ejercicio 12
num= int(input("Ingrese un numero :"))
raiz2 = num**(1/2)
raiz3 = num**(1/3)
print(f"La raiz cuadrada es {raiz2}, la raiz cúbica es {raiz3}")

#Ejercicio 13
numero = input("Ingresa un número: ")
numero_invertido = (numero)[::-1]
print("El número invertido es:", numero_invertido)

#Ejercicio 14
a= input("Ingrese el valor de A: ")
b= input("Ingrese el valor de B: ")
c=b
b=a
a=c
print(f"Ahora el valor de A es {a} y el de B es {b}")

#Ejercicio 15
print("ingrese la hora, minutos y segundos de salida")
hora_salida= int(input(print("ingrese la hora")))
min_salida= int(input(print("ingrese los minutos")))
seg_salida= int(input(print("ingrese los segundos")))
seg_del_viaje= 5415
print("La hora de llegada va a ser:")
seg_horas= hora_salida*3600
seg_min= min_salida*60
seg_total= seg_salida+seg_horas+seg_min+seg_del_viaje

hora_tot= int(seg_total/3600)
seg_total-=(hora_tot*3600)

min_tot= int(seg_total/60)
seg_total-= (min_tot*60)
print(f"{hora_tot}:{min_tot}:{seg_total}")

#Ejercicio 16
nombre= input("Escriba su nombre ")
apellido1=  input("Escriba su primer apellido ")
apellido2=  input("Escriba su segundo apellido ")
print("Las iniciales son: ", nombre[0],apellido1[0], apellido2[0])

#Ejercicio 17
usuario= input("Escriba su nombre ")
print(f"Ahora estás en la matrix, {usuario}")

#Ejercicio 18
cena = int(input("¿Cuánto consto la cena? $"))
cena += cena*0.162
print("Monto a pagar $", cena)

#Ejercicio 19
dd = input("Dia que nació: ")
mm = input("Mes que nació: ")
aa = input("Año que nació: ")
print(f"{dd}/{mm}/{aa}")

#Ejercicio 20
fecha =input("Ingrese fecha de nacimiento en formato DDMMAAAA: ")
print(f"{fecha[0:2]}/{fecha[2:4]}/{fecha[4:]}")

#Ejercicio 21
km = int(input("¿Cuántos kilómetros puede recorrer su moto con 1 litro de combustible? "))
cap =int(input("¿Qué capacidad tiene el tanque? (en litros) "))
dist = int(input("¿Cuántos km recorrerás? "))
viaje= km*cap
tanque_nec = dist/viaje
print("La cantidad de tanques de combustible necesarios: ", tanque_nec)