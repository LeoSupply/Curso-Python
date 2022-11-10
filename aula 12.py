"""
Operadores Lógicos
    and, or, not
    in e not in
"""
# Dados

# Primeiro número
print('Calculadora de expoente')
x = input('Digite a base: ')
if not x:
    print('Por favor, preencha o valor da base!')
# Segundo número
y = input('Digite o número do expoente: ')
if not y:
    print('Por favor, preencha o valor do expoente!')
import time
time.sleep(1)
print()
calculo = int(x)**int(y)
print(f'Resultado: {calculo} ')



