import mysql.connector
from decouple import config


Alt = int(input('''1. Cadastrar-se - 2. Trocar Senha: '''))

"""if Alt == 1:
    from Parameters.QuestionsParameters import *
    
    Tabela = config("Tabela")

    mydb = mysql.connector.connect(host=config("Host"), user=config("User"), password=config("Password"), database=config("Database"))

    mycursor = mydb.cursor()    
    sql = f"INSERT INTO Usuarios(Usuario, Email, Senha, Endereco_IP) VALUE (%s, %s, %s, %s) "
    val = (Nome, Email, Senha, Endereco_IP ) 
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "Registros inseridos")

    if mydb.is_connected(): 
        mycursor.close()
        mydb.close()
        print("Conexão ao MySQL foi encerrada")
else:
    print("Algo deu errado")
    print(Alt)"""
    
if Alt == 2:
    from Parameters.Dados import *
    
    Tabela = config("Tabela")

    mydb = mysql.connector.connect(host=config("Host"), user=config("User"), password=config("Password"), database=config("Database"))

    mycursor = mydb.cursor()    
    sql = "UPDATE Usuarios SET Senha = %s WHERE Senha = %s;"
    val = (Senha_Update_Hash,Senha_Antiga) 
    mycursor.execute(sql, val)
    mydb.commit()
    

    


