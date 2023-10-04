def letterinstring(abc, string):
    if abc in string:
        return True
    else:
        return False

def arraystring(array):  #pasa un array a string
    string=""
    i=0
    while (len(string)<len(array)):
        string+=array[i]
        i+=1
    return string

def strarrays(string):   #pasa un string a array
    array=[]
    i=0
    while (len(array)<len(string)):
        array.append(string[i])
        i+=1
    return array
