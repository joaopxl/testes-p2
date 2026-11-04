# Testes Exercicio 2 - Inversão de palavras

from inversao_palavras import inverter_palavras

def test_inverter_palavras_varias():
    result = inverter_palavras("Olá mundo")
    assert result == "mundo Olá"

def test_inverter_palavras_uma():
    result = inverter_palavras("Python")
    assert result == "Python"

def test_inverter_palavras_vazia():
    result = inverter_palavras("")
    assert result == ""

def test_inverter_palavras_espacos():
    result = inverter_palavras("   ")
    assert result == ""

def test_inverter_palavras_numeros_letras():
    result = inverter_palavras("Python 3.9")
    assert result == "3.9 Python"