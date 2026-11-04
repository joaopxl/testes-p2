# Exercicio 1 - TESTES

import classificacao_produto

# Teste 1
def test_classificar_produto_sem_estoque():
    result = classificacao_produto.classificar_produto(0)
    assert result == "Sem estoque"

# Teste 2
def test_classificar_produto_estoque_baixo():
    result = classificacao_produto.classificar_produto(3)
    assert result == "Estoque baixo"


# Teste 3
def test_classificar_produto_estoque_normal():
    result = classificacao_produto.classificar_produto(10)
    assert result == "Estoque normal"


# Teste 4
def test_classificar_produto_estoque_alto():
    result = classificacao_produto.classificar_produto(25)
    assert result == "Estoque alto"


# Teste 5
def test_classificar_produto_quantidade_invalida():
    result = classificacao_produto.classificar_produto(-1)
    assert result == "Quantidade inválida"