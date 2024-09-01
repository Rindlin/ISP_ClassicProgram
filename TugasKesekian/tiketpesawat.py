import os
proses = True

def daftar_menu():
        print("=================================="
              "\nDaftar Tiket Pesawat yang Tersedia"
              "\n=================================="
              "\n1. Semarang-Jakarta"
              "\n2. Semarang-Surabaya"
              "\n3. Semarang-Medan"
              "\n4. Semarang-Balikpapan"
              "\n=================================="
              "\nKetik 0 untuk Keluar")
    
def pemesanan():
        jum_tiket = int(input("Masukkan Jumlah tiket: "))
        numArray = list()
        num = input("berapa orang yang ingin memesan tiket: ")
        print("masukkan nama pemesan: ")
        for i in range (int(num)):
            i+=1
            n = input("orang ke {}: ".format(i))
            numArray.append(str(n))
        tot_tiket = jum_tiket*harga
        os.system('cls')
        print("\n============================================="
              "\nAnda telah berhasil melskuksn pembelian tiket"
              "\n============================================="
              "\nNama pemesan:{}".format(len(numArray)))
        for x in numArray:
                print(("-{}").format(x))
        print("Total Harga","Rp.",(tot_tiket))

while proses:
    daftar_menu()
    kota = int(input("Masukkan Pilihan [1-4]: "))

    if ((kota)==1):
        print("\n============================================="
              "\nKode  Nama\tKota\t\tHarga"
              "\n      Pesawat\tTujuan\t\tTiket"
              "\n============================================="
              "\n101.  Garuda\tJakarta \tRp950.000"
              "\n102.  Lion Air\tJakarta \tRp800.000"
              "\n103.  Sriwijaya\tJakarta \tRp650.000"
              "\n=============================================")
        noPesawat= int(input("Masukkan kode penerbangan: "))

        if ((noPesawat)==101):
            harga = 950000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        elif ((noPesawat)==102):
            harga = 800000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        elif ((noPesawat)==103):
            harga = 650000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        else:
            os.system('cls')
            print("Kode penerbangan tidak terdaftar")
    elif ((kota)==2):
        print("\n============================================="
              "\nKode  Nama\tKota\t\tHarga"
              "\n      Pesawat\tTujuan\t\tTiket"
              "\n============================================="
              "\n201.  Garuda\tSurabaya \tRp825.000"
              "\n202.  Lion Air\tSurabaya \tRp754.000"
              "\n203.  Sriwijaya\tSurabaya \tRp640.000"
              "\n=============================================")
        noPesawat= int(input("Masukkan kode penerbangan: "))

        if ((noPesawat)==201):
            harga = 825000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        elif ((noPesawat)==202):
            harga = 754000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        elif ((noPesawat)==203):
            harga = 640000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        else:
            os.system('cls')
            print("Kode penerbangan tidak terdaftar")
    elif ((kota)==3):
        print("\n============================================="
              "\nKode  Nama\tKota\t\tHarga"
              "\n      Pesawat\tTujuan\t\tTiket"
              "\n============================================="
              "\n301.  Garuda\tMedan \tRp1.450.000"
              "\n302.  Lion Air\tMedan \tRp1.150.000"
              "\n303.  Sriwijaya\tMedan \tRp850.000"
              "\n=============================================")
        noPesawat= int(input("Masukkan kode penerbangan: "))

        if ((noPesawat)==301):
            harga = 1450000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        elif ((noPesawat)==302):
            harga = 1150000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        elif ((noPesawat)==303):
            harga = 850000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        else:
            os.system('cls')
            print("Kode penerbangan tidak terdaftar")
    elif ((kota)==4):
        print("\n============================================="
              "\nKode  Nama\tKota\t\tHarga"
              "\n      Pesawat\tTujuan\t\tTiket"
              "\n============================================="
              "\n401.  Garuda\tBalikpapan \tRp2.200.000"
              "\n402.  Lion Air\tBalikpapan \tRp1.800.000"
              "\n403.  Sriwijaya\tBalikpapan \tRp1.500.000"
              "\n=============================================")
        noPesawat= int(input("Masukkan kode penerbangan: "))

        if ((noPesawat)==401):
            harga = 2200000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        elif ((noPesawat)==402):
            harga = 1800000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        elif ((noPesawat)==403):
            harga = 1500000
            print("\n"
                  "\n============================================="
                  "\nAnda memilih kode penerbangan", int(noPesawat),
                  "\n=============================================")
            pemesanan()
        else:
            os.system('cls')
            print("Kode penerbangan tidak terdaftar")
    elif ((kota)==0):
        os.system('cls')
        exit()
    else:
        os.system('cls')
        print("***Pilihan Tidak Ada***")



    