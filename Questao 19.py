#implementando a lista:
class Item():
    def __init__(self, dado):
        self.prox = None
        self.ant = None
        self.dado = dado

def imprimir_lista(inicio):
    atual = inicio
    while atual:
        print(atual.dado, end = ", ")
        atual = atual.prox
    print("None")

def inserir_no_inicio(inicio, dado):
    novoItem = Item(dado)
    novoItem.prox = inicio
    if inicio:
        inicio.ant = novoItem
    return novoItem

def inserir_apos_item(item, dado):
    novoItem = Item(dado)
    novoItem.prox = item.prox
    novoItem.ant = item
    if item.prox:
        item.prox.ant = novoItem
    item.prox = novoItem

def inserir_antes_item(item, dado):
    novoItem = Item(dado)
    novoItem.prox = item
    novoItem.ant = item.ant
    if item.ant:
        item.ant.prox = novoItem
    item.ant = novoItem

def inserir_no_fim(inicio, dado):
    novoItem = Item(dado)
    if inicio is None:
        return novoItem

    atual = inicio
    while atual.prox:
        atual = atual.prox

    atual.prox = novoItem
    novoItem = atual
    return inicio

def inicializar_lista():
    inicio = Item(0)
    for i in range(1, 20):
        inserir_no_fim(inicio, i)
    return inicio

#implementando as buscas:
#busca linear
def busca_linear(inicio, valor):
    atual = inicio
    i = 0
    while atual:
        if atual.dado == valor:
            print(f"Iterações: {i}")
            return True
        else:
            atual = atual.prox
        i += 1
    print(f"Iterações: {i}")
    return False

#busca binária
def encontrar_meio(inicio, fim):
    if inicio is None:
        return None

    if inicio == fim:
        return inicio

    lento = inicio
    rapido = inicio.prox

    while rapido != fim:
        rapido = rapido.prox
        lento = lento.prox
        if rapido != fim:
            rapido = rapido.prox

    return lento

def busca_binaria(cabeca, valor):
    comeco = cabeca
    fim = None
    i = 0
    while True:
        meio = encontrar_meio(comeco, fim)

        if meio is None:
            i += 1
            print(f"Iterações: {i}")
            return False

        if meio.dado == valor:
            i += 1
            print(f"Iterações: {i}")
            return True

        elif comeco == fim:
            break

        elif meio.dado < valor:
            comeco = meio.prox

        elif meio.dado > valor:
            fim = meio
        i+=1

    print(f"Iterações: {i}")
    return False

lista = inicializar_lista()
print("Lista:")
imprimir_lista(lista)
valor = int(input("Digite um valor para ser buscado na lista: "))
print("Busca linear:")
if busca_linear(lista, valor):
    print(f"O valor {valor} foi encontrado")
else:
    print(f"O valor {valor} não foi encontrado")

print("Busca binária:")
if busca_binaria(lista, valor):
    print(f"O valor {valor} foi encontrado")
else:
    print(f"O valor {valor} não foi encontrado")
