import mysql.connector
from decouple import config


Alt = int(input("1. Cadastrar-se  --  2. Trocar Senha  --  3. Alterar Email:"))

if Alt == 1:
    from Components.Register import *
    
    Tabela = config("Tabela")

    mydb = mysql.connector.connect(host=config("Host"), user=config("User"), password=config("Password"), database=config("Database"))

    mycursor = mydb.cursor()    
    sql = f"INSERT INTO credenciais_usuarios(Usuario, Email, Senha, Endereco_IP) VALUE (%s, %s, %s, %s) "
    val = (Nome, Email, Senha_Hash, Endereco_IP) 
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "Registros inseridos")

    if mydb.is_connected(): 
        mycursor.close()
        mydb.close()
        print("Conexão ao MySQL foi encerrada")
elif Alt == 2:
    from Components.ChangePassword import *
    
    Tabela = config("Tabela")

    mydb = mysql.connector.connect(host=config("Host"), user=config("User"), password=config("Password"), database=config("Database"))

    mycursor = mydb.cursor()    
    sql = "UPDATE credenciais_usuarios SET Senha = %s WHERE Senha = %s;"
    val = (Senha_Update_Hash,Senha_Antiga) 
    mycursor.execute(sql, val)
    mydb.commit()
elif Alt == 3:
    from Components.ChangeEmail import *
    
    Tabela = config("Tabela")

    mydb = mysql.connector.connect(host=config("Host"), user=config("User"), password=config("Password"), database=config("Database"))

    mycursor = mydb.cursor()    
    sql = "UPDATE credenciais_usuarios SET Email = %s WHERE Usuario = %s AND Senha = %s;"
    val = (EmailAtualizado,Usuario_Email, Senha_Hash_Formatada) 
    mycursor.execute(sql, val)
    mydb.commit()
else:
    print("Algo deu errado", error)
    print(Alt)


    


