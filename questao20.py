class Arvore:

  def __init__(self, valor):
    self.valor = valor
    self.filho = []
    self.pai = None




  def adicionar(self, pai, valor):
    novoNo = Arvore(valor)

    if self.valor == pai:
      novoNo.pai = self
      self.filho.append(novoNo)
      return True

    for no in self.filho:
      if no.adicionar(pai, valor):
        return True

    return False


  # Recursivos
  def encontra(self, valor):
    if self.valor == valor:
      return self

    for no in self.filho:
      aux = no.encontra(valor)
      if aux is not None:
          return aux

    return None

  def contaNoRecursivo(self, n):
    n += 1
    for no in self.filho:
      n = no.contaNoRecursivo(n)

    return n

  def somaNoRecursivo(self, v):

    v += self.valor
    for no in self.filho:
      v = no.somaNoRecursivo(v)

    return v

  def subir(self, p):
    p += 1
    if self.pai is None:
      return p

    p = self.pai.subir(p)
    return p

  def profundidadeNoRecursivo(self, valor, p):
    no = self.encontra(valor)

    if no is None:
      return p

    p = no.subir(p)

    return p


  # Iterativo
  def encontra(self, valor):
    arvore = [self]

    while arvore:
        no = arvore.pop()

        if no.valor == valor:
            return no

        arvore.extend(no.filho)

    return None

  def contaNo(self):
    contador = 0
    arvore = [self]

    while arvore:
        no = arvore.pop()
        contador += 1
        arvore.extend(no.filho)

    return contador


  def somaNo(self):
    soma = 0
    arvore = [self]

    while arvore:
        no = arvore.pop()
        soma += no.valor
        arvore.extend(no.filho)

    return soma


  def profundidadeNo(self, valor):
    no = self.encontra(valor)
    p = -1

    while no is not None:
      p += 1
      no = no.pai

    return p


# Iterativo
raiz = Arvore(10)

raiz.adicionar(10, 5)
raiz.adicionar(10, 6)

raiz.adicionar(5, 15)

raiz.adicionar(6, 6)
raiz.adicionar(6, 7)
raiz.adicionar(6, 8)

raiz.adicionar(8, 9)

print(raiz.valor)

for no in raiz.filho:
  print(no.pai.valor, ' é pai de ', no.valor)

print()

for no in raiz.filho[0].filho:
  print(no.pai.valor, ' é pai de ', no.valor)

print()

for no in raiz.filho[1].filho:
  print(no.pai.valor, ' é pai de ', no.valor)

print()

for no in raiz.filho[1].filho[2].filho:
  print(no.pai.valor, ' é pai de ', no.valor)

print()

print('O numero de nós é: ', raiz.contaNo())

print('A soma de todos os nós é: ', raiz.somaNo())

v = 9
print(f'A profundidade de {v} é: {raiz.profundidadeNo(v)}')


# Recrusivo
raiz = Arvore(10)

raiz.adicionar(10, 5)
raiz.adicionar(10, 6)

raiz.adicionar(5, 15)

raiz.adicionar(6, 6)
raiz.adicionar(6, 7)
raiz.adicionar(6, 8)

raiz.adicionar(8, 9)

print(raiz.valor)

for no in raiz.filho:
  print(no.pai.valor, ' é pai de ', no.valor)

print()

for no in raiz.filho[0].filho:
  print(no.pai.valor, ' é pai de ', no.valor)

print()

for no in raiz.filho[1].filho:
  print(no.pai.valor, ' é pai de ', no.valor)

print()

for no in raiz.filho[1].filho[2].filho:
  print(no.pai.valor, ' é pai de ', no.valor)

print()

print('O numero de nós é: ', raiz.contaNoRecursivo(0))

print('A soma de todos os nós é: ', raiz.somaNoRecursivo(0))

v = 9
print(f'A profundidade de {v} é: {raiz.profundidadeNoRecursivo(v, -1)}')
