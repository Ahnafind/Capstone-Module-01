
#Stock Gudang Logistik XYZ by Ahnaf


# Berikut adalah menu yang akan tampil ketika program dijalankan
Menu = ['1. Summary Stock Logistik XYZ',
        '2. Input Stock Data di Gudang',
        '3. Mengubah Stock Data di Gudang',
        '4. Output Stock Data di Gudang',
        '5. Exit']
#Stock disini menunjukan stock default yang ada pada program saat ini
#SOP membaca atau menulis kode
#Contoh SPCA1: SP = Nama (Sabun dengan Merk P), PC adalah Jenis, dan A1 adalah Lokasi
#SOP membaca atau menulis pada jenis barang
#PC = Personal Care, FC = Food Care, dan HC = Home Care
#SOP membaca atau menulis pada Lokasi barang
#Contoh PA1 menandakan Pallet A di Tier (tingkatan) 01

Stock = [{'Kode' : 'SAPCA1', 
          'Nama' : 'Sabun-A   ', 
          'Jenis' : 'PC',
          'Qty' : 10, 
          'Lokasi' : 'PA1'
          },
        {'Kode' : 'SPPCA2', 
          'Nama' : 'Sabun-P   ', 
          'Jenis' : 'PC',
          'Qty' : 10, 
          'Lokasi' : 'PA2'
          },
         {'Kode' : 'MBFCB1', 
          'Nama' : 'Minuman-B ', 
          'Jenis' : 'FC',
            'Qty' : 15, 
            'Lokasi' : 'PB1'
            },
        {'Kode' : 'MBFCB2', 
          'Nama' : 'Makanan-A ', 
          'Jenis' : 'FC',
            'Qty' : 25, 
            'Lokasi' : 'PB2'
            },
         {'Kode' : 'DWHCC3', 
          'Nama' : 'Detergen-W', 
          'Jenis' : 'HC',
          'Qty' : 20 , 
          'Lokasi' : 'PC3'
          },
                ]

#Main Menu pada Program
def Main_Menu () :
    MainMenu = True
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

#Stock Menu untuk No.1 untuk menampilan dan mencari barang pada Stock Gudang (Read)
def Stock_Menu () :
    StockMenu = True
    while StockMenu != '3' :
        print ('\n --- Stock Menu Gudang XYZ Logistik')
        print ('1. Stock Gudang XYZ Logistik Keseluruhan')
        print ('2. Stock Gudang Berdasarkan Kriteria')
        print ('3. Kembali ke Menu Utama')
        StockMenu = input('Silahkan Pilih Menu Stock Gudang : ')

        if StockMenu == '1':
            
            if len(Stock) != 0:
                
                print('\n List Stock Gudang: ')
                print('Kode\t| Nama \t     | Jenis\t| Qty \t| Lokasi')
                for j, i in enumerate (Stock):
                    print(f"{i['Kode']}  | {i['Nama']} | {i['Jenis']}       | {i['Qty']}    | {i['Lokasi']}")

            else :
                print ('\n --- Stock Tidak Ada di Gudang')
            
            continue
        elif StockMenu == '2':
            if len(Stock) !=0 :
                std = input('Masukan Kode Barang :').upper()
                print (f"Stock Barang dengan Kode : {std}")
                print('Kode\t| Nama \t     | Jenis\t| Qty \t| Lokasi')
                for j, i in enumerate (Stock):
                    if i ['Kode'] == std :
                        print(f"{i['Kode']}  | {i['Nama']} | {i['Jenis']}       | {i['Qty']}    | {i['Lokasi']}")
                        break
                else : 
                    print('Tidak ada Barang')
        elif StockMenu == '3':
            break
        else :
            print('\n Pilihan Menu Tidak ada')

#SOP membaca atau menulis kode
#Contoh SPCA1: SP = Nama (Sabun dengan Merk P), PC adalah Jenis, dan A1 adalah Lokasi
#SOP membaca atau menulis pada jenis barang
#PC = Personal Care, FC = Food Care, dan HC = Home Care
#SOP membaca atau menulis pada Lokasi barang
#Contoh PA1 menandakan Pallet A di Tier (tingkatan) 01
            
#Create Menu untuk No.2 untuk Melakukan input Stock Gudang (Create)
def Create_Menu ():
    while True :
        print('\n --- Menambah Stock di Gudang ---')
        print('1. Input Barang yang ingin di masukan ke dalam stock')
        print('2. Kembali ke menu utama')
        CreateMenu = input ('Silahkan Pilih Menu untuk Menambah Stock Gudang : ')

        if CreateMenu == '1':
            if len(Stock) != 0:
                addKode = input('Masukan Code Barang: ').upper()
                for j, i in enumerate (Stock):
                    if addKode == i['Kode']:
                        print ('Barang Sudah terdaftar')
                        break
                else:
                    addNama = input('Masukan Nama Barang: ').upper()
                    addJenis = input('Masukan Nama Jenis: ').upper()
                    addQty = input('Masukan Nama Qty: ').upper()
                    addLoc = input('Masukan Nama Loc: ').upper()

                    tambahan = {
                        'Kode' : '{}'.format(addKode),
                        'Nama' : '{}'.format(addNama),
                        'Jenis' : '{}'.format(addJenis),
                        'Qty' : '{}'.format(addQty),
                        'Lokasi' : '{}'.format(addLoc)
                    }
                    print('\n Barang yang ditambhakan adalah: ',tambahan)
                    checkerCreate = input('\nApakah Sudah Benar? (Y/N): ').upper()
                    if checkerCreate == 'Y':
                        Stock.append(tambahan)
                        print('\n ---Barang sudah masuk ke dalam Stock Gudang ---')
                    elif checkerCreate == 'N':
                        print('\n ---Barang gagal masuk ke dalam Stock Gudang ---')
                    else:
                        continue

        elif CreateMenu == '2':
            break

        else:
            print('\n ---Pilihan Menu Tidak Ada ---')
            continue

#Update Menu untuk No.3 untuk Melakukan Update Stock Gudang (Update)
#Update Menu juga bisa berguna saat proses inbound dan outbound pada Gudang
def Update_Menu ():
    UpdateMenu = True
    while UpdateMenu != '2' :
        print('\n --- Mengubah Stock di Gudang ---')
        print('1. Mengubah stock barang')
        print('2. Kembali ke menu utama')
        UpdateMenu = input ('Silahkan Pilih Menu untuk Update Data Stock Gudang : ')

        if UpdateMenu =='1':
            if len(Stock) !=0:
                updateKode = input('Masukan Kode Barang: ').upper()

                for i in range(len(Stock)):
                    if updateKode == Stock[i]['Kode'] :
                        print ('Barang yang ingin diubah sebagai berikut: ', Stock[i])
                        namaUpdate = input('\n Masukan kolom yang akan diubah: ').lower()

                        if namaUpdate == 'kode':
                            ubahKode = input('\nUpdate Kode Barang:').upper()
                            checkKode = input('\nData yang akan diubah? (Y/N): ').lower()
                            if checkKode ==  'y':
                                Stock[i]['Kode'] = ubahKode
                                print('\n Data Sudah Ter-Update ')
                                break
                            elif checkKode == 'n':
                                print('\n Data gagal di Update')

                        if namaUpdate == 'nama':
                            ubahNama = input('\nUpdate Nama Barang:').upper()
                            checkNama = input('\nData yang akan diubah? (Y/N): ').lower()
                            if checkNama ==  'y':
                                Stock[i]['Nama'] = ubahNama
                                print('\n Data Sudah Ter-Update ')
                                break
                            elif checkNama == 'n':
                                print('\n Data gagal di Update')

                        if namaUpdate == 'jenis':
                            ubahJenis = input('\nUpdate Jenis Barang:').upper()
                            checkJenis = input('\nData yang akan diubah? (Y/N): ').lower()
                            if checkJenis ==  'y':
                                Stock[i]['Jenis'] = ubahJenis
                                print('\n Data Sudah Ter-Update ')
                                break
                            elif checkJenis == 'n':
                                print('\n Data gagal di Update')

                        if namaUpdate == 'quantity':
                            ubahQTY = input('\nUpdate Quantity Barang:').upper()
                            checkQTY = input('\nData yang akan diubah? (Y/N): ').lower()
                            if checkQTY ==  'y':
                                Stock[i]['Quantity'] = ubahQTY
                                print('\n Data Sudah Ter-Update ')
                                break
                            elif checkQTY == 'n':
                                print('\n Data gagal di Update')

                        if namaUpdate == 'lokasi':
                            ubahLokasi = input('\nUpdate Lokasi Barang:').upper()
                            checkLokasi = input('\nData yang akan diubah? (Y/N): ').lower()
                            if checkLokasi ==  'y':
                                Stock[i]['Lokasi'] = ubahLokasi
                                print('\n Data Sudah Ter-Update ')
                                break
                            elif checkLokasi == 'n':
                                print('\n Data gagal di Update')
                else:
                    print ('\n --- Mohon input pilihan menu sesuai dengan pilihan yang disediakan ---')

#Delete Menu untuk No.4 untuk Melakukan Menghapus Stock Gudang (Delete)
def Delete_Menu ():
    DeleteMenu = True
    while DeleteMenu !='2':
        print('\n --- Delete Stock di Gudang yang sudah tidak dibutuhkan ---')
        print('1. Menghapus stock barang')
        print('2. Kembali ke menu utama')
        DeleteMenu = input ('Silahkan Pilih Menu untuk Menghapus Data Stock Gudang : ')
        
        if DeleteMenu == '1':
            if len(Stock) !=0:
                delCode = input('\n Masukan untuk Kode Barang yang akan dihapus: ').upper()
                for i in range(len(Stock)):
                    if delCode == Stock[i]['Kode']:
                        print('\n Barang yang akan dihapus adalah: ', Stock[i])
                        checkDel = input('\n Apakah data ini akan dihapus di dalam stock? (Y/N): ').lower()
                        if checkDel == 'y':
                            del Stock[i]
                            print('\n Barang berhasil dihapus dari dalam stock')
                            break
                        elif checkDel == 'n':
                            print('\n Barang gagal dihapus dari dalam stock')
                            break
                        else:
                            print('--- Mohon input pilihan menu sesuai dengan pilihan yang disediakan ---')
                    else:
                        print('\n Barang tidak ditemukan!')
                else:
                    print ('\n Barang sudah tidak ada di Stock')
            elif DeleteMenu == '2':
                break
            else:
                print('\n ---Pilihan Menu Tidak ada')

                

Main_Menu ()




                        




                    

