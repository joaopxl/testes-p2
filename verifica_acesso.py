# Exercicio 5 - verificar acesso com mock

usuarios_com_permissao = ["admin"]


def verificar_permissao(usuario):
    return usuario in usuarios_com_permissao


def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return "Acesso autorizado"

    return "Acesso negado"
