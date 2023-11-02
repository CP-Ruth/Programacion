from ejercitacion_clase_ordenamientoyBusqueda import *
from colorama import init, Fore

#Pasa un array a Matriz ordenada 
def array_to_matrix(array):
    matrix=[]
    insertion_sort_ascen(array)
    for k in range(5):
        new_array = array[(k*5):(k*5+5)]
        matrix.append(new_array)
    return matrix

# Pintar los  números que salieron y están en el cartón que armamos
init(autoreset=True)  # Inicializa colorama
def paint_numbers(matrix1, coordenadas):
    matrix = matrix1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for row, column in coordenadas:
                if (i== row and j == column):
                    matrix[i][j] = Fore.BLUE + str(matrix[row][column])
                else:
                    matrix[i][j] = str(matrix[i][j])
    print("---------------------------------\nTu carton es: ")
    for i in range(5):
        if i == 0:
            print("",matrix[i][0],"",matrix[i][1],"",matrix[i][2],"",matrix[i][3],"",matrix[i][4],)
        elif i ==1:
            print("",matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],matrix[i][4],)
        else:
            print(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],matrix[i][4],)
    print("---------------------------------")
    return matrix1

# Buscar un número en una matriz, si está que devuelva sus coordenada
def position(number, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (number== matrix[i][j]):
                #print(f"El número: {number} está en tu cartón")
                return (i,j)

# Función para validar los números
#Si bien la función retorna un valor booleano también le agrega un valor al array si es true.
#tipo: carton/ 
def valid_number_in_array(number, array, type):
    if number in array:
        if type=="Cartón": 
            print("El numero ya esxiste.")
        return False
    elif(number>75 or number<=0):
        if type=="Cartón": 
            print("No está dentro del rango 1-75")
        return False
    else:
        array.append(number)
        return True

# Validar la existencia de las coordenadas que cumplen con el bingo

def coordinates_bingo(coordenadas, matrix):
    stop = True
    # Primero recorre cada fila
    for i in range(len(matrix)):
        sum=0
        for j in range(len(matrix[i])):
            for row, column in coordenadas:
                if (i== row and j == column):
                    sum += 1
        if(sum == 5):
            print(Fore.GREEN +" ¡¡¡¡B I N G O!!!! -- ")
            stop =  False
    # Primero recorre cada columna
    for c in range(len(matrix)):
        sum=0
        for r in range(len(matrix)):
            for row, column in coordenadas:
                if (r== row and c == column):
                    sum += 1
        if(sum == 5):
            print(Fore.GREEN +" ¡¡¡¡B I N G O!!!! | ")
            stop =  False
    for m in range(len(matrix)):
        sum=0
        for row, column in coordenadas:
            if (m == row and m ==column):
                sum += 1
        if(sum == 5):
            print(Fore.GREEN +" ¡¡¡¡B I N G O!!!! X")
            stop =  False
    return stop
