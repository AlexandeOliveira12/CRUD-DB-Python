import socket
from hashlib import sha256
import locale


#Pegar IP
try:
    # Cria um socket para obter o endereço IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Conecta-se a um servidor qualquer (não importa o endereço ou a porta)
    s.connect(('8.8.8.8', 80))
    
    # Obtém o endereço IP do socket
    ip_address = s.getsockname()[0]

except socket.error as e:
    print(f"Erro ao obter o endereço IP: {e}")

finally:
    # Fecha o socket
    s.close()

#Pega o Nome
Nome = input("\nInsira seu Nome de Usuario: ")

#Pega o Email
Email = input("Digite se Email: ")

#Pega a Senha
Senha = input("Insira uma Senha: ")

#Pega o Idioma do S.O
idioma, _ = locale.getdefaultlocale()
print(idioma)

#Transforma a senha em Hash
sha256_hash = sha256()

sha256_hash.update(Senha.encode('utf-8'))

Senha_Hash = sha256_hash.hexdigest()

Endereco_IP = ip_address
    

    


