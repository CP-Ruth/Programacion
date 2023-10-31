
import random

def mouse(camino, time = 0):
    if camino ==3:
        return time + 7
    else:
        time=0
        if camino==2:
            time += 5
        elif camino==1:
            time+= 3
        return mouse(random.randint(1, 3), time)
    
tiempo_salida = mouse(1)
print("Tiempo de demora: " + str(tiempo_salida))

def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

respuesta= f(5112)
print(respuesta)

"""Definir una funcion que al ingresarle un número entero me devuelva en numero invertido. Es decir que la primera posicion pase a ser la ultima, que la segunda pase a ser penultima y asi hasta llegar a la ultima posicion que pasa a ser la primera """