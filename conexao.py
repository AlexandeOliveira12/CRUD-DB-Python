import mysql.connector
from Parameters.QuestionsParameters import *


mydb = mysql.connector.connect(host="127.0.0.1", user='root', password="E=m.c20608", database="escola")

mycursor = mydb.cursor()
sql = "INSERT INTO aluno(nome, idade, sexo) VALUE (%s, %s, %s)"
val = [
(name, idade, sexo)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Registros inseridos")

if mydb.is_connected(): 
    mycursor.close()
    mydb.close()
    print("Conexao ao MySql foi encerrada")



