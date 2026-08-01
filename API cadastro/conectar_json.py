import os
import json

ARQUIVO = "armazenar.json"

def carregar_usuarios():

    if os.path.exists(ARQUIVO):

        # Abre o arquivo no modo leitura ("r")
        # encoding="utf-8" permite acentos e caracteres especiais
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo: #open é uma função nativa do python

            # Lê o conteúdo JSON do arquivo e converte para dicionário Python
            return json.load(arquivo) #load percente ao modulo json
    # Se o arquivo não existir, retorna dicionário vazio
    return {}

def salvar_usuario (chave_usuario, nome, email, senha):
    usuarios = carregar_usuarios()
    usuarios[chave_usuario] = {
        "nome": nome,
        "email": email,
        "senha": senha,
        }
    # Abre o arquivo no modo escrita ("w")
    # Se não existir, ele cria
    # Se existir, substitui o conteúdo antigo
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

        # Converte o dicionário Python para JSON e salva no arquivo
        # indent=4 organiza visualmente com espaçamento
        # ensure_ascii=False mantém acentos normais
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)