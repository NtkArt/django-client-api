import re
from validate_docbr import CPF


def cpf_valido(numero_do_cpf):
    """
        Verifica se o cpf eh valido.
    """
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def nome_valido(nome):
    """
        Verifica se o nome eh valido.
    """
    return nome.isalpha()


def rg_valido(numero_do_rg):
    """
        Verifica se o rg eh valido.
    """
    return len(numero_do_rg) == 9


def celular_valido(numero_celular):
    """
        Verifica se o celular eh valido. (99 99999-9999)
    """
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, numero_celular)
    return response
