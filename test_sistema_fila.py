# Testes exercicio 6 - sistema de fila de atendimento

from unittest.mock import Mock, patch
import sistema_fila

def test_atendimento_realizado_com_sucesso():
    obter_cliente = Mock(return_value="Cliente1")
    registrar = Mock(return_value=True)

    with patch.object(sistema_fila, "obter_proximo_cliente", obter_cliente), patch.object(sistema_fila, "registrar_atendimento", registrar):
        resultado = sistema_fila.atender_proximo_cliente()
    assert resultado == "Atendimento realizado"

def test_fila_vazia():
    obter_cliente = Mock(return_value=None)

    with patch.object(sistema_fila, "obter_proximo_cliente", obter_cliente):
        resultado = sistema_fila.atender_proximo_cliente()
    assert resultado == "Fila vazia"

def test_falha_no_atendimento():
    obter_cliente = Mock(return_value="Cliente1")
    registrar = Mock(return_value=False)

    with patch.object(sistema_fila, "obter_proximo_cliente", obter_cliente), patch.object(sistema_fila, "registrar_atendimento", registrar):
        resultado = sistema_fila.atender_proximo_cliente()
    assert resultado == "Falha no atendimento"

def test_obter_proximo_cliente_foi_chamada():
    obter_cliente = Mock(return_value="Cliente1")

    with patch.object(sistema_fila, "obter_proximo_cliente", obter_cliente):
        sistema_fila.atender_proximo_cliente()
    obter_cliente.assert_called_once()

def test_registrar_atendimento_foi_chamada():
    obter_cliente = Mock(return_value="Cliente1")
    registrar = Mock(return_value=True)

    with patch.object(sistema_fila, "obter_proximo_cliente", obter_cliente), patch.object(sistema_fila, "registrar_atendimento", registrar):
        sistema_fila.atender_proximo_cliente()
    registrar.assert_called_once_with("Cliente1")

def test_registrar_atendimento_nao_foi_chamada_com_fila_vazia():
    obter_cliente = Mock(return_value=None)
    registrar = Mock()

    with patch.object(sistema_fila, "obter_proximo_cliente", obter_cliente), patch.object(sistema_fila, "registrar_atendimento", registrar):
        sistema_fila.atender_proximo_cliente()
    registrar.assert_not_called()