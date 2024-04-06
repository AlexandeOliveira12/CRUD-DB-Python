import mysql.connector
from decouple import config
from hashlib import sha256
import notify2
import random
import string

Usuario_Email = input("Digite o nome de Usuario: ")
Senha = input("Digite sua Senha: ")

sha256Hash = sha256()
sha256Hash.update(Senha.encode('utf-8'))
Senha_Hash_Digitada = sha256Hash.hexdigest()

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
    mycursor.execute(sql, (Usuario_Email,))

    # Obter o resultado da consulta
    resultado = mycursor.fetchone()

    if resultado:
        senha_hash = resultado[0]  # Senha hash armazenada no banco de dados
        # para verificar a senha
        if Senha_Hash_Digitada == senha_hash:
            Senha_Hash_Formatada = Senha_Hash_Digitada
            def gerar_codigo():
                caracteres = string.ascii_lowercase + string.digits
                codigo_gerado = ''.join(random.choices(caracteres, k=6))
                return codigo_gerado

            codigos_gerados = set()
            while True:
                novo_codigo = gerar_codigo()
                if novo_codigo not in codigos_gerados:
                    codigos_gerados.add(novo_codigo)
                    print(f"Novo código gerado: {novo_codigo}")
                    break
            # Inicialize a biblioteca notify2
            notify2.init("2FA")
            # Crie um objeto de notificação
            notification = notify2.Notification("Autenticação Email", f"Seu código de Autenticação é: {novo_codigo}")
            # Exiba a notificação
            notification.show()
            codigo_digitado = input("Digite o código de autenticação: ")
            if codigo_digitado == novo_codigo:
                EmailAtualizado = input("Digite o novo email: ")
            elif codigo_digitado != novo_codigo:
                codigo_digitado = input("Código incorreto, digite novamente: ")
            else:
                print("O código esta incorreto, tente novamente mais tarde!")
except mysql.connector.Error as error:
    print("Erro ao conectar ao banco de dados:", error)







