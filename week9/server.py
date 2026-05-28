from socket import *
import threading

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', 6789))
serverSocket.listen(5) #terima 5 client
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        #menerima pesan dari user
        message = connectionSocket.recv(1024).decode() #decode = mengubah byte menjadi string

        message = message[4:15]
        print(message)
        # filename = message.split()[1] #message = /GET /index.html HTTP/1.1
        #membuka index.html dan menghilangkan "/" di awal
        f = open(message[1:])
        #membaca file html
        outputdata = f.read()
        #kirim respon
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #kirim data
        connectionSocket.sendall(outputdata.encode())
        #tutup koneksi
        connectionSocket.close()
        
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) #send respon bila tdk ditemukan
        connectionSocket.send("<h1>404 Not Found</h1>".encode()) #kirim data 404
        connectionSocket.close()


    serverSocket.close()
    threading.exit()

