# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8;
# dict['School'] = "DPS School"

# print ("Name    : ", dict['Name'])
# print ("Age     : ", dict['Age'])
# print ("Class   : ", dict['Class'])
# print ("School  : ", dict['School'])

# def salam():
#     print ("Assalamu'alaikum wr. wb.")

# def luas_segitiga(alas, tinggi):
#     return (alas * tinggi) / 2

# def luas_persegi(sisi):
#     return (sisi * sisi)

# print(luas_persegi(8))
# print(luas_segitiga(4, 6))
# salam()

# Nama = "Ali"
# Versi = "1.0.0"

# def help():
#     name = "Dictionary"
#     version = "1.0.0"
#     print ("Nama    : %s"%name)
#     print ("Versi   : %s"%version)

# print ("Nama    : %s"%Nama)
# print ("Versi   : %s"%Versi)

# help()

# dict = {'name1': 'Cahyo Jati Jayanto', 'name2': 'Abdurahman', 'name3': 'Darman Yusnan Ely', 'name4': 'Filla Setyono Junior'}
# print ("1. ", dict['name1'])
# print ("2. ", dict['name2'])
# print ("3. ", dict['name3'])
# print ("4. ", dict['name4'])

# def salam2():
#     print ("Selamat Sore...")
# salam2()

def suhu(temp):
    if (temp <= 7):
        return ("Cold")
    elif (temp > 7):
        return ("Hot")
x = int(input('Suhu hari ini adalah : '))
print("Suhu hari ini : ", suhu(x))
suhu(x)

# def tambah(angka1,angka2):
#     return angka1 + angka2

# for i in range(10):
#     print("Hasil ", tambah(i,i+4))

# def jarak(temp):
#     return temp / 1000
# x = int(input('Panjang jalan dalam m: '))
# print("Hasil ", jarak(x))
# from math import sqrt
# def mulai(x):
#     return sqrt(x)
# angka = int(input('Akar dari : '))
# print("Hasilnya adalah :", sqrt(angka))