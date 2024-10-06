def maksfindDivideAndconquer(array, awal, akhir):
    if akhir - awal == 1:
        return abs(array[awal] - array[akhir])
    if awal == akhir:
        return 0
    nilaiTengah = (awal + akhir) // 2
    diffAwal = maksfindDivideAndconquer(array, awal, nilaiTengah)
    diffAkhir = maksfindDivideAndconquer(array, nilaiTengah+1, akhir)
    awalNilaimaks = -float('inf')
    akhirNilaiminim = float('inf')

    for i in range(awal, nilaiTengah+1):
        if array[i] > awalNilaimaks:
            awalNilaimaks = array[i]
    for j in range(nilaiTengah+1, akhir+1):
        if array[j] < akhirNilaiminim:
            akhirNilaiminim = array[j]
    
    beda = abs(awalNilaimaks - akhirNilaiminim)
    return max(diffAwal, diffAkhir, beda)

A = [12, 1, 1, 2, 5, 7, 6, 9, 14]
hasil = maksfindDivideAndconquer(A, 0, len(A)-1)
print("Diketahui nilai selisih terbesar di antara dua bilangan berurutan di dalam A ialah", hasil)