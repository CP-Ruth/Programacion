#Ejercicio 1
name= input("Ingrese un nombre y se repitira 10 veces: ").capitalize()
for i in range(0,10):
  print(name)

#Ejercicio 2
age= int(input("Ingresa tu edad: "))
for i in range(age):
  print(i+1)

#Ejercicio 3
num= int(input("Ingresa un número entero positivo: "))
if num>0:
  for i in range(num+1):
    if i%2!= 0:
      print(i)
else:
  print("No ingreso un entero positivo.") 

#Ejercicio 4
num= int(input("Ingresa un número entero positivo: "))
count=""
for i in range(0,num+1):
  count+= str(num)+", "
  num-=1
print(count)

#Ejercicio 5




#Ejercicio 6
num= int(input("Ingresa un numero : "))
triang=""
for i in range(num):
  triang+="*"
  print(triang)

#Ejercicio 7
print("Ingresa un nuúero y te mostraré su tabla del 1 al 10: ")
num= int(input())
for i in range(10):
  print(f"{num}X{i+1}={num*(i+1)}")

#Ejercicio 8
print("Ingrese un número entero: ")
num= int(input())
for i in range(1,num+1,2):
  ser=""
  for j in range(i,0,-2):
    ser+= str(j)+" "
  print(ser)
  
#Ejercicio 9
print("Introduce la contraseña")
password= input()
while password!="strong":
  print("Introduzca la contraseña correcta:")
  password= input()
print("Contraseña correcta!")

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