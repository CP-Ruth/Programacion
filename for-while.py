#Ejercicios de la semana 4 29/08
#1
alph ="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#cantidad de letras en el abecedario 27
corr= int(input("Cantidad de lugares que se correrán las letras: "))
for j in range(0,5):
  print("Mensaje n°",j+1)
  mes = input("Ingrese su mensaje: ")
  mes_enc=""
  for i in range(0, len(mes)):
    if alph.find(mes[i].upper())<0:
      mes_enc += mes[i]
    else:
      let_corr= alph.find(mes[i].upper())+corr
      if let_corr<27:
        mes_enc += alph[let_corr]
      else:
        let_corr-= 27
        mes_enc += alph[let_corr]
  print(mes_enc)

#2
print("Ingrese números Enteros Positivos. Si quiere para ingrese 0.")
even_n=0
odd_n=0
stop=1
while stop!=0:
  num= input("Su número: ")
  if num=="0":
    stop=0
  else:
    poss=0
    neg=0
    for i in range(0,len(num)):
      num_n= int(num[i])
      if num_n>=0:
        if num_n%2==0:
          even_n+=1
          poss+=1
        else:
          odd_n+=1
          neg+=1
    print(f"Tiene {poss} dígitos pares y {neg} dígitos impares")
          
print(f"cantidad de numeros pares:{even_n}, cantidad de numeros impares: {odd_n}")
