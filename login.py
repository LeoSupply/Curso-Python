"""
Criando um login de teste
"""

# Dados do cadastro
user = "leosupply"
password = "leosupply123"

# Login
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
print()
print("Seus dados estão sendo verificados...")
import time
time.sleep(2)
print()

# Verificar login
if usuario == user and senha == password:
    print("Login realizado com sucesso!")
else:
    print("Usuário não foi encontrado ou a senha foi digitada incorretamente. Tente verificar novamente!")
