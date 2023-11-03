from parcial2_funciones import *

#Mensaje de inicio
print("Saludos. \nBienvenido al testeo de ADN.\nVamos a hacer solo una pequeña prueba de tu ADN")
moment = input("¡No te preocupes, no te vamos pinchar, no es necesaria tu sangre! (aún)\nPara continuar presiona enter.")

while True:

    # 1 Armamos la cadena de ADN, es una lista de Strings.
    adn = []   

    # Armammos los strings y luego los incorporamos a la lista "adn"
    for i in range(6):
        adnrow=""     # String // fila de la matriz

        while True:
            letter = input("Ingresa una letra de - A,T,C,G - : ").upper()
            
            # La funcion "it_on" valida que el dato ingresado sea una de las letras "A,T,C,G "
            # Si es así entonces retorna true e ingresa a la condición.
            if(it_on(letter)):
                adnrow += letter  # Concatena la letra ingresada al String
            
            # Solo si el largo del String "adnrow" es igual a 6 ingresa a la condición, si no continua con el bucle para completar el string hasta que cumpla la condición. 
            if(len(adnrow) == 6):
                adn.append(adnrow)  # Añadimos el string a la lista.
                space_betwen_string(adnrow) # Imprimomos la linea de 6 letras que ingresamos con espacio entre las letras. Es solo un detalle visual.(No modifica al String "adnrow")
                break    
    
    # Una vez que se haya completado el bucle for, que quiere decir que se llenó la matriz 6x6. Imprimimos la matriz que completamos y hacemos que pase por la prueba.
    space_betwen_matrix(adn) # Imprimimos la matriz que se armó. (Nuevamente un detalle visual)

    #print(adn)  Corroborar que adn sigue siendo una lista de string con el formato:  [‘ATGCGA’,’CAGTGC’,’TTATGT’,’AGAAGG’,’CCCCTA’,’TCACTG’]

    is_mutant(adn) # Es la prueba para identificar si el adn ingresado es el de un mutante.

    # Cuando temrina la prueba tenemos la opción de hacer o iniciar una nueva prueba. Si no se requiere entonces solo indicamos que "no". 
    while True:
        moment = input("¿Deseas analizar otro ADN? (si/no)\n").upper()
        if(moment == "SI" or moment == "NO"):
            break
    if(moment == "NO"):
        break

# Mensaje saludo.
print("Gracias por ayudar a Margento a buscar Mutantes. Adios.")

