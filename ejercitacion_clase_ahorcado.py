#Ahorcado
import random

def randomword(list):  #función que me da una palabra aleatoria
    return random.choice(list)

def space(palabra):  #función me va a decolver solo la cantidad de espacios con guiones
    space=""
    while (len(space)<len(palabra)):
        space+="_"
    return space

def strarrays(string):   #pasa un string a array
    array=[]
    i=0
    while (len(array)<len(string)):
        array.append(string[i])
        i+=1
    return array

def arraystring(array):  #pasa un array a string
    string=""
    i=0
    while (len(string)<len(array)):
        string+=array[i]
        i+=1
    return string


def letterinstring(abc, string):
    if abc in string:
        return True
    else:
        return False
    

def ahorcadogame(list,error):
    word_select = randomword(list)  #palabra random
    print(f"Su palabra tiene {len(word_select)} letras: \n{space(word_select)}") #va a mostrar los guiones bajos de la palabra
    arrayguess = strarrays(space(word_select)) #Va a transformar el string de los guines bajos en un array de guiones bajos
        
    while 0<error:
        letter = ""
        print(f"Tiene {error} intentos.")
        #El ingreso de una letra y valida que solo sea UNA LETRA
        while True:  
            if(letter.isdigit()):
                letter = input("Ingrese una LETRA: ").upper()
            elif(len(letter) != 1):
                letter = input("Ingrese UNA letra: ").upper()
            else:
                break
        
        #Comprobar que la letra este en la palabra. Si está agregarla a Arrayspace, si no descontar
        if letterinstring(letter, word_select):
            for i in range(len(word_select)):
                if(word_select[i] == letter):
                    arrayguess[i] = letter  

            stringguess= arraystring(arrayguess)
            print(stringguess)
        else:
            print("Teng! Letra incorrecta")
            error-=1 

words=["THOMAS", "NAZARENO", "PABLO","RODRIGO","URIEL","PAULA","LUCIANO","NICOLAS","RUTH","ELIZABETH"] #Lista con palabras para el juego
num_error=int(input("Ingresa la cantidad de errores que admites: "))

ahorcadogame(words,num_error)



