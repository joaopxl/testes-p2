# Testes - Exercicio 3 - validacao de cpf

from validacao_cpf import validar_cpf

def test_validacao_cpf_11_digitos():
    result = validar_cpf("12345678900")
    assert result == True

def test_validacao_cpf_formatado():
    result = validar_cpf("123.456.789-00")
    assert result == True

def test_validacao_cpf_menos_11_digitos():
    result = validar_cpf("1234567890")
    assert result == False

def test_validacao_cpf_mais_11_digitos():
    result = validar_cpf("123456789000")
    assert result == False

def test_validacao_cpf_caracteres_invalidos():
    result = validar_cpf("1234567890a")
    assert result == False

def test_validacao_cpf_vazio():
    result = validar_cpf("")
    assert result == False