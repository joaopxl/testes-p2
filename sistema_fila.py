# Exercicio 6 - sistema de fila de atendimento

fila_clientes = []

def obter_proximo_cliente():
    if not fila_clientes:
        return None
    return fila_clientes[0]


def registrar_atendimento(cliente):
    return True


def atender_proximo_cliente():
    cliente = obter_proximo_cliente()
    if cliente is None:
        return "Fila vazia"

    if registrar_atendimento(cliente):
        if fila_clientes and fila_clientes[0] == cliente:
            fila_clientes.pop(0)
        return "Atendimento realizado"

    return "Falha no atendimento"
