import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("exemplo_de_alvo.com.br", númerodaporta))
client.send(b"um_texto_qualquer")
response = client.recv(1024) #quantidade de bytes a serem recebidos
print(response.decode()) #saída como no netcat
