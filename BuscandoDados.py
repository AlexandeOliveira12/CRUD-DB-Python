import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user='root', password="E=m.c20608", database="escola")

mycursor = mydb.cursor()
mycursor.execute("select * from aluno")
clientes = mycursor.fetchall()

for clientes in clientes:
    print(clientes)