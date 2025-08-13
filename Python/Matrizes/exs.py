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