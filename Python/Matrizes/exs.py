from random import randint

"""Cria matriz de indentidade"""

# def criar_matriz_identidade(m,n):
#     matriz = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(0)
#             if i == j:
#                 linha[j] = 1
#         matriz.append(linha)
#     return matriz
#
# matriz = criar_matriz_identidade(5,5)
# for matriz_for in matriz:
#     print(matriz_for)

"""Lista quantas palavras repetidas tem em uma frase"""

# texto = "bom dia, boa tarde, boa noite, o salgado é bom"
#
# lista = texto.split()
#
# ocorrencia = {}
#
# for palavra in lista:
#     if palavra in ocorrencia:
#         ocorrencia[palavra]+=1
#     else:
#         ocorrencia[palavra] = 1
#
# ocorrencia = sorted(ocorrencia.items(), key = lambda item: item[1], reverse=True)
#
# print(ocorrencia)

"""Ex matriz de indentidade ao contrário"""

# def criar_matriz_identidade(m,n):
#     matriz = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(0)
#         linha[j - i] = 1
#         matriz.append(linha)
#     return matriz
#
# matriz = criar_matriz_identidade(5,5)
# for matriz_for in matriz:
#     print(matriz_for)

"""Soma dos números dentro da matriz"""

# def criar_matriz_zeros(m,n):
#     matriz = []
#     numero = 1
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(numero)
#             numero += 1
#         matriz.append(linha)
#     return matriz
#
# matriz = criar_matriz_zeros(3,3)
# for matriz_for in matriz:
#     print(matriz_for)
#
# def somar_matriz():
#     soma = 0
#     for linha in matriz:
#         for n in linha:
#             soma += n
#     return soma
#
# res = somar_matriz()
# print(res)


"""Printar apenas os elementos da diagonal principal"""

# def criar_matriz_identidade(m,n):
#     matriz = []
#     diagonal = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(0)
#             if i == j:
#                 linha[j] = random.randint(1,1000)
#                 diagonal.append(linha[j])
#         matriz.append(linha)
#     print(diagonal)
#     return matriz
#
# matriz = criar_matriz_identidade(5,5)
# for matriz_for in matriz:
#     print(matriz_for)

"""Crie uma matriz quadrada com números aleatórios e mostre apenas os elementos
da diagonal secundária. """

# def criar_matriz_identidade(m,n):
#     matriz = []
#     numeros_random = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(0)
#         linha[j - i] = random.randint(0,1000)
#         matriz.append(linha)
#         numeros_random.append(linha[j - i])
#     print(numeros_random)
#     return matriz
#
# matriz = criar_matriz_identidade(5,5)

"""Escreva um programa que calcule a transposta de uma matriz."""

# def criar_matriz_aleatoria(m,n):
#     matriz = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(randint(0,9))
#         matriz.append(linha)
#     return matriz
#
# def transposta(matriz):
#     tamanho_linhas = len(matriz)
#     tamanho_colunas = len(matriz[0])
#     matriz_transposta = []
#
#     for coluna in range(tamanho_colunas):
#         matriz_transposta.append([])
#         for linhas in range(tamanho_linhas):
#             matriz_transposta[coluna].append((matriz[linha][coluna]))
#     return matriz_transposta
#
# matriz = criar_matriz_aleatoria(3,2)
# matriz_transposta = transposta(matriz)
#
# for linha in matriz:
#     print(linha)
#
# print()
#
# for coluna in matriz_transposta:
#     print(coluna)

"""Crie duas matrizes 3x3 e calcule a soma delas."""

def criar_matriz_aleatoria(m,n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(randint(0,20))
        matriz.append(linha)
    return matriz

def criar_matriz_aleatoria_2(a,b):
    matriz = []
    for i in range(a):
        linha = []
        for j in range(b):
            linha.append(randint(0,100))
        matriz.append(linha)
    return matriz

matriz_1 = criar_matriz_aleatoria(3,3)
matriz_2 = criar_matriz_aleatoria_2(3,3)


for matriz_for in matriz_1:
    print(matriz_for)

print( )

for matriz_for_2 in matriz_2:
    print(matriz_for_2)

