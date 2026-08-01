import hashlib
import uuid
import os
from conectar_json import salvar_usuario, carregar_usuarios

class Cliente:
    def __init__(self, nome, email, senha):
        self.chave = str(uuid.uuid4())[:4].upper()
        self.nome = nome
        self.email = email
        # Já podemos salvar a senha criptografada se quiser, ou deixar para o método
        self.senha = self.criptografar(senha)

    def criptografar(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def cadastrando(self):
        openjson = carregar_usuarios() 
        
        for chave, dados in openjson.items():
            if dados["nome"] == self.nome:
                print("Esse usuário já existe.")
                return False # Para a função aqui mesmo se achar

        # Se o loop terminar e não der 'return False', significa que não existe
        salvar_usuario(self.chave, self.nome, self.email, self.senha)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Usuário registrado com sucesso!")
        print(f"Acabamos de gerar sua chave de entrada: {self.chave} \nGuarde o código para efetuar o login futuramente")
        return True


    def logando(self):
        openjson = carregar_usuarios()
        
        for chave, dados in openjson.items():
            if dados["nome"] == self.nome and dados["senha"] == self.senha:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Olá {self.nome}, bem vindo ao banco python!")
                return True
        else:
        # O print de erro fica FORA do loop. Se rodar o loop inteiro e não achar, cai aqui.
            print("Usuário inexistente.")
            return False