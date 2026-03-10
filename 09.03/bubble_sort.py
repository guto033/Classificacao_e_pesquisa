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

algoritmo = bubble_sort(array)
print(algoritmo)
