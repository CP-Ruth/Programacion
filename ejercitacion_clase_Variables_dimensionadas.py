from ejercitacion_clase_Variables_dimensionadas_funciones import* 

# Ejercicio 1
"""#lista de viajeros:
    #[("nombre","DNI", "destino"), ()]
list_passenger=[]

#lista de ciudades y paises:
    #[("ciudad1","pais1"),("ciudad2","pais2"), ()]
list_cityandcountry=[("Paris","Francia"),("Anger", "Francia"),("Mendoza","Argentina"),("San Juan","Argentina")]
#funciones
    #agregar pasajeros

while True: 
    print("\n\nMENÚ:\n\n(1)Agregar pasajeros a la lista de viajeros.\n(2)Agregar ciudades a la lista de ciudades.\n(3)Ciudad de destino del pasajero.\n(4)Cantidad de pasajeros con destino a la ciudad:......\n(5)País de destino de un pasajero.\n(6)Cantidad de pasajeros con destino al país:.......\n(0)Salir del menú.\n-----------------------------------------------------------")
    while True:
        try:
            option=int(input("Ingresa n° de la opción que desea: "))
            break
        except ValueError:
            print("El valor ingresado no es numerico")
            continue
    #Agregar pasajeros a la lista de viajeros
    if(option==1):
        
        list_passenger.append(add_pasajero())
        print(list_passenger)
    #Agregar ciudades a la lista de ciudades   
    elif(option==2):
        
        list_cityandcountry.append(add_city())
        print(list_cityandcountry)
    #Ciudad de destino del pasajero
    elif(option==3):
        
        dni = dni_valid()
        if(len(list_passenger)==0):
            print("Aun no hay registro de pasajeros.")
        else:
            for tupla in list_passenger:
                if dni in tupla:
                    print(f"*El pasajero {tupla[0]} con DNI {tupla[1]} tiene destino a {tupla[2]}*")
                else:
                    print(f"No se encontro al pasajero con el dni: {dni}.\nRevisa los dígitos ingresados\n\n")
    elif(option==4):
        city= input("Ingrese el nombre de la ciudad:\n").title()
        passenger=0
        for tupla in list_passenger:
            if city in tupla:
                passenger+=1
        print(f"La cantidad de pasajeros con distino a {city} es {passenger}")
    elif(option==5):
        dni = dni_valid()
        if(len(list_passenger)==0):
            print("Aun no hay registro de pasajeros.")
        else:
            for tupla in list_passenger:
                if dni in tupla:
                    city= tupla[2]
                    country=""
                    for tupla_b in list_cityandcountry:
                        if city in tupla_b:
                            country=tupla_b[1]
                    print(f"*El pasajero {tupla[0]} con DNI {tupla[1]} tiene destino a {country}*")
                else:
                    print(f"No se encontro al pasajero con el dni: {dni}.\nRevisa los dígitos ingresados\n\n")
    elif(option==6):
        country= input("Ingrese el nombre del país:\n").title()
        passenger=0
        for tupla in list_cityandcountry:
            if country in tupla:
                city=tupla[0]
                for tupla_b in list_passenger:
                    if city in tupla_b:
                        passenger+=1
        print(f"La cantidad de pasajeros con distino a {country} es {passenger}")

    elif(option==0):
        print("Gracias por elegirnos")
        break
"""
# Ejercicio 2

#lista con datos e las compras
#[(cliente, día del mes, monto, domicilio del cliente)]
list_purchase=[("Nuria Costa", 5, 1234.5,"Calle 1 – 456"), ("Jorge Russo", 7, 3999, "Calle 2 – 741"), ("Carina solas", 5, 5000, "Calle 5 -159"), ("Jorge Russo", 7, 3999, "Calle 2 – 741")]

answer=input("¿Queres agregar una compra a tu lista? S/N \n").upper()
if answer== "S":
    list_purchase.append(customer())
else:
    name= inf_customer(list_purchase, 0)
    addrees= inf_customer(list_purchase, 3)
    print("Tus clientes y direcciones son:")
    for i in range(len(name)):
        print(f"{name[i]}: {addrees[i]}")
#me va a imprimir solo los 
