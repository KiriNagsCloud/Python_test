def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'email válido'
    else:
        return 'email incorreto'


def validar_senha(senha):
    caractere = '@#$%&'
    if len(senha) > 8 and \
       any(c.isdigit() for c in senha) and \
       any(c.isupper() for c in senha) and \
       any(c in caractere for c in senha):
        return 'senha válida'
    else:
        return 'senha não contém elementos obrigatórios'


def tamanho_string(nome):
    tamanho = len(nome)
    return tamanho


def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    total = 0
    for num in lista_numeros:
        total += num
    media = total / len(lista_numeros)
    return media


def verificar_maior_idade(idade):
    if idade >= 18:
        return True
    else:
        return False
    
def eh_positivo(num):
    if num >= 0:
        return 'positivo'
    else:
        return 'negativo'

def status_aluno(nota):
    if nota < 3:
        return 'Reprovado'
    elif nota < 7:
        return 'Recuperação'
    else:
        return 'Aprovado'
        
