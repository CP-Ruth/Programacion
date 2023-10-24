# Ordenamiento de Burbuja (Bubble Sort):
def bubble_sort_ascen(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Orden de Selección (Selection Sort):
def selection_sort_ascen(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Tipo de Inserción (Insertion Sort):
def insertion_sort_ascen(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Combinar Ordenación (Merge Sort):

def merge_sort_ascen(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_ascen(L)
        merge_sort_ascen(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


#Ordenamiento De forma descendente.-------------------

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Cambiar la condición de comparación
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

array=[15,12,159,0,153,999,20]
bubble_sort_desc(array)
print(array)

def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:  # Cambiar la condición de comparación
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:  # Cambiar la condición de comparación
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort_desc(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_desc(L)
        merge_sort_desc(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:  # Cambiar la condición de comparación
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

