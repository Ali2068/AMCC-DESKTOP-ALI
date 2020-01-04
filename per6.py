hdef konversi(x,y,z,):
    #(x = nilai suhu, y = satuan suhu awal, z = satuan suhu tujuan)
    print("C = celcius, R = reamur, F = fahrenheit, K = kelvin")
y=str(input("Tentukan suhu apa yang ingin kamu konversi ? (pilih C/R/F/K) : "))
if (y == 'C'):
    z=str(input("Ke satuan apa kamu ingin konversikan? (R/F/K) : "))
    if (z == 'R'):
        x=float(input("Masukkan nilai celcius suhu yang ingin kamu ubah menjadi reamur : "))
        R=((4/5)*x)
        print ("Jadi, suhu dalam Reamur adalah :",R)
    elif (z == 'F'):
        x=float(input("Masukkan nilai celcius suhu yang ingin kamu ubah menjadi fahrenheit : "))
        F=(((9/5)*x)+32)
        print("Jadi, suhu dalam Fahrenheit adalah :",F)
    elif (z == 'K'):
        x=float(input("Masukkan nilai celcius suhu yang ingin kamu ubah menjadi kelvin : "))
        K=(x+273)
        print("Jadi, suhu dalam Kelvin adalah :",K)
    else :
        print("Satuan suhu yang kamu masukkan salah, silahkan pilih R/F/K")
elif (y == 'R'):
    z=str(input("Ke satuan apa kamu ingin konversikan? (C/F/K) : "))
    if (z == 'C'):
        x=float(input("Masukkan nilai reamur suhu yang ingin kamu ubah menjadi celcius : "))
        C=((5/4)*x)
        print ("Jadi, suhu dalam Celcius adalah :",C)
    elif (z == 'F'):
        x=float(input("Masukkan nilai reamur suhu yang ingin kamu ubah menjadi fahrenheit : "))
        F=(((9/4)*x)+32)
        print("Jadi, suhu dalam Fahrenheit adalah :",F)
    elif (z == 'k'):
        x=float(input("Masukkan nilai reamur suhu yang ingin kamu ubah menjadi kelvin : "))
        K=(((5/4)*x)+273)
        print("Jadi, suhu dalam Kelvin adalah :",K)
    else :
        print("Satuan suhu yang kamu masukkan salah, silahkan pilih C/F/K")
elif (y == 'F'):
    z=str(input("Ke satuan apa kamu ingin konversikan? (C/R/K) : "))
    if (z == 'C'):
        x=float(input("Masukkan nilai fahrenheit suhu yang ingin kamu ubah menjadi celcius : "))
        C=((x-32)*(5/9))
        print ("Jadi, suhu dalam Celcius adalah :",C)
    elif (z == 'R'):
        x=float(input("Masukkan nilai fahrenheit suhu yang ingin kamu ubah menjadi reamur : "))
        R=((x-32)*(4/9))
        print("Jadi, suhu dalam Reamur adalah :",R)
    elif (z == 'k'):
        x=float(input("Masukkan nilai fahrenheit suhu yang ingin kamu ubah menjadi kelvin : "))
        K=(((x-32)*(5/9))+273)
        print("Jadi, suhu dalam Kelvin adalah :",K)
    else :
        print("Satuan suhu yang kamu masukkan salah, silahkan pilih C/R/K")
elif (y == 'k'):
    z=str(input("Ke satuan apa kamu ingin konversikan? (C/R/F) : "))
    if (z == 'C'):
        x=float(input("Masukkan nilai kelvin suhu yang ingin kamu ubah menjadi celcius : "))
        C=(x-273)
        print ("Jadi, suhu dalam Celcius adalah :",C)
    elif (z == 'R'):
        x=float(input("Masukkan nilai kelvin suhu yang ingin kamu ubah menjadi reamur : "))
        R=((x-273)*(4/5))
        print("Jadi, suhu dalam Reamur adalah :",R)
    elif (z == 'F'):
        x=float(input("Masukkan nilai kelvin suhu yang ingin kamu ubah menjadi fahrenheit : "))
        F=(((x-273)*(9/5))+32)
        print("Jadi, suhu dalam Fahrenheit adalah :",F)
    else :
        print("Satuan suhu yang kamu masukkan salah, silahkan pilih C/R/F")
else :
    print("Satuan suhu yang kamu masukkan salah, silahkan pilih C/R/F/K")
konversi('x','y','z')