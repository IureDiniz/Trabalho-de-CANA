"Representa um nó individual da lista encadeada"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"Estrutura da lista encadeada com funções auxiliares"
class LinkedList:
    def __init__(self):
        self.head = None

    # Adiciona um elemento ao final da lista
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Imprime a lista de forma legível
    def print_list(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) if elements else "Lista Vazia")

"Encontra o nó do meio da lista usando o método de dois ponteiros"
def get_middle(head):
    if not head:
        return head

    # O ponteiro 'fast' anda duas casas, enquanto 'slow' anda uma
    slow = head
    fast = head.next

    # Quando 'fast' chegar ao fim, 'slow' estará no meio.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

"Intercala duas listas encadeadas ordenadas em uma única lista ordenada"
def sorted_merge(left, right):
    # Se uma das metades for vazia, retorna a outra
    if not left:
        return right
    if not right:
        return left

    # Escolhe o menor valor e chama a função recursivamente para o próximo nó
    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)

    return result

"Função principal do Merge Sort para listas encadeadas"
def merge_sort(head):
    # Se a lista estiver vazia ou tiver apenas um elemento
    if not head or not head.next:
        return head

    # Encontra o meio da lista
    middle = get_middle(head)
    next_to_middle = middle.next

    # Divide a lista em duas metades (quebra o vínculo)
    middle.next = None

    # Aplica o merge_sort recursivamente em ambas as metades
    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    # Intercala as duas metades ordenadas
    sorted_list = sorted_merge(left, right)
    
    return sorted_list

"Exemplo de uso"
lista = LinkedList()

for valor in [38, 27, 43, 3, 9, 82, 10]:
    lista.append(valor)

print("Lista original:")
lista.print_list()

lista.head = merge_sort(lista.head)

print("\nLista ordenada:")
lista.print_list()