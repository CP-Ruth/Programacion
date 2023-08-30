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


#Ejercicio 11


#Ejercicio 12


#Ejercicio 13


#Ejercicio 14
#Ejercicio 15
#Ejercicio 16

#Ejercicio 17

#Ejercicio 18
#Ejercicio 19
#Ejercicio 20
