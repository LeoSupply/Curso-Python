"""
Iniciar com letra , pode conter numeros, separar _, letras minusculas
"""
nome='Cadastro'
print(nome)

nome = 'Leo Freitas'
idade = 17
altura = 1.73
e_maior = idade > 18
peso = 80
imc = peso // (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Peso:', peso)
print('Maior de idade:', e_maior)
print('IMC:', imc)
print('IMC Acima do normal:', bool(imc >25))