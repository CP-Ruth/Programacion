from tp5_funciones import*

#Ejercicio 1

"""while True:
    try:
        dni=int(input("Ingresa tu DNI: "))
        break
    except ValueError:
        print("El valor ingresado no es numerico")
        continue
print(ciclingdni(dni))"""

#Ejercicio 2

"""words = input("Ingrese un String: ")
longstring(lastword(words))
"""
#ejercicio3
"""print("Puede ingresar más de un nombre y al final el apellido. Si tuviera más de un apellido, ingrese uno.")
fullname = input("Ingresa tu nombre completo: ").title()
while True:
    while True:
        try:
            dni=int(input("Ingresa tu DNI: "))
            break
        except ValueError:
            print("El valor ingresado no es numerico")
            continue
    if(ciclingdni(dni)):
        break
    else:
        print("Este número no tiene 7 u 8 digitos")

print(f"Nombre: {fullname} \nDNI:{dni} \nID: {identificador(fullname,dni)}")
"""
#Ejercicio 4

"""number1 = int(input("Ingresa un número: "))
number2 = int(input("Ingresa otro número: "))
multiplo(number1,number2)
multiplo(number2,number1)"""

#Ejercicio 5

"""days=int(input("Cantidad de días a introducir:\n"))
for i in range(days):
    print(f"Día: {i+1}")
    tempmax=int(input("Ingresa la temperatura máxima: "))
    tempmin=int(input("Ingresa la temperatura mínima: "))
    print(f"La temperatura media del dia es de {medium(tempmax,tempmin)}°C")
"""
#Ejercicio 6

"""words = input("Ingresa un texto:\n")
print(spacebetween(words))"""

#Ejercicio 7

"""a=[]
#¿Debería crear una función para validar los valores numéricos?
while True:
    try:
        quantity = int(input("¿Cuántos numeros quieres ingresar?\n"))
        break
    except ValueError:
        print("El valor ingresado no es numérico")
        continue
for i in range(quantity):
    while True:
        try:
            number = int(input(f"{i+1}: "))
            break
        except ValueError:
            print("El valor ingresado no es numérico")
            continue
    a.append(number)

max_min_num(a)"""

#Ejercicio 8

"""radius=int(input("Ingresa el valor de la circunferencia: "))
perim_area(radius)"""

#Ejercicio 9

"""time=0
while True:
    user_name = input("Ingresa tu usuario: ")
    user_password = input("Ingresa tu contraseña: ")
    if (login(user_name,user_password)):
        print(f"Ingreso exitoso!\nNúmero de intentos: {time}")
        break
    else:
        print("Usuario o contraseña incorrecta.\nVuelva a intentarlo.")
        time+=1
    if(time==3):
        print(f"Número de intentos: {time}\nAcceso denegado.")"""

#Ejercicio 10
#Haria una lista de diccionarios. Lo recorreria por elementos para calcular por separado el descuento de cada proucto e iría haciendo la sumatoria en un total.

"""product={
    'producto': 'Yerba',
    'precio' : 1500,
    'cantidad' : 2
}
print(discount(product,10)) #imprime el precio del producto con su descuento y 
"""
#Ejercicio 11

"""names=['lucas','juan','santiago','roberto','nahuel']

print(order_lists(array_number,names))"""
#Ejercicio 12
"""sentence = input("Ingresa una frase: \n")
print(string_dictionary(sentence))
"""
#Ejercicio 13
#Escribir una función que calcule el módulo de un vector.
"""vector = (5,6)
print(module_vector(vector))
"""
#Ejercicio 14

"""number_prim = int(input("Ingrese un número: "))
print(prime_number(number_prim))
"""
#Ejercicio 15




#Ejercicio 16

number = input("Ingrese un numero entrero de varias cifras: ")
digit = input("Ingrese el valor de UN dígito: ")

print(exist(number, digit))

#Ejercicio 17

