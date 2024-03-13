# GAME TEBAK KATA HANGMAN
Hangman adalah permainan tebak kata klasik yang menantang pemain untuk menebak kata yang dipilih secara acak dari daftar kata yang telah ditentukan sebelumnya. Kata tersebut kemudian ditampilkan sebagai garis, dengan setiap garis mewakili satu huruf dalam kata tersebut. Pemain diberikan kesempatan untuk menebak huruf-huruf yang terdapat pada kata tersebut. Jika huruf yang ditebak oleh pemain ada dalam kata, maka huruf tersebut akan ditampilkan di posisi garis yang sesuai dalam kata. Namun, jika huruf yang ditebak salah, maka pemain akan kehilangan satu kesempatan. Kesempatan dalam permainan Hangman ini direpresentasikan dalam bentuk gambar Hangman yang tergantung. Setiap tebakan yang salah akan menyebabkan bagian-bagian dari gambar Hangman ditampilkan secara bertahap. Apabila semua bagian gambar Hangman telah digambar sebelum pemain berhasil menebak kata, maka pemain dinyatakan kalah.

## Spesifikasi Game
Berikut merupakan spesifikasi dari game tebak kata Hangman yang dibuat.
- Pemain yang ingin memainkan game harus terlebih dahulu mendaftar. Setiap pemain harus memiliki username yang unik.
- Kata yang harus ditebak pemain akan dibangkitkan secara acak oleh program berdasarkan suatu daftar kata yang telah terdefinisi.
- Pemain mendapat informasi berupa panjang kata, kemudian pemain harus memberikan tebakan huruf per huruf yang menyusun kata. Untuk setiap huruf yang ditebak, jika huruf merupakan bagian dari kata, huruf ditampilkan pada posisi yang sesuai, sementara jika huruf bukan merupakan bagian dari kata, Hangman secara bertahap akan ditampilkan untuk setiap kesalahan baru.
- Dalam proses menebak kata, pemain mendapatkan skor dengan ketentuan (100 - n^2), dimana n adalah jumlah tebakan salah. Apabila jumlah tebakan salah telah mencapai total 8, maka pemain mendapat skor 0 dan gambar Hangman akan terbentuk sempurna.
- Untuk seorang pemain, game ini dapat diulang sampai pemain menyatakan ingin berhenti. Skor yang tersimpan adalah skor tertinggi yang pernah diperoleh oleh pemain tersebut.
- Informasi Top Ten, yaitu daftar 10 pemain dengan skor tertinggi, dapat ditampilkan.
- Untuk setiap pemain, riwayat kata yang pernah ditebak disimpan, sehingga ketika program membangkitkan kata yang harus ditebak, maka kata tersebut tidak boleh sama dengan kata yang sudah pernah ditebak sebelumnya, kecuali apabila seluruh kata dalam daftar kata sudah pernah ditebak oleh pemain.
- Status game dapat disimpan ke dalam file eksternal untuk di-_load_ ulang ketika program dijalankan di lain waktu.

## Fitur Game
Game tebak kata Hangman memiliki beberapa menu berikut.
1. Login / Register / Change User

   Menu ini digunakan untuk memasukkan nama pemain lama atau melakukan registrasi pemain baru dengan meminta input berupa username pemain. Apabila pemain tercatat sedang memainkan game, maka menu ini dapat digunakan untuk mengubah pemain (_change user_), baik menjadi pemain dengan username baru maupun username lama.
2. Start Game

   Menu ini digunakan untuk memulai game tebak kata Hangman.
3. Top Ten

   Menu ini akan menampilkan daftar 10 pemain dengan skor tertinggi.
4. Info Pengguna

   Menu ini akan menampilkan info terkait pemain yang sedang aktif, seperti skor tertinggi.
5. Keluar
   
   Menu ini digunakan untuk keluar dari program game tebak kata Hangman.
