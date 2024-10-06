def recursive_max(arr):
    if len(arr) == 0: # Jika keadaan list kosong (base case)
        return None
    elif len(arr) == 1: # Keadaan jika listnya 1 maka, akan dijawab dirinya sendiri (base case)
        return arr[0]
    else: #(recursive case)
        maxItem = recursive_max(arr[1:]) #Membaca dari indeks satu sampai indeks terakhir
        return maxItem if maxItem > arr[0] else arr[0] 

print(recursive_max([1,2,3,4,5,1]))

