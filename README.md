# Capstone-Module-01
## Capstone Project Module 01 dengan Study Case Stock Gudang
Kita semua tau bahwa industri Logistik sangatlah besar di Indonesia ini.
Salah satu yang menjadi CORE BUSINESS di Logistik adalah Warehouse.
Warehouse merupakan tempat atau point dimana barang disimpan di ruangan yang besar.
Dalam menyimpan suatu barang didalam ruangan atau yang kita sebut Gudang pastinya harus kita monitoring agar Outbound (barang keluar) dan Inbound (barang masuk) berjalan dengan sempurna.
Sebagai pengelola gudang diperlukan monitoring yang ketat sehingga kerugian (Bad Expense) perusahaan tidak meningkat.
Maka dibuatlah sebuah program sederhana untuk melakukan monitoring pada sebuah Gudang dimana pada Study Case Kali ini Gudang XYZ yang akan menjadi perusahaan menggunakan program ini.

## Berikut Menu Program Sederhana yang akan ditampilkan saat program dijalankan
### MainMenu = True
    while MainMenu != '5' :
        print('\n --- Stock Data Gudang XYZ Logistik ---\n')
        for i in Menu :
            print(i)
        MainMenu = input('Silahkan Ketik Menu: ')
        if MainMenu == '1' :
            Stock_Menu ()
        elif MainMenu == '2' :
            Create_Menu ()
        elif MainMenu == '3' :
            Update_Menu ()
        elif MainMenu == '4' :
            Delete_Menu ()
        elif MainMenu == '5' :
            print ('\n Terima Sudah Telah Melihat Stock Gudang XYZ Logistik')
            break
            
### No.1 Menampilan dan mencari barang pada Stock Gudang (Read)
Di Step ini program akan menjalankan fungsi untuk melihat Stock Gudang XYZ secara keseluruhan atau mencari barang berdasarkan kode.
#### Terdapat 3 Opsi Yaitu :
        print ('\n --- Stock Menu Gudang XYZ Logistik')
        print ('1. Stock Gudang XYZ Logistik Keseluruhan')
        print ('2. Stock Gudang Berdasarkan Kriteria')
        print ('3. Kembali ke Menu Utama')
        StockMenu = input('Silahkan Pilih Menu Stock Gudang : ')
### No.2 Melakukan input Stock Gudang (Create)
Kemudian disini program bermaksud untuk melakukan input barang saat adanya proses inboound pada Warehouse.
#### Terdapat 2 Opsi Yaitu :
        print('\n --- Menambah Stock di Gudang ---')
        print('1. Input Barang yang ingin di masukan ke dalam stock')
        print('2. Kembali ke menu utama')
        CreateMenu = input ('Silahkan Pilih Menu untuk Menambah Stock Gudang : ')

### No.3 Melakukan Update Stock Gudang (Update)
Kemudian disini program bermaksud untuk melakukan output barang saat adanya proses outbound pada Warehouse.
#### Terdapat 2 Opsi Yaitu :
        print('\n --- Mengubah Stock di Gudang ---')
        print('1. Mengubah stock barang')
        print('2. Kembali ke menu utama')
        UpdateMenu = input ('Silahkan Pilih Menu untuk Update Data Stock Gudang : ')

### No.4 Melakukan Menghapus Stock Gudang (Delete)
Lalu untuk penghapusan stock pada gudang bisa menggunakan program disini.
#### Terdapat 3 Opsi Yaitu :
        print('\n --- Delete Stock di Gudang yang sudah tidak dibutuhkan ---')
        print('1. Menghapus stock barang')
        print('2. Kembali ke menu utama')
        DeleteMenu = input ('Silahkan Pilih Menu untuk Menghapus Data Stock Gudang : ')

### No.5 Exit dari Program

##### Untuk Lebih Jelasnya bisa dilihat di file Final_CP_Ahnaf022024.py.

## Terima Kasih
