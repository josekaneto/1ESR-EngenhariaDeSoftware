from argparse import ZERO_OR_MORE

# numero = 10
# lista = [1, 7, 8, 9]
#
# class AlunosBurrosException(Exception):
#     def __init__(self, mensagem = "Os alunos são muito burros para executar esse programa!"):
#         self.mensagem = mensagem
#         super().__init__(self.mensagem)
#
#
# try:
#     if True:
#         raise AlunosBurrosException
#
# except Exception as e:
#     print("Deu erro:", e)

# try:
#      print(numero / 0)
#     # print(lista[2])
#
# except ZeroDivisionError as e:
#     print("Não posso dividir por zero: ", e)
#
# except Exception as e:
#     print("Deu erro: ", e)
#
# finally:
#     print("Encerrando")