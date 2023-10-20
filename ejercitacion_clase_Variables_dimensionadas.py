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

"""#lista con datos e las compras
#[(cliente, día del mes, monto, domicilio del cliente)]
list_purchase=[("Nuria Costa", 5, 1234.5,"Calle 1 – 456"), ("Jorge Russo", 7, 3999, "Calle 2 – 741"), ("Carina solas", 5, 5000, "Calle 5 -159"), ("Jorge Russo", 7, 3999, "Calle 2 – 741")]

answer=input("¿Queres agregar una compra a tu lista? S/N \n").upper()
if answer== "S":
    list_purchase.append(customer())
else:
    # La pocision de cada nombre y direccion corresponde a la misma tupla
    name= inf_customer(list_purchase, 0)  #Lista con los nombre de los clientes 
    addrees= inf_customer(list_purchase, 3)  #lista con las direcciones
    print("Tus clientes y direcciones son:")
    for i in range(len(name)):
        print(f"{name[i]}: {addrees[i]}")"""

# Ejercicio 3
#socio={'numero': '' ,'nombre': '' , 'apellido' : '', 'fecha de ingreso' :  (ddmmaaaa), 'cuota al día' : }
keys=('número', 'nombre y apellido', 'fecha de ingreso', 'cuota')
members_list=[{'número': '1', 'nombre y apellido': 'Amanda Nuñes', 'fecha de ingreso': '17/03/2009', 'cuota': 'cuota al dia'}, {'número': '2', 'nombre y apellido': 'Barbara Molina', 'fecha de ingreso': '17/03/2009', 'cuota': 'cuota al dia'}, {'número': '3', 'nombre y apellido': 'Lautaro Campos', 'fecha de ingreso': '17/03/2009', 'cuota': 'cuota al dia'}]
dictionary_member={}
while True:
    option= int(input("(1)Agregar Socios.\n(2)Mostrar cantidad de socios.\n(3)Añadir registo de cancelación de una cuota.\n(4)Modificacion de fecha de ingreso.\n(5)Dar de baja a un socio.\n(6)Listado de socios.\nOpción: "))
    if(option== 1):
        #Cargar información de los socios en un diccionario para acceder por número de socio.
        for i in range(len(keys)):
            values = input(f"Ingresa {keys[i]}: ")
            dictionary_member[keys[i]]= values
        members_list.append(dictionary_member)
    elif(option==2):
        #Informar cantidad de socios del club
        print("Cantidad de socios activos: ", len(members_list))
    elif(option==3):
        #Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
        """while True:
            try:
                number_member= int(input("Ingresa el número del socio: "))
                break
            except ValueError:
                print("El valor ingresado no es numerico")
                continue"""
        number_member= input("Ingresa el número del socio: ")
        for dictionary in members_list:
            for valor in dictionary.values():
                if(valor == number_member):
                    dictionary['cuota']= input("Cuota al día/Cuota atrasada: ").title()
    elif(option==4):
        #Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018
        date=input("Ingrese una fecha:")
        for dictionary in members_list:
            for valor in dictionary.values():
                if(valor==date):
                    print(f"El socio n° {dictionary['número']} con fecha {date}")
                    dictionary['fecha de ingreso']= input("Nueva fecha de ingreso(dd/mm/aaaa): ")
    elif(option==5):
        #Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
        name_lastname= input("ingrese el nombre y apellido del socio: ")
        index_delete=0

        for index, dictionary in enumerate(members_list):
            if dictionary.get('nombre y apellido') == name_lastname:
                index_delete=index
        #tuve problema porque intente borrar un diccionario min¿entras lo recorria
        members_list.pop(index_delete)

    elif(option==6):
        print(members_list)