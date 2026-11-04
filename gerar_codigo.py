# Exercicio 4 - gerar codigo com mock

import random


def gerar_codigo():
    numero = random.randint(1000, 9999)
    return f"USR-{numero}"


def criar_identificacao(nome):
    codigo = gerar_codigo()
    return f"Usuário {nome} cadastrado com código {codigo}."
