import re
from validate_docbr import CPF

def cpf_invalido(cpf):
    cpf = CPF()
    return not cpf.validate(cpf)

def celular_invalido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return not resposta

def nome_invalido(nome):
    return not nome.isalpha()
