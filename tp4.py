#Ejercicio 1
x = 0
while x <= 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print('The value ' + str(x) + ' of x was skipped')
        pass
    else:
        print('The value of the loop is: '+ str(x))
    if x == 15:
        print('The execution of the loop was broken when x was ' + str(x))
        break

#Ejercicio 1
sentence= input("Escribe una oración: ").upper()
while sentence:
  if sentence[-1]==" ":
    break
  sentence+=". "+ input("Escribe una oración: ").upper()
print(sentence)
 
#Ejercicio 2
balance = 0
logbook = "\n"
entry = "."
while entry != "":
    print("\n")
    entry = input("¿Qué operación desea realizar? \n Deposito(D) --- Retiro(R), e ingrese el monto.\n Para finalizar ingrese un espacio vacío: ")
    if entry != "":
        operation = entry[0]
        entry = entry.split()
        del entry[0]
        sum = int(entry[0])
        operation = operation.upper()
    if operation == "D":
        deposit = sum
        logbook = logbook + f"D {deposit} \n"
        balance = balance + deposit
    elif operation == "R":
        whitdrew = sum
        if balance - whitdrew < 0:
            print("Saldo insuficiente \n")
        else:
            logbook = logbook + f"R {whitdrew} \n"
            balance = balance - whitdrew
    else:
        print("Operación ingresada inválida \n")


print(f"Bitácora: \n {logbook}")


print(f"Saldo final: {balance}")

#Ejercicio 3
numbers=[]
escape=1
number_prime=0
while escape==1:
    num=int(input('Ingresar numero:'))
    if num>=1:
        numbers.append(num)
        divisor=0
        for n in range(1,num+1):
            if num%n==0:
                divisor+=1
        if divisor==2:
            number_prime+=1
    elif num==0:
        break
    else:
        print('Ingresar numeros positivos')
   
print(f'Numero ingresados:{numbers}')
print(f'Numeros primos:{number_prime}')

#Ejercicio 4
year1 = int(input("Ingrese el primer año: "))
year2 = int(input("Ingrese el segundo año: "))
year_list = []
year_mult = []


for i in range(year1, year2 + 1):
    if (i % 4 == 0) and i % 100 != 0 or i % 400 == 0:
        year_list.append(i)
    elif i % 10 == 0:
        year_mult.append(i)

print(f"Los años bisiestos entre los ingresados son: {year_list} ")
if (len(year_mult) != 0):
    print("Los años múltiplos de 10 son: ", year_mult)

#Ejercicio 5
for i in range(1,21):
    if i % 2 != 0:
        continue
    else:
        print(i)

#Ejercicio 6
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
search= int(input("Ingrese el numero que desea buscar:"))
for i in list:
    if search in list:
        print("Lo encontre!")
        break
    else:
        print("El numero no esta en la lista ")

#Ejercicio 7
print("Bienvenido al sistemas de menú interactivo")
option = 5
print("menú 1: Atencion ")
print("menú 2: Trámites ")
print("menú 3: Consultas ")
while option != 0:
    option_1 =int(input("Por favor ingrese 1(uno), para el menú 1. Ingrese 2(dos), para el menú 2. Ingrese 3(tres) para el menú 3 o ingrese 0(cero) para salir: "))
    if option_1 == 0:
        print("Usted ha ingresado 0 para salir del programa. Hasta pronto. ")
        break
    elif option_1 == 1:
        print("Usted ha ingresado 1.  Atención: ...")
    elif option_1 == 2:
        print("Usted ha ingresado 2. Trámites: ... ")
    elif option_1 == 3:
        print("Usted ha ingresado 3. Consultas: ...")
    else:
        print("La opción ingresada no corresponde, inténtelo nuevamente. ")
