# Exercicio 2

def inverter_palavras(texto):
    if not texto:
        return ""
    
    palavras = texto.split()
    palavras_invertidas = palavras[::-1]
    frase_invertida = " ".join(palavras_invertidas)
    
    return frase_invertida