'''def fatorial(n):
    if n < 2:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))

def multi(m,n):
    if m == 0 or n == 0:
        return 0
    if n == 1:
        return m

    return m + multi(m, n - 1)

print(multi(2,5))'''

'''def contagem_regresiva(m):
    if m == 0:
        return 0
    print(m)
    return contagem_regresiva(m - 1)

print(contagem_regresiva(10))'''

def contar_vogais(texto):
    if len(texto) == 0:
        return 0
    if texto[0] in 'aeiou':
        return 1 + contar_vogais(texto[1:])

    return 0 + contar_vogais(texto[1:])

print(contar_vogais('carlos'))