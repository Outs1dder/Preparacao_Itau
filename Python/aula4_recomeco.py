conta = {
    "titular": "Rafael",
    "saldo": 1000.00,
}

valor_pix = 150.00

if conta["saldo"] >= valor_pix:
    print(f"PIX de R$ {valor_pix} autorizado com sucesso!")

    novo_saldo = conta["saldo"] - valor_pix
    print(f"Seu novo saldo é R$ {novo_saldo}")

else: 
    print("Saldo insuficiente para realizar essa operação.")