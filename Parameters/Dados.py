import mysql.connector
from decouple import config
from hashlib import sha256

Usuario_Cliente = input("Qual seu usuario? ")
Senha = input("digite sua Senha: ")
Senha_Nova_Pura = input("digite a nova senha: ")

Hash256_Senha_Antiga = sha256()

Hash256_Senha_Antiga.update(Senha.encode('utf-8'))

Senha_Antiga_Hash= Hash256_Senha_Antiga.hexdigest()

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
        mycursor.execute(sql, (Usuario_Cliente,))

        # Obter o resultado da consulta
        resultado = mycursor.fetchone()

        if resultado:  # Se o usuário existe
            senha_hash = resultado[0]  # Senha hash armazenada no banco de dados
            # Aqui você deve usar um algoritmo de hash seguro, como bcrypt
            # para verificar a senha
            if Senha_Antiga_Hash == senha_hash:
                print("Senha correta.")
                Senha_Antiga = Senha_Antiga_Hash
                
                sha256_hash_senha_nova = sha256()

                sha256_hash_senha_nova.update(Senha_Nova_Pura.encode('utf-8'))

                Senha_Update_Hash = sha256_hash_senha_nova.hexdigest()    
            else:
                print(f"Senha incorreta. {Senha}")
        else:
            print("Usuário não encontrado.")

except mysql.connector.Error as error:
    print("Erro ao conectar ao banco de dados:", error)
    
print(Senha_Update_Hash)