# PROGRAM HANGMAN


# KAMUS 
# hewan, buah, kota, negara, benda, semua : array of str
# buatmain : pemanggilan file eksternal main
# buatuser : pemanggilan file eksternal users
# buatscore : pemanggilan file eksternal scores
# pilihan : int
# user : array of str
# daftarscore : array of int
# data_user_skor, dataskor : array of dict


# ALGORITMA
import random


# List kata pada permainan Hangman ini
hewan = ["anjing", "kucing", "sapi", "badak", "kuda", "beruang", "singa", "gajah", "rusa", "harimau", "kerbau", "macan", "serigala", "buaya", "kelinci"]
buah = ["apel", "jeruk", "mangga", "anggur", "pepaya", "pisang", "semangka", "stroberi", "rambutan", "kiwi", "durian", "salak", "alpukat", "nanas", "melon"]
kota = ["bandung", "jakarta", "padang", "surabaya", "pekanbaru", "solo", "bengkulu", "palembang", "bogor", "medan", "semarang", "bekasi", "banjarmasin", "depok", "malang"]
negara = ["indonesia", "malaysia", "belanda", "india", "portugal", "singapura", "thailand", "taiwan", "vietnam", "jepang", "filipina", "italia", "jerman", "rusia", "spanyol"]
benda = ["jam", "buku", "pena", "pensil", "sisir", "kertas", "kacamata", "meja", "kursi", "lampu", "kalkulator", "komputer", "penggaris", "senter", "kulkas"]
semua = [', '.join(hewan) + ', ' + ', '.join(buah) + ', ' + ', '.join(kota) + ', ' + ', '.join(negara) + ', ' + ', '.join(benda)]

# Membuat file eksternal 
buatmain = open('main', 'a')          # membuat file eksternal main
buatmain.close()
buatuser = open('users', 'a')         # membuat file eksternal users
buatuser.close()
buatscore = open('scores', 'a')       # membuat file eksternal scores
buatscore.close()



# Fungsi menu yang dapat dipilih oleh user

pilihan = 0
def menu(pilihan) :

    # KAMUS LOKAL
    # milih : str
    # pilihan : int

    # ALGORITMA
    print('======== M E N U ========')
    print('1. Login atau register')
    print('2. Start game')
    print('3. Top ten')
    print('4. Info pengguna')
    print('5. Keluar')
    print('=========================')
    milih = input("Silahkan pilih menu yang diinginkan >>> ")
    print()
    if (milih == '1') and (pilihan == 0) :                                                # jika user memilih login / register dan kondisi pilihan masih bernilai 0, maka user dapat melakukan login / register
        pilihan = 1                                                                       
        input_username()                                                                  
        menu(pilihan)                                                                     # setelah melakukan login/register, user akan dikembalikan ke menu utama
    elif (milih == '1') and (pilihan == 1) :                                              # jika user memilih 1 dan kondisi pilihan bernilai 1, maka berarti user sudah melakukan login / register
        print('Anda sudah melakukan login atau register! Silahkan pilih menu lainnya.')   
        print()
        menu(pilihan)                                                                     # user akan dikembalikan ke menu utama 
    elif (milih == '2') and (pilihan == 0):                                               # jika user memilih start game, tetapi belum melakukan login / register
        print('Harap mengisi login atau register terlebih dahulu sebelum start game!')    
        print()
        menu(pilihan)                                                                     # user akan dikembalikan ke menu utama
    elif (milih == '2') and (pilihan == 1) :                                              # jika user memilih start game dan sudah melakukan login / register
        caramain()                                                                        # cara bermain Hangman akan dicetak
        main_play()                                                                       # program akan menjalankan fungsi main_play sehingga user dapat mulai bermain
        play_again()                                                                      # program akan menjalankan fungsi play_again sehingga user dapat memilih untuk mengulang permainan atau tidak
    elif (milih == '3') :                                                                 # jika user memilih top ten
        toptenscore()                                                                     # fungsi toptenscore() akan dijalankan untuk menampilkan daftar top ten
        dataskor.clear()
        menu(pilihan)                                                                     # setelah itu, user akan dikembalikan ke menu utama
    elif (milih == '4') and (pilihan == 0) :                                              # jika user memilih info pengguna, tetapi belum melakukan login / register
        print('Harap mengisi login atau register terlebih dahulu!')                       
        print()
        menu(pilihan)                                                                     # user akan dikembalikan ke menu utama
    elif (milih == '4') and (pilihan == 1) :                                              # jika user memilih info pengguna dan sudah melakukan login / register
        infopengguna()                                                                    # fungsi infopengguna dijalankan untuk menampilkan info pengguna
        menu(pilihan)                                                                     # user akan dikembalikan ke menu utama
    elif (milih == '5') and (pilihan == 0) :                                              # jika user memilih keluar, tetapi belum pernah login / register
        print('Anda belum melakukan login atau register! Silahkan pilih menu lainnya.')   
        print()
        print()                                                                           # user akan dikembalikan ke menu utama
        menu(pilihan)
    elif (milih == '5') and (pilihan == 1) :                                              # jika user memilih keluar dan sudah pernah login/ register
        print()                                                                         
        print('Anda berhasil keluar dari permainan Hangman ini!')                         # maka user dapat keluar dari program 
        print()
    else :
        menu(pilihan)   
  



user = []

# Fungsi input_username di bawah ini bertujuan untuk login atau register dengan username

def input_username():

    # KAMUS LOKAL 
    # old : pemanggilan file eksternal main
    # taken : bool
    # username : str

    # ALGORITMA
    old = open("main", "r")               # Membaca file eksternal main
    taken = False                         # Menyatakan apakah username telah terambil atau belum.
    print('Masukkan username Anda')
    username = input("Username : ")
    for data in old.readlines():          # Pengulangan untuk membaca file eksternal main.
        if (username + "\n") == data:
            taken = True
            break
    old.close()
    if taken:                             # Saat username sudah pernah te-register.
        print("Halo " + username + "! Selamat datang kembali!")
        print()
        user.append(username)             # menambahkan username ke array user
    if not (taken):                       # Saat username belum pernah te-register.
        print("Username " + username + " belum ada \n\nSilahkan register terlebih dahulu")
        cek_username()                    # Memanggil fungsi cek_username




# Fungsi mengecek apakah username yang diinput sudah pernah digunakan pengguna lain

def cek_username() :

    # KAMUS LOKAL
    # usernamee : str
    # exist : bool
    # old0, new : pemanggilan file eksternal main
    # wordsof : pemanggilan file eksternal wordsof + usernamee

    # ALGORITMA
    usernamee = input("Buat username : ")                                     # input username
    print()
    exist = False                                                             # beri nilai boolean exist = False
    old0 = open("main", "r")                                                  # membuka file eksternal main untuk dibaca
    for data in old0.readlines() :                                            # pengulangan untuk membaca data pada file eksternal main :
        if (usernamee + "\n") == data :                                       # jika username sama dengan data pada file eksternal (yang berarti username telah digunakan oleh pengguna lain), maka :
            exist = True                                                      # beri nilai boolean exist = True
            break                                                             # pengulangan dihentikan
    old0.close()                                                              # menutup file eksternal main
    if exist == True :                                                        # jika nilai boolean exist sama dengan True (yang berarti username telah digunakan oleh pengguna lain), maka :
        print('Sudah ada pengguna lain yang menggunakan username ' + usernamee + '!' + ' Harap masukkan username lain' + '!')       # cetak bahwa sudah ada pengguna lain yang menggunakan username tersebut
        print()
        cek_username()                                                        # memanggil lagi fungsi cek_username()
    else :                                                                    # jika nilai boolean exist sama dengan False (yang berarti username belum digunakan oleh pengguna lain), maka :
        print("Register berhasil! Selamat datang " + usernamee + "!")         # cetak bahwa register berhasil
        print()
        new = open("main", "a")                                               # membuka file eksternal main untuk ditambahkan
        new.write(usernamee + "\n")                                           # menambahkan username ke file eksternal main
        new.close()                                                           # menutup file eksternal main untuk disimpan
        wordsof = open('wordsof'+usernamee, 'a')                              # membuat file eksternal wordsof + usernamee
        wordsof.close()
        user.append(usernamee)                                                # menambahkan username ke array user
    



# Fungsi memilih tema kata

def pilih_tema(hewan,buah,kota,negara,benda,semua) :

    # KAMUS LOKAL
    # Pilihan_Permainan = str
    # kata, hewan, buah, negara, benda, semua = array of str

    # ALGORITMA
    # Output tampilan pilihan tema yang tersedia
    print()
    print('Anda bisa memilih tema kata berikut ini!')
    print()
    print('========== Tema kata yang tersedia ==========')
    print('1. Hewan')
    print('2. Buah')
    print('3. Kota')
    print('4. Negara')
    print('5. Benda')
    print('6. Semua = gabungan seluruh tema di atas')
    print('=============================================')
    print()

    Pilihan_Permainan = input("Masukkan tema kata  = ")   # input tema kata yang diinginkan user

    # Percabangan menentukan list kata berdasarkan tema kata pilihan user
    if (Pilihan_Permainan == "1") :
        kata = hewan
    elif (Pilihan_Permainan == "2") :
        kata = buah
    elif (Pilihan_Permainan == "3") :
        kata = kota
    elif (Pilihan_Permainan == "4") :
        kata = negara
    elif (Pilihan_Permainan == "5") :
        kata = benda
    elif (Pilihan_Permainan == "6") :
        kata = semua
    else :
        kata = pilih_tema(hewan,buah,kota,negara,benda,semua)
    return kata




# Fungsi menampilkan cara bermain Hangman

def caramain() :

    # KAMUS LOKAL
    # tidak ada variabel khusus

    # ALGORITMA
    print()
    print('========== !! CARA BERMAIN HANGMAN !! ==========')
    print()
    print('1. Anda harus memilih tema kata terlebih dahulu dengan memasukkan nomor dari tema kata yang ditampilkan.')
    print()
    print('2. Gambar Hangman yang masih kosong akan ditampilkan dan jumlah huruf juga akan ditampilkan. ')
    print()
    print('3. Anda akan diminta untuk menebak 1 huruf atau katanya secara utuh. Misal kata "saya", maka Anda hanya bisa menebak huruf "s", "a", atau "y", atau kata "saya".')
    print('   Anda memiliki 8 kesempatan. Kesempatan akan berkurang 1 setiap kali tebakan Anda salah. Jika kesempatan Anda habis, maka Anda tidak dapat menebak lagi.')
    print('   Jika Anda menebak lebih dari 1 huruf dengan banyak huruf yang tidak sama dengan huruf pada kata, maka input Anda akan dianggap tidak valid dan Anda akan diminta menebak lagi.')
    print('   Jika Anda menebak huruf yang sudah pernah Anda tebak, maka tebakan Anda tidak akan dianggap salah dan kesempatan Anda tidak akan berkurang.')
    print()
    print('4. Setelah Anda berhasil menebak kata ataupun tidak berhasil menebak kata, maka kata dan skor Anda akan ditampilkan.')
    print('   Skor dihitung berdasarkan 100 dikurang dengan kuadrat dari jumlah kesalahan Anda. Jika kesalahan Anda sebanyak 8, maka skor Anda otomatis adalah 0.')
    print()
    print('5. Pertanyaan untuk mengulang permainan akan ditampilkan. Jika ingin mengulang permainan, maka jawab "ya", dan jika tidak ingin mengulang permainan, maka jawab "tidak".')
    print('   Permainan dapat terus diulang sampai Anda menjawab "tidak".')
    print()
    print('6. Jika Anda mengulang permainan, maka pertanyaan untuk mengganti user akan ditampilkan. Jika ingin mengganti user, maka jawab "ya", dan jika tidak ingin mengganti user, maka jawab "tidak".')
    print('   Anda dapat mengganti user ke username lama Anda ataupun membuat username baru.')
    print('   Fitur change user ini juga dapat Anda manfaatkan untuk bermain secara multiplayer.')
    print()
    print('7. Jika Anda sudah tidak mengulang permainan, maka skor tertinggi masing-masing user yang bermain akan ditampilkan.')
    print()
    print('8. Untuk masing-masing user, akan ditampilkan pertanyaan apakah ingin menyimpan skor tersebut atau tidak.')
    print('   Jika user yang ditanya ingin menyimpan skor, maka jawab "ya". Jika user yang ditanya tidak ingin menyimpan skor, maka jawab "tidak".')
    print('   Jika menjawab "ya", apabila user pernah bermain sebelumnya dengan skor sebelumnya disimpan, maka skor yang sebelumnya tersimpan akan diganti dengan skor saat ini.')
    print()
    print('================================================')
    print()




daftarscore = []
data_user_skor = []


# Fungsi permainan Hangman

def play(word):

    # KAMUS LOKAL
    # minus, kesempatan, score, index, i, val : int
    # tebakan_huruf, tebakan_kata, word_as_list : array of str
    # tebakan : boolean
    # solusi kata, menebak, key : str
    # indices : array of int
    # datauserskor : dict

    # ALGORITMA
    # Mendefinisikan variabel
    minus = 0
    solusi_kata = "-" * len(word)       # untuk menampilkan banyak huruf dengan tanda -
    tebakan = False
    tebakan_huruf = []
    tebakan_kata = []
    kesempatan = 8

    # Mencetak tampilan awal bermain Hangman
    print()
    print()
    print("===== Silahkan mulai bermain Hangman ! ======")
    print(display_hangman(kesempatan))
    print(solusi_kata)
    print('Jumlah huruf =', len(word))
    print()
  
    # Menentukan benar atau salah jawaban yang diinput user
    while not tebakan and kesempatan > 0:                       # pengulangan dilakukan selama kesempatan masih ada
        menebak = input("Tebak huruf atau kata = ").upper()         # input huruf atau kata
        print()
        if len(menebak) == 1 and menebak.isalpha():                 # jika yang ditebak berupa huruf
            if menebak in tebakan_huruf :                               # jika huruf sudah terdaftar di array tebakan_huruf (sudah pernah ditebak)
                print("Anda sudah menebak huruf", menebak, "!")
            elif menebak not in word:                                   # jika huruf tidak ada pada kata, kesempatan berkurang 1 dan minus bertambah 1
                print("Yah, tebakan Anda SALAH :(, huruf", menebak, "tidak ada pada kata. Ayo coba lagi !")
                kesempatan -= 1                                         
                minus = minus + 1                                       
                tebakan_huruf.append(menebak) 
            else:                                                       # jika huruf ada pada kata, tanda - untuk posisi huruf yang ditebak akan diganti dengan huruf yang ditebak
                print("Hebat, tebakan Anda BENAR :D, huruf", menebak, "ada pada kata. Ayo lanjutkan !")
                tebakan_huruf.append(menebak)
                word_as_list = list(solusi_kata)
                indices = [i for i, letter in enumerate(word) if letter == menebak]
                for index in indices:
                    word_as_list[index] = menebak
                solusi_kata = "".join(word_as_list)
                if "-" not in solusi_kata:
                    tebakan = True
        elif len(menebak) == len(word) and menebak.isalpha():     # jika yang ditebak berupa kata
            if menebak in tebakan_kata:                                 # jika kata sudah terdaftar di array tebakan_kata (sudah pernah ditebak)
                print("Anda sudah menebak kata", menebak, "!")
            elif menebak != word:                                       # jika huruf tidak ada pada kata, kesempatan berkurang 1 dan minus bertambah 1
                print("Yah, tebakan Anda SALAH :(, kata", menebak, "bukan kata yang dimaksud. Ayo coba lagi !")
                kesempatan -= 1
                minus = minus + 1
                tebakan_kata.append(menebak)
            else:                                                       # jika huruf ada pada kata, seluruh tanda - akan diganti dengan kata yang ditebak
                tebakan = True
                solusi_kata = word
        else:
            print("Input tidak valid")
        print(display_hangman(kesempatan))
        print(solusi_kata)
        print("\n")
    if tebakan :                                          # jika kata dapat ditebak
        print("SELAMAT, Anda berhasil menebak kata " + word + " !")
    else:                                                 # jika kata tidak berhasil ditebak
        print("Maaf, kesempatan Anda sudah habis. Kata di atas adalah " + word + ". Anda dapat mengulang permainan Hangman ini.")
    print()
    print()

    # Menghitung score
    if (minus < 8) :                            # jika minus kurang dari 8, maka :
      score = 100-(minus**2)                    # score = 100 - kuadrat dari minus
    else :                                      # jika minus lebih atau sama dengan 8, maka :
      score = 0                                 # score = 0
    daftarscore.append(score)                   # score ditambahkan ke array daftarscore

    # Mengisi array data_user_skor
    if (len(user)>0) :                          # jika banyak user lebih dari 0, maka :
        key = user[(len(user)-1)]               # key = user indeks terakhir 
        val = score                             # val = score
        datauserskor = {key : val}              # datauserskor = dictionary dari user indeks terakhir beserta scorenya
        data_user_skor.append(datauserskor)     # mengisi array data_user_skor dengan datauserskor (dictionary dari user indeks terakhir beserta scorenya)

    # Mencetak score
    print('===== Skor =====')                   
    print('Skor Anda =', score)                 # mencetak skor
    print('================')
    print()
    print()



# Fungsi menampilkan gambar Hangman

def display_hangman(kesempatan):

    # KAMUS LOKAL
    # stages : array of str

    # ALGORITMA
    stages = [  """
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |       \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |     
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |--
                   |      
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      
                   |      
                   |
                   |
                   |
                   -
                   """
              
    ]
    return stages[kesempatan]



# Menampilkan pilihan change user / ganti username kepada pemain

def change_user() :
    
    # KAMUS LOKAL
    # change : str

    # ALGORITMA
    print()
    change = input('Apakah Anda ingin melakukan change user? (Ya/Tidak)  >>>  ')
    print()
    if change.upper() == 'YA':
        input_username()                  # Menjalankan fungsi login atau register
        main_play()                       # Kemudian, menjalankan fungsi play
    elif change.upper() == 'TIDAK':
        main_play()                       # Langsung menjalankan fungsi play
    else:
        change_user()                     # Apabila pengguna salah memasukkan antara Ya/Tidak, fungsi ini akan dipanggil kembali



# Fungsi mengulang permainan Hangman kembali

def play_again() :

    # KAMUS LOKAL
    # pilihan : int

    # ALGORTIMA
    while input('Apakah Anda ingin mengulang permainan Hangman? (Ya/Tidak)  >>>  ').upper() == 'YA' :     # pengulangan selama pengguna menjawab Ya (ingin mengulang permainan Hangman kembali) :
         change_user()                                                                                    # memanggil fungsi change_user() di atas 
    print()                                                                                               # pengguna menjawab Tidak (tidak ingin mengulang permainan Hangman), maka :
    skortertinggi(data_user_skor)                                                                         # memanggil fungsi skortertinggi(data_user_skor) untuk mengolah skor tertinggi selama permainan
    cetakapakahskordisimpan()                                                                             # memanggil fungsi cetakapakahskordisimpan() untuk memproses apakah user ingin menyimpan skornya
    data_skor()                                                                                           # memanggil fungsi data_skor()
    print()                                                                                               
    pilihan = 1                                                                                           # beri nilai pilihan = 1
    menu(pilihan)                                                                                         # memanggil fungsi menu(pilihan) untuk menampilkan menu



# Fungsi menjalankan permainan Hangman

def main_play() :

    # KAMUS LOKAL
    # word : pemanggilan fungsi get_word()

    # ALGORITMA
    word = get_word()        # memanggil fungsi get_word() untuk memperoleh kata
    isi_kata(word)           # memanggil fungsi isi_kata(word) untuk membuat history word yang telah dimainkan oleh user
    play(word)               # memanggil fungsi play(word) untuk melakukan permainan Hangman



# Fungsi mengacak kata dan mengkapitalkan semua huruf dari kata yang terpilih

def get_word() :  

    # KAMUS LOKAL
    # list_kata : pemanggilan fungsi pilih_tema (hewan,buah,kota,negara,benda,semua) berupa array of str
    # carikata : pemanggilan file eksternal wordsof + user
    # historykata : array of str
    # word : pemanggilan module random untuk list_kata berupa str
    # i, j : int

    # ALGORITMA 
    list_kata = pilih_tema(hewan,buah,kota,negara,benda,semua)     # memproses fungsi pilih_tema(hewan,buah,kota,negara,benda,semua) untuk memperoleh tema yang diinginkan user
    carikata = open('wordsof'+user[(len(user)-1)], 'r')            # membuka file eksternal wordsof + user untuk dibaca
    historykata = []                                
    for line in carikata.readlines() :                             # pengulangan untuk isi setiap baris di file eksternal wordsof + user :
        historykata.append(line)                                   # tambahkan isi baris ke array historykata
    carikata.close()                                               # menutup file eksternal wordsof + user
    word = random.choice(list_kata)                                # word = memilih kata secara random berdasarkan tema yang dipilih user
    if (len(historykata) == len(list_kata)) :                      # jika jumlah indeks array historykata sama dengan jumlah indeks array tema yang dipilih user (yang berarti user telah memainkan seluruh kata pada tema tersebut), maka :
        word = word                                                # word tidak berubah
    else :                                                         # jika jumlah indeks array historykata kurang dari jumlah indeks array tema yang dipilih user (yang berarti masih ada kata yang belum dimainkan user pada tema tersebut), maka :
        for i in range(0, len(historykata)) :                      # pengulangan i dilakukan sebanyak jumlah indeks array history kata untuk melakukan pengecekan ulang pada seluruh array historykata sehingga diperoleh word yang belum pernah dimainkan user :
          for j in range(0, len(historykata)) :                    # pengulangan j dilakukan sebanyak jumlah indeks array history kata :
            while historykata[j] == word.upper() + "\n" :          # selama historykata indeks ke j sama dengan word, maka :
                word = random.choice(list_kata)                    # dilakukan pemilihan kata secara random lagi berdasarkan tema yang dipilih user
    return word.upper()                                            # mengembalikan word yang seluruh hurufnya dikapitalkan



# Fungsi menambahkan kata yang telah dimainkan user ke file eksternal wordsof + user

def isi_kata(word) : 

    # KAMUS LOKAL
    # data_kata : array of str
    # words00 : pemanggilan file eksternal wordsof + user
    # kata_kata : bool
    # i : int

    # ALGORITMA         
    data_kata = []                                              
    words00 = open('wordsof'+user[(len(user)-1)], 'r')          # membuka file eksternal wordsof + user untuk dibaca
    for line in words00.readlines() :                           # pengulangan untuk isi setiap baris di file eksternal wordsof + user :
        data_kata.append(line)                                  # tambahkan isi baris ke array data_kata
    words00.close()                                             # menutup file eksternal wordsof + user
    kata_kata = True                                            # memberi nilai boolean kata_kata = True
    if len(data_kata)>0 :                                       # jika jumlah indeks array data_kata lebih besar dari 0, maka :
        for i in range(0,len(data_kata)) :                      # pengulangan i dilakukan sebanyak jumlah indeks array data_kata :
            if data_kata[i] == word + "\n":                     # jika data_kata indeks i sama dengan word (yang berarti word sudah ada di file eksternal history kata), maka :
                kata_kata = False                               # memberi nilai boolean kata_kata = False
                break                                           # pengulangan dihentikan
    if kata_kata == True :                                      # jika kata_kata bernilai boolean True (yang berarti word belum ada), maka :
        words00 = open('wordsof'+user[(len(user)-1)], 'a')      # membuka file eksternal wordsof + user untuk ditambahkan
        words00.write(word + "\n")                              # menambahkan word di file eksternal wordsof + user
        words00.close()                                         # menutup file eksternal wordsof + user untuk disimpan




# Fungsi memperoleh skor tertinggi dari masing-masing user yang melakukan permainan Hangman, 
# sehingga program dapat digunakan juga untuk battle beberapa user dengan menggunakan username yang berbeda

def skortertinggi(data_user_skor) :

    # KAMUS LOKAL
    # i, j, val, val1, val2 : int
    # key, key1, key2 : str
    # datauserskor : array of dict
    # a : bool

    # ALGORTIMA                       
    # Mengurutkan data_user_skor dari yang tertinggi ke yang terendah
    if (len(data_user_skor)>0) :                                         # jika jumlah indeks data_user_skor lebih besar dari 0, maka :
        for i in range(0,len(data_user_skor)) :                          # pengulangan i sebanyak jumlah indeks data_user_skor : 
            for j in range(0,(len(data_user_skor)-i)) :                  # pengulangan j sebanyak jumlah indeks data_user_skor dikurang i : (untuk meletakkan skor terendah di posisi terakhir)
                for key,val in data_user_skor[j].items() :               # untuk key, value dari dictionary pada data_user_skor indeks j :
                    key1 = key                                           # beri nilai key1 = key
                    val1 = val                                           # beri nilai key2 = val
                for key,val in data_user_skor[j+i].items() :             # untuk key, value dari dictionary pada data_user_skor indeks j+i :
                    key2 = key                                           # beri nilai key1 = key
                    val2 = val                                           # beri nilai key2 = val
                if key1 == key2 :                                        # jika key1 sama dengan key2 (yang berarti username masih sama), maka :
                    if val1 < val2 :                                                                      # jika val1 lebih kecil dari val2 (nilai skor pada indeks j lebih kecil dari nilai skor pada indeks j+i), maka :
                        data_user_skor[j],data_user_skor[j+i] = data_user_skor[j+i],data_user_skor[j]     # posisi data_user_skor indeks j ditukar dengan posisi data_user_skor indeks j+i, sehingga value pada data_user_skor indeks j lebih besar daripada value pada data_user_skor indesks j+i

        # Mengambil data_user_skor yang tertinggi untuk masing-masing user 
        datauserskor = []
        for i in range(0,len(data_user_skor)) :                     # pengulangan i sebanyak jumlah indeks data_user_skor :
            a = False                                               # beri nilai boolean a = False
            for j in range(1,len(data_user_skor)-i) :               # pengulangan j mulai dari 1 sampai jumlah indeks data_user_skor dikurang i :
                for key,val in data_user_skor[i].items() :          # untuk key, value dari dictionary pada data_user_skor indeks i :
                    key1 = key                                      # beri nilai key1 = key 
                for key,val in data_user_skor[i+j].items() :        # untuk key, value dari dictionary pada data_user_skor indeks i+j :
                    key2 = key                                      # beri nilai key2 = key
                if key1 == key2 :                                   # jika key1 sama dengan key2 (yang berarti username sama), maka :
                    a = True                                        # beri nilai boolean a = True
                    break                                           # pengulangan dihentikan
            if a == True :                                      # jika nilai boolean a adalah True :
                datauserskor.append(data_user_skor[i+j])        # tambahkan data_user_skor indeks i+j ke array datauserskor (bertujuan untuk mengambil seluruh data_user_skor, kecuali data_user_skor yang berisi skor tertinggi username)
        for i in range(0,len(datauserskor)) :                   # pengulangan i sebanyak jumlah indeks datauserskor :
            data_user_skor.remove(datauserskor[i])              # data_user_skor yang terdapat di datauserskor indeks i akan dibuang, sehingga data_user_skor hanya berisi username beserta skor tertingginya




# Fungsi mengisi data user beserta skor tertingginya ke file eksternal users dan scores

def simpanskor() :

    # KAMUS LOKAL
    # skorusertinggi : pemanggilan fungsi skortertinggi(data_user_skor)
    # users0, users000 : pemanggilan file eksternal users
    # scores0, scores00, scores000 : pemanggilan file eksternal scores
    # data_users : array of str
    # data_scores : array of int
    # data : bool
    # j, val, score, baris : int
    # key, user, data_baru : str

    # ALGORITMA                                          

    # Mengisi array data_users
    users0 = open('users', 'r')                               # membuka file eksternal users untuk dibaca
    data_users = []                                       
    for line in users0.readlines() :                          # pengulangan untuk isi setiap baris di file eksternal users :
        data_users.append(line)                               # tambahkan isi baris ke array data_users
    users0.close()                                            # menutup file eksternal users

    # Mengisi array data_scores 
    scores0 = open('scores', 'r')                             # membuka file eksternal scores untuk dibaca
    data_scores = []
    for line in scores0.readlines() :                         # pengulangan untuk isi setiap baris di file eksternal scores :
        data_scores.append(line)                              # tambahkan isi baris ke array data_scores
    scores0.close()                                           # menutup file eksternal scores

    # Mengisi data_user_skor yang ingin disimpan ke file eksternal
    data = False                                              # memberi nilai boolean data = False
    if (len(data_user_skor)>0) :                              # jika jumlah indeks array data_user_skor lebih besar dari 0 (yang berarti terdapat username yang telah bermain), maka :
        for key,val in data_user_skor[indeks_user].items() :  # untuk key dan value dictionary pada data_user_skor indeks_user :
            user = key                                        # beri nilai user = key
            score = val                                       # beri nilai score = value
        if (len(data_users)>0) :                              # jika jumlah indeks array data_users lebih besar dari 0 (yang berarti terdapat username yang telah bermain sebelumnya), maka :
            for j in range(0,len(data_users)) :               # pengulangan j sebanyak jumlah indeks array data_users :
                if data_users[j] == user + "\n" :             # jika data_users indeks j sama dengan user (yang berarti username telah ada di file eksternal users), maka :
                    baris = j                                 # memberi nilai baris = j (indeks ketika data_users sama dengan user)
                    data = True                               # memberi nilai boolean data = True
                    break                                     # pengulangan dihentikan
        if data == True :                                     # jika nilai boolean data sama dengan True (yang berarti username telah ada di file eksternal users), maka :
            data_scores[baris] = str(score) + '\n'            # data_scores indeks baris diganti dengan score
            data_baru = ''.join(data_scores)                  # menggabungkan data_scores sehingga tanda kurung siku array dan koma serta spasi di dalamnya hilang
            scores00 = open('scores', 'w')                    # membuka file eksternal scores untuk diubah isinya
            scores00.write(data_baru)                         # mengubah data file eksternal scores dengan data_baru
            scores00.close()                                  # menutup file eksternal scores untuk disimpan
        elif data == False :                                  # jika nilai boolean data sama dengan False (yang berarti username belum ada di file eksternal users), maka :
            users000 = open('users', 'a')                     # membuka file eksternal users untuk ditambahkan
            scores000 = open('scores', 'a')                   # membuka file eksternal scores untuk ditambahkan
            users000.write(user + '\n')                       # menambahkan user ke file eksternal users
            scores000.write(str(score) + '\n')                # menambahkan score ke file eksternal scores
            users000.close()                                  # menutup file eksternal users untuk disimpan 
            scores000.close()                                 # menutup file eksternal scores untuk disimpan 




# Fungsi mencetak skor tertinggi masing-masing user

def skortinggi() :

    # KAMUS LOKAL
    # i, val : int
    # key : str

    # ALGORITMA
    skortertinggi(data_user_skor)                                         # memanggil fungsi skortertinggi(data_user_skor) untuk memproses skor tertinggi masing-masing user
    for i in range(0,len(data_user_skor)) :                               # pengulangan i sebanyak jumlah indeks data_user_skor :
        for key,val in data_user_skor[i].items() :                        # pengulangan mengambil username dan nilai skor dari dataindeks i-1 :
            print('Username', key, ' >>> ', 'Skor tertinggi =', val)      # mencetak username beserta skornya




# Fungsi menanyakan dan memproses apakah skor disimpan atau tidak

def apakahskordisimpan() :

    # KAMUS LOKAL
    # simpan : str

    # ALGORITMA
    simpan = input('Apakah skor username ' + pemain + ' ingin disimpan? (Ya/Tidak)  >>>  ').upper()       # menanyakan kepada user apakah skor ingin disimpan
    print()
    if simpan == 'YA' :                                                                                   # jika skor ingin disimpan, maka :
        simpanskor()                                                                                      # memanggil fungsi simpanskor() untuk memproses penyimpanan skor
        print('Skor username ' + pemain + ' telah diperbaharui')                                          # memberitahu user bahwa skor telah diperbaharui
        print()
    elif (simpan != 'YA') and (simpan != 'TIDAK') :                                                       # jika user menginput selain "ya" dan "tidak", maka :
        apakahskordisimpan()                                                                              # memanggil fungsi apakahskordisimpan() kembali



# Fungsi mencetak apakah skor ingin disimpan untuk masing-masing user

def cetakapakahskordisimpan() :

    # KAMUS LOKAL
    # i, val, indeks_user : int
    # key, pemain : str

    # ALGORITMA
    print()
    print('===== Untuk permainan Hangman pada putaran kali ini =====')
    skortinggi()                                                          # memanggil fungsi skortinggi() untuk mencetak skor tertinggi masing-masing user
    print('=========================================================')
    print()
    for i in range(0,len(data_user_skor)) :                               # pengulangan i sebanyak jumlah indeks data_user_skor :
        for key,val in data_user_skor[i].items() :                        # pengulangan mengambil username dan nilai skor dari dataindeks i-1 :
            global indeks_user                                            # global bertujuan agar variabel indeks_user dapat digunakan tidak hanya di def cetakapakahskordisimpan() saja
            indeks_user = i
            global pemain                                                 # global bertujuan agar variabel pemain dapat digunakan tidak hanya di def cetakapakahskordisimpan() saja
            pemain = key
            apakahskordisimpan()                                          # memanggil fungsi apakahskordisimpan() untuk menanyakan dan memproses apakah skor disimpan atau tidak
    print()




# Fungsi memasangkan username dengan skornya dari file eksternal users dan scores

dataskor = []
def data_skor() :

    # KAMUS LOKAL
    # data_user : array of str
    # data_score : array of int
    # users1 : pemanggilan file eksternal users
    # scores1 : pemanggilan file eksternal scores
    # i, j, val, val1, val2 : int
    # key : str
    # data_user_score : dict
    # dataa : bool

    # ALGORITMA
    # Mengambil seluruh isi data file eksternal users   
    data_user = []
    users1 = open('users', 'r')           # membuka file eksternal users untuk dibaca
    for line in users1.readlines() :      # pengulangan untuk isi setiap baris di file eksternal users :
        data_user.append(line)            # tambahkan isi baris ke array data_user
    users1.close()                        # menutup file eksternal users

    # Mengambil seluruh isi data file eksternal scores
    data_score = []
    scores1 = open('scores', 'r')         # membuka file eksternal scores untuk dibaca
    for line in scores1.readlines() :     # pengulangan untuk isi setiap baris fi file eksternal scores
        data_score.append(int(line))      # tambahkan isi baris ke data_score dalam bentuk integer
    scores1.close()                       # menutup file eksternal scores

    # Memasangkan user dengan scorenya dan menambahkannya ke array dataskor
    if (len(data_user)>0) :                                 # jika jumlah indeks data_user (banyak data di file eksternal users) lebih besar dari 0 (yang berarti terdapat username yang telah bermain sebelumnya), maka :
        for i in range(0,len(data_user)) :                  # pengulangan i sebanyak jumlah indeks data_user : (untuk mengolah seluruh isi data_user)
            key = data_user[i]                              # beri nilai key = data_user indeks i
            val = data_score[i]                             # beri nilai val = data_score indeks i
            data_user_score = {key : val}                   # data_user_score = dictionary dari key,val
            dataa = True                                    # beri nilai boolean dataa = True
            for j in range(0,len(dataskor)) :               # pengulangan j sebanyak jumlah indeks dataskor : (untuk melakukan pengecekan pada isi array dataskor)
                if dataskor[j] == data_user_score :         # jika dataskor indeks j sama dengan dictionary dari key,val (yang berarti dictionary dari key,val sudah ada di dataskor), maka :
                    dataa = False                           # beri nilai boolean dataa = False
                    break                                   # pengulangan dihentikan
            if dataa == True :                              # jika nilai boolean dataa sama dengan True (yang berarti dictionary dari key,val belum ada di dataskor), maka :
                dataskor.append(data_user_score)            # tambahkan dictionary dari key,val ke array dataskor
        
        # Mengurutkan array dataskor dari skor yang tertinggi
        for i in range(0,len(dataskor)) :                                       # pengulangan i sebanyak jumlah indeks dataskor : 
            for j in range(0,(len(dataskor)-1)) :                               # pengulangan j sebanyak jumlah indeks data_user_skor dikurang 1 : (untuk meletakkan skor terendah di posisi terakhir)
                for key,val in dataskor[j].items() :                            # untuk key dan value dari dictionary pada array dataskor indeks j :
                    val1 = val                                                  # beri nilai val1 = value
                for key,val in dataskor[j+1].items() :                          # untuk key dan value dari dictionary pada array dataskor indeks j + 1 :
                    val2 = val                                                  # beri nilai val2 = value
                if val1 < val2 :                                                # jika val1 lebih kecil dari val2 (nilai skor pada indeks j lebih kecil dari nilai skor pada indeks j + 1), maka :
                    dataskor[j], dataskor[j+1] = dataskor[j+1], dataskor[j]     # tukar posisi dataskor indeks j dengan posisi dataskor indeks j + 1, sehingga value pada dataskor indeks j lebih besar daripada value pada dataskor indesks j+1



# Fungsi mengolah pencetakan 10 skor tertinggi pertama, sehingga :
# Apabila skor tertinggi ke-11 sama dengan skor tertinggi ke-10, maka skor tertinggi ke-11 tidak akan dicetak

def cetaktopten(dataskor) :
    
    # KAMUS LOKAL
    # i, val : int
    # key : str

    # ALGORITMA
    print()
    print('===== FIRST TOP TEN =====')
    if (0 < len(dataskor) < 10) :                                                   # jika jumlah indeks dataskor lebih besar dari 0 dan kurang dari 10, maka :
        for i in range(1,len(dataskor)+1) :                                         # dilakukan pengulangan indeks i dari skor tertinggi pertama sampai skor tertinggi akhir pada array dataskor
            for key, val in dataskor[i-1].items() :                                 # pengulangan mengambil username dan nilai skor indeks i-1 :
                key = key.strip()                                                   # menghilangkan ganti baris
                print(str(i) + '.', 'Username', key, ' >>> ', 'Skor =', val)        # cetak username beserta nilai skornya
    else :                                                                          # jika jumlah indeks dataskor lebih atau sama dengan sepuluh, maka :
        for i in range(1,11) :                                                      # dilakukan pengulangan indeks i dari skor tertinggi pertama sampai skor tertinggi sepuluh
            for key, val in dataskor[i-1].items() :                                 # pengulangan mengambil username dan nilai skor indeks i-1
                key = key.strip()                                                   # menghilangkan ganti baris pada key
                print(str(i) + '.', 'Username', key, ' >>> ', 'Skor =', val)        # mencetak username beserta nilai skornya                     
    print('=========================')
    print()



# Fungsi melakukan pencetakan 10 skor tertinggi pertama

def toptenscore() :
    
    # KAMUS LOKAL
    # pilihan : int

    # ALGORITMA
    pilihan = 1                                                                         # beri nilai pilihan sama dengan 1
    data_skor()                                                                         # memanggil fungsi data_skor()
    if (len(dataskor)==0) :                                                             # jika jumlah indeks dataskor sama dengan 0, maka :
        print('Belum ada skor pengguna yang tersimpan dalam permainan Hangman ini.')    # cetak bahwa belum ada pengguna yang memainkan permainan Hangman ini
        print()
    else :                                                                              # jika jumlah indeks dataskor lebih besar dari 0, maka :                                   
        cetaktopten(dataskor)                                                           # memanggil fungsi cetaktopten(dataskor) untuk mencetak 10 skor tertinggi pertama



# Fungsi menampilkan info pengguna 
def infopengguna() :

    # KAMUS LOKAL
    # pilihan, i, j, val : int
    # usersama : array of str
    # key, pengguna : str
    # b, same : bool

    # ALGORITMA
    pilihan = 1                                                               # beri nilai pilihan sama dengan 1
    data_skor()                                                               # memanggil fungsi data_skor()
    usersama = []
    
    # Membuang username yang sama pada array user
    for i in range(0,len(user)) :              # pengulangan i sebanyak jumlah indeks user :
        b = False                              # beri nilai boolean b = False
        for j in range(1,len(user)-i) :        # pengulangan j dari 1 sampai jumlah indeks user dikurang i :
            if user[i] == user[i+j] :          # jika user indeks i sama dengan user indeks i+j (yang berarti username sama), maka :
                b = True                       # beri nilai boolean b = True
                break                          # pengulangan dihentikan
        if b == True :                         # jika nilai boolean b adalah True, maka :
            usersama.append(user[i+j])         # tambahkan user indeks i+j ke array usersama (bertujuan untuk mengambil username yang ada lebih dari 1)
    for i in range(0,len(usersama)) :          # pengulangan i sebanyak jumlah indeks usersama :
        user.remove(usersama[i])               # username yang terdapat di usersama indeks i akan dibuang, sehingga tidak ada username yang sama pada array user
    
    # Menampilkan info pengguna
    print('====== INFO PENGGUNA ======')                                
    # Menampilkan skor yang tersimpan
    print('--- Skor Tersimpan ---')
    if (len(dataskor) > 0) :                                            # jika jumlah indeks array dataskor lebih besar dari 0, maka :
        for i in range(0,len(user)) :                                   # pengulangan i sebanyak jumlah indeks array user :
            for j in range(0,len(dataskor)) :                           # pengulangan j sebanyak jumlah indeks array dataskor :
                same = False                                            # beri nilai boolean same = False
                for key,val in dataskor[j].items() :                    # untuk key, value dari dictionary pada dataskor indeks j :
                    key = key.strip()                                   # strip untuk menghilangkan ganti baris pada key
                if user[i] == key :                                     # jika user indeks i sama dengan key (yang berarti username terdapat pada dictionary dataskor), maka :
                    same = True                                         # beri nilai boolean same = True
                    break                                               # pengulangan dihentikan
            if same == True :                                           # jika same bernilai boolean True (username terdapat pada dictionary dataskor), maka :
                print('Username', key, ' >>> ', 'Skor terakhir Anda yang tersimpan =', val)   # cetak username beserta skornya
            else :                                                      # jika same bernilai boolean False (username tidak ada pada dictionary dataskor), maka :
                pengguna = user[i]                                      # pengguna adalah user indeks i
                print('Skor username', pengguna, 'belum pernah tersimpan')     # cetak bahwa skor user belum pernah tersimpan
    else :                                                              # jika jumlah indeks array dataskor sama dengan 0, maka :
        print('Skor Anda belum pernah tersimpan')                       # cetak bahwa skor user belum pernah tersimpan
    print()
    # Menampilkan skor tertinggi untuk satu run
    print('--- Skor Tertinggi pada Putaran Permainan ini ---')
    if (len(data_user_skor)==0) :                                                           # jika jumlah indeks data_user_skor sama dengan 0 (yang berarti user belum start game), maka :
        print('Skor Anda tidak ada karena Anda belum memainkan permainan Hangman ini.')     # cetak bahwa pengguna belum memainkan permainan Hangman ini
    else :                                                                                  # jika jumlah indeks dataskor lebih besar dari 0, maka :
        skortinggi()                                                                        # memanggil fungsi skortinggi() untuk mencetak masing-masing user beserta skor tertingginya
    print('==========================')
    print()
    dataskor.clear()                                                                        # menghapus seluruh elemen array dataskor



# Program utama dijalankan dengan :
    
menu(pilihan)     # memanggil fungsi menu(pilihan)
