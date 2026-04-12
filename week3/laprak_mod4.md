### **Difa Auliya Andini Putri - 103072400112**

# **Laporan Praktikum Modul 4: DNS**

### **Tujuan Praktikum**
Dapat menginvestigasi cara kerja DNS menggunakan Wireshark.

### **A. Nslookup**
Domain Name System (DNS) merupakan sistem yang digunakan untuk menerjemahkan nama domain menjadi alamat IP agar perangkat dapat saling berkomunikasi dalam jaringan. Pada praktikum ini digunakan perintah nslookup untuk melakukan query ke server DNS dan mengamati respon yang diberikan.

**Perintah 1 - jalankan:**
nslookup www.mit.edu<br>

<img src="../assets/images/dns1.png" width="500px"><br>

Perintah ini digunakan untuk meminta alamat IP dari domain www.mit.edu dengan menggunakan DNS server lokal. Hasilnya menunjukkan sistem menggunakan DNS server tusbind.ac.id dengan alamat IP 10.217.7.77. Respon yang diberikan bersifat non-authoritative, yang menandakan bahwa jawaban tidak langsung berasal dari server DNS otoritatif, melainkan dari cache atau hasil query ke server DNS lain, hasil juga menampilkan nama host dan alamat IP dari domain yang dicari.<br>

**Perintah 2- jalankan:**
nslookup -type=NS mit.edu<br>

<img src="../assets/images/dns2.png" width="500px"><br>

Perintah ini digunakan untuk mengetahui server DNS yang bertanggung jawab terhadap domain mit.edu dengan menggunakan opsi -type=NS. Hasil yang diperoleh menunjukkan bahwa sistem menggunakan DNS server tusbind.ac.id dengan alamat IP 10.217.7.77. Respon yang diberikan bersifat non-authoritative, yang menandakan bahwa jawaban tidak langsung berasal dari server DNS otoritatif. hasil menampilkan beberapa nama server yang menangani domain mit.edu, yang merupakan server DNS otoritatif untuk domain tersebut, beserta alamat IP yang terkait.<br>

**Perintah 3- jalankan:**
nslookup www.aiit.or.kr bitsy.mit.edu<br>

<img src="../assets/images/dns3.png" width="500px"><br>

Perintah ini digunakan untuk meminta alamat IP dari domain www.aiit.or.kr dengan mengirimkan query langsung ke DNS server bitsy.mit.edu, bukan ke DNS server lokal, permintaan tidak mendapatkan respon dan mengalami timeout. ini menunjukkan bahwa server DNS yang dituju tidak memberikan jawaban terhadap permintaan yang dikirimkan. Kondisi ini dapat terjadi karena beberapa kemungkinan, seperti server tidak aktif, tidak dapat diakses, atau adanya pembatasan jaringan seperti firewall.<br>

### **Pengujian Mandiri**
a. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP 
server tersebut?<br>

<img src="../assets/images/dns5.png" width="450px"><br>

Perintah ini digunakan untuk mendapatkan alamat IP dari server web di Asia. Berdasarkan hasil yang diperoleh, alamat IP dari server tersebut adalah **45.60.35.225**.<br>

b. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.<br>

<img src="../assets/images/dns6.png" width="550px"><br>

Perintah ini digunakan untuk mengetahui server DNS otoritatif dari universitas di Eropa, yaitu domain **ox.ac.uk**. server DNS yang menangani domain tersebut adalah **auth6.dns.ox.ac.uk, dns1.ox.ac.uk, dns0.ox.ac.uk, dns2.ox.ac.uk, auth4.dns.ox.ac.uk, dan auth5.dns.ox.ac.uk**, domain universitas tersebut memiliki beberapa server DNS otoritatif untuk meningkatkan keandalan dan ketersediaan layanan.<br>

c. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail 
melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?<br>

<img src="../assets/images/dns7.png" width="550px"><br>
Pada percobaan ini, permintaan ke server DNS ox.ac.uk tidak berhasil dan menghasilkan query refused, yang menunjukkan bahwa server tersebut tidak melayani permintaan dari luar.<br>

Selanjutnya dilakukan query menggunakan DNS server lokal:<br>
<img src="../assets/images/dns8.png" width="550px"><br>

Berdasarkan hasil yang diperoleh, server email untuk yahoo.com adalah mta5.am0.yahoodns.net, mta6.am0.yahoodns.net, dan mta7.am0.yahoodns.net.<br>


### **B. Ipconfig**
Perintah ipconfig merupakan salah satu tools yang digunakan untuk melihat dan membantu mendiagnosis konfigurasi jaringan pada host. Perintah ini dapat menampilkan informasi terkait TCP/IP, seperti alamat IP, server DNS, jenis adaptor, dan informasi jaringan lainnya.
Dengan menggunakan perintah ipconfig, pengguna dapat mengetahui kondisi jaringan yang sedang digunakan serta membantu dalam proses troubleshooting jika terjadi masalah koneksi.

**Perintah 1 - jalankan:**
**ipconfig /all**<br>

<img src="../assets/images/ipcon1.png" width="450px"><br>

Perintah ini digunakan untuk menampilkan informasi konfigurasi jaringan pada host, perangkat menggunakan adaptor Wi-Fi dengan alamat IP 10.218.1.58, subnet mask 255.255.240.0, dan default gateway 10.218.0.253. DNS server yang digunakan adalah 10.217.7.77, yang berfungsi untuk menerjemahkan nama domain menjadi alamat IP.

**Perintah 2 - jalankan:**
**ipconfig /displaydns**<br>

<img src="../assets/images/ipcon2.png" width="450px"><br>

Perintah ini digunakan untuk menampilkan daftar DNS cache yang tersimpan pada host. Berdasarkan hasil yang diperoleh, terlihat beberapa domain yang pernah diakses seperti unleash.codeium.com, relay.avica.com, dan server.codeium.com beserta alamat IP-nya. sistem menyimpan hasil resolusi DNS sementara untuk mempercepat akses ke domain yang sama tanpa harus melakukan query ulang ke server DNS.<br>

**Perintah 3 - jalankan:**
**ipconfig /flushdns**<br>

<img src="../assets/images/ipcon3.png" width="550px"><br>

Perintah ini digunakan untuk menghapus seluruh DNS cache yang tersimpan pada sistem. Berdasarkan hasil yang diperoleh, proses penghapusan cache berhasil dilakukan yang ditandai dengan pesan “Successfully flushed the DNS Resolver Cache”. semua data DNS yang tersimpan sebelumnya telah dihapus, sehingga sistem akan melakukan query ulang ke DNS server saat mengakses domain.<br>

### **C. Tracing DNS dengan Wireshark**

**Langkah-Langkah:**
1. Buka Command Prompt (CMD), lalu jalankan perintah berikut untuk mengetahui alamat IP host: (10.218.1.58)<br>

    <img src="../assets/images/ipcon4.png" width="550px"><br>

2. jalankan **ipconfig /flushdns** untuk mengosongkan DNS cache:<br>

    <img src="../assets/images/ipcon3.png" width="550px"><br>

3. Buka browser dan kosongkan cache agar tidak menggunakan data yang tersimpan sebelumnya.

4. Buka Wireshark, lalu masukkan filter: "ip.addr == <your_IP_address>" Bagian 
<your_IP_address> diisi dengan alamat IP Anda yang didapatkan melalui ipconfig.<br>

    <img src="../assets/images/ipcon5.png" width="550px"><br>

5. Mulai proses capture paket di Wireshark.

6. Buka browser dan akses website: http://www.ietf.org<br>

    <img src="../assets/images/ipcon6.png" width="550px"><br>

7. Setelah halaman terbuka, hentikan proses capture.

**Jawab beberapa pertanyaan berikut:**
1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP 
atau TCP?<br>

    <img src="../assets/images/ipcon7.png" width="550px"><br>

    <img src="../assets/images/ipcon8.png" width="550px"><br>
Berdasarkan hasil pengamatan pada paket DNS, pesan permintaan (Standard query) dikirimkan menggunakan protokol UDP, pada bagian User Datagram Protocol, pesan permintaan dan balasan DNS menggunakan UDP.

2. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya?<br>

    <img src="../assets/images/ipcon9.png" width="550px"><br>
Port tujuan pada pesan permintaan DNS adalah 53, port sumber yang digunakan pada pesan balasan DNS adalah 62158, yaitu port yang sebelumnya digunakan oleh client saat mengirim permintaan.<br> 
DNS Request -> Source Port (client): 62158 & Destination Port (server): 53<br>
DNS Response -> Source Port (server): 53 & Destination Port (client): 62158<br>

3. Pada pesan permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal anda 
(gunakan ipconfig untuk mencari tahu)? Apakah kedua alamat IP tersebut sama?<br>

    <img src="../assets/images/ipcon11.png" width="350px"><br>
A   lamat IP tujuan adalah 10.217.7.77. DNS server lokal host juga memiliki alamat IP 10.217.7.77. kedua alamat IP tersebut sama, permintaan DNS dikirim langsung ke DNS server lokal.<br>

4. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? Apakah pesan 
permintaan tersebut mengandung ”jawaban” atau ”answers”?<br> 

    <img src="../assets/images/ipcon12.png" width="450px"><br>
Dari pesan tersebut adalah A (Address), yaitu untuk meminta alamat IP dari suatu domain, pesan permintaan tidak mengandung answer, nilai Answer RRs: 0.<br>

5.  Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di 
dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut?<br>

    <img src="../assets/images/ipcon13.png" width="450px"><br>
    pesan balasan DNS (Standard query response), terdapat 1 answer, Answer RRs: 1. Isi dari jawaban tersebut adalah alamat IP dari domain yang diminta, 146.112.41.2 untuk domain doh.opendns.com<br>

6. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS?<br> 

    <img src="../assets/images/ipcon14.png" width="550px"><br>
alamat IP pada paket TCP SYN sesuai dengan alamat IP yang terdapat pada pesan balasan DNS, yaitu 146.112.41.2.

7. Halaman web yang sebelumnya anda akses (http://www.ietf.org) memuat beberapa 
gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin 
mengakses suatu gambar?<br>

    <img src="../assets/images/ipcon15.png" width="550px"><br>
tidak, host tidak perlu mengirimkan permintaan DNS baru setiap kali mengakses gambar, karena alamat IP domain sudah disimpan dalam cache DNS sehingga dapat digunakan kembali tanpa melakukan query ulang.

### **1. Analisis DNS menggunakan nslookup www.mit.edu**
 
1. Mulai pengambilan paket. 
2. Lakukan perintah nslookup www.mit.edu pada cmd<br>

    <img src="../assets/images/dns1.png" width="550px"><br>

3. Hentikan pengambilan paket, lalu filter "dns".<br>
    <img src="../assets/images/ipcon16.png" width="550px"><br>
<br>    

**Menjawab Pertanyaan:**

1. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasan DNS?<br>

    <img src="../assets/images/ipcon17.png" width="550px"><br>
    <img src="../assets/images/ipcon18.png" width="550px"><br>
    port tujuan pada pesan permintaan DNS adalah 53, sedangkan port sumber pada pesan balasan DNS adalah 53. client menggunakan port 57534 saat mengirim permintaan, dan port tersebut menjadi port tujuan pada saat menerima balasan dari server.

2. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda?<br>

    <img src="../assets/images/ipcon19.png" width="550px"><br>
pesan permintaan DNS dikirim ke alamat IP 10.217.7.77, dan alamat IP tersebut merupakan DNS server lokal.

3. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” atau ”answers”? <br>

    <img src="../assets/images/ipcon20.png" width="350px"><br>
jenis (type) dari pesan permintaan DNS adalah A (Host Address), dan pesan tersebut tidak mengandung jawaban karena nilai Answer RRs = 0.

4. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di 
dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?<br>

    <img src="../assets/images/ipcon21.png" width="350px"><br>
terdapat 3 jawaban pada pesan balasan DNS. isi dari setiap jawaban tersebut adalah dua record CNAME (alias domain) yaitu www.mit.edu
 → www.mit.edu.edgekey.net
 dan www.mit.edu.edgekey.net
 → e9566.dscb.akamaiedge.net, serta satu record A yang berisi alamat IP yaitu 23.217.163.122.

### **2. Analisis DNS menggunakan nslookup –type=NS mit.edu**
 
Ulangi percobaan sebelumnya, namun gunakan perintah nslookup -type=NS mit.edu pada cmd<br>

<img src="../assets/images/dns2.png" width="500px"><br>  

**Menjawab Pertanyaan:**

1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut merupakan default alamat IP server DNS lokal Anda? <br>

    <img src="../assets/images/ipcon22.png" width="550px"><br>
    pesan permintaan DNS dikirim ke alamat IP 10.217.7.77, dan alamat IP tersebut merupakan default alamat IP server DNS lokal.

2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan tersebut mengandung ”jawaban” atau ”answers”?<br>

    <img src="../assets/images/ipcon23.png" width="550px"><br>
jenis (type) dari pesan permintaan DNS adalah NS, dan pesan tersebut tidak mengandung jawaban karena nilai Answer RRs = 0.

3. Periksa pesan balasan DNS. Apa nama server MIT yang diberikan oleh pesan balasan? 
Apakah pesan balasan ini juga memberikan alamat IP untuk server MIT tersebut? <br>

    <img src="../assets/images/ipcon24.png" width="350px"><br>
terdapat 8 jawaban pada pesan balasan DNS, yang berisi record NS (name server) untuk domain mit.edu, yaitu ns1-37.akam.net, asia2.akam.net, eur5.akam.net, use2.akam.net, use5.akam.net, asia1.akam.net, usw2.akam.net, dan ns1-173.akam.net. selain itu terdapat additional records yang berisi alamat IP dari beberapa name server tersebut.

### **3. Analisis DNS menggunakan nslookup www.aiit.or.kr bitsy.mit.edu**
 
Ulangi percobaan sebelumnya, namun gunakan perintah nslookup www.aiit.or.kr bitsy.mit.edu pada cmd<br>

<img src="../assets/images/dns3.png" width="500px"><br>  

**Menjawab Pertanyaan:**

1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut merupakan default alamat IP server DNS lokal Anda? <br>

    <img src="../assets/images/ipcon25.png" width="550px"><br>
    alamat IP 18.0.72.3 merupakan alamat dari server DNS bitsy.mit.edu yang digunakan secara langsung pada perintah nslookup, sehingga bukan merupakan DNS server lokal.

2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan tersebut mengandung ”jawaban” atau ”answers”? <br>

    <img src="../assets/images/ipcon26.png" width="550px"><br>
jenis (type) dari pesan permintaan DNS adalah A, dan pesan tersebut tidak mengandung jawaban karena nilai Answer RRs = 0.

3. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di 
dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut? <br>

    <img src="../assets/images/dns3.png" width="350px"><br>
tidak terdapat pesan balasan DNS karena permintaan mengalami timeout, sehingga server tidak memberikan jawaban terhadap query yang dikirimkan.



