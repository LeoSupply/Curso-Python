# Variaveis
nome = "Leo Freitas"
idade = 18
peso = 80
altura = 1.73
ano_atual = 2022
imc = peso / (altura ** 2)
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')