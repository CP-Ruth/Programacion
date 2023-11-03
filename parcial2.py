from parcial2_funciones import *



while True:
    # 1 Armamos la cadena de ADN 
    adn = []
    for i in range(6):
        adnrow=""
        while True:

            letter = input("Ingresa una letra de - A,T,C,G - : ").upper()
            #si retorna True:
            if(it_on(letter)):
                adnrow +=letter
            if(len(adnrow) == 6):
                adn.append(adnrow)
                space_betwen_string(adnrow) # Imprimomos la linea de 6 letras que ingresamos
                break    
    space_betwen_matrix(adn) # Imprimimos la matriz que se armó.
    is_mutant(adn)

    while True:
        moment = input("¿Deseas analizar otro ADN? (si/no)\n").upper()
        if(moment == "SI" or moment == "NO"):
            break
    if(moment == "NO"):
        break
print("Gracias por ayudar a Margento a buscar Mutantes. Adios.")

