import os
import time

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Texto do menu principal do sistema bancário
menu = """

************
* DIO BANK *
************

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Texto menu de opções para depósito
deposito_menu = """ 

*********************
* DIO BANK DEPOSITO *
*********************  

""" 

# Texto menu de opções para  saque
saque_menu = """ 

******************
* DIO BANK SAQUE *
****************** 

""" 

# Texto menu de opções para extrato
extrato_menu = """ 

********************
* DIO BANK EXTRATO *
********************  

""" 


# Função para limpar o console
def clear_console(): 
    os.system('cls' if os.name == 'nt' else 'clear')

# função depositar
def depositar():
    try:
        clear_console()
        print(deposito_menu)
        valor = float(input("Informe o valor do depósito: "))

        if valor <= 0:
            clear_console()
            print(deposito_menu)
            print("Insira um valor válido")
            time.sleep(2)
            return None
        else:
            return valor, (f"Depósito: R$ {valor:.2f}\n")
        
    except ValueError:
        print("Valor inválido. Tente novamente.")
        time.sleep(1)
        return None

# função sacar
def sacar():
    try:
        clear_console()
        print(saque_menu)
        valor = float(input("Informe o valor do saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de 3 saques diários excedido!")
            time.sleep(2)
            return None
        elif valor <= 0 or valor > limite:
            clear_console()
            print(saque_menu)
            print("Insira um valor válido")
            time.sleep(2)
            return None
        elif saldo < valor:
            print("Saldo insuficiente!")
            time.sleep(2)
            return None
        else:
            return valor, (f"Saque: R$ {valor:.2f}\n")
    except ValueError:
        print("Valor inválido. Tente novamente.")
        time.sleep(1)
        return None

# função extrato bancário
def extratobancario(extrato, saldo):
    clear_console()
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    time.sleep(5)
        
# Menu principal do sistema bancário
while True:
    clear_console()
    opcao = input(menu)
    if opcao == "d":
        deposito = depositar()
        if deposito == None:
            continue
        else:
            saldo += deposito[0]
            extrato += deposito[1]
    elif opcao == "s":
        saque = sacar()
        if saque == None:
            continue
        else:
            saldo -= saque[0]
            extrato += saque[1]
            numero_saques += 1
    elif opcao == "e":
        extratobancario(extrato, saldo)
    elif opcao == "q":
        print("Saindo do sistema. Até logo!")
        time.sleep(1)
        clear_console()
        break
    else:
       clear_console()
       print("Opção inválida. Tente novamente.")
       time.sleep(1)
       continue