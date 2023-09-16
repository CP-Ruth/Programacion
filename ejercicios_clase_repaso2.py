#Ejercicios de repaso 2
#1
"""sentences=input("ingresa una frase o palabra:\n")
if( len(sentences)==4):
    sentences+="!"
else:
    sentences+= "?"
print(sentences)"""

#2
print("Juguemos al ahorcado. Elige una palabra de la siguiente lista:")
names=["nazareno", "rodrigo", "thomas", "paula","uriel", "pablo"]
number=int(input("Elige un numero entre el 1 y el 6 : "))
select_name=names[number-1]
fount_name=""
print("Tu palabra tiene", len(select_name),"letras")
for i in range(len(select_name)):
    fount_name+="_"
while(number<7):
    
    letter=input("Ingresa una letra: ").lower()
    
    if(select_name.index(letter)>0):
        print(f"La letra {letter} está en la palabra")
        
        for i in range(len(select_name)):
            if(select_name[i]==letter):
                fount_name[i]= letter
print(fount_name)