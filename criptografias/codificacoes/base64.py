from __future__ import annotations

import base64
import binascii


STANDARD = "Standard (RFC 4648)"
URL_SAFE = "URL safe (RFC 4648 §5)"
FILENAME_SAFE = "Filename safe"

ALFABETOS: dict[str, tuple[str, str]] = {
    STANDARD: (
        "Alfabeto padrao: letras, numeros, + e /.",
        "+/8=",
    ),
    URL_SAFE: (
        "Variante segura para URLs: substitui + por - e / por _.",
        "-_8=",
    ),
    FILENAME_SAFE: (
        "Variante segura para nomes de arquivo: substitui / por - e mantem +.",
        "+-8=",
    ),
}

_TRADUCOES_CODIFICACAO = {
    STANDARD: None,
    URL_SAFE: bytes.maketrans(b"+/", b"-_"),
    FILENAME_SAFE: bytes.maketrans(b"/", b"-"),
}

_TRADUCOES_DECODIFICACAO = {
    STANDARD: None,
    URL_SAFE: bytes.maketrans(b"-_", b"+/"),
    FILENAME_SAFE: bytes.maketrans(b"-", b"/"),
}


def _validar_alfabeto(alfabeto: str) -> None:
    if alfabeto not in ALFABETOS:
        raise ValueError(f"Alfabeto Base64 desconhecido: {alfabeto}")


def codificar_bytes(dados: bytes, alfabeto: str) -> str:
    _validar_alfabeto(alfabeto)
    codificado = base64.b64encode(dados)
    traducao = _TRADUCOES_CODIFICACAO[alfabeto]
    if traducao is not None:
        codificado = codificado.translate(traducao)
    return codificado.decode("ascii")


def decodificar_bytes(texto: str, alfabeto: str) -> bytes:
    _validar_alfabeto(alfabeto)
    try:
        dados = texto.encode("ascii")
    except UnicodeEncodeError as erro:
        raise ValueError("O texto Base64 deve conter apenas caracteres ASCII.") from erro

    traducao = _TRADUCOES_DECODIFICACAO[alfabeto]
    if traducao is not None:
        dados = dados.translate(traducao)

    try:
        return base64.b64decode(dados, validate=True)
    except binascii.Error as erro:
        raise ValueError("Texto Base64 inválido para o alfabeto selecionado.") from erro


def codificar(texto: str, alfabeto: str) -> str:
    return codificar_bytes(texto.encode("utf-8"), alfabeto)


def decodificar(texto: str, alfabeto: str) -> str:
    try:
        return decodificar_bytes(texto, alfabeto).decode("utf-8")
    except UnicodeDecodeError as erro:
        raise ValueError("O Base64 decodificado não representa texto UTF-8 válido.") from erro
