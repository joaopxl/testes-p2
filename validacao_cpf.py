# Exercicio 3 - validacao de cpf

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) == 11 and cpf.isdigit():
        return True
    else:
        return False