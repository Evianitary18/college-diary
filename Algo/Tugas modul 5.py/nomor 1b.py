def countKDivideAndConquer (arr,key):
    n = len(arr)
    if n == 0:
        return 0
        if n == 1:
            if arr[0] == key:
                return 1
            else:
                return 0
                mid = n // 2
                left_count = countKDivideAndConquer(arr[:mid],key)
                right_count =countKDivideAndConquer(arr[mid:], key)
                return left_count + right_count
        
arr = [3,5,1,2,3,5,2,5,4,3]
key = 5
count = countKDivideAndConquer(arr, key)
print("Jumlah anggota arr yang sama dengan", key, "adalah", count)