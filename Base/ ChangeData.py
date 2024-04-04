import mysql.connector
from decouple import config
from Components.Data import *

mydb = mysql.connector.connect(
    host=config("Host"),
    user=config("User"),
    password=config("Password"),
    database=config("Database")
)

mycursor = mydb.cursor()
sql = "UPDATE Usuarios SET Email = %s WHERE Usuario = %s;"
values = (Usuario_Cliente)

mycursor.execute(sql, values)
mydb.commit()
print("Registro atualizado com sucesso.")
