### **Difa Auliya Andini Putri - 103072400112**

# **Laporan Praktikum Modul 5: UDP**

### **Tujuan Praktikum**
Dapat dapat menginvestigasi cara kerja protokol UDP menggunakan Wireshark.

### **Pendahuluan**
Pada modul ini dilakukan pengamatan terhadap protokol transport UDP (User Datagram Protocol) menggunakan Wireshark. UDP merupakan protokol yang bersifat sederhana, tidak menggunakan koneksi (connectionless), dan memiliki struktur header yang tetap serta tidak kompleks. Karena sifatnya yang ringan, UDP sering digunakan pada layanan yang membutuhkan kecepatan seperti DNS, streaming, dan SNMP. Pada praktikum ini, analisis dilakukan dengan menangkap paket UDP dan mengamati struktur header serta isi datanya.


### **Tugas**
Mulailah menangkap paket di Wireshark. Kemudian lakukanlah sesuatu yang akan menyebabkan 
host Anda mengirim dan menerima beberapa paket UDP. Terkadang, tanpa melakukan apapun 
(kecuali jika melakukan penangkapan melalui Wireshark), beberapa paket UDP yang dikirimkan oleh 
orang lain akan terekam dalam jejak. Simple Network mengirimkan 
pesan SNMP di dalam UDP sehingga Anda akan menemukan beberapa pesan SNMP (dan juga paket 
UDP) di dalam trace. 

**Pertanyaan:**

1. Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak 
“field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan! <br>

    <img src="../assets/images/udp2.png" width="550px"><br>
    pada bagian User Datagram Protocol, header UDP terdiri dari empat field utama, yaitu:<br>
    Source Port<br>
    Destination Port<br>
    Length<br>
    Checksum<br>
    Keempat field tersebut merupakan komponen standar yang digunakan untuk mengidentifikasi sumber dan tujuan komunikasi, panjang data, serta pengecekan kesalahan.

2. Perhatikan informasi “content field” pada paket yang Anda pilih di pertanyaan 1. Berapa 
panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP?<br>

    <img src="../assets/images/udp2.png" width="550px"><br>
Setiap field pada header UDP memiliki panjang yang sama, yaitu 2 byte, dengan rincian:<br>
Source Port: 2 byte<br>
Destination Port: 2 byte<br>
Length: 2 byte<br>
Checksum: 2 byte<br>
Dengan demikian, total panjang header UDP adalah 8 byte, yang menunjukkan bahwa struktur UDP bersifat sederhana dan tetap.

3.  Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui paket UDP pada trace. <br>

    <img src="../assets/images/udp2.png" width="350px"><br>
Field Length menunjukkan total panjang segmen UDP yang mencakup header dan payload. Berdasarkan paket yang dianalisis diperoleh:
- Length = 58 byte
- Header = 8 byte
- Payload = 50 byte<br>
 Hasil tersebut sesuai karena 8 + 50 = 58 byte, sehingga dapat disimpulkan bahwa field Length merepresentasikan total panjang segmen UDP secara keseluruhan.

4.  Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk: jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2) <br>

    Field Length memiliki ukuran 2 byte (16 bit) sehingga nilai maksimum yang dapat direpresentasikan adalah 65.535 byte. Karena nilai tersebut mencakup header UDP, maka maksimum payload yang dapat dikirim adalah:

    65.535 − 8 = 65.527 byte

    kapasitas maksimum data dalam satu segmen UDP adalah 65.527 byte.

5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk pada pertanyaan 4)<br>

    Field port pada UDP memiliki panjang 2 byte (16 bit), sehingga nilai maksimum yang dapat digunakan adalah:

    2¹⁶ − 1 = 65.535

    Dengan demikian, nomor port terbesar yang dapat digunakan sebagai port sumber adalah 65.535, dengan rentang port dari 0 hingga 65.535.


6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan 
desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada 
datagram IP yang mengandung segmen UDP<br>

    Berdasarkan pengamatan pada header IP, protokol UDP memiliki nomor:

    Desimal: 17
    Heksadesimal: 0x11

    Nilai ini digunakan pada field Protocol di header IP untuk menandakan bahwa datagram membawa segmen UDP.
    <img src="../assets/images/udp3.png" width="550px"><br>

7. Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket 
UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua 
merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari 
paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut!

    Berdasarkan pengamatan pasangan paket UDP, terlihat bahwa nomor port pada paket request dan response saling berkebalikan. Pada paket request:

- Source Port = 4334
- Destination Port = 161

    Sedangkan pada paket response:

- Source Port = 161
- Destination Port = 4334

    Hal ini menunjukkan bahwa pada komunikasi UDP, balasan dikirim kembali ke port asal pengirim, sehingga port sumber dan tujuan akan bertukar antara request dan response.<br>

    <img src="../assets/images/udp3.png" width="550px"><br>

