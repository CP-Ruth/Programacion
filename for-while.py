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