print("Mi Programa para el Parcial")
name = input("Ingresa tu nombre: \n")

#menú de opciones
print("------------------------------------------------------\nMenú de juegos. \n (1) Juego de números \n (2) Juego de palabras")
option= input(f"{name}: Ingresa el número del juego que quieres jugar: ")
while (option!="1" and option!="2"):
    option= input("Ingresa el número del juego que quieres jugar: ")

#juego opcion (1)
if(option=="1"):
    print("------------------------------------------------------\nIngresa la cantidad de enteros que quieras. Para parar ingresa 0 (cero)\nLa consola te mostrará el mayor numero par que has ingresado y  promedio de los números impares.")
    #Validacion de un número entero
    number_op1=1
    #Comienzo de calculos del juego
    even_number=0  #Para encontrar al número más grande.
    odd_number=0  #Sumatoria de impares.
    numbers_odd=0  #Cantidad de impares
    while(number_op1!=0):
        while True:
            try:
                number_op1= int(input("Ingresa un número entero: "))  
                break
            except ValueError:
                print("El número ingresado no es un número entero válido. Inténtalo de nuevo.")

        if (number_op1%2==0):
            if(number_op1>even_number):
                even_number=number_op1
        else:
            numbers_odd+=1
            odd_number+=number_op1

    print(f"El número PAR más grande es: {even_number}\nEl promedio de los números impares es: {odd_number/numbers_odd}")
else:
    print("------------------------------------------------------\nFrases y vocales.\nIngresa una frase y te diré la cantidad que hay de cada vocal.")
    phrase=input(f"{name}: Ingresa una frase: ").lower()
    vowel_a=0
    vowel_e=0
    vowel_i=0
    vowel_o=0
    vowel_u=0

    for i in range(len(phrase)):
        if(phrase[i]=="a"):
            vowel_a+=1
        elif(phrase[i]=="e"):
            vowel_e+=1
        elif(phrase[i]=="i"):
            vowel_i+=1
        elif(phrase[i]=="o"):
            vowel_o+=1
        elif(phrase[i]=="u"):
            vowel_u+=1
    print(f"La cantidad por cada vocal es: \nA: {vowel_a}\nE: {vowel_e}\nI: {vowel_i}\nO: {vowel_o}\nI: {vowel_i}\nO: {vowel_o}\nU: {vowel_u}")

ask=input("si yano quiere volver a jugar ingrese 0 ")





