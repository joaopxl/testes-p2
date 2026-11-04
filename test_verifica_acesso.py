# Testes exercicio 5 - verificar acesso com mock

from unittest.mock import Mock, patch
import verifica_acesso


def test_usuario_com_permissao():
    verificar = Mock(return_value=True)

    with patch.object(verifica_acesso, "verificar_permissao", verificar):
        resultado = verifica_acesso.acessar_sistema("admin")

    assert resultado == "Acesso autorizado"


def test_usuario_sem_permissao():
    verificar = Mock(return_value=False)

    with patch.object(verifica_acesso, "verificar_permissao", verificar):
        resultado = verifica_acesso.acessar_sistema("visitante")

    assert resultado == "Acesso negado"


def test_verificar_permissao_foi_chamada():
    verificar = Mock(return_value=True)

    with patch.object(verifica_acesso, "verificar_permissao", verificar):
        verifica_acesso.acessar_sistema("admin")

    verificar.assert_called_once()


def test_verificar_permissao_recebeu_usuario_correto():
    verificar = Mock(return_value=True)

    with patch.object(verifica_acesso, "verificar_permissao", verificar):
        verifica_acesso.acessar_sistema("admin")

    verificar.assert_called_once_with("admin")


def test_mock_simula_os_dois_cenarios():
    verificar = Mock()

    with patch.object(verifica_acesso, "verificar_permissao", verificar):
        verificar.return_value = True
        assert verifica_acesso.acessar_sistema("admin") == "Acesso autorizado"

        verificar.return_value = False
        assert verifica_acesso.acessar_sistema("visitante") == "Acesso negado"
