conta_restaurante = float(input('Digite a conta do restaurante: '))
gorjeta_restaurante = float(input('Quantos porcento de gotjeta deseja dar para o restaurante: '))

gorjeta = conta_restaurante * (gorjeta_restaurante / 100)
total = conta_restaurante + gorjeta

print(f'O total da conta do restaurante com a gorjeta é: {total}')
print('O valor da gorjeta é: ', gorjeta)