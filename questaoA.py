import matplotlib.pyplot as plt
import random
import timeit

def geraLista(tam):
    random.seed()
    i = 0
    lista = []
    while i < tam:
        lista.append(random.randint(1, tam))
        i += 1

    return lista


def bubbleSort(lista):
    i = 0
    while i < len(lista) :
        j = 0
        while j < len(lista) - 1:
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
            j += 1
        i += 1

def insertionSort(lista):
    for i in range(1, len(lista)):
        x = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > x:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = x

def selectionSort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min]:
                min = j

        lista[i], lista[min] = lista[min], lista[i]

def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

def quickSort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    quickSort(menores)
    quickSort(maiores)

    insertionSort(menores)
    insertionSort(maiores)


    lista.clear()
    for x in menores:
        lista.append(x)
    lista.append(pivo)
    for x in maiores:
        lista.append(x)

def countingSort(lista):
  tab = [0] * (len(lista)+1)

  for v in lista:
    tab[v] += 1

  for i in range(len(lista)):
    lista.pop()

  for i in range(len(tab)):
    for j in range(tab[i]):
      lista.append(i)


def countingSortParaRadix(lista, exp):
    tab = [[], [], [], [], [], [], [], [], [], []]

    for v in lista:
        digito = (v // exp) % 10
        tab[digito].append(v)

    for _ in range(len(lista)):
        lista.pop()

    for i in range(len(tab)):
        for item in tab[i]:
            lista.append(item)

def radixSort(lista):

    exp = 1
    while len(lista) // exp > 0:
        countingSortParaRadix(lista, exp)
        exp *= 10

def bucketSort(lista):
    bucket = []

    for i in range(int(len(lista) / 1000)):
        bucket.append([])

    for num in lista:
        i = int(num/ len(lista) / 1000)
        bucket[i].append(num)

    for i in range(len(bucket)):
        mergeSort(bucket[i])

    lista.clear()
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            lista.append(bucket[i][j])

def shellSort(lista):
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2

def heapify(lista, n, i):
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and lista[i] < lista[l]:
        maior = l
    if r < n and lista[maior] < lista[r]:
        maior = r
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heapSort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
      heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
      lista[i], lista[0] = lista[0], lista[i]
      heapify(lista, i, 0)




# Esse código é equivalente ao main.
# Aqui é aplicado cada método de ordenação e calculado seu tempo
# vetor tamanhos especifica o tamanho de cada lista.
tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

# Deve existir um vetor ou lista para cada método de ordenação
# O intuito é armazenar o tempo de ordenação de cada método de acordo com o tamanho
temposBurbbleSort = []
temposInsertionSort = []
temposSelectionSort = []
temposMergeSort = []
temposQuickSort = []
temposCountingSort = []
temposRadixSort = []
temposBucketSort = []
temposShellSort = []
temposHeapSort = []

for tamanho in tamanhos :
    lista = geraLista(tamanho)
    # Em python tudo é objeto, ou seja, passagem por referência.
    # Por isso é feito da cópia da lista
    # Nos métodos de ordenação o aluno deve aplicar o vetor lista_teste
    lista_teste = list(lista) #copia a lista

    # Esta instrução calcula o tempo de ordenação usando Bubble sort.
    # O discente precisa construir uma instrução dessa para cada método de ordenação
    # O que vai mudar é vetor que você adiciona o tempo e o método em si
    temposBurbbleSort.append(timeit.timeit("bubbleSort({})".format(lista_teste),setup="from __main__ import bubbleSort", number=1))
    temposInsertionSort.append(timeit.timeit("insertionSort({})".format(lista_teste),setup="from __main__ import insertionSort", number=2))
    temposSelectionSort.append(timeit.timeit("selectionSort({})".format(lista_teste),setup="from __main__ import selectionSort", number=3))
    temposMergeSort.append(timeit.timeit("mergeSort({})".format(lista_teste),setup="from __main__ import mergeSort", number=4))
    temposQuickSort.append(timeit.timeit("quickSort({})".format(lista_teste),setup="from __main__ import quickSort", number=5))
    temposCountingSort.append(timeit.timeit("countingSort({})".format(lista_teste),setup="from __main__ import countingSort", number=6))
    temposRadixSort.append(timeit.timeit("radixSort({})".format(lista_teste),setup="from __main__ import radixSort", number=7))
    temposBucketSort.append(timeit.timeit("bucketSort({})".format(lista_teste),setup="from __main__ import bucketSort", number=8))
    temposShellSort.append(timeit.timeit("shellSort({})".format(lista_teste),setup="from __main__ import shellSort", number=9))
    temposHeapSort.append(timeit.timeit("heapSort({})".format(lista_teste),setup="from __main__ import heapSort", number=10))

    # Este print é opcional e serve para mostrar quais tamanhos foram ordenados
    print( "Lista de tamanho {}".format(tamanho), " ordenada")



    fig, ax = plt.subplots()

# Existem as funçõews semilogx ou lolog ou plot para exibir o gráfico
# Alguns deles exibem uma curva melhor
# O discente precisa, por exemplo, usar a função plot para cada método de ordenação
#ax.semilogx(tamanhos, temposBurbbleSort, label="Bubble Sort")
#ax.loglog(tamanhos, temposBurbbleSort, label="Bubble Sort")
ax.plot(tamanhos, temposBurbbleSort, label="Bubble Sort")
ax.plot(tamanhos, temposInsertionSort, label="Insertion Sort")
ax.plot(tamanhos, temposSelectionSort, label="Selection Sort")
ax.plot(tamanhos, temposMergeSort, label="Merge Sort")
ax.plot(tamanhos, temposQuickSort, label="Quick Sort")
ax.plot(tamanhos, temposCountingSort, label="Counting Sort")
ax.plot(tamanhos, temposRadixSort, label="Radix Sort")
ax.plot(tamanhos, temposBucketSort, label="Bucket Sort")
ax.plot(tamanhos, temposShellSort, label="Shell Sort")
ax.plot(tamanhos, temposHeapSort, label="Heap Sort")


#Configuracoes do grafico
plt.ylabel("TEMPO")
plt.xlabel("TAMANHO")

# Confirgura Legenda
legend = ax.legend(loc='upper left', shadow=True)

frame = legend.get_frame()
frame.set_facecolor('0.90')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)
plt.savefig("imagens/questaoA/0-OrdenacoesTempos.png")


fig, ax = plt.subplots()

ax.plot(tamanhos, temposBurbbleSort, label="Bubble Sort")
ax.plot(tamanhos, temposInsertionSort, label="Insertion Sort")
ax.plot(tamanhos, temposSelectionSort, label="Selection Sort")


#Configuracoes do grafico
plt.ylabel("TEMPO")
plt.xlabel("TAMANHO")

# Confirgura Legenda
legend = ax.legend(loc='upper left', shadow=True)

frame = legend.get_frame()
frame.set_facecolor('0.90')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)
plt.savefig("imagens/questaoA/1-OrdenacoesMaioresTempos.png")

fig, ax = plt.subplots()

ax.plot(tamanhos, temposShellSort, label="Shell Sort")
ax.plot(tamanhos, temposHeapSort, label="Heap Sort")
ax.plot(tamanhos, temposMergeSort, label="Merge Sort")
ax.plot(tamanhos, temposQuickSort, label="Quick Sort")
ax.plot(tamanhos, temposBucketSort, label="Bucket Sort")


#Configuracoes do grafico
plt.ylabel("TEMPO")
plt.xlabel("TAMANHO")

# Confirgura Legenda
legend = ax.legend(loc='upper left', shadow=True)

frame = legend.get_frame()
frame.set_facecolor('0.90')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)
plt.savefig("imagens/questaoA/2-OrdenacoesMediosTempos.png")

fig, ax = plt.subplots()

ax.plot(tamanhos, temposMergeSort, label="Merge Sort")
ax.plot(tamanhos, temposCountingSort, label="Counting Sort")
ax.plot(tamanhos, temposRadixSort, label="Radix Sort")

#Configuracoes do grafico
plt.ylabel("TEMPO")
plt.xlabel("TAMANHO")

# Confirgura Legenda
legend = ax.legend(loc='upper left', shadow=True)

frame = legend.get_frame()
frame.set_facecolor('0.90')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)
plt.savefig("imagens/questaoA/3-OrdenacoesMenoresTempos.png")


