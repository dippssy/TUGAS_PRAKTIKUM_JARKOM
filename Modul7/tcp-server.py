from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) #tcp

#meng bind server
serverSocket.bind(
    ('', serverPort)
)

#server siap menerima koneksi
serverSocket.listen(1)

print("[SYSTEM] Server TCP siap digunakan")

running = True
while running:
    #menerima koneksi dari client
    connectionSocket, addr = serverSocket.accept() ##menangkap tuple
    print("[SYSTEM] Terhubung dengan:", addr)
    
    while True:
        #pesan yang diterima = 101001
        message = connectionSocket.recv(2048).decode()

        if not message:
            break
        #cek apakah exit    
        if message.lower() == "exit":
            print("[SYSTEM] client ingin keluar")
            running = False
            break   

        #mofid capslock
        modifiedMessage = message.upper()
        print("[SERVER] Pesan yang diterima: ", modifiedMessage)

        #kirim balik ke client
        connectionSocket.send(
            modifiedMessage.encode()
        )

    connectionSocket.close()
serverSocket.close()        
