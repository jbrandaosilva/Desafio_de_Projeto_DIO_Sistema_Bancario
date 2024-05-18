menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        operacao = float(input("Informe o valor a ser depositado: "))
        
        if operacao > 0:
            saldo += operacao
            extrato += f"\nDeposito: R$ {operacao:.2f}\n"
            extrato += f"Saldo: R$ {saldo:.2f}\n" 
            print("Transação realizada com sucesso!")                                 
        else:
            print("Valor invalido! Tente novamente.")
            
    elif opcao == "s":
        operacao = float(input("Digite o valor do saque desejado: "))
        
        excecao_saques = numero_saques >= LIMITE_SAQUES
        exececao_limite = operacao > 500
        saldo_insuficiente = operacao > saldo
        
        if excecao_saques:
            print("Número de saques diário excedido! Volte amanhã!")
            
        elif exececao_limite:
            print(f"O valor desejada excede o limite de saque. O limite de saque da conta é de R$ {limite:.2f}")
        
        elif saldo_insuficiente:
            print("Saldo insuficiente!")
            
        else:
                saldo -= operacao
                extrato += f"\nSaque: R$ {operacao:.2f}\n"
                extrato += f"Saldo: R$ {saldo:.2f}\n"
                numero_saques += 1     
                print("Transação realizada com sucesso!")  
            
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            
        print("=========================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operaçãõ inválida, por favor selecione novamente a operação desejada.")
        