"""
Lista 5


Definição de um identificador:

- Um identificador válido deve começar com uma letra e conter apenas letras ou dı́gitos.
    Além disso, deve ter no mı́nimo um e no máximo seis caracteres de comprimento
"""
import re


def is_valid_identifier(string: str) -> bool:
    return is_valid_size(string) and is_valid_format(string)


def is_valid_format(string: str):
    if not string[0].isalpha():
        return False
    return re.match(r"^[\w\d]+$", string)


def is_valid_size(string: str):
    return 0 < len(string) < 7
