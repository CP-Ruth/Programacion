#Semana 3  Martes - 22/08/2023

print("Ingrese dia de la semana y Fecha.")
fecha = input("Formato: dia,dd/mm  ")
dia_semana = fecha.index(',')
dia = fecha[0:dia_semana]
dia= dia.lower()
#print(dia)
dd_fin= fecha.index('/')
dd= int(fecha[dia_semana+1:dd_fin])
#print(dd)
mm=int( fecha[dd_fin+1:])
#print(mm)

if (dia!="lunes" and dia!="martes" and dia!="miercoles" and dia!="jueves" and dia!="viernes"):
    print("Dia incorrecto, vuelva a ingresar la fecha")

if(dd>31):
  print("DD incorrecto, vuelva a ingresar la fecha")

elif(mm>12):
  print("MM incorrecto, vuelva a ingresar la fecha")
else:
  print("Fecha ingresada de forma correcta!")

if(dia=="lunes" or dia=="martes" or dia=="miercoles"):
  examen= input("¿Hubo examen? (si/no)   ")
  if(examen=="si"):
    alumn_aprob=int(input("Ingrese cantidad de alumnos aprobados: "))
    alumn_desap=int(input("Ingrese cantidad de alumnos desaprobados: "))
    alumn_total= alumn_aprob+alumn_desap
    aprobados= int(alumn_aprob*100/alumn_total)
    print(f"Porcentaje de aprob: {aprobados}%")
elif(dia=="jueves"):
  print("Los jueves hay practicas habladas")
  asistencia= int(input("Ingrese la cantidad de alumnos que asistieron: "))
  total_al=int(47)
  if(asistencia>(total_al/2)):
    print("Asistió la mayoría")
  else:
    print("No asistio la mayoría")
else:
  if(dd==1 and (mm==1 or mm==7)):
    print("Comienzo de nuevo ciclo")
    cant_a=int(input("Ingrese la cantidad de alumnos nuevos: "))
    arancel=int(input("ingrese el arancel: $"))
    ing_total= arancel*cant_a
    print("El ingreso total es $",ing_total)
  