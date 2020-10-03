print("program konversi suhu dari celcius")
C = int(input("masukkan suhu dalam celcius: "))
X = input("konversi ke K/R/F: ")

if X == "K":
    K = C + 273
    print("%d celcius itu %d kelvin" % (C, K))
elif X == "R":
    R = (4 / 5) * C
    print("%d celcius itu %d reamur" % (C, R))
elif X == "F":
    F = ((9 / 5) * C) + 32
    print("%d celcius itu %d farenheit" % (C, F))
else:
    print("ERROR!")
