import mysql.connector
from decouple import config
from hashlib import sha256

Usuario_Cliente = input("\nQual seu usuário? ")
Senha = input("Digite sua senha: ")
Senha_Nova_Pura = input("Digite a nova senha: ")

Hash256_Senha_Antiga = sha256()
Hash256_Senha_Antiga.update(Senha.encode('utf-8'))
Senha_Antiga_Hash = Hash256_Senha_Antiga.hexdigest()

Senha_Update_Hash = None  # Defina inicialmente como None

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
            print("\nSenha Atualizada")
            Senha_Antiga = Senha_Antiga_Hash

            sha256_hash_senha_nova = sha256()
            sha256_hash_senha_nova.update(Senha_Nova_Pura.encode('utf-8'))
            Senha_Update_Hash = sha256_hash_senha_nova.hexdigest()
        else:
            print("A senha está incorreta.")
    else:
        print("O usuário não foi encontrado.")

except mysql.connector.Error as error:
    print("Erro ao conectar ao banco de dados:", error)

if Senha_Update_Hash is not None:  # Verifica se a variável foi definida
    print(f"Hash da nova senha: {Senha_Update_Hash}")
    print(f"Hash da senha antiga: {senha_hash}")
else:
    print("Não foi possível gerar o hash da nova senha.")
