"""
Operadores Relacionais
    == igualdade
    >= maior que ou igual a
    < menor que
    > maior que
    <= menor que ou igual a
    != diferente
"""
print("Formulario de Empréstimos")
nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))
print()
print("Seus dados estão sendo processados...")
import time
time.sleep(3)
print()
print("Dados coletados com sucesso!")
print()
# Minimo para pegar o empréstimo
idade_limite = 18
idade_jovem = 20
idade_adulto = 30


# if idade >= idade_limite:
#   print(f'{nome} pode pegar o empréstimo.')
# else:
#    print(f'{nome} não pode pegar o empréstimo')

if idade >= idade_jovem and idade <= idade_adulto:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo')
