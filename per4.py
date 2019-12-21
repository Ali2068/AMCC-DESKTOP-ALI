dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;
dict['School'] = "DPS School"

print ("Name    : ", dict['Name'])
print ("Age     : ", dict['Age'])
print ("Class   : ", dict['Class'])
print ("School  : ", dict['School'])

def salam():
    print ("Assalamu'alaikum wr. wb.")

def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print ("Luas Segitiga = %f"%luas)

def luas_persegi(sisi):
    luas = (sisi * sisi)
    print ("Luas Persegi = %f"%luas)

luas_persegi(8)
luas_segitiga(4, 6)
salam()

Nama = "Ali"
Versi = "1.0.0"

def help():
    name = "Dictionary"
    version = "1.0.0"
    print ("Nama    : %s"%name)
    print ("Versi   : %s"%version)

print ("Nama    : %s"%Nama)
print ("Versi   : %s"%Versi)

help()