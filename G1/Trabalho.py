import random
import time
import sys
sys.setrecursionlimit(10000)


def vetor_aleatorio(n):
    return [random.randint(0, n*2) for _ in range(n)]

def vetor_ordenado(n):
    return list(range(n))

def vetor_inverso(n):
    return list(range(n, 0, -1))


def bubble_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]
    return time.time() - start

def bubble_sort_otimizado(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocou = True
        if not trocou: break
    return time.time() - start

def insertion_sort(arr):
    start = time.time()
    for i in range(1, len(arr)):
        v, c = arr[i], i-1
        while c >= 0 and v < arr[c]:
            arr[c+1] = arr[c]
            c -= 1
        arr[c+1] = v
    return time.time() - start

def insertion_sort_recursivo(arr):
    def rec(a, n):
        if n <= 1: return
        rec(a, n-1)
        u, j = a[n-1], n-2
        while j >= 0 and a[j] > u:
            a[j+1] = a[j]; j -= 1
        a[j+1] = u
    s = time.time()
    rec(arr, len(arr))
    return time.time() - s

def selection_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if arr[j] < arr[m]: m = j
        arr[i], arr[m] = arr[m], arr[i]
    return time.time() - start

def selection_sort_recursivo(arr):
    def rec(a, i):
        if i >= len(a)-1: return
        m = i
        for j in range(i+1, len(a)):
            if a[j] < a[m]: m = j
        a[i], a[m] = a[m], a[i]
        rec(a, i+1)
    s = time.time()
    rec(arr, 0)
    return time.time() - s

def shell_sort(arr):
    start = time.time()
    n, g = len(arr), len(arr)//2
    while g > 0:
        for i in range(g, n):
            t, j = arr[i], i
            while j >= g and arr[j-g] > t:
                arr[j] = arr[j-g]; j -= g
            arr[j] = t
        g //= 2
    return time.time() - start

def shell_sort_otimizado(arr):
    start = time.time()
    n, h = len(arr), 1
    while h < n // 3: h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            t, j = arr[i], i
            while j >= h and arr[j-h] > t:
                arr[j] = arr[j-h]; j -= h
            arr[j] = t
        h //= 3
    return time.time() - start


def executar_testes(nome_cenario, dados):
    algos = {
        "Bubble Base": bubble_sort,
        "Bubble Otimizado": bubble_sort_otimizado,
        "Insertion Base": insertion_sort,
        "Insertion Rec.": insertion_sort_recursivo,
        "Selection Base": selection_sort,
        "Selection Rec.": selection_sort_recursivo,
        "Shell Base": shell_sort,
        "Shell Knuth": shell_sort_otimizado
    }
    
    tempos = {nome: func(dados.copy()) for nome, func in algos.items()}
    pior = max(tempos.values())
    
    print(f"\nArray: {nome_cenario} ({len(dados)} elementos)")
    print(f"{'Algoritmo':<20} | {'Tempo (s)':<10} | {'Diferença Relativa'}")
    print("-" * 55)
    for nome, t in tempos.items():
        diff = ((t - pior) / pior) * 100 if pior > 0 else 0
        print(f"{nome:<20} | {t:.5f}s  | ({diff:>7.2f}%)")


N = 1000

executar_testes("ALEATÓRIO", vetor_aleatorio(N))
executar_testes("ORDENADO", vetor_ordenado(N))
executar_testes("INVERSO", vetor_inverso(N))
