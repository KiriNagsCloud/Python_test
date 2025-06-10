# Condições (if/else) def = chamar função 'function'
def eh_par(numero):
    if numero % 2 == 0:
        return 'é par'
    else:
        return 'é impar'

def somar (a,b):
        return a + b

def subtrair(a,b):
    return a - b

def test_verifica_se_numero_par():
        assert eh_par(2) == 'é par'
        assert eh_par(3) == 'é impar'
        
def test_verifica_soma_e_subtrair():
    assert somar(5, 6) == 11
    assert subtrair(10, 8) == 2