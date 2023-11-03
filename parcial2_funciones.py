from colorama import init, Fore
init(autoreset=True)  # Inicializa colorama

#Validar que las letra ingresada sea A,T,C,G
def it_on(letra):
    letter = ["A","T","C","G"]
    if (letra in letter):
        return True
    else:
        print("El valor ingresado es incorrecto.")
        return False
    
#Imprimir los string con espacio intermedio SOLO TOMA LA FILA - FILA
# option= fila entonces me imprime la fila cuando esta completa
# option= matriz entonces me imprime la matriz completa
def space_betwen_string(element):
    new_string= ""
    for i in range(len(element)):
        new_string += " "+element[i]
    print(new_string)

# Imprime la matriz de stings con espacio intermedio entre las letras
def space_betwen_matrix(matrix):

    print("---------------------------------\n\nTu ADN matiz:")
    for j in matrix:
        space_betwen_string(j)
    print("---------------------------------")

init(autoreset=True)  # Inicializa colorama

# Pintar 
def paint_letter(matrix1, coordenadas):
    
    matrix = []
    
    for i in range(6):
        row_matrix = []
        for j in range(6):
            row_matrix.append( matrix1[i][j])
            for row, column in coordenadas:
                if (row == i and column == j):
                    row_matrix[j] = Fore.YELLOW + matrix1[i][j]
        
        matrix.append(row_matrix)
    
    print("---------------------------------\nTu adn es: ")
    
    for i in range(6):
        print(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],matrix[i][4],matrix[i][5])
    print("---------------------------------")

#Funcion para corroborar si es mutante
def is_mutant(matrix):
    stop = False
    # Primero recorre cada fila
    for j in range(6):
        for i in range(3):
            if (matrix[j][i]==matrix[j][i+1] ==matrix[j][i+2] ==matrix[j][i+3]):
                coordinate=[(j,i),(j,i+1),(j,i+2),(j,i+3)]
                print(Fore.GREEN +" ¡¡¡¡M U T A N T E !!!! == ")
                paint_letter(matrix, coordinate)
                stop = True
                break
        if(stop):
            break
    # Segundo recorre cada columna
    for c in range(len(matrix)):
        for r in range(3):
            if(matrix[r][c] == matrix[r+1][c] == matrix[r+2][c] == matrix[r+3][c]):
                coordinate=[(r,c),(r+1,c),(r+2,c),(r+3,c)]
                print(Fore.GREEN +" ¡¡¡¡M U T A N T E !!!! || ")
                paint_letter(matrix,coordinate)
                stop =  True
                break
        if(stop):
            break
    # Tercero diagonales \\
    "matrix[i][j] == matrix[i+1][j+1]"
    for i in range(3):
        for j in range(3):
            if(matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]):
                coordinate = [(i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3)]
                print(Fore.GREEN +" ¡¡¡¡M U T A N T E !!!! \\ ")
                paint_letter(matrix,coordinate)
                stop =  True
                break
        if(stop):
            break
    # Cuarto diagonales //
    for i in range(5,2,-1):
        for j in range(3):
            if(matrix[i][j] == matrix[i-1][j+1] == matrix[i-2][j+2] == matrix[i-3][j+3]):
                coordinate = [(i,j),(i-1,j+1),(i-2,j+2),(i-3,j+3)]
                print(Fore.GREEN +" ¡¡¡¡M U T A N T E !!!! // ")
                paint_letter(matrix, coordinate)
                stop =  True
                break
        if(stop):
            break
    if(stop == False):
        print(Fore.RED + "No es mutante")


"""# Ejemplo
lolo =["AAAATC","ATGCCC","TTAGTT","ATCGTT","ACTGGC","ATTGGC"] #//
space_betwen_matrix(lolo)
is_mutant(lolo)
"""

