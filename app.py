from __future__ import annotations

import customtkinter as ctk

from criptografias.codificacoes.base64 import (
    ALFABETOS,
    decodificar,
    codificar,
)
from criptografias.cifras.vigenere import descriptografar, criptografar


ASCII_ART = r"""
  ____ ____  __ ____  _____ __  __
 / ___|  _ \|  |  _ \| ____|  \/  |
| |   | |_) |  | |_) |  _| | |\/| |
| |___|  _ <|__|  __/| |___| |  | |
 \____|_| \_\  |_|   |_____|_|  |_|
"""

FUNDO = "#000000"
SUPERFICIE = "#0b0b0b"
BORDA = "#292929"
TEXTO = "#eeeeee"
TEXTO_SECUNDARIO = "#929292"
DESTAQUE = "#42d6c5"


class AplicativoCriptografia(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Ferramenta de Criptografia")
        self.geometry("1020x680")
        self.minsize(780, 540)
        self.configure(fg_color=FUNDO)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.alfabeto_atual = next(iter(ALFABETOS))
        self.algoritmo_atual = "Base64"
        self.itens_algoritmo: dict[str, ctk.CTkButton] = {}
        self.estado: ctk.CTkLabel | None = None
        self.executar: ctk.CTkButton | None = None
        self.chave_vigenere: ctk.CTkEntry | None = None
        self.menu_alfabeto: ctk.CTkOptionMenu | None = None
        self.ajuda_texto: ctk.CTkLabel | None = None

        self._criar_cabecalho()
        self._criar_area_de_trabalho()

    def _criar_cabecalho(self) -> None:
        cabecalho = ctk.CTkFrame(self, fg_color=FUNDO, corner_radius=0)
        cabecalho.grid(row=0, column=0, padx=20, pady=(14, 10), sticky="ew")
        cabecalho.grid_columnconfigure(1, weight=1)

        arte = ctk.CTkLabel(
            cabecalho,
            text=ASCII_ART,
            font=("Consolas", 10, "bold"),
            text_color=DESTAQUE,
            justify="left",
        )
        arte.grid(row=0, column=0, rowspan=2, padx=(0, 16), sticky="w")

        titulo = ctk.CTkLabel(
            cabecalho,
            text="FERRAMENTA DE CRIPTOGRAFIA",
            font=("Segoe UI", 19, "bold"),
            text_color=TEXTO,
            anchor="w",
        )
        titulo.grid(row=0, column=1, sticky="sw")

        subtitulo = ctk.CTkLabel(
            cabecalho,
            text="ESPAÇO DE TRABALHO",
            font=("Segoe UI", 11),
            text_color=TEXTO_SECUNDARIO,
            anchor="w",
        )
        subtitulo.grid(row=1, column=1, pady=(3, 0), sticky="nw")

    def _criar_area_de_trabalho(self) -> None:
        area = ctk.CTkFrame(self, fg_color=FUNDO, corner_radius=0)
        area.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        area.grid_columnconfigure(0, weight=0, minsize=235)
        area.grid_columnconfigure(1, weight=1)
        area.grid_rowconfigure(0, weight=1)

        self._criar_painel_algoritmos(area)
        self.paineis_direita = ctk.CTkTabview(
            area,
            corner_radius=4,
            segmented_button_selected_color="#176b63",
            segmented_button_selected_hover_color="#20877c",
            segmented_button_unselected_color=SUPERFICIE,
            segmented_button_unselected_hover_color="#1d1d1d",
        )
        self.paineis_direita.grid(row=0, column=1, sticky="nsew")
        bancada = self.paineis_direita.add("Bancada")
        ajuda = self.paineis_direita.add("Ajuda")
        self._criar_painel_texto(bancada)
        self._criar_painel_ajuda(ajuda)

    def _criar_painel_algoritmos(self, area: ctk.CTkFrame) -> None:
        painel = ctk.CTkFrame(
            area,
            fg_color=SUPERFICIE,
            corner_radius=4,
            border_width=1,
            border_color=BORDA,
        )
        painel.grid(row=0, column=0, padx=(0, 10), sticky="nsew")
        painel.grid_columnconfigure(0, weight=1)
        painel.grid_rowconfigure(2, weight=1)

        titulo = ctk.CTkLabel(
            painel,
            text="CRIPTOGRAFIAS",
            font=("Segoe UI", 13, "bold"),
            text_color=TEXTO,
            anchor="w",
        )
        titulo.grid(row=0, column=0, padx=14, pady=(16, 4), sticky="ew")

        descricao = ctk.CTkLabel(
            painel,
            text="Selecione um algoritmo",
            font=("Segoe UI", 11),
            text_color=TEXTO_SECUNDARIO,
            anchor="w",
        )
        descricao.grid(row=1, column=0, padx=14, pady=(0, 12), sticky="ew")

        lista = ctk.CTkScrollableFrame(
            painel,
            fg_color="transparent",
            corner_radius=4,
            scrollbar_button_color="#363636",
            scrollbar_button_hover_color="#505050",
        )
        lista.grid(row=2, column=0, padx=8, pady=(0, 8), sticky="nsew")
        lista.grid_columnconfigure(0, weight=1)

        for indice, nome in enumerate(("Base64", "Vigenère")):
            item = ctk.CTkButton(
                lista,
                text=nome,
                height=36,
                anchor="w",
                font=("Segoe UI", 12, "bold"),
                text_color=TEXTO,
                fg_color="#176b63" if nome == self.algoritmo_atual else SUPERFICIE,
                hover_color="#20877c",
                corner_radius=4,
                command=lambda algoritmo=nome: self._selecionar_algoritmo(algoritmo),
            )
            item.grid(row=indice, column=0, padx=4, pady=4, sticky="ew")
            self.itens_algoritmo[nome] = item

        ajuda = ctk.CTkButton(
            painel,
            text="?  Ajuda do algoritmo",
            height=32,
            anchor="w",
            font=("Segoe UI", 11),
            text_color=TEXTO_SECUNDARIO,
            fg_color="transparent",
            hover_color="#1d1d1d",
            corner_radius=4,
            command=self._mostrar_ajuda,
        )
        ajuda.grid(row=3, column=0, padx=12, pady=(0, 12), sticky="ew")


    def _criar_painel_texto(self, area: ctk.CTkFrame) -> None:
        painel = ctk.CTkFrame(
            area,
            fg_color=FUNDO,
            corner_radius=0,
        )
        painel.grid(row=0, column=1, sticky="nsew")
        painel.grid_columnconfigure(0, weight=1)
        painel.grid_rowconfigure(1, weight=1)
        painel.grid_rowconfigure(4, weight=1)

        entrada_titulo = ctk.CTkLabel(
            painel,
            text="ENTRADA",
            font=("Segoe UI", 12, "bold"),
            text_color=TEXTO,
            anchor="w",
        )
        entrada_titulo.grid(row=0, column=0, pady=(2, 8), sticky="w")

        copiar_entrada = ctk.CTkButton(
            painel,
            text="COPIAR",
            width=82,
            height=28,
            font=("Segoe UI", 10, "bold"),
            fg_color=SUPERFICIE,
            hover_color="#1d1d1d",
            corner_radius=4,
            command=self._copiar_entrada,
        )
        copiar_entrada.grid(row=0, column=0, pady=(0, 4), sticky="e")

        self.entrada = ctk.CTkTextbox(
            painel,
            corner_radius=4,
            border_width=1,
            border_color=BORDA,
            fg_color=SUPERFICIE,
            text_color=TEXTO,
            font=("Consolas", 13),
            wrap="word",
        )
        self.entrada.grid(row=1, column=0, sticky="nsew")

        acoes = ctk.CTkFrame(painel, fg_color="transparent", corner_radius=0)
        acoes.grid(row=2, column=0, pady=(12, 8), sticky="ew")
        acoes.grid_columnconfigure(1, weight=1)

        self.operacao = ctk.CTkSegmentedButton(
            acoes,
            values=["Criptografar", "Descriptografar"],
            selected_color="#176b63",
            selected_hover_color="#20877c",
            unselected_color=SUPERFICIE,
            unselected_hover_color="#1d1d1d",
            text_color=TEXTO,
            corner_radius=4,
        )
        self.operacao.set("Criptografar")

        self.menu_alfabeto = ctk.CTkOptionMenu(
            acoes,
            values=list(ALFABETOS),
            width=210,
            height=34,
            font=("Segoe UI", 11),
            fg_color=SUPERFICIE,
            button_color="#292929",
            button_hover_color="#404040",
            dropdown_fg_color=SUPERFICIE,
            dropdown_hover_color="#176b63",
            text_color=TEXTO,
            corner_radius=4,
            command=self._alterar_alfabeto,
        )
        self.menu_alfabeto.set(self.alfabeto_atual)
        self.menu_alfabeto.grid(row=0, column=1, padx=4, sticky="e")

        self.chave_vigenere = ctk.CTkEntry(
            acoes,
            width=210,
            height=34,
            placeholder_text="Chave (somente A-Z)",
            font=("Segoe UI", 11),
            fg_color=SUPERFICIE,
            border_color=BORDA,
            text_color=TEXTO,
            corner_radius=4,
        )
        self.chave_vigenere.grid(row=0, column=1, padx=4, sticky="e")
        self.chave_vigenere.grid_remove()

        ajuda_algoritmo = ctk.CTkButton(
            acoes,
            text="?",
            width=30,
            height=30,
            font=("Segoe UI", 12, "bold"),
            fg_color=SUPERFICIE,
            hover_color="#1d1d1d",
            corner_radius=4,
            command=self._mostrar_ajuda,
        )
        self.operacao.grid(row=0, column=0, padx=(0, 8), sticky="w")
        ajuda_algoritmo.grid(row=0, column=2, padx=(4, 8), sticky="e")

        self.executar = ctk.CTkButton(
            acoes,
            text="EXECUTAR",
            width=120,
            height=34,
            font=("Segoe UI", 12, "bold"),
            fg_color="#176b63",
            hover_color="#20877c",
            corner_radius=4,
            command=self._executar,
        )
        self.executar.grid(row=0, column=3, sticky="e")

        resultado_titulo = ctk.CTkLabel(
            painel,
            text="SAÍDA",
            font=("Segoe UI", 12, "bold"),
            text_color=TEXTO,
            anchor="w",
        )
        resultado_titulo.grid(row=3, column=0, pady=(0, 8), sticky="w")

        copiar_resultado = ctk.CTkButton(
            painel,
            text="COPIAR",
            width=82,
            height=28,
            font=("Segoe UI", 10, "bold"),
            fg_color=SUPERFICIE,
            hover_color="#1d1d1d",
            corner_radius=4,
            command=self._copiar_resultado,
        )
        copiar_resultado.grid(row=3, column=0, pady=(0, 4), sticky="e")

        self.resultado = ctk.CTkTextbox(
            painel,
            corner_radius=4,
            border_width=1,
            border_color=BORDA,
            fg_color=SUPERFICIE,
            text_color=TEXTO,
            font=("Consolas", 13),
            wrap="word",
            state="disabled",
        )
        self.resultado.grid(row=4, column=0, sticky="nsew")

        self.estado = ctk.CTkLabel(
            painel,
            text="Base64 selecionado. Escolha o alfabeto e informe um texto.",
            font=("Segoe UI", 10),
            text_color=TEXTO_SECUNDARIO,
            anchor="w",
        )
        self.estado.grid(row=5, column=0, pady=(8, 0), sticky="ew")

    def _criar_painel_ajuda(self, painel: ctk.CTkFrame) -> None:
        painel.grid_columnconfigure(0, weight=1)
        painel.grid_rowconfigure(1, weight=1)

        titulo = ctk.CTkLabel(
            painel,
            text="SOBRE O ALGORITMO",
            font=("Segoe UI", 15, "bold"),
            text_color=TEXTO,
            anchor="w",
        )
        titulo.grid(row=0, column=0, padx=14, pady=(12, 8), sticky="ew")

        conteudo = ctk.CTkScrollableFrame(
            painel,
            fg_color=SUPERFICIE,
            corner_radius=4,
            border_width=1,
            border_color=BORDA,
        )
        conteudo.grid(row=1, column=0, padx=8, pady=(0, 8), sticky="nsew")
        conteudo.grid_columnconfigure(0, weight=1)

        self.ajuda_texto = ctk.CTkLabel(
            conteudo,
            text=self._texto_ajuda(),
            font=("Segoe UI", 12),
            text_color=TEXTO,
            justify="left",
            anchor="nw",
            wraplength=600,
        )
        self.ajuda_texto.grid(row=0, column=0, padx=14, pady=14, sticky="nw")

        voltar = ctk.CTkButton(
            painel,
            text="VOLTAR À BANCADA",
            height=34,
            font=("Segoe UI", 11, "bold"),
            fg_color="#176b63",
            hover_color="#20877c",
            corner_radius=4,
            command=lambda: self.paineis_direita.set("Bancada"),
        )
        voltar.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="ew")

    def _texto_ajuda(self) -> str:
        if self.algoritmo_atual == "Vigenère":
            return (
                "VIGENÈRE\n\n"
                "Cifra clássica que desloca cada letra de acordo com uma palavra-chave. "
                "A chave se repete ao longo do texto. Não é segura para proteger "
                "informações atuais.\n\n"
                "A implementação transforma apenas letras A-Z; espaços, números, "
                "pontuação e outros caracteres são preservados e não consomem a chave. "
                "A caixa diferencia maiúsculas e minúsculas. A chave aceita somente "
                "letras ASCII de A a Z.\n\n"
                "Exemplo:\n"
                "Texto: ATTACKATDAWN\n"
                "Chave: LEMON\n"
                "Criptografado: LXFOPVEFRNHR\n"
                "Descriptografado: ATTACKATDAWN"
            )

        exemplos = "\n".join(
            f"{nome}: {exemplo}" for nome, (_, exemplo) in ALFABETOS.items()
        )
        return (
            "BASE64\n\n"
            "Base64 transforma bytes em texto usando caracteres de um alfabeto. "
            "É uma codificação, não criptografia: não protege o conteúdo com uma chave.\n\n"
            "As variantes representam os mesmos bytes FB FF; apenas alguns caracteres "
            "do alfabeto mudam. O sinal = é o preenchimento (padding). Na bancada, "
            "o texto é convertido para bytes UTF-8 antes da codificação.\n\n"
            f"{exemplos}"
        )

    def _selecionar_algoritmo(self, algoritmo: str) -> None:
        self.algoritmo_atual = algoritmo
        for nome, item in self.itens_algoritmo.items():
            item.configure(fg_color="#176b63" if nome == algoritmo else SUPERFICIE)

        if self.menu_alfabeto is None or self.chave_vigenere is None:
            return

        if algoritmo == "Base64":
            self.chave_vigenere.grid_remove()
            self.menu_alfabeto.grid()
            mensagem = "Base64 selecionado. Escolha o alfabeto e informe um texto."
        else:
            self.menu_alfabeto.grid_remove()
            self.chave_vigenere.grid()
            mensagem = "Vigenère selecionada. Informe uma chave de letras A-Z."

        if self.estado is not None:
            self.estado.configure(text=mensagem, text_color=TEXTO_SECUNDARIO)
        if self.ajuda_texto is not None:
            self.ajuda_texto.configure(text=self._texto_ajuda())

    def _alterar_alfabeto(self, valor: str) -> None:
        self.alfabeto_atual = valor
        if self.ajuda_texto is not None and self.algoritmo_atual == "Base64":
            self.ajuda_texto.configure(text=self._texto_ajuda())

    def _mostrar_ajuda(self) -> None:
        if self.ajuda_texto is None:
            return
        self.ajuda_texto.configure(text=self._texto_ajuda())
        self.paineis_direita.set("Ajuda")

    def _executar(self) -> None:
        texto = self.entrada.get("1.0", "end-1c")
        try:
            criptografar_operacao = self.operacao.get() == "Criptografar"
            if self.algoritmo_atual == "Base64":
                if criptografar_operacao:
                    resultado = codificar(texto, self.alfabeto_atual)
                else:
                    resultado = decodificar(texto, self.alfabeto_atual)
            else:
                chave = self.chave_vigenere.get() if self.chave_vigenere else ""
                if criptografar_operacao:
                    resultado = criptografar(texto, chave)
                else:
                    resultado = descriptografar(texto, chave)
        except ValueError as erro:
            self._definir_resultado("")
            if self.estado is not None:
                self.estado.configure(text=str(erro), text_color="#ff7777")
            return

        self._definir_resultado(resultado)
        if self.estado is not None:
            self.estado.configure(
                text="Operação concluída.",
                text_color=DESTAQUE,
            )

    def _definir_resultado(self, texto: str) -> None:
        self.resultado.configure(state="normal")
        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", texto)
        self.resultado.configure(state="disabled")

    def _copiar_entrada(self) -> None:
        self._copiar_texto(self.entrada.get("1.0", "end-1c"), "Entrada copiada.")

    def _copiar_resultado(self) -> None:
        self._copiar_texto(
            self.resultado.get("1.0", "end-1c"),
            "Saída copiada.",
        )

    def _copiar_texto(self, texto: str, mensagem: str) -> None:
        self.clipboard_clear()
        self.clipboard_append(texto)
        if self.estado is not None:
            self.estado.configure(text=mensagem, text_color=DESTAQUE)


def main() -> None:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = AplicativoCriptografia()
    app.mainloop()


if __name__ == "__main__":
    main()
