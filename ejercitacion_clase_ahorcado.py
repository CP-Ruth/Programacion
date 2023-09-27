#Ahorcado
import random

words=["THOMAS", "NAZARENO", "PABLO","RODRIGO","URIEL","PAULA","LUCIANO","NICOLAS","RUTH","ELIZABETH"] #Lista con palabras para el juego
word_select= random.choice(words)  #palabra random

#Me muestra los espacios de la palabra
space=""
while (len(space)<len(word_select)):
    space+="_"
print(f"Su palabra tiene {len(word_select)} letras: \n{space}")

print(word_select) #Me muestra la palabra.

#Valida que solo sea UNA LETRA
letter=""
while True:
    if(letter.isdigit()):
        letter=input("Ingrese una LETRA: ").upper()
    elif(len(letter)!=1):
        letter=input("Ingrese UNA letra: ").upper()
    else:
        break

#Trandormar el string de Space en array
arrayspace=[]
while (len(arrayspace)<len(word_select)):
    arrayspace.append("_")

#Comprobar que la letra este en la palabra. Si esta agregarla a Arrayspace
for i in range(len(word_select)):
    if(word_select[i]==letter):
        arrayspace[i]=letter    

#Pasar el arrayspace a string
space=""
i=0
while (len(space)<len(word_select)):
    space+=arrayspace[i]
    i+=1


print(space)



