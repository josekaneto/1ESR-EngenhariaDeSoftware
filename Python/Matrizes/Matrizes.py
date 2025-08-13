# alunos = [
#     {
#     "Nome": "André",
#     "local": "osasco"
#     },
#     {
#     "Nome": "João",
#     "local": "São Paulo"
#     }
#
# ]
#
# print(alunos[1]["Nome"])
# print(alunos[0]["local"])
#
# numero = int(input("Digite um quantos zeros você quer colocar na lista: "))
# numeros = []
#
# for n in range(numero):
#     numeros.append(0)
#
# print(numeros)

# aaa = [[0,1,2],
#        [3,4,5],
#        [6,7,8]]
#
# for i in range(len(aaa)):
#     for n in range(len(aaa[i])):
#         print(aaa[i][n])
#
#
# matriz = []
# m = 3
# n = 3
#
# for linha in range(m):
#     matriz.append([])
#     for coluna in range(n):
#         matriz[linha].append(0)
# for linha in matriz:
#     print(linha)


# def criar_matriz_zeros(m,n):
#     matriz = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(0)
#         matriz.append(linha)
#     return matriz
#
# matriz = criar_matriz_zeros(2,2)
# for matriz_for in matriz:
#     print(matriz_for)