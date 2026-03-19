pix_cliente ={
        "nome": "Rafael",
        "valor": 150.50,
        "banco_destino": "Nubank"

}

valor_transferencia = pix_cliente["valor"]
nome_cliente = pix_cliente["nome"]

print(f"O {nome_cliente} enviou R$ {valor_transferencia} para o {pix_cliente['banco_destino']}.")