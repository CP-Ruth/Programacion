def ciclingdni(num_dni):
    if(len(str(num_dni))==8 or len(str(num_dni))==7):
        return True
    else:
        return False
    
def dni_valid():
    while True:
        try:
            dni = (int(input("Ingrese el DNI del pasajero: ")))
            if(ciclingdni(dni)):
                break
            else:
                print("El DNI tiene que tener entre 7 u 8 digitos.")
        except ValueError:
            print("El valor ingresado no es numerico")
            continue
    return dni

def add_pasajero():
    passenger_name = (input("Ingrese nombre  y apellido del pasajero del pasajero: ").title())
    passenger_dni = dni_valid()
    passenger_ciudad=(input("Ingrese el la ciudad de destino: ").title())
    passenger= (passenger_name,passenger_dni,passenger_ciudad)
    return passenger

def add_city():
    city_name = input("Ingrese el nombre de la ciudad: ").title()
    country_name = input("Ingrese el nombre del país: ").title()
    city_country = (city_name, country_name) 
    return city_country

#ejercicio 2
def customer():
    tupla=(input("Ingrese Nombre y apellido del cliente: "),input("Día del mes: "), input("Monto: "), input("Domicilio: "))
    return tupla

