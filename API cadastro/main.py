from fastapi import FastAPI
from chekout import Cliente
from conectar_json import salvar_usuario, carregar_usuarios
from pydantic import BaseModel, EmailStr
import uuid


app = FastAPI()

class formato(BaseModel):
    nome: str
    email: EmailStr
    senha: str


###########################################################################################
#GET - ME MOSTRA OS DADOS DO USUÁRIO

@app.get("/analise")
def mostrar(chave):
    usuarios = carregar_usuarios()
    categoria_selecionada = usuarios.get(chave)
    if categoria_selecionada:
        return categoria_selecionada
    else:
        return {"erro": "Cliente não encontrado com essa chave"}


###########################################################################################
#POST -  CRIA PARA MIM DADOS NOVOS

@app.post("/analise")   
def criar (criando:formato):
    chave = str(uuid.uuid4())[:4].upper()
    openjson = carregar_usuarios() 
        #para fazer o put use essa chave nova a baixo, 
        # o mesmo conceito do for, mas mude para o mesmo nome da 
        # chave ao inves de criar uma nova
    for chave_nova, dados in openjson.items():
            if dados["nome"] == criando.nome:
                return("Esse usuário já existe.")
    
    salvar_usuario(chave, criando.nome, criando.email, criando.senha) 

    return(f"Usuário registrado com sucesso! Acabamos de gerar sua chave de entrada")


###########################################################################################
#PUT - EDITA OS DADOS (UPDATE)

def buscar(buscando:formato):

    chave = str(uuid.uuid4())[:4].upper()
    openjson = carregar_usuarios() 
    for chave in openjson.items():
        return
    # for chave, dados in openjson.items():
    #         if dados["nome"] == buscando.nome:
    #             return("Esse usuário já existe.")
    
    # salvar_usuario(chave, buscando.nome, buscando.email, buscando.senha) 

    # return("Usuário registrado com sucesso! Acabamos de gerar sua chave de entrada")


@app.put("/usuarios/{chave}")
def editar(chave, buscando:formato):
    usuarios = carregar_usuarios()
    categoria_selecionada = usuarios.get(chave)
    if categoria_selecionada:
        buscar(buscando)
        salvar_usuario(chave, buscando.nome, buscando.email, buscando.senha) 
        return "Os dados do usuário foram editados!"
    else:
        return {"erro: Cliente não encontrado com essa chave"}



###########################################################################################
#DELETE - PARA APAGAR OS DADOS ESPECIFICOS

         

    
    




# while True:
#     inicial = input("L=Login, C=Cadastrar, E=Sair: ").upper()
    
#     if inicial == "L":
#         nome = input("Digite seu primeiro nome: ")
#         email = ""
#         senha = input("Digite sua senha: ")
#         criando = Cliente(nome, email, senha)
#         criando.logando()
#     elif inicial == "C":
#         nome = input("Digite seu primeiro nome: ")
#         email = input("Digite seu email: ")
#         senha = input("Digite sua senha: ")
#         criando = Cliente(nome, email, senha)
#         criando.cadastrando()
#     elif inicial == "E":
#         break
#     else:
#         print("Erro, tente novamente")    