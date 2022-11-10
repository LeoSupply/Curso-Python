"""
Entrada de dados
"""
# Variaveis
print("Bem Vindo(a) ao formulario do LeoSupply")
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
altura = float(input("Qual é sua altura? "))
peso = float(input("Qual é o seu peso? "))
ano_atual = 2022
ano_nascimento = (ano_atual - idade)
imc = (peso / altura ** 2)
print()
print("Estou verificando seus dados...")
import time
time.sleep(3)
print()
print("Dados verificados com sucesso!")
import time
time.sleep(3)
print()
print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}.')
print(f'Seu IMC de acordo com seu peso de -> {peso}kg e sua altura de -> {altura} é equivalente a {imc:.2f}.')

