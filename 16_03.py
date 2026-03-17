import random
import time


array = []
random.seed(2026)
array = [random.randint(10,50) for _ in range(10)]


def busca_num():
    numero = int(input("\nDigite um número: "))
    return numero

def busca(array, numero):
    for i in range(len(array)):
        if array[i] == numero:
            print("O número está na lista\n")
            return
    print("O número não está na lista")

def ordenar_lista(array):
    start_time = time.time()
    tam = len(array)
    for j in range(tam-1):
        maior = j
        for i in range(j+1, tam):
            if array[i] < array[maior]:
                maior = i
        array[j], array[maior] = array[maior], array[j]
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def transferencia(array):
    start_time = time.time()
    tam = len(array)
    array2 = []
    maior = 0
    
    for i in range(len(array)):
        if array[i] > maior:
            array2.append(array[i])
            maior = array[i]
    end_time = time.time()
    elapsed_time = end_time - start_time        
    return elapsed_time

def bubble_sort(array):
    n = len(array) - 1
    for i in range (len(array) - 1):
        k= 0
        while k<n - i:
            if array[k]>array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]
            k+=1

    return array

    
#numero = busca_num()
#busca(array, numero)

#ordenacao = ordenar_lista(array)
#print(ordenacao)

#transferir = transferencia(array)
##array.clear()
##print(array)
#print(transferir)

#algoritmo = bubble_sort(array)
#print(algoritmo)

"""def insertion_sort(array):
    for i in range(1, len(array)):
        valor = array[i]
        chave = i - 1

        while chave >= 0 and valor < array[chave]:
            array[chave + 1] = array[chave]
            chave -= 1

        array[chave + 1] = valor

    print(array)
"""



"""
def insertion_sort2(array):
    cont = 1
    for i in array:
        if i > array[cont]:
            num = array[cont]
            array.pop(i)
            array.insert(num)

    print(array)
"""



def shell_sort(array):
    n = len(array)
    salto = n // 2
    while salto > 0:
        for i in range(salto, n):
            temp = array[i]
            j = i

            while j >= salto and array[j-salto] > temp:
                array[j] = array[j-salto]
                j -= salto

            array[j] = temp

        salto //= 2

    print(array)


   

shell_sort(array)
