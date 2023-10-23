import math

#Ejercicio 1
def ciclingdni(num_dni):
    if(len(str(num_dni))==8 or len(str(num_dni))==7):
        return True
    else:
        return False
#Ejercicio 2
def lastword(string):
    palabralista = string.split(' ')
    last= palabralista[-1]
    return last

def longstring(string):
    long = len(string)
    return print(long)

#Ejercicio 3
def string_array(string):
    array=string.split()
    return array

def identificador(nombre, n_documento):
    firs_name = string_array(nombre)[0]
    last_name_number = str(len(string_array(nombre)[-1]))
    firs_three_dni = str(n_documento)[:3]
    return firs_name+last_name_number+firs_three_dni


#Ejercicio 4
def multiplo(num1, num2):
    if(num1%num2==0):
        return print(f"{num1} es multiplo de {num2}")

#Ejercicio 5
def medium(a,b):
    medium=(a+b)/2
    return medium

#Ejercicio 6
def spacebetween(text):
    i=0
    string_space=""
    while(i<len(text)):
        string_space+=text[i]+" "
        i+=1
    return string_space

#Ejercicio 7
def max_min_num(array):
    max = array[0]
    min = array[0]
    for i in range(len(array)):
        if max<array[i]:
            max=array[i]
        if min>array[i]:
            min=array[i]
    return print(f"El máximo valor es: {max}\nEl mínimo valor es: {min}")

#Ejercicio 8
def perim_area(radius):
    area=radius*radius*3,14
    perim= 2*3,14*radius
    return print(f"El área: {area}, el perímetro: {perim}")

#Ejercicio 9
def login(user,password):
    if(user=="usuario1" and password=="asdasd"):
        return True

#Ejercicio 10

def discount(dictionary, percentage):
    price_discount=0
    for key,value in dictionary.items():
        if(key == 'precio'):
            price_discount = value - (value*percentage/100)
        if(key == 'cantidad'):
            price_discount *= value
    return price_discount

#Ejercicio 11

def array_number(palabra):
    palabra =  len(palabra)
    return palabra

def order_lists(función, lista):
    new_list=[0]*len(lista)
    for i in range(len(lista)):
        new_list[i]=función(lista[i])
    return new_list

#Ejercicio 12

def string_dictionary(string):
    words= string.split()
    dictionary_words ={}
    for word in words:
        dictionary_words[word] = len(word)
    return dictionary_words

#Ejercicio 13

def module_vector(vector):
    sum = 0
    for i in range(len(vector)):
        sum += vector[i]*vector[i]
    module = math.sqrt(sum)
    return module

#Ejercicio 14

def prime_number(number):
    sum=0
    prime = False
    until = int(number/2)+1
    for i in range(until):
        if(i != 0 and number % i == 0):
            sum +=1
    if(sum==1):
        prime = True
    return prime

#Ejercicio 15
#Ejercicio 16

def exist(numero_largo, digito):
    sum = 0
    for i in range(len(numero_largo)):
        if(numero_largo[i]== digito):
            sum +=1
    return sum

#Ejercicio 17
