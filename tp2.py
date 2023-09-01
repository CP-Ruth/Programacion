#Ejercicio 1
anios= int(input("¿Cuántos años tiene su computadora? "))
if anios <= 2:
  print("El computador es nuevo.")
else:
  print("El computador es viejo.")

#Ejercicio 2
anios= int(input("¿Cuántos años tiene su computadora? "))
if anios <= 2 and anios>=0 :
  print("El computador es nuevo.")
elif anios>2:
  print("El computador es viejo.")
else:
  print("Error, no puede escribir un numero negativo.")

#Ejercicio 3
nom1=input("Ingrese el nombre. ").upper()
nom2=input("Ingrese otro nombre. ").upper()
if nom1[0]==nom2[0]:
  print("Coincidencia")
else:
  print("No hay coincidencia")

#Ejercicio 4
print("Hora de votar. Las opciones son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.")
voto = input("su voto: ").upper()
if voto== "A":
  print("Usted ha votado por el partido Rojo")
elif voto=="B":
  print("Usted ha votado por el partido Verde")
elif voto=="C":
  print("Usted ha votado por el partido Azul")
else:
  print("Opción errónea.")

#Ejercicio 5
letra= input("Ingrese una letra :").upper()
if len(letra)== 1:
  if letra== "A" or letra== "E"  or letra== "I" or letra== "O" or letra== "U":
    print("Es una vocal.")
  else:
    print("Es consonante.")
else:
  print("Debe ingresar solo UNA letra.")

#Ejercicio 6
año = int(input('Ingresar año:'))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
  print('Año bisiesto.')
else:
  print('Año no bisiesto.')

#Ejercicio 7
print("Ingresar tres números")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
print("El número mas grande es")
max = a
if b> max:
  max = b
if c>max:
 max=c
print(max)

#Ejercicio 8
user= input("Ingrese su usuario: ")
password= input("Ingrese contraseña: ")
if user=="Gwenevere" and password=="excalibur":
  print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
  print("Acceso denegado")

#Ejercicio 9
alph ="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#print(alph.index("M")) posicion de M=[12] y N=[13]
name = input("Ingrese su nombre: ").upper()
sex = input("Ingrese su sexo M/H: ").upper()
if (sex=="M" and alph.index(name[0])<12) or (sex=="H"  and alph.index(name[0])>13) :
  print("Pertenece al grupo A")
else:
  print("Pertenece al grupo B")

#Ejercicio 10
age= int(input("Ingrese su edad: "))
if age<4:
  print("Puede entrar gratis.")
elif age>=4 and age<18:
  print("Debe pagar $500")
else:
  print("Debe pagar $1000")

#Ejercicio 11
pizza= input("¿Pizza vegetariana? (S/N) ").upper()
if pizza=="S":
  ing= input("¿Pimiento o tofu? ").lower()
  print("Pizza Vegetariana. Ingredientes: Mozzarella, tomate y ",ing)
else:
  ing= input("¿Peperoni, Jamón o Salmón? ").lower()
  print("Pizza Normal. Ingredientes: Mozzarella, tomate y ",ing)

#Ejercicio 12
year= int(input("Año actual: "))
year_d= int(input("Año a comparar: "))
if year>=year_d:
  print(f"Han pasado:{year-year_d} años")
else:
  print(f"Faltan: {year_d-year} años")

#Ejercicio 13
a=int(input("num1= "))
b=int(input("num2= "))
if a>=b:
  if a%b==0:
    print(a," es múltiplo de ", b)
  else:
    print(a," no es múltiplo de ", b)
else:
  if b%a==0:
    print(b," es múltiplo de ", a)
  else:
    print(b," no es múltiplo de ", a)

#Ejercicio 14
print("Ingresar los coeficientes de una ecuacion de primer grado ax + b = 0")
a=int(input("a="))
b=input("b=")

if a==0 and b!=0:
  print("No hay solución")
elif a!=0 and b== "-x":
  print("infinitas soluciones")
elif a!=0 :
  b=int(b)
  x=-b/a
  print("la solución es x= ", x)

#Ejercicio 15


#Ejercicio 16
#Ejercicio 17
#Ejercicio 18
#Ejercicio 19