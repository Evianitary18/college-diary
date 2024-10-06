def BinarySearch(data1, key):
    low = 0
    panjang = len(data1) -1
    Found = False
    while low <= panjang and not Found:
        nilai_tengah = (low+panjang)//2
        if key == data1[nilai_tengah]:
            Found = True
        elif key > data1[nilai_tengah]:
            low = nilai_tengah + 1
        else:
            panjang = nilai_tengah - 1
    if Found ==  True:
        print("Data ditemukan")
    else:
        print("Data tidak ditemukan")

data1 = [1,2,3,4,5,6,7,8,9,10]
data1.sort()
print(data1)
key = int(input("Cari data: "))
BinarySearch(data1, key)
