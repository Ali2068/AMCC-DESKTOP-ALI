def main():
    print("program konversi suhu dari celcius")
    C = int(input("masukkan suhu dalam celcius"))
    X = input("konversi e K/R/F:")
    konversi(C,X)


def konversi(C,X):
    if x.title() == "k":
        K = C + 273
        print("%d celcius itu %d kelvin " % (C, K))
    elif x.title() == "F":
        F = ((9/5)) *