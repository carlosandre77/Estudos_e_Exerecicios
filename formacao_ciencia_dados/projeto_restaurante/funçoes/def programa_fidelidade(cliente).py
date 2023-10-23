def programa_fidelidade(cliente):
    if cliente["n_pedidos"] % 5 == 0:
        desconto = 0.1  # 10% de desconto
        return desconto
    else:
        return 0