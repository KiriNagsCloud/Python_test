from funcoes import verifica_email, validar_senha, calcular_media, verificar_maior_idade, eh_positivo, status_aluno

def test_verifica_email():
    assert verifica_email('teste@gmail.com') == 'email válido'
    assert verifica_email('teste.com') == 'email incorreto'

def test_validar_senha():
    assert validar_senha('Senha123@') == 'senha válida'
    assert validar_senha('senha') == 'senha não contém elementos obrigatórios'

def test_calcular_media():
    assert calcular_media([10, 20, 30]) == 20
    assert calcular_media([]) == 0

def test_verificar_maior_idade():
    assert verificar_maior_idade(20) is True
    assert verificar_maior_idade(10) is False

def test_eh_positivo():
    assert eh_positivo(5) == 'positivo'
    assert eh_positivo(-1) == 'negativo'

def test_status_aluno():
    assert status_aluno(2.9) == 'Reprovado'
    assert status_aluno(5) == 'Recuperação'
    assert status_aluno(8) == 'Aprovado'

