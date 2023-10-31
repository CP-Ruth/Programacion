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
"""
4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
•	1 es impar.
•	Si un número es impar, su antecesor es par; y viceversa.
"""
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



#Ejercicio 6
#Ejercicio 7
#Ejercicio 8
#Ejercicio 9
#Ejercicio 10
#Ejercicio 11