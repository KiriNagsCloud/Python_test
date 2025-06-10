def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'email valido'
    else:
        return 'email incorreto'


def validar_senha(senha):
    caracteres = '@#$%&'
    if len(senha) > 8 and \
       any(c.isdigit() for c in senha) and \
       any(c.isupper() for c in senha) and \
       any(c in caracteres for c in senha):
        return 'senha valida'
    else:
        return 'senha incorreta'


# Testes
def test_verifica_email():
    assert verifica_email('a@gmail.com') == 'email valido'
    assert verifica_email('b@gmail') == 'email incorreto'


def test_validar_senha():
    assert validar_senha('Abcdef123@') == 'senha valida'
    assert validar_senha('abc') == 'senha incorreta'
