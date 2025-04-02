frase = "Python é uma linguagem poderosa"

tabela = str.maketrans('aeiou', '     ')

print(frase.translate(tabela))