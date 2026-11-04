# Exercicio 1

def classificar_produto(quantidade):
    if quantidade < 0:
        return "Quantidade inválida"
    if quantidade == 0:
        return "Sem estoque"
    elif quantidade <= 5:
        return "Estoque baixo"
    elif quantidade <= 20:
        return "Estoque normal"
    else:
        return "Estoque alto"