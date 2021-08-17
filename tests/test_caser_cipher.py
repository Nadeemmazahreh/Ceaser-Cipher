from caser_cipher import __version__
from caser_cipher.caser_cipher import encrypt, decrypt, crack


def test_version():
    assert __version__ == '0.1.0'

def test_encryption():
    actual = encrypt('abc',1)
    assert actual == 'bcd'

