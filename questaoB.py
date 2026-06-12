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

    return lista


def buscaLinear(lista, valor):
  for i in range(len(lista)):
    if lista[i] == valor:
      break

def buscaLinearSentinela(lista, valor):
  lista.append(valor)

  i = 0
  while lista[i] != valor:
    i += 1

def buscaBinaria(lista, valor):
  esquerda = 0
  direita = len(lista) - 1

  while esquerda <= direita:
    meio = (esquerda + direita) // 2
    if lista[meio] == valor:
      break

    if lista[meio] < valor:
      esquerda = meio + 1
    else:
      direita = meio - 1


def buscaBinariaRapida(lista, valor):
  esquerda = 0
  direita = len(lista) - 1

  while esquerda <= direita:
    meio = (esquerda + direita) // 2

    if lista[meio] <= valor:
      esquerda = meio + 1
    else:
      direita = meio - 1


tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

temposLinearAleatorio = []
temposLinearOrdenado = []

temposSentinelaAleatorio = []
temposSentinelaOrdenado = []

temposBinaria = []
temposBinariaRapida = []


for tamanho in tamanhos :
    lista = geraLista(tamanho)
    listaAleatoria = list(lista)
    listaOrdenada = mergeSort(list(lista))
    valor = random.randint(1, tamanho)


    temposLinearAleatorio.append(timeit.timeit("buscaLinear({}, {})".format(listaAleatoria, valor),setup="from __main__ import buscaLinear", number=1))
    temposLinearOrdenado.append(timeit.timeit("buscaLinear({}, {})".format(listaOrdenada, valor),setup="from __main__ import buscaLinear", number=2))

    temposSentinelaAleatorio.append(timeit.timeit("buscaLinearSentinela({}, {})".format(listaAleatoria, valor),setup="from __main__ import buscaLinearSentinela", number=3))
    temposSentinelaOrdenado.append(timeit.timeit("buscaLinearSentinela({}, {})".format(listaOrdenada, valor),setup="from __main__ import buscaLinearSentinela", number=4))

    temposBinaria.append(timeit.timeit("buscaBinaria({}, {})".format(listaOrdenada, valor),setup="from __main__ import buscaBinaria", number=5))
    temposBinariaRapida.append(timeit.timeit("buscaBinariaRapida({}, {})".format(listaOrdenada, valor),setup="from __main__ import buscaBinariaRapida", number=6))

    print( "Lista de tamanho {}".format(tamanho), " ordenada" )

fig, ax = plt.subplots()

# Existem as funçõews semilogx ou lolog ou plot para exibir o gráfico
# Alguns deles exibem uma curva melhor
# O discente precisa, por exemplo, usar a função plot para cada método de ordenação
#ax.semilogx(tamanhos, temposBurbbleSort, label="Bubble Sort")
#ax.loglog(tamanhos, temposBurbbleSort, label="Bubble Sort")
ax.plot(tamanhos, temposLinearOrdenado, label="Linear Ordenada")
ax.plot(tamanhos, temposSentinelaOrdenado, label="Sentinela Ordenada")
ax.plot(tamanhos, temposBinaria, label="Binária")
ax.plot(tamanhos, temposBinariaRapida, label="Binária Rápida")

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
plt.savefig("imagens/questaoB/BuscasOrdenadas.png")


fig, ax = plt.subplots()
ax.plot(tamanhos, temposLinearAleatorio, label="Linear Aleatoria")
ax.plot(tamanhos, temposSentinelaAleatorio, label="Sentinela Aleatoria")
ax.plot(tamanhos, temposBinaria, label="Binária")
ax.plot(tamanhos, temposBinariaRapida, label="Binária Rápida")

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
plt.savefig("imagens/questaoB/BuscasAleatorias.png")


fig, ax = plt.subplots()
ax.plot(tamanhos, temposBinaria, label="Binária")
ax.plot(tamanhos, temposBinariaRapida, label="Binária Rápida")

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
plt.savefig("imagens/questaoB/BuscasBinarias.png")