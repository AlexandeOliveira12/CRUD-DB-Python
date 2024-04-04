import mysql.connector
from decouple import config

def verificar_nome_usuario(nome_usuario):
    try:
        # Conectar ao banco de dados MySQL
        conexao = mysql.connector.connect(
            host=config('Host'),
            user=config('User'),
            password=config('Password'),
            database=config('Database')
        )

        # Criar um cursor para executar consultas SQL
        cursor = conexao.cursor()

        # Executar uma consulta SQL para verificar se o nome de usuário já existe
        consulta = "SELECT COUNT(*) FROM Usuarios WHERE Usuario = %s"
        cursor.execute(consulta, (nome_usuario,))

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        # Verificar se o nome de usuário já existe
        if resultado[0] > 0:
            #print("O nome de usuário '{}' já está em uso.".format(nome_usuario))
            print(False)
        else:
            #print("O nome de usuário '{}' está disponível.".format(nome_usuario))
            print(True)

    except mysql.connector.Error as erro:
        print("Erro ao conectar ao banco de dados MySQL:", erro)

    finally:
        # Fechar o cursor e a conexão
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
nome = input("Digite o Usuario: ")
# Testar a função com um nome de usuário específico
verificar_nome_usuario(nome)
