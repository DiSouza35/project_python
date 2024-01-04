nome = 'Diego'
sobrenome = 'Souza'
peso = 95
altura = 1.87
imc = peso / (altura ** 2)

# f-strings

linha_1 = f'{nome} {sobrenome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}.'

print(linha_1)
print(linha_2)