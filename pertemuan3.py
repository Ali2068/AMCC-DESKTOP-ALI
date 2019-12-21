Nama = ['Yana', 2012, 63, "189 cm"]
Kelas = ['SI02', 'IF03', 'MI02', 'IF02']

print ("Nama    : ", Nama[0])
print ("ThAng   : ", Nama[1])
print ("BB      : ", Nama[2])
print ("TB      : ", Nama[3])
print ("Kelas   : ", Kelas[0])


Satuan = [1, 2, 3, 4, 5, 6]
Puluhan = [10, 20, 30, 40, 50]

print(sum(Satuan))
print(sum(Puluhan))
a = Satuan + Puluhan
print(sum(a))

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup = ('fisika', 'kimia', 1993, 2017)

print ("tup", tup)
del tup
print ("Setelah menghapus tupple : ")