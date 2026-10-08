from __future__ import annotations


def _validar_chave(chave: str) -> str:
    chave = chave.upper()
    if not chave or not all("A" <= letra <= "Z" for letra in chave):
        raise ValueError("A chave deve conter apenas letras de A a Z.")
    return chave


def _transformar(texto: str, chave: str, deslocamento: int) -> str:
    chave_validada = _validar_chave(chave)
    resultado: list[str] = []
    indice_chave = 0

    for caractere in texto:
        if "A" <= caractere <= "Z":
            base = ord("A")
        elif "a" <= caractere <= "z":
            base = ord("a")
        else:
            resultado.append(caractere)
            continue

        valor_chave = ord(chave_validada[indice_chave % len(chave_validada)]) - ord("A")
        valor_texto = ord(caractere) - base
        resultado.append(chr((valor_texto + deslocamento * valor_chave) % 26 + base))
        indice_chave += 1

    return "".join(resultado)


def criptografar(texto: str, chave: str) -> str:
    return _transformar(texto, chave, 1)


def descriptografar(texto: str, chave: str) -> str:
    return _transformar(texto, chave, -1)
