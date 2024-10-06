panjanglist = int(input("Masukkan panjang list: "))

data = [1,2,3,4,5,1]
for i in range(panjanglist):
    data.append(int(input(f"Masukkan bilangan yang ke-{i+1} : ")))

def temukan_angka_terbesar(a,b):
    if a != panjanglist:
        for i in data:
            if data[a] > i:
                if data[a] > b:
                    b = data[a]
        temukan_angka_terbesar(a+1,b)
    else:
        print("")
        print(f"Bilangan yang paling besar adalah {b}")

temukan_angka_terbesar(0,0)

