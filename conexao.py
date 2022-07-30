#Importa a lib
import mysql.connector
from decouple import config

#Cria o objeto e passa os parametros: host, user, password e database
con = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))

#Cria a condição 
if con.is_connected():
    #Mostrara a versão do mysql
    db_info = con.get_server_info()
    print("Conectado ao servidor mysql versão: ", db_info)
    #Cria um cursor para dar comandos ao db, executa comandos usando o cursor e exibe-os
    cursor = con.cursor()
    #Executa os comandos passados ao cursor
    cursor.execute("select database();")
    linha = cursor.fetchone()
    #Exibe os comandos
    print("Conectado ao banco de dados ",linha)
#Cria a condição para encerrar a conexão     
if con.is_connected(): 
    
    #Encerra o cursor
    cursor.close()
    
    #Encerra a conexão
    con.close()
    print("Conexao ao MySql foi encerrada")
    
    
