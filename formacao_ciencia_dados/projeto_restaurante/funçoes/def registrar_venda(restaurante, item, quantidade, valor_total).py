

def registrar_venda(restaurante, item, quantidade, valor_total):
    venda = {
        "restaurante": restaurante["nome"],
        "item": item,
        "quantidade": quantidade,
        "valor_total": valor_total,
    }
    historico_vendas.append(venda)