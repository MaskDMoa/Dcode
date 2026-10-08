# Dcode

Ferramenta experimental de desktop para testar codificações e cifras clássicas.

## Testar no Windows

Baixe `Dcode.exe` na página [Releases](https://github.com/MaskDMoa/Dcode/releases)
e execute-o. O executável é portátil; não é um instalador e não exige Python.

## Gerar o executável a partir do código

Com Python instalado, instale as dependências de build e execute o script no
PowerShell:

```powershell
python -m pip install -r requirements-build.txt
.\build.ps1
```

O arquivo será criado em `dist\Dcode.exe`. Ao enviar uma tag no formato `v*`,
o GitHub Actions compila o aplicativo para Windows e publica o executável em
uma Release.

Base64 é uma codificação, não criptografia. Vigenère é uma cifra clássica para
fins didáticos; não use este aplicativo para proteger dados sensíveis.
