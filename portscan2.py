import socket


ports = [80, 443, 20, 21, 22, 25, 53, 23, 69, 139, 137, 445, 8080, 8443] 
target = "example.com"

for p in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	code = client.connect_ex((target, p)) #site or IP
	if code == 0:
		print(p, "OPEN")
	else:
		print(p, "CLOSED OR FILTERED")
