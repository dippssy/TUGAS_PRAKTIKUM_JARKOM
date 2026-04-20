### **Difa Auliya Andini Putri - 103072400112**

# **Laporan Praktikum Modul 7: Socket Programming**

### **Tujuan Praktikum**
1. Mampu membuat program berbasis socket UDP
2. Mampu membuat program berbasis socket TCP

### **Program Socket dengan TCP**
TCP adalah protokol berorientasi koneksi. Ini berarti bahwa sebelum klien dan
server dapat mulai mengirim data satu sama lain, mereka harus terlebih dahulu handshake dan
membuat koneksi TCP. Salah satu ujung koneksi TCP terpasang ke soket klien dan ujung lainnya
terpasang ke soket server. Saat membuat koneksi TCP, kita mengaitkannya dengan alamat soket
klien (alamat IP dan nomor port) dan alamat soket server (alamat IP dan nomor port). TCP memastikan data terkirim dengan benar (reliable), tidak hilang, berurutan. Sebelum komunikasi, TCP melakukan proses Three-way handshake (SYN, SYN-ACK, ACK).

**TCP Client:**
```python
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
```
**Penjelasan Kode TCP Client:**
1. **socket(AF_INET, SOCK_STREAM)** → Membuat socket TCP berbasis IPv4
2. **connect((serverName, serverPort))** → Menghubungkan client ke server
3. **input()** → Mengambil pesan dari user
4. **send(message.encode())** → Mengirim pesan dalam bentuk byte
5. **recv(2048)** → Menerima balasan dari server (maks 2048 byte)
6. **decode()** → Mengubah byte menjadi string
7. **if message == "exit"** → Menghentikan program
8. **close()** → Menutup koneksi

**TCP Server:**
```python
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
```

**Penjelasan Kode TCP Server:**
1. **socket(AF_INET, SOCK_STREAM)** → Membuat socket TCP
2. **bind(('', serverPort))** → Mengikat server ke port tertentu
3. **listen(1)** → Server menunggu koneksi dari client
4. **accept()** → Menerima koneksi dari client
5. **recv(2048)** → Menerima pesan dari client
6. **decode()** → Mengubah byte menjadi string
7. **message.upper()** → Mengubah pesan menjadi huruf besar
8. **send()** → Mengirim kembali hasil ke client
9. **if message == "exit"** → Menghentikan server
10. **close()** → Menutup koneksi

