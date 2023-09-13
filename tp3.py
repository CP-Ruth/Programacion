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
num = int(input("Ingrese un número entero positivo: "))
cont= 0
if  num>1:
  for i in range(2, int(num/2)+1):
    #print(i)
    if num%i==0:
      cont+=1
if cont>=1 or num<=1:
  print("No es primpo")
else:
  print("Es primo")

#Ejercicio 11
word=input("Ingrese una palabra: ")
drow=""
for i in range(len(word)-1,-1,-1):
  drow+=word[i]
print(drow)

#Ejercicio 12
print("Escriba una frase:")
sent=input().lower()
print("Digame una letra y le diré cuantas veces aparece en la frase.")
lett=input("Letra: ").lower()
time=0
for i in range(len(sent)):
  if sent[i]==lett:
    time+=1
print(f"La letra {lett} aparece: {time}")
  
#Ejercicio 13
sent= input("Escribe lo que quieras: ")
array=[]
cont=0
while sent!="salir":
  array.append(sent)
  sent= input("Escribe lo que quieras: ")
  cont+=1
for i in range(cont):
 print(array[i])

#Ejercicio 14
a,b= int(input("Ingrese un numero: ")),int(input("Ingrese otro número : "))
even=[]
odd=[]
  #ran=range(b,a+1) if a>b else ran=range(a,b+1)
if a>b:
  ran=range(b,a+1)
else:
  ran=range(a,b+1)
for i in ran:
 # print(i)
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print(f"Los números pares son: {even}. Los números impares son: {odd}")

#Ejercicio 15
num= int(input("Ingrese un número mayor a cero y le doy sus divisores: "))
print("Sus divisores son:")
for i in range(1,num+1):
  if num%i==0:
    print(i)

#Ejercicio 16
amount=int(input("¿Cuantos números desea ingresar? "))
neg=0
for i in range(1,amount+1):
  num= int(input(f"Número{i}°: "))
  if num<0:
    neg+=1
print(f"Introdujiste {neg} números negativos")

#Ejercicio 17
phrase=input("Ingresa una frase: ").lower()
vowel="aeiou"
print("Las vocales que aparecen: ")
for j in range(0,len(vowel)):
    if phrase.find(vowel[j])>-1:
      print(vowel[j])  

#Ejercicio 18
fibonacci=[0,1]
for i in range(2,11):
  nuevo= fibonacci[i-2]+fibonacci[i-1]
  fibonacci.append(nuevo)
#fibonacci.append('...')
print(fibonacci)

#Ejercicio 19
amount= int(input("¿Cuánto quieres ahorrar? "))
piggy_bank=0
while amount>piggy_bank:
  num=int(input("$$ a guardar: $"))
  if num>0:
   piggy_bank+=num
  else:
    print("-.- No puede ser un número negativo.")
print("¡Llegaste al monto deseado!")

#Ejercicio 20
num=int(input("Ingresa un numero: "))
sum=0
while num!=0:
  sum+= num
  num=int(input("Ingresa un numero: "))
print(f"La sumatoria de todos los numeros distintos de cero ingresados: {sum}")

#Ejercicio 21
print("Ingresa números enteros positivos, cuando quieras para ingresa el cero: ")
num=int(input("n°: "))
max=0
while num>0:
  if num>max:
    max=num
  num=int(input("n°: "))
print("El número más grande es: ",max)

#Ejercicio 22
num=int(input("Ingrese un numero entero positivo: "))
even=0
while num>0:
  if num%2==0:
    even+=1
  sum=0
  for i in range(len(str(num))):
    sum+=int(str(num)[i])
  print("La suma de los dígitos es: ", sum)
  num=int(input("Ingrese un numero entero positivo: "))
print("En total ingresaste",even," números pares")

#Ejercicio 23
#Ejercicio 24
price=float(input("Precio del producto: $"))
total=0
while price!=0:
  if price>0:
    total+=price
    price=float(input("Precio del producto: $"))
  else:
    print("Los precios no pueden ser negativos.")
    price=float(input("Precio del producto: $"))
if total>=1000:
  discount = total - total*0.1
  print("Tiene descuento del 10%. Su total es $",discount)
else:
  print("Monto total $",total)
  
#Ejercicio 25