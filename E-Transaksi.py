# mendeklrasikan variabel program untuk menyimpan nama file CSV yang akan digunakan untuk menyimpan data transaksi.
program = "e-transaksi.csv"

#menggunakan infinite loop terus menampilkan menu transaksi dan menunggu input dari pengguna. 
#Loop ini akan berlanjut sampai pengguna memilih untuk keluar, yaitu menu no 4
while True:
    #menampilkan output "E-Transaksi" di terminal
    print("\n", "="*26, "\n|", " "*5, "E-TRANSAKSI", " "*5, "|", "\n", "="*26)
    #menampilkan output menu di terminal agar user bisa mengetahui menu apa yang ingin diakses
    print("\tMenu: ", "\n1. Menampilkan data transaksi", "\n2. Menambah transaksi", "\n3. Menghapus transaksi", "\n4. Keluar")
    #meminta user menginputkan nomer menu yang ingin dijalankan, dan menyimpannya dalam variabel menu
    menu = int(input("Pilih menu yang diinginkan: "))
    #menggunakan kondisi if, jika nomer menu yang diinput adalah 1, maka akan menjalankan perintah:
    if menu == 1:
        #untuk menampilkan pesan keterangan di terminal
        print("Tanggal;Barang;Jumlah Barang;Total Harga")
        #membuka file CSV dan membaca isinya
        with open(program, 'r') as file:
            #mencetak/menampilkan data file ke terminal
            print(file.read())
    #jika nomer menu yang diinput adalah 2 maka akan menjalankan perintah:
    elif menu == 2:
        #menggunakan infinite loop, yang akan terus menampilkan opsi menambahkan transaksi hingga
        #user memilih untuk tidak ingin transaksi lagi (n)
        while True: 
            #meminta user menginputkan tanggal transaksi, dan menyimpannya dalam variabel tanggal
            tanggal = input("Masukkan tanggal transaksi dilakukan: ")
            #meminta user menginputkan barang yang ditransaksi, dan menyimpannya dalam variabel nama_barang
            nama_barang = input("Masukkan barang yang dibeli: ")
            #menggunakan infinite loop untuk terus menampilkan input harga dan jumlah barang apabila input tidak valid
            while True:
                #meminta user menginputkan harga barang yang ditransaksi, dan menyimpannya dalam variabel harga
                harga = int(input("Masukkan harga barang: "))
                #meminta user menginputkan jumlah barang yang ditransaksi, dan menyimpannya dalam variabel jumlah_barang
                jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
                #jika harga atau jumlah yang diinput bernilai 0 atau negatif, maka akan menjalankan perintah:
                if harga <= 0 or jumlah_barang <= 0:
                    #menampilkan "Invalid Input, Masukkan bilangan bulat positif" 
                    print("Invalid Input, Masukkan bilangan bulat positif")
                #jika input sesuai, maka loop akan berhenti
                else:
                    break
            #menghitung total harga transaksi dengan mengkalikan variabel harga dan jumlah_barang lalu 
            #disimpan pada variabel total_harga 
            total_harga = harga*jumlah_barang
            #mendeklarasikan variabel transaksi yang berisi gabungan string dari tanggal, nama_barang, 
            #jumlah_barang, dan total harga
            transaksi = f"{tanggal};{nama_barang};{jumlah_barang};{total_harga}\n"
            #membuka file CSV dan meng-append atau menambahkan data baru ke akhir file tanpa menghapus yang sudah ada
            with open(program, 'a') as file:
                #menulis string transaksi ke file yang dibuka.
                file.write(transaksi)
            #menampilkan pesan "Berhasil menambahkan transaksi" di terminal
            print("Berhasil menambahkan transaksi.")
            #meminta user menginputkan y/n dan menyimpannya dalam variabel transaksilagi
            transaksilagi = input("Apakah masih ada transaksi yang ingin ditambahkan? (y/n): ")
            #selama nilai dari transaksilagi adalah "y" atau "n", maka akan menjalankan tugas:
            while transaksilagi != "y" and transaksilagi != "n":
                #meminta user menginputkan y/n dan menyimpannya dalam variabel transaksilagi
                transaksilagi = input("Apakah masih ada transaksi yang ingin ditambahkan? (y/n): ")
            #jika nilai dari transaksilagi adalah "n", maka loop akan berhenti
            if transaksilagi == "n":
                break
    #jika nomer menu yang diinput adalah 3 maka akan menjalankan perintah:
    elif menu == 3:
        #menggunakan infinite loop untuk terus menampilkan data yang suda ada dan meminta input nomer
        #data yang dihapus apabila input tidak valid
        while True:
            #menampilkan pesan "Data saat ini yaitu:" di terminal
            print("Data saat ini yaitu: ")
            #untuk menampilkan pesan keterangan di terminal
            print("Tanggal;Barang;Jumlah Barang;Total Harga")
            #membuka file CSV dan membaca isinya
            with open(program, 'r') as file:
                #membaca semua baris dalam file dan menyimpannya dalam bentuk daftar (list) dalam variabel data. 
                #Setiap elemen daftar akan berisi satu baris dari file.
                data = file.readlines()
            #menggunakan loop for, dimana untuk setiap baris data akan melakukan perintah, 
            #Fungsi enumerate() digunakan untuk mendapatkan indeks baris saat ini dan baris itu sendiri dalam setiap iterasi loop.
            for i, line in enumerate(data):
                #menampilkan indeks baris yang ditambah 1 dan isi baris tersebut ke terminal
                print(i+1, ". ", line)
            #meminta user menginputkan nomer data yang ingin dihapus, dan menyimpannya dalam variabel delete
            delete = int(input("Masukkan nomor data yang ingin dihapus: "))
            #menggunakan kondisi yang memeriksa apakah nomor yang dimasukkan oleh pengguna berada
            #dalam kisaran nomor data yang ada (dari 1 hingga jumlah baris data), jika 
            if delete >= 1 and  delete < len(data)+1:
                #menghapus nilai yang ada di list data (yaitu 1 baris data) sesuai dengan indeks yang diinginkan 
                #karena nilai delete/inputan dari user itu indeks-1, maka diperlukan delete-1 agar sesuai dengan
                #indeks data yang ingin dihapus
                data.pop(delete-1)
                #membuka file kembali, dengan mode w/write, yaitu meng-overwrite data sebelumnya
                with open(program, 'w') as file:
                    #Karena satu baris telah dihapus, maka menulis ulang file dengan variabel data
                    #yang berisi data-data tanpa baris data yang sudah dihapus tadi
                    file.writelines(data)
                #menampilkan pesan "Data berhasil dihapus." di terminal
                print("Data berhasil dihapus.")
                #jika nomer yang diinput sesuai dan data berhasil dihapus, loop akan berhenti
                break
            #jika nomer yang diinput tidak sesuai, maka akan menjalankan perintah
            else:
                #menampilkan pesan "Invalid indeks" di terminal
                print("Invalid indeks.")
    #jika nomer menu yang diinput adalah 4 maka akan menjalankan perintah:
    elif menu == 4:
        #menampilkan pesan "Terimakasih telah melakukan transaksi" di terminal
        print("Terimakasih telah melakukan transaksi")
        #loop akan berhenti, program juga akan berhenti
        break
    #jika nomer menu yang diinput adalah selain 1,2,3,4 maka akan menjalankan perintah:
    else:
        #menampilkan pesan "Invalid Input. Please try again." di terminal
        print("Invalid Input. Please try again.")
    

