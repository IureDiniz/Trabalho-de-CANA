texto = input("Digite uma string: ")

letras = list(texto)

for i in range(len(letras)):

    if 'A' <= letras[i] <= 'Z':

        codigo_ascii = ord(letras[i])
        codigo_ascii = codigo_ascii + 32
        letras[i] = chr(codigo_ascii)

for i in range(len(letras) - 1):

    menor = i

    for j in range(i + 1, len(letras)):

        if letras[j] < letras[menor]:
            menor = j

    temp = letras[i]
    letras[i] = letras[menor]
    letras[menor] = temp

resultado = ""

for letra in letras:
    resultado += letra

print("String ordenada:", resultado)