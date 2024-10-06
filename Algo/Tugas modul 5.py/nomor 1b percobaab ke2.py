def countOccurrence(array, key):
    n = len(array)
    #basis algoritma
    if n == 0:
        return 0
    if n == 1:
        if array[0] == key:
            return 1
        else:
            return 0
    #algoritma divide = memilah dan membagi
    # membagi nilai A menjadi solusi yang lebih kecil
    mid = n // 2
    left_count = countOccurrence(array[:mid], key)
    right_count = countOccurrence(array[mid:], key)
    #algoritma conquer = mengurutkan kembali
    return left_count + right_count

# penggunaan
A = [1,2,5,6,8,8,8,9,11,12,23,24,23,23,60,1,3 ]
k = (int(input("masukan angka: ")))
hasil = countOccurrence(A, k)
print("diketahui jumlah anggota A yang memiliki nilai sama dengan k adalah ", hasil) 

