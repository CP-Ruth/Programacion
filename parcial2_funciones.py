from colorama import init, Fore #importacion para usar colores :D 
init(autoreset=True)  # Inicializa colorama

# Validar que las letra ingresada sea A,T,C,G
def it_on(letra):
    letter = ["A","T","C","G"]  # Lista de String con las letras permitidas
    
    # Si la letra ingresada está en la lista de Strings retorna true, si no devuelve el mensaje de que el valor no correspode y retorna false.
    if (letra in letter):  
        return True
    else:
        print("El valor ingresado es incorrecto.")
        return False

# Imprimir los string con espacio intermedio SOLO TOMA LA FILA - FILA
def space_betwen_string(element):
    new_string= ""

    # Recorremos el string, y por cada vuelta agregamos un espacio más la letra del string a un nuevo string que luego imprimiremos.
    for i in range(len(element)):
        new_string += " "+element[i]
    print(new_string)

# Imprime la matriz de stings con espacio intermedio entre las letras
def space_betwen_matrix(matrix):

    print("---------------------------------\n\nTu ADN matiz:")
    # Recorremos la matrix por cada elemento(en este caso cada string). Luego usamos la función "space_betwen_string" para imprimir cada fila de la matriz con espacio intermedio.
    for j in matrix: 
        space_betwen_string(j)
    print("---------------------------------")

init(autoreset=True)  # Inicializa colorama

# Pintar solo aquellos valores de la matriz que se especifican en las coordenadas ingresadas.

def paint_letter(matrix1, coordenadas):
    
    matrix = []  # Nueva lista(de listas) para especificar los elementos que vamos a pintar.
    
    for i in range(6):
        row_matrix = []  # Acá vamos a armar una lista de string por cada letra. 
        for j in range(6):
            row_matrix.append( matrix1[i][j]) # Acá añadimos por sepasado cada letra del string de la matriz "matrix1".
            
            # Acá corroboramos si el elemento que ingresamos, si posición es igual a alguna de las coordenadas ingresadas.
            # Coordenadas es una lista de tuplas.
            for row, column in coordenadas:

                # Si la posición que se recorre es igual a una de las coordenadas entonces se reemplza ese valor por el codigo para pintarlo más la letra que había.
                if (row == i and column == j):
                    row_matrix[j] = Fore.YELLOW + matrix1[i][j]
        
        matrix.append(row_matrix)  # Una vez que completamos la fila, la añadimos a la matriz que vamos a imprimir.
    
    print("---------------------------------\nTu adn es: ")
    
    # Para imprimir la matriz con colores tengo que especificar su posición/ imprimir elemento por elemento.
    for i in range(6):
        print(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],matrix[i][4],matrix[i][5])
    print("---------------------------------")

# Funcion para corroborar si es mutante
def is_mutant(matrix):

    # Primero recorre cada fila
    for j in range(6):
        for i in range(3):
            # Por cada fila recorro los primeros cuatro valores corroborando si esos 4 valores son iguales, si no es así se corre un lugar a la derecha corroborando esos 4 lugares. Dos veces se corre a la derecha. Luego de no encontrar coincidencias baja una fila y repite procedimiento.
            if (matrix[j][i]==matrix[j][i+1] ==matrix[j][i+2] ==matrix[j][i+3]):
                # En caso que esas 4 posiciones sean iguales en valor, se toman esas posiciones para guardarlas cada una en una tupla como coordenadas para luego pasarlas en "paint_letter" junto con la matriz "adn" para imprimir con color.
                coordinate=[(j,i),(j,i+1),(j,i+2),(j,i+3)]
                print(Fore.GREEN +" ¡¡¡¡M U T A N T E !!!! == ")
                paint_letter(matrix, coordinate)
                return True #

    # Segundo recorre cada columna
    for c in range(len(matrix)):
        for r in range(3):
            #Es un procedimiento parecido al enterios solo que ahora verificamos los valores de manera vertical o por columna. Por lo que ahora en vez de ir a la derecha, bajamos 2 lugares. 
            if(matrix[r][c] == matrix[r+1][c] == matrix[r+2][c] == matrix[r+3][c]):
                coordinate=[(r,c),(r+1,c),(r+2,c),(r+3,c)]
                print(Fore.GREEN +" ¡¡¡¡M U T A N T E !!!! || ")
                paint_letter(matrix,coordinate)
                return True

    # Tercero diagonales \\
    "matrix[i][j] == matrix[i+1][j+1]"
    for i in range(3):
        for j in range(3):
            # En el caso de las diagonales, la matriz se recorre de izquierda a derecha, de arriba a abajo. Se toman las primeras 4 filas y y se recorren las 3 primeras opciones de diagonales(de izquierda a derecha).
            # Si  no hay coincidencias bajamos una fila y tomamos el valor de las 4 filas siguiente empezando por esa nueva (cambio del valor de i por el for) y se repite procedimiento de las diagonales de izquierda a derecha.
            if(matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]):
                coordinate = [(i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3)]
                print(Fore.GREEN +" ¡¡¡¡M U T A N T E !!!! \\ ")
                paint_letter(matrix,coordinate)
                return True

    # Cuarto diagonales //
    for i in range(5,2,-1):
        for j in range(3):
            # Para estas diagonales tenemos el mismo procedimiento solo que esta vez empezamos desde abajo. Es decir iniciamos el For desde la posicion 5 más los 3 valores anteriores a partir de 5 (filas: 5,4,3,2). Seguimos corroborando coincidencias de sus valores de izquierca a derecha.
            if(matrix[i][j] == matrix[i-1][j+1] == matrix[i-2][j+2] == matrix[i-3][j+3]):
                coordinate = [(i,j),(i-1,j+1),(i-2,j+2),(i-3,j+3)]
                print(Fore.GREEN +" ¡¡¡¡M U T A N T E !!!! // ")
                paint_letter(matrix, coordinate)
                return True

    return False, print(Fore.RED + "No es mutante")


"""# Ejemplo
lolo =["ATAATC","AGGCCC","GTAATT","ATCATT","ACTGCC","ATTGGC"]  #No mutante
#lolo =["ATAATC","ATGCCC","GTAGTT","ATCGTT","ACTGGC","ATTGGC"]  #Mutante
#lolo =["ATAATC","AGGCCC","GTAGTT","ATCGTT","ACTGGC","ATTGGC"]  #Mutante
#lolo =["ATAATC","AGGCCC","GTCGTT","ATCCTT","ACTGCC","ATTGGC"]  #Mutante
#lolo =["ATAATC","AGGCCC","GTCCTT","ATCATT","ACTGCC","ATTGGC"]  #Mutante
space_betwen_matrix(lolo)
is_mutant(lolo)"""


