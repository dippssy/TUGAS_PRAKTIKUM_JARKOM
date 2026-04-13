#Socket = penjumlahan, bagi, kurang, kali
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

running = True
while running:
    #input
    message = input(">> ")

    #kirim ke server
    #encode = abcdef = 1010100110
    clientSocket.send(message.encode())
    
    #kalo exit = socket tutup
    if message == "exit":
        print("[SYSTEM] Keluar dari program")
        running = False
        break

    #menerima pesan dari server
    modifiedMessage = clientSocket.recv(2048) #abc = 01100110010101, diset max bytenya 2048
    print("[SERVER] pesan: ", modifiedMessage.decode())

#tutup socket yang tidak dipakai
clientSocket.close()
print("[SYSTEM] Socket ditutup")  