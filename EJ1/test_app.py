# test_crypto_app.py
import pytest
import hashlib
from app import (
    hash_sha256,
    verificar_password,
    base64_encode,
    base64_decode
)




def test_sha256_hash_correcto():
    texto = "hola"
    esperado = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    assert hash_sha256(texto) == esperado



def test_verificacion_password_correcta():
    password = "1234"
    hash_pw = hash_sha256(password)
    assert verificar_password(password, hash_pw) is True


def test_verificacion_password_incorrecta():
    hash_pw = hash_sha256("1234")
    assert verificar_password("12345", hash_pw) is False


def test_base64_encode():
    assert base64_encode("hola") == "aG9sYQ=="


def test_base64_decode():
    assert base64_decode("aG9sYQ==") == "hola"


def test_base64_encode_decode_integridad():
    texto = "Mensaje secreto 123!"
    assert base64_decode(base64_encode(texto)) == texto
