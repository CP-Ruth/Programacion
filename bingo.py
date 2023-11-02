from bingo_funciones import*
import random

option ="si"
while (option != "no"):
    # CARTON DEL JUEGO----------------------------------------------------------------------------------------------------------------------
    cardboard_array=[] 
    print("Vamos a armar tu carton para jugar al bingo.\nVas a ingresar 25 números entre 1 y 75.\nNo se pueden repetir numeros en tu cartón. ") #Explicación de cómo llenar el cartón.
    
    #Solicita al usuario que ingrese 25 números únicos, uno a la vez, para completar su cartón de bingo. Los números deben estar en el rango de 1 a 75.
    for i in range(25):
        while True:
            #Validación, tienen que ser números enteros.
            while True:
                try:
                    cardboard_num=int(input(f"Ingresa un numero al cartón {i+1}: "))
                    break
                except ValueError:
                    print("El valor ingresado no es numérico")
                continue

            #Validación, números únicos y que esten dentro del rango 1-75.
            stop = valid_number_in_array(cardboard_num, cardboard_array,"Cartón")
            #Si ya se lleno el array, es decir si ya estan los 25 números
            if(stop):
                break
    
    print("\n\n¡Muy bien ya tenemos tu carton!")
    moment=input("¿Estás listo para jugar? Presiona enter. ")
    print("\n¡Comencemos con el BINGO!\n\n")

    #cardboard_array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    #Paso el Array con los números del cartón a una matriz ordenada y la muestro.
    cardboard_matrix = array_to_matrix(cardboard_array)
    matrix_color = array_to_matrix(cardboard_array)
    
    
    # COMIENZA EL BINGOO--------------------------------------------------------------------------------------------------------------------
    bingo_array= []
    coordinates=[]
    ready=True
    while ready:
        
        while True:
            num_random=  random.randint(1, 75)
            stop = valid_number_in_array(num_random, bingo_array, "Bingo")
            
            if(stop):
                print("Los números que salieron:\n",bingo_array)
                # Si el número random está en el array de los numeros de nuestro carton entonces:
                if(num_random in cardboard_array):
                    print(Fore.CYAN + f"\n¡El número {num_random} está en tu cartón!")
                    coordinates.append(position(num_random,cardboard_matrix))
                    paint_numbers(matrix_color, coordinates)

                    ready = coordinates_bingo(coordinates, cardboard_matrix)

                    moment=input("Siguiente, preciona cualquier tecla: ")
                    
                break
        """if(ready):
            continue
        else:
            break"""






    #Final de la partida. Pregunta para continuar o dejar de jugar.
    while True:
        option= input("¿Quiere volver a jugar? (si/no)\n").lower()
        if(option == "si" or option =="no"):
            break
        else:
            continue

print("¡Gracias por jugar con nosotros!   :) ")

