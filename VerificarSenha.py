import mysql.connector
from hashlib import sha256
from decouple import config

# Função para verificar a senha
def verificar_senha(username, senha):
    try:
        # Conectar ao banco de dados
        mydb = mysql.connector.connect(
            host=config("Host"),
            user=config("User"),
            password=config("Password"),
            database=config("Database")
        )

        # Criar cursor
        mycursor = mydb.cursor()

        # Consulta SQL para obter a senha do usuário
        sql = "SELECT Senha FROM Usuarios WHERE Usuario = %s;"

        # Executar a consulta
        mycursor.execute(sql, (username,))

        # Obter o resultado da consulta
        resultado = mycursor.fetchone()

        if resultado:  # Se o usuário existe
            senha_hash = resultado[0]  # Senha hash armazenada no banco de dados
            # Aqui você deve usar um algoritmo de hash seguro, como bcrypt
            # para verificar a senha
            if senha == senha_hash:
                print("Senha correta.")
            else:
                print("Senha incorreta.")
        else:
            print("Usuário não encontrado.")

    except mysql.connector.Error as error:
        print("Erro ao conectar ao banco de dados:", error)
        
        
username = input("Digite seu Nome de Usuario: ")
senha = input("Digite sua Senha: ")

sha256_hash = sha256()

sha256_hash.update(senha.encode('utf-8'))

senha_inserida = sha256_hash.hexdigest()
print(senha_inserida)
verificar_senha(username, senha_inserida)