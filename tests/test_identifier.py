from identifier import __version__
from identifier.validators import is_valid_identifier


def test_version():
    assert __version__ == '0.1.0'


def test_identifier_with_valid_first_character():
    assert is_valid_identifier('aa')


def test_identifier_with_invalid_first_character():
    assert not is_valid_identifier('12aa')


def test_characters_validation():
    assert not is_valid_identifier('a&&$')
    assert is_valid_identifier('abc12')


def test_length_validation():
    assert not is_valid_identifier('')
    assert not is_valid_identifier('abcd1234')
    assert is_valid_identifier('ab12')
