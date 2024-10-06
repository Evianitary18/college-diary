panjanglist = int(input("Masukkan panjang list: "))

data = []
for i in range(panjanglist):
    data.append(int(input(f"Masukkan bilangan ke-{i+1} : ")))

def palindrom(a,b):
    if b == panjanglist:
        print("")
        print("Value : List yang diinputkan merupakan palindrom")
    else:
        if data[a] == data[-b]:
            palindrom(a+1, b+1)
        else:
            print("")
            print("Value : List yang diinputkan bukan palindrom")

palindrom(0,1)

