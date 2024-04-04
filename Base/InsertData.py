import mysql.connector
from decouple import config
from Components.QuestionsParameters import *
#from Parameters.QuestionsParameters import *

Tabela = config("Tabela")

mydb = mysql.connector.connect(host=config("Host"), user=config("User"), password=config("Password"), database=config("Database"))

mycursor = mydb.cursor()
sql = f"INSERT INTO Usuarios(Usuario, Email, Senha, Endereco_IP) VALUE (%s, %s, %s, %s) "
val = (Nome, Email, Senha_Hash, Endereco_IP ) 
mycursor.execute(sql, val)
mydb.commit()
#print(mycursor.rowcount, "Registros inseridos")

if mydb.is_connected(): 
    mycursor.close()
    mydb.close()
    print("Conexão ao MySQL foi encerrada")



