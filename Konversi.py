import os

def main():
    Pilihan = input(
        "Masukkan Pilihan :\n"
        "(B) Konversi Bilangan\n"
        "(S) Konversi Suhu\n"
        "(P) Perulangan Bentuk\n"
        "(B/S/P)? "
    )
    if Pilihan.title() == "S":
        print("Program konversi Suhu dari Celcius")
        C = int(input("Masukkan Suhu dalam Celcius: "))
        X = input("Konversi ke K/R/F: ")
        konversi(C, X)
    elif Pilihan.title() == "B":
        print("Program konversi Desimal, Binary, Octal, Hexadecimal")
        print("Angka Binary diawali 0b, Hexa diawali 0x, Oktal diawali 0o")
        print("Pilih [1] untuk Desimal ke Binary")
        print("Pilih [2] untuk Desimal ke Hexa")
        print("Pilih [3] untuk Desimal ke Octal")
        print("Pilih [4] untuk Binary ke Desimal")
        print("Pilih [5] untuk Binary ke Hexa")
        print("Pilih [6] untuk Binary ke Oktal")
        print("Pilih [7] untuk Hexa ke Binary")
        print("Pilih [8] untuk Hexa ke Desimal")
        print("Pilih [9] untuk Hexa ke Octal")
        print("Pilih [10] untuk octal ke Binary")
        print("Pilih [11] untuk octal ke Desimal")
        print("Pilih [12] untuk octal ke Hexa")
        i = int(input("Masukkan pilihan anda: "))
        con_bil(i)
    elif Pilihan.title() == "P":
        print("Program perulangan bentuk")
        print("Pilih [1] Bentuk Piramida")
        print("Pilih [2] Bentuk Belah Ketupat")
        i = int(input("Masukkan pilihan anda:"))
        bentuk(i)
    else:
        print("Error!")


def konversi(C, X):
    if X.title() == "K":
        K = C + 273
        print("%d Celcius itu %d Kelvin" % (C, K))
    elif X.title() == "R":
        R = (4 / 5) * C
        print("%d Celcius itu %d Reamur" % (C, R))
    elif X.title() == "F":
        F = ((9 / 5) * C) + 32
        print("%d Celcius itu %d Fahrenheit" % (C, F))
    else:
        print("ERROR!")
    konfirmasi()


def con_bil(i):
    if i == 1:
        x = int(input("masukkan angka Desimal: "))
        print(bin(x))
    elif i == 2:
        x = int(input("masukkan angka Desimal: "))
        print(hex(x))
    elif i == 3:
        x = int(input("masukkan angka Desimal: "))
        print(oct(x))
    elif i == 4:
        x = int(input("masukkan angka Binary: "), 2)
        print(x)
    elif i == 5:
        x = int(input("masukkan angka Binary: "), 2)
        print(hex(x))
    elif i == 6:
        x = int(input("masukkan angka Binary: "), 2)
        print(oct(x))
    elif i == 7:
        x = int(input("masukkan angka Hexa: "), 16)
        print(bin(x))
    elif i == 8:
        x = int(input("masukkan angka Hexa: "), 16)
        print(x)
    elif i == 9:
        x = int(input("masukkan angka Hexa: "), 16)
        print(oct(x))
    elif i == 10:
        x = int(input("masukkan angka Octal: "), 8)
        print(bin(x))
    elif i == 11:
        x = int(input("masukkan angka Octal: "), 8)
        print(x)
    elif i == 12:
        x = int(input("masukkan angka Octal: "), 8)
        print(hex(x))
    else:
        print("Pilihan anda salah")
    konfirmasi()

def bentuk(i):
    if i == 1:
        x = int(input("Masukkan angka :"))
        piramid(x)
    elif i == 2:
        x = int(input("Masukkan angka :"))
        belah_k(x)
    else:
        print("Pilihan anda salah")
    konfirmasi()


def piramid(x):
    string = ""
    bar = x
    while bar >= 0:
        kol = bar
        while kol > 0:
            string = string + "   "
            kol = kol - 1
        kiri = 1
        while kiri < (x - (bar - 1)):
            string = string + " * "
            kiri = kiri + 1
        kanan = 1
        while kanan < kiri - 1:
            string = string + " * "
            kanan = kanan + 1
        string = string + "\n\n"
        bar = bar - 1
    print(string)


def belah_k(x):
    string = ""
    bar = x
    while bar >= 0:
        kol = bar
        while kol > 0:
            string = string + "   "
            kol = kol - 1
        kiri = 1
        while kiri < (x - (bar - 1)):
            string = string + " * "
            kiri = kiri + 1
        kanan = 1
        while kanan < kiri - 1:
            string = string + " * "
            kanan = kanan + 1

        string = string + "\n\n"
        bar = bar - 1
    bar = 1
    while bar <= x:
        kol = bar + 1
        while kol > 1:
            string = string + "   "
            kol = kol - 1
        kiri = 0
        while kiri < (x - bar):
            string = string + " * "
            kiri = kiri + 1
        kanan = kiri
        while kanan > 1:
            string = string + " * "
            kanan = kanan - 1
        string = string + "\n\n"
        bar = bar + 1
    print(string)


def konfirmasi():
    while True:
        ulang = input("Apakah anda ingin mengulangi?(y/t): ")
        if ulang.title() == "Y":
            cls()
            main()
        elif ulang.title() == "T":
            break
        break


def cls():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
