"""def ciclingdni(num_dni):
    if(len(str(num_dni))==8 or len(str(num_dni))==7):
        return True
    else:
        return False
while True:
    try:
        dni=int(input("Ingresa tu DNI: "))
        break
    except ValueError:
        print("El valor ingresado no es numerico")
        continue
print(ciclingdni(dni))"""

def temperature(a,b):
    return(a+b)/2

days=int(input("Cantidad de días a introducir:\n"))
for i in range(days):
    tempmax=int(input("Ingresa la temperatura máxima: "))
    tempmin=int(input("Ingresa la temperatura mínima: "))
