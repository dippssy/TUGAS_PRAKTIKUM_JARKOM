from socket import *

serverName = "localhost"
serverPort = 12000 

#AF inet itu ipv4, | SOCK_STREAM itu TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

#hubungan | connect
clientSocket.connect(
    (serverName, serverPort)
)

print("[SYSTEM] Masukkan Pesan")
