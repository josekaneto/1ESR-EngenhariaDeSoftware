'''frase = 'Boa noite, estou com uma bixeira na testa'

for letra in frase:
    print(letra)'''

'''for i in range (0, 30):
    print(i)'''

'''lista = ['a', 'd', 'y', 'p']

for i, c in enumerate(lista):
    print(i, ':', c)'''

'''lista = ['a', 'd', 'y', 'p']

if 'a' in lista:
    print('A lista contém a letra a')'''

'''palavra = 'bobalhao'

if 'boba' in palavra:
    print('Esta contido')'''

'''palavra = 'bobalhao'

if 'bobo' not in palavra:
    print('Não Esta contido')'''

'''for i in range(0, 30):
    if i == 15:
        break
    print(i)'''

'''for i in range(0, 30):
    if i % 2 != 0:
        continue
    print(i)'''

'''a = ['john', 'charles', 'mike']
b = ['jenny', 'christy', 'monica']

x = zip(a,b)
print(list(x))'''

'''names = ['jhon', 'robert']
surnames = ['smith', 'de niro']
number = [1, 2]

for name, surnames, number in zip(names, surnames, number):
    print(name, surnames, number)'''

'''pares = [i for i in range(0, 101) if i % 2 == 0]

print(pares)'''

'''pares = [i**2 for i in range(0, 101) ]

print(pares)
'''

'''currentNumber = 0

while currentNumber <= 10:
    print(currentNumber)
    currentNumber += 1'''

'''while True:
    entrada = input('Digite algo: ')

    if entrada == 'quit':
        break
    else:
        print('O texto digitado foi: '+ entrada)'''

'''currentNumber = 0

while currentNumber < 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
        continue
    else:
        print(currentNumber)'''