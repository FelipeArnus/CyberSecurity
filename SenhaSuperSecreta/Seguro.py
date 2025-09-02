
import os

def conectar_banco():
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASSWORD")

    if not usuario or not senha:
        print("Erro: credenciais não encontrados nas variaveis de ambiente. ")
        return
    
    print(f"Conectando ao banco com usuario '{usuario} e {senha}'")

conectar_banco()