# Testes exercicio 4 - gerar codigo com mock 

from unittest.mock import Mock, patch
import gerar_codigo


def test_mensagem_gerada_corretamente():
    gerar = Mock(return_value="USR-1234")

    with patch.object(gerar_codigo, "gerar_codigo", gerar):
        resultado = gerar_codigo.criar_identificacao("Carlos")

    assert resultado == "Usuário Carlos cadastrado com código USR-1234."


def test_gerar_codigo_foi_chamada():
    gerar = Mock(return_value="USR-1234")

    with patch.object(gerar_codigo, "gerar_codigo", gerar):
        gerar_codigo.criar_identificacao("Carlos")

    gerar.assert_called()


def test_gerar_codigo_foi_chamada_uma_vez():
    gerar = Mock(return_value="USR-1234")

    with patch.object(gerar_codigo, "gerar_codigo", gerar):
        gerar_codigo.criar_identificacao("Carlos")

    gerar.assert_called_once()


def test_mock_simula_diferentes_codigos():
    gerar = Mock()

    with patch.object(gerar_codigo, "gerar_codigo", gerar):
        gerar.return_value = "USR-1111"
        assert gerar_codigo.criar_identificacao("Carlos") == "Usuário Carlos cadastrado com código USR-1111."

        gerar.return_value = "USR-9999"
        assert gerar_codigo.criar_identificacao("Ana") == "Usuário Ana cadastrado com código USR-9999."


def test_comportamento_com_nomes_diferentes():
    gerar = Mock(return_value="USR-1234")

    with patch.object(gerar_codigo, "gerar_codigo", gerar):
        resultado_carlos = gerar_codigo.criar_identificacao("Carlos")
        resultado_ana = gerar_codigo.criar_identificacao("Ana")

    assert resultado_carlos == "Usuário Carlos cadastrado com código USR-1234."
    assert resultado_ana == "Usuário Ana cadastrado com código USR-1234."
