<div align="center">

# Dcode

**Ferramenta experimental de desktop para testar codificações e cifras clássicas.**

[![Release](https://img.shields.io/github/v/release/MaskDMoa/Dcode?style=for-the-badge&logo=github&color=2ea44f)](https://github.com/MaskDMoa/Dcode/releases)
[![Downloads](https://img.shields.io/github/downloads/MaskDMoa/Dcode/total?style=for-the-badge&logo=github&color=0078d4)](https://github.com/MaskDMoa/Dcode/releases)
[![Plataforma](https://img.shields.io/badge/plataforma-Windows-0078d4?style=for-the-badge&logo=windows&logoColor=white)](#testar-no-windows)
[![Python](https://img.shields.io/badge/python-3.x-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

[![Build](https://img.shields.io/github/actions/workflow/status/MaskDMoa/Dcode/build.yml?style=flat-square&logo=githubactions&logoColor=white&label=build)](https://github.com/MaskDMoa/Dcode/actions)
[![Último commit](https://img.shields.io/github/last-commit/MaskDMoa/Dcode?style=flat-square&logo=git&logoColor=white)](https://github.com/MaskDMoa/Dcode/commits)
[![Issues](https://img.shields.io/github/issues/MaskDMoa/Dcode?style=flat-square&logo=github&logoColor=white)](https://github.com/MaskDMoa/Dcode/issues)
[![Stars](https://img.shields.io/github/stars/MaskDMoa/Dcode?style=flat-square&logo=github&logoColor=white)](https://github.com/MaskDMoa/Dcode/stargazers)

<a href="https://github.com/MaskDMoa/Dcode/releases"><img src="https://api.iconify.design/lucide:download.svg?color=%230078d4" width="16" height="16" align="top"> Baixar</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="#gerar-o-executavel"><img src="https://api.iconify.design/lucide:hammer.svg?color=%230078d4" width="16" height="16" align="top"> Compilar</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="https://github.com/MaskDMoa/Dcode/issues"><img src="https://api.iconify.design/lucide:bug.svg?color=%230078d4" width="16" height="16" align="top"> Reportar bug</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="#contribuindo"><img src="https://api.iconify.design/lucide:handshake.svg?color=%230078d4" width="16" height="16" align="top"> Contribuir</a>

</div>

---

<a id="sumario"></a>
## <img src="https://api.iconify.design/lucide:list.svg?color=%230078d4" width="26" height="26" align="top"> Sumário

- [Sobre](#sobre)
- [Recursos](#recursos)
- [Prévia](#previa)
- [Testar no Windows](#testar-no-windows)
- [Gerar o executável a partir do código](#gerar-o-executavel)
- [Releases automáticas](#releases-automaticas)
- [Aviso de segurança](#aviso-de-seguranca)
- [Contribuindo](#contribuindo)
- [Licença](#licenca)
- [Autor](#autor)

---

<a id="sobre"></a>
## <img src="https://api.iconify.design/lucide:info.svg?color=%230078d4" width="26" height="26" align="top"> Sobre

O **Dcode** é um aplicativo de desktop criado para **experimentar, estudar e
entender** codificações e cifras clássicas de forma prática, direto no
computador, sem depender de sites de terceiros.

É um projeto **experimental e didático**: ótimo para aprender como cada
técnica transforma um texto, mas **não** para proteger dados reais.

<a id="recursos"></a>
## <img src="https://api.iconify.design/lucide:sparkles.svg?color=%230078d4" width="26" height="26" align="top"> Recursos

- <img src="https://api.iconify.design/lucide:monitor.svg?color=%230078d4" width="16" height="16" align="top"> **Aplicativo desktop** com interface gráfica
- <img src="https://api.iconify.design/lucide:package.svg?color=%230078d4" width="16" height="16" align="top"> **Executável portátil** para Windows: sem instalador e sem Python
- <img src="https://api.iconify.design/lucide:binary.svg?color=%230078d4" width="16" height="16" align="top"> **Base64**: codificação e decodificação de texto
- <img src="https://api.iconify.design/lucide:key-round.svg?color=%230078d4" width="16" height="16" align="top"> **Vigenère**: cifra clássica com chave
- <img src="https://api.iconify.design/lucide:workflow.svg?color=%230078d4" width="16" height="16" align="top"> **Build automatizado** com GitHub Actions a cada nova tag

<a id="previa"></a>
## <img src="https://api.iconify.design/lucide:image.svg?color=%230078d4" width="26" height="26" align="top"> Prévia

> Adicione aqui uma captura de tela do aplicativo.
> Salve a imagem em `docs/screenshot.png` e troque este bloco por:
>
> ```markdown
> ![Dcode em execução](docs/screenshot.png)
> ```

<a id="testar-no-windows"></a>
## <img src="https://api.iconify.design/lucide:app-window.svg?color=%230078d4" width="26" height="26" align="top"> Testar no Windows

1. Acesse a página de [**Releases**](https://github.com/MaskDMoa/Dcode/releases).
2. Baixe o arquivo **`Dcode.exe`** da versão mais recente.
3. Dê dois cliques para executar.

> [!NOTE]
> O executável é **portátil**: não é um instalador e **não exige Python**.
> Se o Windows SmartScreen exibir um alerta, clique em **Mais informações →
> Executar assim mesmo** (o executável não é assinado digitalmente).

<a id="gerar-o-executavel"></a><a id="gerar-o-executavel-a-partir-do-codigo"></a>
## <img src="https://api.iconify.design/lucide:hammer.svg?color=%230078d4" width="26" height="26" align="top"> Gerar o executável a partir do código

### Pré-requisitos

- Windows com **PowerShell**
- **Python 3** instalado e disponível no `PATH`
- **Git** (para clonar o repositório)

### Passo a passo

```powershell
# 1. Clone o repositório
git clone https://github.com/MaskDMoa/Dcode.git
cd Dcode

# 2. Instale as dependências de build
python -m pip install -r requirements-build.txt

# 3. Gere o executável
.\build.ps1
```

O arquivo será criado em **`dist\Dcode.exe`**.

<a id="releases-automaticas"></a>
## <img src="https://api.iconify.design/lucide:rocket.svg?color=%230078d4" width="26" height="26" align="top"> Releases automáticas

Ao enviar uma tag no formato `v*`, o **GitHub Actions** compila o aplicativo
para Windows e publica o executável em uma Release automaticamente.

```bash
git tag v1.0.0
git push origin v1.0.0
```

```mermaid
flowchart LR
    A[git tag v*] --> B[git push]
    B --> C[GitHub Actions]
    C --> D[Build no Windows]
    D --> E[Dcode.exe na Release]
```

<a id="aviso-de-seguranca"></a>
## <img src="https://api.iconify.design/lucide:triangle-alert.svg?color=%23d29922" width="26" height="26" align="top"> Aviso de segurança

> [!WARNING]
> - **Base64 é uma codificação, não criptografia.** Qualquer pessoa consegue
>   reverter o texto sem chave alguma.
> - **Vigenère é uma cifra clássica para fins didáticos.** Ela é facilmente
>   quebrada por criptoanálise moderna.
> - **Não use este aplicativo para proteger dados sensíveis**, como senhas,
>   documentos ou informações pessoais.

<a id="contribuindo"></a>
## <img src="https://api.iconify.design/lucide:handshake.svg?color=%230078d4" width="26" height="26" align="top"> Contribuindo

Contribuições são muito bem-vindas!

1. Faça um **fork** do projeto
2. Crie uma branch: `git checkout -b feature/minha-ideia`
3. Faça o commit: `git commit -m "feat: adiciona minha ideia"`
4. Envie para o seu fork: `git push origin feature/minha-ideia`
5. Abra um **Pull Request**

Encontrou um problema ou tem uma sugestão? Abra uma
[issue](https://github.com/MaskDMoa/Dcode/issues).

<a id="licenca"></a>
## <img src="https://api.iconify.design/lucide:scale.svg?color=%230078d4" width="26" height="26" align="top"> Licença

Este projeto ainda não define uma licença. Para permitir uso e contribuições
de outras pessoas, adicione um arquivo `LICENSE` (por exemplo, MIT) à raiz
do repositório e atualize esta seção.

<a id="autor"></a>
## <img src="https://api.iconify.design/lucide:user.svg?color=%230078d4" width="26" height="26" align="top"> Autor

Feito por **[MaskDMoa](https://github.com/MaskDMoa)**.

<div align="center">

<img src="https://api.iconify.design/lucide:star.svg?color=%23d29922" width="16" height="16" align="top"> Se o projeto te ajudou, deixe uma estrela no repositório.

</div>
