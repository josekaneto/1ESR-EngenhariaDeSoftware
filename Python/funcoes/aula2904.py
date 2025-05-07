def saudacao():
    print(f'Olá Alunos feiosos e nóias!')

# saudacao()

def saudacao(nome):
    return (f'Olá {nome} feioso e nóia!')

saudacao("Celso")

mensage = saudacao('Celso')

print(mensage)

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(media)
 
calcular_media(10, 9)

def somar(a, b):
    return a + b

args = [3,5]
resultado = somar(*args)
print(resultado)

kwargs = {'a': 3, 'b': 5}
resultado = somar(**kwargs)
print(resultado)

def somar(a = 2, b = 3):
    return a + b

resultado = somar(5, 10)
print(resultado)

def altera_a(a):
    a = a + 1
    print(a)

a = 2
altera_a(a)
print(a)

def altera_lista(lista):
    lista.append(2)
    lista.append(5)
    print(lista)

lista = [1, 7, 8, 3]
altera_lista(lista[:])

print(lista)

def soma_total(*numeros):
    return sum(numeros)

print(soma_total(1, 2, 3))
print(soma_total(10, 20, 30, 40))
print(soma_total())

def exibir_informacoes(**informacoes):
    for chave, valor in informacoes.items():
        print(f'{chave}: {valor}')

exibir_informacoes(nomes='Ana', idade=25, cidade='São Paulo')
exibir_informacoes(produto='Notebook', preco=2500.00, marca='Dell')

expression = "5 + 5 * 3"

resultado = eval(expression)
print(resultado)

x = 10
y = 5

expressao = 'x * y + 2'

resultado = eval(expressao)

print(resultado)

x = 2

expressao = ('print(x + 3 * 5)')

eval(expressao, {}, {'x':x})

code_str = '''
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
print(result)'''

exec(code_str)


