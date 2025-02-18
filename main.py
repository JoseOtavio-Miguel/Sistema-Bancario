from datetime import datetime
from abc import ABC
import os
import textwrap

class Conta:
    def __init__(self):
        self.saldo = 0
        self.num_saque_dia = 0
        self.limite_saque = 3
        self.limite_valor_saque = 500
        self.extrato = []
        
        
    def exibir_extrato(self):
        os.system('cls')
        print(f"=========  EXTRATO  ========== \n")
        cont = 1
        for transacao in self.extrato:
            print(f"\tTransação nº {cont}")
            print(f"Transação: {transacao['transação']}")
            print(f"Valor: {transacao['valor']}")
            print(f"Data: {transacao['data']}")
            print("\n")
            cont+=1
        print(f"============================== \n")   
        print(f"Saldo: R${self.saldo:.2f} \n\n")
        
        
        
    def adiciona_extrato(self, transacao, valor):
        self.extrato.append(
            {
                "transação" : transacao,
                "valor" : valor,
                "data" : datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )
    
    
    def deposito(self):
        valor = int(input(" Valor do Depósito : "))
        if(valor <= 0):
            print("Valor Inválido")
        else:
            print(" Depósito Realizado com Sucesso ")
            self.saldo += valor
            self.adiciona_extrato("Depósito", valor)
        
        
    def saque(self):
        valor = int(input(" Valor do Saque : "))
        if(self.num_saque_dia > self.limite_saque):
            print(" Limite de Saque atingido !")
        else:
            if(valor > self.saldo):
                print(" Saldo Insuficiente para a Transação!")
            else:
                if(valor <= 0 or valor > self.limite_valor_saque):
                    print(" Valor Inválido ")
                else:
                    print(" Saque Realizado com Sucesso !")
                    print(f"============================== \n")
                    self.saldo -= valor
                    self.adiciona_extrato("Saque", valor)
        return 
            


def menu():
    menu = """
    ------------ MENU --------------
    [d] - \tDEPOSITAR
    [s] - \tSACAR
    [e] - \tEXTRATO
    [q] - \tSAIR
    => """
    
    return input(textwrap.dedent(menu)) #Remove espaços extras à esquerda da entrada (string[menu])


def main():
    conta = Conta()
    while True:
        opcao = menu()

        if opcao == "d":
            conta.deposito()

        elif opcao == "s":
            conta.saque()

        elif opcao == "e":
            conta.exibir_extrato()

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

main()