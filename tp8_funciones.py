#Ejercicio 1
def digit(n):
    
    if n>0:
        return 1+digit(n//10)
    else:
        return 0

#Ejercicio 2
#n es potencia    b es base
def potencia(n,b):
    if(n>b):
        return potencia(n/b,b)
    elif(n==b):
        return True
    else:
        return False

#Ejercicio 3

def rfind_in(frase, letra, index=0):
    
    results = []
    index = frase.find(letra, index)
    if index != -1:
        results.append(index)
        results += rfind_in(frase, letra, index + 1)
    return results

#Ejercicio 4

def par(n):
    if(n== 1):
        return False
    else:
        return impar(n-1)

def impar(n):
    if(n== 1):
        return True
    else:
        return par(n-1)

#Ejercicio 5

def Max(array):
    if (len(array) == 0):
        return array[0]
    else:
        max = max(array[1:])
        if array[0]> max:
            return array[0]
        else:
            return max

#Ejercicio 6

def repli(array,number,index=0):
    if index == (len(array)):
        return []
    results = []
    for i in range(number):
        results.append(array[index])
    return results + repli(array, number,index + 1)

#Ejercicio 7
def k(n,p, index = 1):
    if (n==index):
        return n*p
    elif(n<p):
        return p*index + k(n,p,index +1)

#Ejercicio 8
def k(f,c, index = 1):
    if (f==index):
        return 1
    elif(f > index):
        return index + k(f,c,index +1)




#Ejercicio 9
#Ejercicio 10
#Ejercicio 11